# Hyperswitch Operational Runbook Library

This directory contains operational runbooks for managing Hyperswitch in production environments. Each runbook provides step-by-step procedures for common operational tasks, incident response, and maintenance activities.

## Runbook Categories

### 📋 Incident Response
Runbooks for handling production incidents and outages.

- **[Incident Response Playbook](./incident-response.md)** - General incident handling procedures
- **[Database Failure](./database-failure.md)** - PostgreSQL failover and recovery
- **[Cache Failure](./cache-failure.md)** - Redis cluster issues and recovery
- **[Payment Processor Outage](./processor-outage.md)** - Handling PSP connectivity issues
- **[High Latency](./high-latency.md)** - Performance degradation response
- **[Security Incident](./security-incident.md)** - Security breach response

### 🔧 Maintenance & Operations
Regular maintenance procedures and operational tasks.

- **[Backup and Restore](./backup-restore.md)** - Database backup verification and restoration
- **[Certificate Rotation](./certificate-rotation.md)** - SSL/TLS certificate renewal
- **[Database Maintenance](./database-maintenance.md)** - Index optimization and cleanup
- **[Log Rotation](./log-rotation.md)** - Log file management and archival
- **[Scaling Operations](./scaling.md)** - Horizontal and vertical scaling procedures
- **[Patch Management](./patching.md)** - Security patches and updates

### 🚀 Deployment & Release
Procedures for deploying changes and managing releases.

- **[Blue-Green Deployment](./deployment-blue-green.md)** - Zero-downtime deployments
- **[Rollback Procedures](./rollback.md)** - Rolling back failed deployments
- **[Database Migration](./database-migration.md)** - Schema changes and migrations
- **[Feature Flag Management](./feature-flags.md)** - Enabling/disabling features
- **[Environment Promotion](./environment-promotion.md)** - Promoting between environments

### 📊 Monitoring & Alerting
Setting up and maintaining observability systems.

- **[Alert Configuration](./alert-configuration.md)** - Setting up monitoring alerts
- **[Dashboard Creation](./dashboard-creation.md)** - Building monitoring dashboards
- **[Log Analysis](./log-analysis.md)** - Troubleshooting using logs
- **[Metrics Interpretation](./metrics-guide.md)** - Understanding key metrics
- **[Synthetic Monitoring](./synthetic-monitoring.md)** - End-to-end health checks

### 🔐 Security & Compliance
Security-related operational procedures.

- **[Access Review](./access-review.md)** - Periodic access audits
- **[Secret Rotation](./secret-rotation.md)** - API key and credential rotation
- **[Vulnerability Scanning](./vulnerability-scanning.md)** - Security assessments
- **[Compliance Checks](./compliance-checks.md)** - PCI DSS and other compliance
- **[Audit Trail Review](./audit-trail.md)** - Reviewing system logs for compliance

### 💾 Disaster Recovery
Procedures for major disaster scenarios.

- **[Disaster Recovery Plan](./disaster-recovery.md)** - Overview of DR procedures
- **[Region Failover](./region-failover.md)** - Multi-region failover procedures
- **[Data Corruption Recovery](./data-corruption.md)** - Recovering from data corruption
- **[Complete Environment Recreation](./environment-recreation.md)** - Rebuilding from scratch

## Quick Reference

### Severity Levels

| Level | Description | Response Time | Examples |
|-------|-------------|---------------|----------|
| **SEV-1** | Critical - Complete outage | 15 minutes | All payments failing |
| **SEV-2** | High - Major degradation | 30 minutes | 50% payment failure rate |
| **SEV-3** | Medium - Partial impact | 2 hours | Specific connector down |
| **SEV-4** | Low - Minimal impact | 4 hours | Monitoring gaps |

### Emergency Contacts

| Role | Contact | Escalation |
|------|---------|------------|
| **On-call Engineer** | PagerDuty/Slack | Auto-escalates after 15 min |
| **Engineering Lead** | Slack: @eng-leads | After 30 minutes |
| **VP Engineering** | Email/Phone | After 1 hour |
| **Hyperswitch Support** | support@hyperswitch.io | Enterprise customers |

### Key Dashboards

- **Health Overview**: https://grafana.hyperswitch.io/d/health
- **Payment Metrics**: https://grafana.hyperswitch.io/d/payments
- **Infrastructure**: https://grafana.hyperswitch.io/d/infrastructure
- **Error Rates**: https://grafana.hyperswitch.io/d/errors

### Useful Commands

```bash
# Check service health
kubectl get pods -n hyperswitch

# View recent logs
kubectl logs -f deployment/hyperswitch-router -n hyperswitch

# Check database connectivity
psql -h $DB_HOST -U $DB_USER -c "SELECT count(*) FROM payments;"

# Check Redis connectivity
redis-cli -h $REDIS_HOST ping

# Restart specific service
kubectl rollout restart deployment/hyperswitch-router -n hyperswitch
```

## Contributing

When adding new runbooks:
1. Use the [runbook template](./TEMPLATE.md)
2. Include clear preconditions and postconditions
3. Provide rollback procedures where applicable
4. Test procedures in a staging environment
5. Include relevant metrics and SLAs
6. Review with the operations team

## Review Schedule

- **Weekly**: Incident post-mortems and lessons learned
- **Monthly**: Runbook accuracy review and updates
- **Quarterly**: Full disaster recovery drill
- **Annually**: Comprehensive runbook audit

---

**Last Updated**: April 2026  
**Owner**: Site Reliability Engineering Team  
**Questions?** Contact: sre@hyperswitch.io