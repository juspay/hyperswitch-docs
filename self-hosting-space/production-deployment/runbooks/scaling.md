# Scaling Operations Runbook

**Purpose**: Procedures for horizontally and vertically scaling Hyperswitch infrastructure.

**Audience**: SREs, DevOps engineers, platform engineers

**Last Updated**: April 2026

## Overview

This runbook provides procedures for scaling Hyperswitch components to handle increased load, seasonal traffic spikes, or business growth.

## Scaling Types

| Type | Description | Use Case | Downtime |
|------|-------------|----------|----------|
| **Horizontal Pod Scaling** | Add/remove application pods | Traffic increases | None |
| **Vertical Pod Scaling** | Increase CPU/memory per pod | Memory-intensive operations | Rolling restart |
| **Cluster Scaling** | Add worker nodes | Maxed out cluster capacity | None |
| **Database Scaling** | Read replicas, sharding | Database bottlenecks | Minimal |
| **Cache Scaling** | Redis cluster expansion | Cache saturation | None |

## Horizontal Pod Autoscaling (HPA)

### Current HPA Configuration

```yaml
# View current HPA settings
kubectl get hpa -n hyperswitch

# Example output:
# NAME                 REFERENCE                       TARGETS   MINPODS   MAXPODS   REPLICAS
# hyperswitch-router   Deployment/hyperswitch-router   45%/70%   5         50        12
```

### Manual Scale-Up

**When to use:**
- Predictable traffic spike (e.g., flash sale)
- HPA reaction time too slow
- Preemptive scaling before event

**Immediate Scale-Up:**
```bash
# Scale to specific replica count
kubectl scale deployment hyperswitch-router \
  --replicas=20 -n hyperswitch

# Verify scaling
kubectl get deployment hyperswitch-router -n hyperswitch

# Watch pods come online
kubectl get pods -n hyperswitch -w
```

**Schedule-Based Scaling (CronJob):**
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: scale-up-for-sale
  namespace: hyperswitch
spec:
  schedule: "0 8 * * 5"  # Every Friday at 8 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: scaler
            image: bitnami/kubectl:latest
            command:
            - kubectl
            - scale
            - deployment/hyperswitch-router
            - --replicas=30
            - -n
            - hyperswitch
          restartPolicy: OnFailure
```

### Adjust HPA Limits

**Increase max replicas:**
```bash
kubectl patch hpa hyperswitch-router -n hyperswitch \
  --patch '{"spec":{"maxReplicas":100}}'
```

**Modify target CPU utilization:**
```bash
kubectl patch hpa hyperswitch-router -n hyperswitch \
  --patch '{"spec":{"targetCPUUtilizationPercentage":60}}'
```

**View HPA events:**
```bash
kubectl describe hpa hyperswitch-router -n hyperswitch
```

## Vertical Scaling

### Application Pods

**Increase resource limits:**
```bash
# Patch deployment resources
kubectl patch deployment hyperswitch-router -n hyperswitch \
  --patch '{
    "spec": {
      "template": {
        "spec": {
          "containers": [{
            "name": "router",
            "resources": {
              "limits": {
                "cpu": "2000m",
                "memory": "4Gi"
              },
              "requests": {
                "cpu": "1000m",
                "memory": "2Gi"
              }
            }
          }]
        }
      }
    }
  }'
```

**Rolling restart to apply:**
```bash
kubectl rollout restart deployment/hyperswitch-router -n hyperswitch
kubectl rollout status deployment/hyperswitch-router -n hyperswitch
```

### Node Pool Scaling

**AWS EKS:**
```bash
# Scale node group
aws eks update-nodegroup-config \
  --cluster-name hyperswitch-cluster \
  --nodegroup-name general-workers \
  --scaling-config minSize=3,maxSize=20,desiredSize=10

# Verify
aws eks describe-nodegroup \
  --cluster-name hyperswitch-cluster \
  --nodegroup-name general-workers \
  --query 'nodegroup.scalingConfig'
```

**GKE:**
```bash
gcloud container clusters resize hyperswitch-cluster \
  --node-pool general-pool \
  --num-nodes 10 \
  --zone us-central1-a
```

**AKS:**
```bash
az aks nodepool scale \
  --cluster-name hyperswitch-cluster \
  --resource-group hyperswitch-rg \
  --name nodepool1 \
  --node-count 10
```

## Database Scaling

### Read Replica Scaling

**Add read replica:**
```bash
# AWS RDS
aws rds create-db-instance-read-replica \
  --db-instance-identifier hyperswitch-db-replica-2 \
  --source-db-instance-identifier hyperswitch-db \
  --db-instance-class db.r5.xlarge

# Wait for creation
aws rds wait db-instance-available \
  --db-instance-identifier hyperswitch-db-replica-2
```

**Update application to use replicas:**
```bash
# Update configmap with new replica endpoint
kubectl patch configmap hyperswitch-config -n hyperswitch \
  --patch '{
    "data": {
      "DATABASE_REPLICA_URL": "postgresql://readonly@replica-2.cluster-xxx.us-east-1.rds.amazonaws.com:5432/hyperswitch"
    }
  }'

# Rolling restart
kubectl rollout restart deployment/hyperswitch-router -n hyperswitch
```

### Database Vertical Scaling

**Scale up instance size:**
```bash
# AWS RDS - requires maintenance window or immediate
aws rds modify-db-instance \
  --db-instance-identifier hyperswitch-db \
  --db-instance-class db.r5.2xlarge \
  --apply-immediately

# Monitor scaling progress
aws rds wait db-instance-available \
  --db-instance-identifier hyperswitch-db
```

⚠️ **Warning**: Causes brief downtime (typically 2-5 minutes)

## Cache Scaling

### Redis Cluster Expansion

**Add Redis node:**
```bash
# Scale StatefulSet
kubectl scale statefulset redis-cluster --replicas=6 -n hyperswitch

# Wait for pods
kubectl wait --for=jsonpath='{.status.readyReplicas}'=6 \
  statefulset/redis-cluster -n hyperswitch

# Reshard cluster (if using Redis Cluster)
kubectl exec -it redis-cluster-0 -n hyperswitch -- \
  redis-cli --cluster reshard redis-cluster-0.redis-cluster:6379
```

**Increase Redis memory:**
```bash
# Update Redis configuration
kubectl patch configmap redis-config -n hyperswitch \
  --patch '{
    "data": {
      "redis.conf": "maxmemory 4gb\nmaxmemory-policy allkeys-lru"
    }
  }'

# Restart Redis
kubectl rollout restart statefulset/redis-cluster -n hyperswitch
```

## Capacity Planning

### Monitoring Key Metrics

**Track these metrics for scaling decisions:**

```bash
# Pod CPU/Memory usage
kubectl top pods -n hyperswitch

# Node utilization
kubectl top nodes

# Payment throughput
kubectl exec -it deployment/hyperswitch-router -n hyperswitch -- \
  psql -c "SELECT 
    DATE_TRUNC('minute', created_at) as time,
    COUNT(*) as txns_per_minute
  FROM payment_attempt 
  WHERE created_at > NOW() - INTERVAL '1 hour'
  GROUP BY time
  ORDER BY time DESC
  LIMIT 10;"

# Database connections
kubectl exec -it deployment/hyperswitch-router -n hyperswitch -- \
  psql -c "SELECT count(*) FROM pg_stat_activity;"
```

### Scaling Triggers

| Metric | Current | Scale Up At | Scale Down At |
|--------|---------|-------------|---------------|
| **Pod CPU** | 45% | 70% | 30% |
| **Pod Memory** | 60% | 80% | 40% |
| **DB Connections** | 80 | 150 | 50 |
| **Latency (p99)** | 150ms | 500ms | 100ms |
| **Queue Depth** | 100 | 1000 | 50 |

## Seasonal/Flash Sale Scaling

### Pre-Event Checklist

**1 Week Before:**
- [ ] Scale to 2x normal capacity
- [ ] Warm up caches
- [ ] Verify database connection pools
- [ ] Test load balancer configuration
- [ ] Confirm payment processor limits

**Day Of:**
- [ ] Monitor dashboards continuously
- [ ] Have runbook ready
- [ ] Notify payment processors of increased volume
- [ ] Enable aggressive caching

**Commands:**
```bash
# Pre-scale for event
kubectl scale deployment hyperswitch-router --replicas=40 -n hyperswitch

# Increase DB connection pool temporarily
kubectl set env deployment/hyperswitch-router \
  DATABASE_POOL_SIZE=100 \
  REDIS_POOL_SIZE=50 \
  -n hyperswitch

# Enable circuit breakers for less critical paths
kubectl set env deployment/hyperswitch-router \
  WEBHOOK_CIRCUIT_BREAKER_ENABLED=true \
  ANALYTICS_CIRCUIT_BREAKER_ENABLED=true \
  -n hyperswitch
```

### Post-Event Scale Down

```bash
# Gradual scale down (monitor closely)
kubectl scale deployment hyperswitch-router --replicas=30 -n hyperswitch

# Wait 30 minutes, monitor metrics
sleep 1800

kubectl scale deployment hyperswitch-router --replicas=20 -n hyperswitch

# Eventually return to normal
kubectl scale deployment hyperswitch-router --replicas=10 -n hyperswitch

# Reset environment variables
kubectl set env deployment/hyperswitch-router \
  DATABASE_POOL_SIZE= \
  REDIS_POOL_SIZE= \
  -n hyperswitch
```

## Auto-Scaling Configuration

### Cluster Autoscaler

**AWS EKS Cluster Autoscaler:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-autoscaler
  namespace: kube-system
spec:
  template:
    spec:
      containers:
      - name: cluster-autoscaler
        image: k8s.gcr.io/autoscaling/cluster-autoscaler:v1.26.0
        command:
        - ./cluster-autoscaler
        - --cloud-provider=aws
        - --namespace=hyperswitch
        - --nodes=3:50:general-workers
```

**Verify autoscaler is running:**
```bash
kubectl logs -f deployment/cluster-autoscaler -n kube-system
```

### KEDA for Event-Driven Scaling

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: hyperswitch-scaler
  namespace: hyperswitch
spec:
  scaleTargetRef:
    name: hyperswitch-router
  minReplicaCount: 5
  maxReplicaCount: 100
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring.svc:9090
      metricName: http_requests_total
      threshold: '1000'
      query: sum(rate(http_requests_total{service="hyperswitch-router"}[2m]))
  - type: postgresql
    metadata:
      host: postgres.hyperswitch.svc
      port: "5432"
      userName: hyperswitch
      passwordFromEnv: DB_PASSWORD
      dbName: hyperswitch
      sslmode: disable
      query: "SELECT COUNT(*) FROM queue WHERE status = 'pending'"
      targetQueryValue: "100"
```

## Troubleshooting Scaling Issues

### Pods Stuck Pending

**Diagnose:**
```bash
# Check why pod is pending
kubectl describe pod <pod-name> -n hyperswitch | grep -A 10 Events

# Common causes:
# - Insufficient CPU/memory
# - No nodes available
# - PVC not bound
# - Image pull errors

# Check node capacity
kubectl describe node <node-name> | grep -A 5 Allocatable
```

**Solutions:**
```bash
# Scale node group if cluster capacity maxed
aws eks update-nodegroup-config \
  --cluster-name hyperswitch-cluster \
  --nodegroup-name general-workers \
  --scaling-config desiredSize=15

# Or reduce pod resource requests temporarily
kubectl patch deployment hyperswitch-router -n hyperswitch \
  --patch '{"spec":{"template":{"spec":{"containers":[{"name":"router","resources":{"requests":{"cpu":"500m","memory":"1Gi"}}}]}}}}'
```

### Database Connection Pool Exhaustion

**Symptoms:**
- High latency
- Connection timeout errors
- Pool exhausted messages in logs

**Immediate Fix:**
```bash
# Increase pool size
kubectl set env deployment/hyperswitch-router \
  DATABASE_POOL_SIZE=150 \
  DATABASE_TIMEOUT=30000 \
  -n hyperswitch

# Restart to apply
kubectl rollout restart deployment/hyperswitch-router -n hyperswitch
```

**Long-term Fix:**
- Add read replicas (see Database Scaling section)
- Optimize slow queries
- Implement connection pooling at application level

### Memory Leak Detection

**Identify leaking pods:**
```bash
# Monitor memory usage over time
kubectl top pods -n hyperswitch --sort-by=memory

# Check for OOMKilled pods
kubectl get pods -n hyperswitch -o json | \
  jq '.items[] | select(.status.containerStatuses[0].lastState.terminated.reason == "OOMKilled") | .metadata.name'
```

**Temporary mitigation:**
```bash
# Set memory limit and enable OOM restart
kubectl patch deployment hyperswitch-router -n hyperswitch \
  --patch '{
    "spec": {
      "template": {
        "spec": {
          "containers": [{
            "name": "router",
            "resources": {
              "limits": {
                "memory": "2Gi"
              }
            }
          }]
        }
      }
    }
  }'
```

## Rollback Procedures

### Undo Scale Operation

```bash
# If scale-up caused issues, roll back
kubectl rollout undo deployment/hyperswitch-router -n hyperswitch

# Or manually scale down
kubectl scale deployment hyperswitch-router --replicas=10 -n hyperswitch

# Monitor error rates
kubectl logs -f deployment/hyperswitch-router -n hyperswitch | grep ERROR
```

### Emergency Circuit Breaker

If scaling causes cascading failures:

```bash
# Enable global circuit breaker
kubectl set env deployment/hyperswitch-router \
  GLOBAL_CIRCUIT_BREAKER_ENABLED=true \
  GLOBAL_ERROR_THRESHOLD=50 \
  -n hyperswitch

# Scale to safe minimum
kubectl scale deployment hyperswitch-router --replicas=3 -n hyperswitch

# Investigate root cause
kubectl logs deployment/hyperswitch-router -n hyperswitch --previous
```

## Best Practices

### Do's
- ✅ Scale gradually (avoid large jumps)
- ✅ Monitor metrics during scaling
- ✅ Test scaling procedures in staging
- ✅ Document scaling events
- ✅ Set up automated alerts
- ✅ Plan for scale-down after events

### Don'ts
- ❌ Scale blindly without monitoring
- ❌ Ignore database connection limits
- ❌ Scale during deployments
- ❌ Forget to scale supporting services (cache, DB)
- ❌ Leave test scaling configs in production

## Metrics and SLAs

### Scaling SLAs

| Operation | Target Time | Maximum Time |
|-----------|-------------|--------------|
| **Pod Scale-Up** | 30 seconds | 2 minutes |
| **Node Provisioning** | 2 minutes | 5 minutes |
| **Database Failover** | 30 seconds | 2 minutes |
| **Cache Resharding** | 1 minute | 5 minutes |

### Post-Scaling Verification

```bash
# Verify all pods healthy
kubectl get pods -n hyperswitch

# Check payment success rate
kubectl exec -it deployment/hyperswitch-router -n hyperswitch -- \
  psql -c "
    SELECT 
      COUNT(CASE WHEN status = 'succeeded' THEN 1 END) * 100.0 / COUNT(*) as success_rate
    FROM payment_attempt 
    WHERE created_at > NOW() - INTERVAL '5 minutes';"

# Check latency
curl -w "%{time_total}\n" -o /dev/null -s \
  https://api.hyperswitch.io/health
```

## Tools and Resources

- **Kubectl Autoscale**: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- **Cluster Autoscaler**: https://github.com/kubernetes/autoscaler
- **KEDA**: https://keda.sh/
- **Goldilocks**: https://github.com/FairwindsOps/goldilocks (resource recommendations)

---

**Document Owner**: Platform Engineering Team  
**Review Frequency**: Monthly  
**Next Review**: May 2026  
**Last Load Test**: [Date of last test]