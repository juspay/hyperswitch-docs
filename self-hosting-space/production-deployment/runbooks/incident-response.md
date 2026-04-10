# Incident Response Playbook

**Purpose**: Standardized procedure for responding to production incidents in Hyperswitch deployments.

**Audience**: On-call engineers, SREs, engineering leads

**Last Updated**: April 2026

## Overview

This playbook provides a structured approach to incident response, ensuring timely identification, communication, and resolution of issues affecting Hyperswitch payment processing.

## Severity Classification

### SEV-1: Critical (All hands on deck)
**Indicators:**
- Complete payment processing outage
- Data loss or corruption
- Security breach
- Compliance violation

**Response Time**: 15 minutes
**SLA**: Resolve within 4 hours
**Escalation**: Immediate to VP Engineering

### SEV-2: High (Major impact)
**Indicators:**
- >50% payment failure rate
- Multiple connector failures
- Database primary node down
- Significant performance degradation (>5s latency)

**Response Time**: 30 minutes
**SLA**: Resolve within 8 hours
**Escalation**: After 1 hour to Engineering Lead

### SEV-3: Medium (Partial impact)
**Indicators:**
- Single connector failure
- Elevated error rates (10-50%)
- Non-critical service degradation
- Specific region affected

**Response Time**: 2 hours
**SLA**: Resolve within 24 hours

### SEV-4: Low (Minimal impact)
**Indicators:**
- Monitoring gaps
- Non-critical warnings
- Capacity concerns

**Response Time**: 4 hours
**SLA**: Resolve within 72 hours

## Incident Response Lifecycle

### Phase 1: Detection (0-5 minutes)

**Detection Sources:**
- PagerDuty alerts
- Monitoring dashboards
- Customer complaints
- Automated anomaly detection

**Immediate Actions:**
1. Acknowledge alert in PagerDuty/Slack
2. Join incident channel: `#incident-YYYY-MM-DD-<brief-description>`
3. Notify team via Slack: `@channel SEV-X incident started`
4. Check current status in Grafana dashboards:
   - [Health Overview](https://grafana.hyperswitch.io/d/health)
   - [Payment Metrics](https://grafana.hyperswitch.io/d/payments)

**Command to check service status:**
```bash
kubectl get pods -n hyperswitch
kubectl get events -n hyperswitch --sort-by='.lastTimestamp'
```

### Phase 2: Assessment (5-15 minutes)

**Determine:**
- [ ] Severity level
- [ ] Scope of impact (which regions, connectors, features)
- [ ] Start time of incident
- [ ] Recent deployments or changes
- [ ] Error messages and logs

**Investigation Commands:**
```bash
# Check recent deployments
kubectl rollout history deployment/hyperswitch-router -n hyperswitch

# View recent error logs
kubectl logs -l app=hyperswitch-router -n hyperswitch --since=1h | grep ERROR

# Check payment failure rate
psql -h $DB_HOST -U $DB_USER -c "
  SELECT 
    status,
    COUNT(*) 
  FROM payment_attempt 
  WHERE created_at > NOW() - INTERVAL '1 hour'
  GROUP BY status;
"
```

**Update Status Page:**
- Create incident on status page
- Set appropriate severity
- Initial message: "We are investigating reports of [issue]."

### Phase 3: Communication (Continuous)

**Stakeholder Updates:**

| Timeframe | Audience | Channel | Content |
|-----------|----------|---------|---------|
| Immediate | Internal team | Slack #incidents | Alert triggered, investigating |
| 15 min | Internal stakeholders | Slack #general | Severity, scope, ETA |
| 30 min | Customers | Status page | Public acknowledgment |
| 1 hour | Executive team | Email/Slack | Business impact, mitigation progress |
| Every 30 min | All stakeholders | Status page + Slack | Progress updates |

**Status Page Templates:**

**Initial (Identified):**
```
We are currently investigating an issue affecting [service/region]. 
Some users may experience [symptom]. We will provide updates as soon as possible.

Impact: [Brief description]
Started: [Timestamp UTC]
Status: Investigating
```

**Update (In Progress):**
```
We have identified the cause of the issue and are actively working on a fix.
[Optional: Estimated resolution time]

Root Cause: [Brief technical description]
Progress: [What has been done / what remains]
ETA: [Estimated time to resolution]
```

**Resolved:**
```
The issue has been resolved. All services are now operating normally.

Duration: [X minutes/hours]
Resolution: [What fixed the issue]
Next Steps: [Follow-up actions]
```

### Phase 4: Mitigation (Varies by severity)

**Immediate Mitigation Options:**

1. **Circuit Breaker Activation** (for connector failures)
```bash
# Disable failing connector via API
curl -X POST https://api.hyperswitch.io/v1/admin/circuit-breaker \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "connector": "stripe",
    "action": "open",
    "reason": "Incident-2026-04-10: High failure rate"
  }'
```

2. **Failover to Standby** (for database/cache)
```bash
# Trigger database failover
kubectl exec -it postgres-primary-0 -- pg_ctl promote

# Verify new primary
kubectl get pods -l app=postgres -n hyperswitch
```

3. **Scale Up** (for capacity issues)
```bash
# Horizontal pod autoscaling
kubectl scale deployment hyperswitch-router --replicas=10 -n hyperswitch

# Or use HPA
kubectl autoscale deployment hyperswitch-router \
  --min=5 --max=20 --cpu-percent=70 -n hyperswitch
```

4. **Rollback Deployment** (for bad releases)
```bash
# Rollback to previous version
kubectl rollout undo deployment/hyperswitch-router -n hyperswitch

# Verify rollback
kubectl rollout status deployment/hyperswitch-router -n hyperswitch
```

### Phase 5: Resolution

**Verification Steps:**
1. Check error rates returned to baseline
2. Verify payment success rate > 95%
3. Confirm all connectors healthy
4. Check latency returned to normal
5. Run synthetic transaction test

**Commands:**
```bash
# Check payment success rate
psql -h $DB_HOST -U $DB_USER -c "
  SELECT 
    DATE_TRUNC('minute', created_at) as minute,
    COUNT(CASE WHEN status = 'succeeded' THEN 1 END) * 100.0 / COUNT(*) as success_rate
  FROM payment_attempt 
  WHERE created_at > NOW() - INTERVAL '30 minutes'
  GROUP BY minute
  ORDER BY minute DESC
  LIMIT 10;
"

# Check latency
curl -w "@curl-format.txt" -o /dev/null -s \
  https://api.hyperswitch.io/health
```

### Phase 6: Post-Incident

**Within 24 Hours:**
1. Schedule post-mortem meeting
2. Send preliminary incident report
3. Update status page to resolved
4. Close PagerDuty incident

**Within 1 Week:**
1. Conduct blameless post-mortem
2. Document root cause analysis
3. Create action items with owners and due dates
4. Publish final incident report
5. Update runbooks based on learnings

## Role Responsibilities

### Incident Commander (IC)
- Overall coordination and decision-making
- Communication with stakeholders
- Resource allocation
- Declares incident resolved

### Technical Lead (TL)
- Technical investigation and diagnosis
- Implements fixes
- Coordinates with subject matter experts
- Validates resolution

### Scribe
- Documents timeline of events
- Records actions taken
- Maintains incident log
- Assists with post-mortem

### Communications Lead (for SEV-1/2)
- Manages status page updates
- Coordinates customer communications
- Handles media inquiries (if applicable)
- Briefs executive team

## Runbook-Specific Procedures

### Database Connection Pool Exhaustion

**Symptoms:**
- High latency on all requests
- "Connection pool exhausted" errors
- Database monitoring shows high connection count

**Mitigation:**
1. Check current connection count:
```sql
SELECT count(*) FROM pg_stat_activity;
```

2. Identify and terminate idle connections:
```sql
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE state = 'idle' 
AND state_change < NOW() - INTERVAL '5 minutes';
```

3. Temporarily increase pool size:
```bash
kubectl set env deployment/hyperswitch-router \
  DATABASE_POOL_SIZE=50 -n hyperswitch
```

4. Root cause analysis:
- Check for connection leaks in application code
- Verify connection timeout settings
- Review long-running queries

### Redis Cache Failure

**Symptoms:**
- Increased database load
- Higher latency for cached data
- Redis connection errors

**Mitigation:**
1. Check Redis health:
```bash
kubectl get pods -l app=redis -n hyperswitch
redis-cli -h $REDIS_HOST ping
```

2. If Redis down, restart:
```bash
kubectl delete pod redis-master-0 -n hyperswitch
# Wait for pod recreation
kubectl rollout status statefulset/redis-master -n hyperswitch
```

3. Fall back to database-only mode (temporary):
```bash
kubectl set env deployment/hyperswitch-router \
  REDIS_ENABLED=false -n hyperswitch
```

### Payment Processor Outage

**Symptoms:**
- High failure rate for specific connector
- Timeout errors from connector
- PSP status page shows issues

**Mitigation:**
1. Disable failing connector:
```bash
curl -X POST https://api.hyperswitch.io/v1/admin/connectors/stripe/disable \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

2. Enable automatic retry to alternative connector
3. Monitor traffic shift to backup connector
4. Re-enable when PSP confirms resolution:
```bash
curl -X POST https://api.hyperswitch.io/v1/admin/connectors/stripe/enable \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

## Escalation Matrix

| Time | Action | Who |
|------|--------|-----|
| T+0 | Acknowledge and assess | On-call Engineer |
| T+15 (SEV-1) | Escalate to Tech Lead | On-call Engineer |
| T+30 (SEV-1/2) | Escalate to Engineering Manager | Incident Commander |
| T+1 hour | Executive briefing | Engineering Manager |
| T+2 hours (SEV-1) | VP Engineering involvement | Engineering Manager |
| T+4 hours (SEV-1) | CEO notification | VP Engineering |
| T+8 hours (SEV-2) | Extended war room | VP Engineering |

## Communication Templates

### Slack Message (Initial)
```
🚨 INCIDENT ALERT 🚨
Severity: SEV-[1-4]
Service: [Affected service]
Impact: [Brief description]
Channel: #[incident-channel]
IC: @oncall-engineer
Status: Investigating
```

### Executive Update Email
```
Subject: [SEV-X] Incident Update - [Service] - [Time]

Overview:
- Incident Start: [Time UTC]
- Severity: SEV-X
- Impact: [Business impact description]
- Affected: [Regions/customers/features]

Current Status:
[Current situation]

Actions Taken:
1. [Action 1]
2. [Action 2]

Next Steps:
[Planned actions with owners]

ETA for Resolution: [Time or TBD]

Questions? Contact: [Incident Commander]
```

## Tools and Resources

### Monitoring
- **Grafana**: https://grafana.hyperswitch.io
- **PagerDuty**: https://hyperswitch.pagerduty.com
- **Datadog**: https://app.datadoghq.com (if configured)

### Communication
- **Slack**: #incidents, #engineering-announcements
- **Status Page**: https://status.hyperswitch.io
- **Conference Bridge**: [Zoom/Meet link]

### Documentation
- **Architecture**: [Link to architecture docs]
- **Deployment History**: `kubectl rollout history`
- **Change Log**: [Link to recent changes]
- **Contact List**: [Internal contacts doc]

## Lessons Learned Log

Recent incidents and key learnings:

| Date | Incident | Severity | Key Learning | Action Item |
|------|----------|----------|--------------|-------------|
| 2026-03-15 | Database failover | SEV-2 | PG failover took 8 min | Implemented Patroni |
| 2026-02-28 | Redis outage | SEV-3 | No HA Redis config | Deployed Redis Sentinel |
| 2026-01-10 | Payment spike | SEV-2 | Autoscaling too slow | Adjusted HPA thresholds |

---

**Document Owner**: Site Reliability Engineering  
**Review Frequency**: Monthly  
**Next Review Date**: May 2026