# Backup and Restore Runbook

**Purpose**: Procedures for backing up Hyperswitch data and restoring from backups.

**Audience**: Database administrators, SREs, on-call engineers

**Last Updated**: April 2026

## Overview

This runbook covers backup strategies, verification procedures, and disaster recovery restoration for Hyperswitch databases and configuration.

## Backup Strategy

### What Gets Backed Up

| Component | Method | Frequency | Retention |
|-----------|--------|-----------|-----------|
| **PostgreSQL Database** | pg_dump + WAL archiving | Daily full, continuous incremental | 30 days full, 7 days incremental |
| **Redis Cache** | RDB snapshots + AOF | Every 6 hours | 24 hours |
| **Configuration** | Git + S3 | On every change | Indefinite (versioned) |
| **Application Logs** | S3/CloudWatch | Continuous | 90 days |
| **TLS Certificates** | AWS ACM/HashiCorp Vault | On rotation | Until expiry |

### Backup Schedule

```
Daily Full Backup:     02:00 UTC (off-peak hours)
Incremental (WAL):     Continuous
Redis Snapshots:       00:00, 06:00, 12:00, 18:00 UTC
Configuration:         On deployment/git push
Log Archival:          Daily at 01:00 UTC
```

## Automated Backups

### PostgreSQL Automated Backup

**Using AWS RDS (if applicable):**
```bash
# Verify automated backups are enabled
aws rds describe-db-instances \
  --db-instance-identifier hyperswitch-db \
  --query 'DBInstances[0].[BackupRetentionPeriod,PreferredBackupWindow]'
```

**Using Self-Managed PostgreSQL with pgBackRest:**
```bash
# Verify pgBackRest is running
pgbackrest info

# Check stanza status
pgbackrest --stanza=hyperswitch check

# List available backups
pgbackrest --stanza=hyperswitch info
```

**Cron job for manual backup verification:**
```bash
# Add to crontab (run daily at 03:00 UTC)
0 3 * * * /usr/local/bin/verify-backup.sh >> /var/log/backup-verify.log 2>&1
```

### Configuration Backup

**Kubernetes manifests:**
```bash
# Backup all Hyperswitch configurations
kubectl get all -n hyperswitch -o yaml > /backup/k8s-manifests-$(date +%Y%m%d).yaml

# Backup ConfigMaps and Secrets
kubectl get configmaps -n hyperswitch -o yaml > /backup/configmaps-$(date +%Y%m%d).yaml
kubectl get secrets -n hyperswitch -o yaml > /backup/secrets-$(date +%Y%m%d).yaml

# Sync to S3
aws s3 sync /backup/ s3://hyperswitch-backups/configs/ --delete
```

## Manual Backup Procedures

### Emergency Database Backup

**When to use:**
- Before major schema migrations
- Before destructive operations
- If automated backup system is down

**Procedure:**
```bash
#!/bin/bash
# emergency-backup.sh

BACKUP_DIR="/mnt/backups/emergency"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="hyperswitch"
DB_HOST="${DB_HOST:-localhost}"
DB_USER="${DB_USER:-hyperswitch}"

echo "Starting emergency backup at $(date)"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Perform pg_dump with compression
pg_dump -h "$DB_HOST" -U "$DB_USER" \
  -Fd "$DB_NAME" \
  -j 4 \
  -f "$BACKUP_DIR/${DB_NAME}_${DATE}" \
  --verbose 2>&1 | tee "$BACKUP_DIR/backup_${DATE}.log"

# Compress backup
tar -czf "$BACKUP_DIR/${DB_NAME}_${DATE}.tar.gz" \
  -C "$BACKUP_DIR" "${DB_NAME}_${DATE}"

# Upload to S3
aws s3 cp "$BACKUP_DIR/${DB_NAME}_${DATE}.tar.gz" \
  "s3://hyperswitch-backups/emergency/"

# Cleanup local backup (keep last 5)
ls -t "$BACKUP_DIR"/*.tar.gz | tail -n +6 | xargs rm -f

echo "Emergency backup completed at $(date)"
```

**Execute:**
```bash
chmod +x emergency-backup.sh
./emergency-backup.sh
```

### Pre-Migration Backup

**Before any database migration:**
```bash
# 1. Create snapshot (if using RDS)
aws rds create-db-snapshot \
  --db-instance-identifier hyperswitch-db \
  --db-snapshot-identifier pre-migration-$(date +%Y%m%d-%H%M%S)

# 2. Wait for snapshot completion
aws rds wait db-snapshot-available \
  --db-snapshot-identifier pre-migration-$(date +%Y%m%d-%H%M%S)

# 3. Also create logical backup
pg_dump -h $DB_HOST -U $DB_USER -Fc hyperswitch > \
  /backup/pre-migration-$(date +%Y%m%d).dump

# 4. Tag the backup
aws s3 cp /backup/pre-migration-$(date +%Y%m%d).dump \
  s3://hyperswitch-backups/migrations/ \
  --metadata migration-id=MIGRATION-2026-04-10
```

## Restore Procedures

### Point-in-Time Recovery (PITR)

**Scenario**: Recover database to specific point in time (e.g., before data corruption)

**Using RDS:**
```bash
# Identify recovery time (UTC)
RECOVERY_TIME="2026-04-10T14:30:00Z"

# Create new instance from point-in-time
aws rds restore-db-instance-to-point-in-time \
  --source-db-instance-identifier hyperswitch-db \
  --target-db-instance-identifier hyperswitch-db-recovery \
  --restore-time "$RECOVERY_TIME" \
  --allocated-storage 100

# Wait for restoration
aws rds wait db-instance-available \
  --db-instance-identifier hyperswitch-db-recovery

# Verify data before switching
psql -h hyperswitch-db-recovery.cluster-xxx.us-east-1.rds.amazonaws.com \
  -U hyperswitch -c "SELECT COUNT(*) FROM payments WHERE created_at > '2026-04-10';"
```

**Using pgBackRest:**
```bash
# Stop application
kubectl scale deployment hyperswitch-router --replicas=0 -n hyperswitch

# Restore to specific point in time
pgbackrest --stanza=hyperswitch restore \
  --type=time \
  --target="2026-04-10 14:30:00" \
  --target-action=promote

# Start PostgreSQL
sudo systemctl start postgresql

# Verify recovery
psql -U hyperswitch -c "SELECT pg_is_in_recovery();"  # Should return 'f'

# Scale application back up
kubectl scale deployment hyperswitch-router --replicas=5 -n hyperswitch
```

### Full Database Restore

**Scenario**: Complete database restoration (disaster recovery)

**From pg_dump:**
```bash
#!/bin/bash
# full-restore.sh

DUMP_FILE="$1"
DB_HOST="${DB_HOST:-localhost}"
DB_NAME="${DB_NAME:-hyperswitch}"
DB_USER="${DB_USER:-hyperswitch}"

if [ -z "$DUMP_FILE" ]; then
    echo "Usage: $0 <dump_file>"
    exit 1
fi

echo "WARNING: This will DESTROY existing database and restore from $DUMP_FILE"
read -p "Are you sure? Type 'RESTORE' to continue: " confirm

if [ "$confirm" != "RESTORE" ]; then
    echo "Restore cancelled"
    exit 1
fi

# Stop application
kubectl scale deployment hyperswitch-router --replicas=0 -n hyperswitch

# Terminate existing connections
psql -h "$DB_HOST" -U postgres -c "
  SELECT pg_terminate_backend(pid) 
  FROM pg_stat_activity 
  WHERE datname = '$DB_NAME';
"

# Drop and recreate database
dropdb -h "$DB_HOST" -U postgres "$DB_NAME"
createdb -h "$DB_HOST" -U postgres "$DB_NAME"

# Restore from dump
pg_restore -h "$DB_HOST" -U "$DB_USER" \
  -d "$DB_NAME" \
  -j 4 \
  --verbose \
  "$DUMP_FILE" 2>&1 | tee /var/log/pg-restore.log

# Analyze tables for query optimization
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "ANALYZE;"

# Start application
kubectl scale deployment hyperswitch-router --replicas=5 -n hyperswitch

echo "Restore completed. Check logs at /var/log/pg-restore.log"
```

### Configuration Restore

**Restore Kubernetes manifests:**
```bash
# From S3 backup
aws s3 cp s3://hyperswitch-backups/configs/k8s-manifests-20260410.yaml /tmp/

# Apply configurations
kubectl apply -f /tmp/k8s-manifests-20260410.yaml

# Verify
kubectl get pods -n hyperswitch
```

**Restore Secrets (if not using external secret management):**
```bash
# WARNING: Ensure you have permission to handle secrets
aws s3 cp s3://hyperswitch-backups/configs/secrets-20260410.yaml /tmp/
kubectl apply -f /tmp/secrets-20260410.yaml
```

## Backup Verification

### Automated Verification

**Daily verification script:**
```bash
#!/bin/bash
# verify-backup.sh

set -e

S3_BUCKET="hyperswitch-backups"
LATEST_BACKUP=$(aws s3 ls s3://$S3_BUCKET/postgres/ | sort | tail -n 1 | awk '{print $4}')
TEMP_DIR="/tmp/backup-verify"

echo "Verifying backup: $LATEST_BACKUP"

# Download latest backup
mkdir -p "$TEMP_DIR"
aws s3 cp "s3://$S3_BUCKET/postgres/$LATEST_BACKUP" "$TEMP_DIR/"

# Extract and verify integrity
cd "$TEMP_DIR"
tar -tzf "$LATEST_BACKUP" > /dev/null && echo "Archive integrity: OK" || echo "Archive integrity: FAILED"

# Restore to temporary database for verification
dropdb --if-exists hyperswitch_verify 2>/dev/null || true
createdb hyperswitch_verify

pg_restore -d hyperswitch_verify \
  --exit-on-error \
  --verbose \
  "$TEMP_DIR/$LATEST_BACKUP" 2>&1 | tail -20

# Run verification queries
psql -d hyperswitch_verify -c "
  SELECT 
    'payments' as table_name, COUNT(*) as row_count 
  FROM payments
  UNION ALL
  SELECT 'merchants', COUNT(*) FROM merchants
  UNION ALL
  SELECT 'connectors', COUNT(*) FROM connectors;
" > /var/log/backup-verify-results.log

# Cleanup
dropdb hyperswitch_verify
rm -rf "$TEMP_DIR"

# Send notification
if [ $? -eq 0 ]; then
  echo "Backup verification SUCCESSFUL"
  curl -X POST "$SLACK_WEBHOOK_URL" \
    -H 'Content-type: application/json' \
    -d '{"text":"✅ Daily backup verification passed for '"$LATEST_BACKUP"'"}'
else
  echo "Backup verification FAILED"
  curl -X POST "$SLACK_WEBHOOK_URL" \
    -H 'Content-type: application/json' \
    -d '{"text":"🚨 Backup verification FAILED for '"$LATEST_BACKUP"'. Check /var/log/backup-verify-results.log"}'
  exit 1
fi
```

### Manual Verification Steps

1. **Check backup exists:**
```bash
aws s3 ls s3://hyperswitch-backups/postgres/ | tail -5
```

2. **Verify backup size:**
```bash
aws s3 ls s3://hyperswitch-backups/postgres/latest.dump
# Should be > 100MB (adjust threshold based on your data)
```

3. **Test restore on staging:**
```bash
# Restore to staging environment
pg_restore -h staging-db.internal -U postgres \
  -d hyperswitch_staging \
  s3://hyperswitch-backups/postgres/latest.dump

# Run smoke tests
./scripts/smoke-tests.sh
```

## Disaster Recovery Scenarios

### Scenario 1: Primary Database Loss

**Recovery Time Objective (RTO)**: 30 minutes  
**Recovery Point Objective (RPO)**: 5 minutes

**Steps:**
1. Activate standby database
2. Update application DNS/endpoints
3. Verify data consistency
4. Rebuild primary as new standby

### Scenario 2: Complete Region Failure

**RTO**: 2 hours  
**RPO**: 15 minutes

**Steps:**
1. Promote read replica in secondary region
2. Update global load balancer configuration
3. Restore from cross-region backup if needed
4. Fail over traffic

### Scenario 3: Accidental Data Deletion

**RTO**: 1 hour  
**RPO**: 5 minutes (if caught quickly)

**Steps:**
1. Stop application writes
2. Identify point-in-time before deletion
3. Restore to temporary instance
4. Extract and reinsert deleted data
5. Resume application

## Best Practices

### Do's
- ✅ Test restores monthly
- ✅ Keep backups in multiple regions
- ✅ Encrypt backups at rest
- ✅ Monitor backup job success
- ✅ Document backup procedures
- ✅ Maintain backup inventory

### Don'ts
- ❌ Store backups only locally
- ❌ Skip backup verification
- ❌ Forget to backup configuration
- ❌ Keep backups indefinitely without cleanup
- ❌ Share backup credentials widely

## Monitoring and Alerting

### Key Metrics

| Metric | Warning Threshold | Critical Threshold |
|--------|------------------|-------------------|
| Last Backup Age | > 25 hours | > 30 hours |
| Backup Size Change | -20% or +50% | -50% or +100% |
| Backup Duration | > 2x avg | > 4x avg |
| Restore Test Failed | N/A | Any failure |
| Storage Capacity | > 80% | > 90% |

### Alerts

**Configure in Datadog/CloudWatch:**
```json
{
  "name": "Backup Age Critical",
  "query": "max(last_6h):max:aws.rds.backup_retention_period{dbinstance:hyperswitch} < 1",
  "message": "@pagerduty-critical No recent backup detected!",
  "priority": "P1"
}
```

## Troubleshooting

### Backup Failing

**Check:**
```bash
# Disk space
df -h /mnt/backups

# Database connectivity
psql -h $DB_HOST -U $DB_USER -c "SELECT 1;"

# S3 permissions
aws s3 ls s3://hyperswitch-backups/

# Backup process logs
tail -100 /var/log/pgbackrest.log
```

### Restore Taking Too Long

**Optimization:**
```bash
# Use parallel jobs
pg_restore -j 8 -d hyperswitch backup.dump

# Temporarily increase maintenance_work_mem
psql -c "SET maintenance_work_mem = '2GB';"

# Disable synchronous commit (temporary)
psql -c "ALTER SYSTEM SET synchronous_commit = off;"
```

### Corrupted Backup

**Recovery:**
```bash
# Try previous day's backup
aws s3 ls s3://hyperswitch-backups/postgres/ | grep $(date -d 'yesterday' +%Y%m%d)

# Or use point-in-time recovery
pgbackrest --stanza=hyperswitch restore --type=time --target="2026-04-09 12:00:00"
```

## Tools and Resources

- **pgBackRest**: https://pgbackrest.org/
- **AWS RDS Backup**: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html
- **Velero** (K8s backup): https://velero.io/
- **S3 Lifecycle Policies**: Automatic archival and cleanup

---

**Document Owner**: Database Administration Team  
**Review Frequency**: Monthly  
**Test Restore Schedule**: First Sunday of each month  
**Next Review**: May 2026