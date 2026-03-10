---
icon: monitor-waveform
---

# Monitoring and Alerts for Juspay Hyperswitch

## TL;DR

This guide shows you how to set up complete monitoring and alerting for your Juspay Hyperswitch deployment. You'll configure metrics collection, log aggregation, dashboards, and alerts to ensure your payment system runs reliably. Expect to spend 2-3 hours on initial setup and validation.

---

## What You'll Learn

- How the observability stack works (Promtail, Loki, Prometheus, Grafana)
- How to collect application and infrastructure metrics
- How to configure alerts with severity levels
- How to set up notification channels
- How to validate your monitoring configuration

---

## Before You Start

### Prerequisites

| Requirement | Version/Details |
|-------------|-----------------|
| Kubernetes cluster | 1.25+ |
| Helm | 3.12+ |
| kubectl | Configured for your cluster |
| Juspay Hyperswitch | Deployed and running |
| Access to configure Prometheus/Grafana | Admin rights |

### What You'll Configure

| Component | Purpose |
|-----------|---------|
| Prometheus | Metrics storage and alerting engine |
| Grafana | Visualisation dashboards |
| Promtail | Log collection agent |
| Loki | Log storage and query |
| OpenTelemetry Collector | Application metrics export |
| Alertmanager | Alert routing and notifications |

---

## Quick Reference: Key Terms

| Acronym | Definition |
|---------|------------|
| **P95** | 95th percentile latency — 95% of requests complete at or below this time |
| **P99** | 99th percentile latency — 99% of requests complete at or below this time |
| **Sev 1** | Severity 1 — Critical issue requiring immediate response |
| **Sev 2** | Severity 2 — High priority issue requiring prompt attention |
| **Sev 3** | Severity 3 — Medium priority issue to address during business hours |
| **SRE** | Site Reliability Engineering — practice of maintaining reliable systems |
| **SLA** | Service Level Agreement — commitment to service availability/performance |

---

## Observability Overview

Reliable operation of a production Juspay Hyperswitch deployment requires comprehensive observability across infrastructure, application behaviour, and transaction performance.

Observability is based on two primary data sources:

| Element | Description | Purpose |
|---------|-------------|---------|
| Logs | Chronological record of events and operations | Used for debugging, auditing, troubleshooting failures |
| Metrics | Numerical measurements collected over time | Used for performance monitoring, capacity planning, alerting |

---

## Setup Sequence

Follow these steps in order to set up monitoring and alerting.

### Step 1: Verify Prerequisites

```bash
# Check Kubernetes cluster version
kubectl version --short

# Verify Hyperswitch is running
kubectl get pods -n Hyperswitch

# Check Helm is installed
helm version
```

**Expected outcome:** All pods in `Running` state, Helm version 3.12+.

---

### Step 2: Install Prometheus

```bash
# Add Prometheus Helm repository
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install Prometheus with Alertmanager
helm install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  --create-namespace \
  --set alertmanager.enabled=true \
  --set server.persistentVolume.enabled=true \
  --set server.persistentVolume.size=50Gi
```

**Expected outcome:** Prometheus pods running in `monitoring` namespace.

---

### Step 3: Install Grafana

```bash
# Add Grafana Helm repository
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Install Grafana
helm install grafana grafana/grafana \
  --namespace monitoring \
  --set persistence.enabled=true \
  --set persistence.size=10Gi \
  --set adminPassword='your-secure-password'
```

**Expected outcome:** Grafana pod running, accessible via port-forward.

---

### Step 4: Install Loki and Promtail

```bash
# Install Loki for log aggregation
helm install loki grafana/loki \
  --namespace monitoring \
  --set persistence.enabled=true \
  --set persistence.size=50Gi

# Install Promtail on each node
helm install promtail grafana/promtail \
  --namespace monitoring \
  --set loki.serviceName=loki
```

**Expected outcome:** Loki and Promtail pods running, logs flowing.

---

### Step 5: Configure OpenTelemetry Collector

Apply this configuration to export application metrics:

```yaml
# otel-collector-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: monitoring
data:
  otel-collector-config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318

    exporters:
      prometheus:
        endpoint: "0.0.0.0:8889"
        const_labels:
          source: Hyperswitch

      logging:
        loglevel: info

    processors:
      batch:
        timeout: 1s
        send_batch_size: 1024

    service:
      pipelines:
        metrics:
          receivers: [otlp]
          processors: [batch]
          exporters: [prometheus, logging]
```

Apply the configuration:

```bash
kubectl apply -f otel-collector-config.yaml
```

**Expected outcome:** OpenTelemetry Collector receiving and exporting metrics.

---

### Step 6: Configure Prometheus to Scrape Hyperswitch

Add this scrape configuration to your Prometheus setup:

```yaml
# prometheus-scrape-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-scrape-config
  namespace: monitoring
data:
  Hyperswitch-scrape-config.yaml: |
    scrape_configs:
      - job_name: 'Hyperswitch-app'
        kubernetes_sd_configs:
          - role: pod
            namespaces:
              names:
                - Hyperswitch
        relabel_configs:
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
            action: keep
            regex: true
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
            action: replace
            target_label: __metrics_path__
            regex: (.+)
          - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
            action: replace
            regex: ([^:]+)(?::\d+)?;(\d+)
            replacement: $1:$2
            target_label: __address__

      - job_name: 'otel-collector'
        static_configs:
          - targets: ['otel-collector.monitoring.svc:8889']
```

Apply and reload Prometheus:

```bash
kubectl apply -f prometheus-scrape-config.yaml
# Trigger Prometheus reload via SIGHUP or restart pod
```

**Expected outcome:** Prometheus targets page showing Hyperswitch endpoints as UP.

---

## Monitoring Architecture

Data flows through the following components:

```
┌─────────────────────┐     ┌──────────────────────┐     ┌─────────────┐
│  Hyperswitch Pods   │────▶│ OpenTelemetry        │────▶│  Prometheus │
│                     │     │ Collector            │     │             │
└─────────────────────┘     └──────────────────────┘     └──────┬──────┘
                                                                │
┌─────────────────────┐     ┌──────────────────────┐            │
│  Application Logs   │────▶│ Promtail             │────▶│       ▼
│                     │     │ (per node)           │     │  ┌─────────┐
└─────────────────────┘     └──────────────────────┘     │  │ Grafana │
                                                         │  │         │
┌─────────────────────┐     ┌──────────────────────┐     │  │Dashboards│
│  Node/System Metrics│────▶│ Node Exporter        │────▶│  └─────────┘
│                     │     │ CloudWatch           │     │
└─────────────────────┘     └──────────────────────┘     │
                                                         │  ┌─────────┐
┌─────────────────────┐     ┌──────────────────────┐     └──│ Alert-  │
│  Logs (centralised) │◀────│ Loki                 │◀───────│ manager │
│                     │     │                      │        └─────────┘
└─────────────────────┘     └──────────────────────┘
```

---

## Application Metrics

Juspay Hyperswitch services emit the following application metrics:

| Metric | Description | Use Case |
|--------|-------------|----------|
| `http_requests_total` | Total HTTP requests | Request rate monitoring |
| `http_request_duration_seconds` | Request latency | Performance tracking |
| `authorization_success_rate` | Successful authorisations | Business health |
| `http_errors_total` | Total error responses | Error rate alerting |

---

## Infrastructure Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| `node_cpu_utilisation_percent` | Node CPU utilisation | Sev 2: >70%, Sev 1: >80% |
| `node_memory_utilisation_percent` | Node memory consumption | Sev 2: >70%, Sev 1: >80% |
| `node_disk_utilisation_percent` | Disk utilisation | Sev 2: >80%, Sev 1: >90% |
| `node_network_receive_bytes_total` | Network usage | Baseline anomaly |

---

## Log Collection

Promtail scrapes logs from containers and nodes, sending them to Loki for centralised storage:

```yaml
# promtail-config snippet
scrape_configs:
  - job_name: Hyperswitch-logs
    kubernetes_sd_configs:
      - role: pod
        namespaces:
          names:
            - Hyperswitch
    pipeline_stages:
      - json:
          expressions:
            level: level
            message: message
            timestamp: timestamp
      - labels:
          level:
      - timestamp:
          source: timestamp
          format: RFC3339
```

---

## Monitoring Dashboards

### Kubernetes Cluster Monitoring

Track infrastructure health:

| Metric | Visualisation |
|--------|---------------|
| CPU utilisation by pods | Time series graph |
| Memory utilisation by pods | Time series graph |
| CPU utilisation by nodes | Gauge/cluster view |
| Memory utilisation by nodes | Gauge/cluster view |
| Pod restart counts | Bar chart/table |
| Node health status | Status panel |

### Application Monitoring

Track API performance:

| Metric | Visualisation |
|--------|---------------|
| API route performance | Heatmap/table |
| Request throughput by endpoint | Time series |
| API latency (P95 / P99) | Percentile graphs |
| HTTP status code distribution | Pie chart |
| Error rates across services | Time series |

### Payment and Transaction Monitoring

Track business metrics:

| Metric | Visualisation |
|--------|---------------|
| Total transactions initiated | Counter |
| Total transactions processed | Counter |
| Authorisation success rate | Percentage gauge |
| Transaction status distribution | Pie chart |
| Error codes returned by processors | Table |
| Payment method distribution | Bar chart |

---

## Alerting

### Alert Severity Definitions

| Severity | Response Time | Description |
|----------|---------------|-------------|
| **Sev 1** | Immediate (15 min) | Service-impacting outage or critical failure |
| **Sev 2** | Within 1 hour | Significant degradation requiring prompt attention |
| **Sev 3** | Within 4 hours | Non-critical issue, address during business hours |

### Infrastructure Alerts

| Condition | Severity | Rationale |
|-----------|----------|-----------|
| CPU or memory utilisation > 80% | Sev 1 | Risk of service failure |
| CPU or memory utilisation > 70% | Sev 2 | Early warning for capacity planning |
| Health check endpoint non-2xx | Sev 1 | Service unavailable |
| Disk utilisation > 90% | Sev 1 | Risk of write failures |
| Pod restart count > 5 in 10 min | Sev 2 | Unstable pod behaviour |

### Application Alerts

| Condition | Severity | Rationale |
|-----------|----------|-----------|
| 5xx API responses | Sev 1 | Service errors affecting merchants |
| Abnormal 4xx rate (>10x baseline) | Sev 2 | Potential API misuse or client issues |
| P99 latency > 5 seconds | Sev 2 | Degraded user experience |
| Error rate > 5% | Sev 2 | Elevated failure rate |

### Business Alerts

| Condition | Severity | Rationale |
|-----------|----------|-----------|
| Success rate drop > 30% | Sev 1 | Major payment disruption |
| Success rate drop > 20% | Sev 2 | Significant payment impact |
| Success rate drop > 10% | Sev 3 | Early warning of degradation |
| Transaction volume drop > 50% | Sev 1 | Potential system-wide issue |

---

## YAML Alert Rule Examples

Create `Hyperswitch-alerts.yaml` and apply to Prometheus:

```yaml
# Hyperswitch-alerts.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: Hyperswitch-alerts
  namespace: monitoring
  labels:
    app: prometheus
    role: alert-rules
spec:
  groups:
    - name: infrastructure
      interval: 30s
      rules:
        # Sev 1: Critical CPU utilisation
        - alert: HighCPUUtilisation
          expr: |
            100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
          for: 5m
          labels:
            severity: sev1
            team: sre
          annotations:
            summary: "High CPU utilisation on {{ $labels.instance }}"
            description: "CPU utilisation is above 80% (current value: {{ $value }}%)"
            runbook_url: "https://wiki.internal/runbooks/high-cpu"

        # Sev 2: Warning CPU utilisation
        - alert: ElevatedCPUUtilisation
          expr: |
            100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 70
          for: 10m
          labels:
            severity: sev2
            team: sre
          annotations:
            summary: "Elevated CPU utilisation on {{ $labels.instance }}"
            description: "CPU utilisation is above 70% (current value: {{ $value }}%)"

        # Sev 1: Critical memory utilisation
        - alert: HighMemoryUtilisation
          expr: |
            (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100 > 80
          for: 5m
          labels:
            severity: sev1
            team: sre
          annotations:
            summary: "High memory utilisation on {{ $labels.instance }}"
            description: "Memory utilisation is above 80% (current value: {{ $value }}%)"

        # Sev 1: Disk utilisation critical
        - alert: HighDiskUtilisation
          expr: |
            (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100 < 10
          for: 5m
          labels:
            severity: sev1
            team: sre
          annotations:
            summary: "Low disk space on {{ $labels.instance }}"
            description: "Disk utilisation is above 90% (available: {{ $value }}%)"

    - name: application
      interval: 30s
      rules:
        # Sev 1: 5xx errors
        - alert: High5xxErrorRate
          expr: |
            (
              sum(rate(http_requests_total{status=~"5..", namespace="Hyperswitch"}[5m]))
              /
              sum(rate(http_requests_total{namespace="Hyperswitch"}[5m]))
            ) * 100 > 1
          for: 2m
          labels:
            severity: sev1
            team: sre
          annotations:
            summary: "High 5xx error rate in Hyperswitch"
            description: "5xx error rate is {{ $value }}%"

        # Sev 2: Elevated 4xx errors
        - alert: Elevated4xxErrorRate
          expr: |
            (
              sum(rate(http_requests_total{status=~"4..", namespace="Hyperswitch"}[5m]))
              /
              sum(rate(http_requests_total{namespace="Hyperswitch"}[5m]))
            ) * 100 > 10
          for: 5m
          labels:
            severity: sev2
            team: sre
          annotations:
            summary: "Elevated 4xx error rate in Hyperswitch"
            description: "4xx error rate is {{ $value }}%"

        # Sev 2: High P99 latency
        - alert: HighP99Latency
          expr: |
            histogram_quantile(0.99,
              sum(rate(http_request_duration_seconds_bucket{namespace="Hyperswitch"}[5m])) by (le)
            ) > 5
          for: 5m
          labels:
            severity: sev2
            team: sre
          annotations:
            summary: "High P99 latency in Hyperswitch"
            description: "P99 latency is {{ $value }}s"

    - name: business
      interval: 60s
      rules:
        # Sev 1: Major success rate drop
        - alert: CriticalSuccessRateDrop
          expr: |
            (
              sum(rate(authorization_success_total{namespace="Hyperswitch"}[10m]))
              /
              sum(rate(authorization_total{namespace="Hyperswitch"}[10m]))
            ) < 0.7
          for: 5m
          labels:
            severity: sev1
            team: payments
            pager: true
          annotations:
            summary: "CRITICAL: Payment success rate dropped > 30%"
            description: "Current success rate: {{ $value | humanizePercentage }}"

        # Sev 2: Significant success rate drop
        - alert: HighSuccessRateDrop
          expr: |
            (
              sum(rate(authorization_success_total{namespace="Hyperswitch"}[10m]))
              /
              sum(rate(authorization_total{namespace="Hyperswitch"}[10m]))
            ) < 0.8
          for: 10m
          labels:
            severity: sev2
            team: payments
          annotations:
            summary: "Payment success rate dropped > 20%"
            description: "Current success rate: {{ $value | humanizePercentage }}"

        # Sev 3: Moderate success rate drop
        - alert: ModerateSuccessRateDrop
          expr: |
            (
              sum(rate(authorization_success_total{namespace="Hyperswitch"}[10m]))
              /
              sum(rate(authorization_total{namespace="Hyperswitch"}[10m]))
            ) < 0.9
          for: 15m
          labels:
            severity: sev3
            team: payments
          annotations:
            summary: "Payment success rate dropped > 10%"
            description: "Current success rate: {{ $value | humanizePercentage }}"
```

Apply the alert rules:

```bash
kubectl apply -f Hyperswitch-alerts.yaml
```

---

## Notification Channel Configuration

Configure Alertmanager to route alerts to your channels.

### Slack Notifications

```yaml
# alertmanager-config.yaml
apiVersion: v1
kind: Secret
metadata:
  name: alertmanager-config
  namespace: monitoring
type: Opaque
stringData:
  alertmanager.yml: |
    global:
      slack_api_url: 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'
      smtp_smarthost: 'smtp.gmail.com:587'
      smtp_from: 'alerts@yourcompany.com'
      smtp_auth_username: 'alerts@yourcompany.com'
      smtp_auth_password: '${SMTP_PASSWORD}'

    route:
      receiver: 'default'
      group_by: ['alertname', 'severity', 'team']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 4h
      routes:
        - match:
            severity: sev1
          receiver: 'critical-alerts'
          continue: true
        - match:
            severity: sev2
          receiver: 'high-priority-alerts'
        - match:
            team: payments
          receiver: 'payments-team'

    receivers:
      - name: 'default'
        slack_configs:
          - channel: '#alerts-general'
            title: '{% raw %}{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}{% endraw %}'
            text: '{% raw %}{{ range .Alerts }}{{ .Annotations.description }}{{ end }}{% endraw %}'

      - name: 'critical-alerts'
        slack_configs:
          - channel: '#alerts-critical'
            title: '🚨 SEV 1: {% raw %}{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}{% endraw %}'
            text: |
              {% raw %}{{ range .Alerts }}
              *Summary:* {{ .Annotations.summary }}
              *Description:* {{ .Annotations.description }}
              *Runbook:* {{ .Annotations.runbook_url }}
              {{ end }}{% endraw %}
            send_resolved: true
        pagerduty_configs:
          - service_key: '${PAGERDUTY_SERVICE_KEY}'
            severity: critical

      - name: 'high-priority-alerts'
        slack_configs:
          - channel: '#alerts-high'
            title: '⚠️ SEV 2: {% raw %}{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}{% endraw %}'
            send_resolved: true

      - name: 'payments-team'
        slack_configs:
          - channel: '#payments-alerts'
            title: '{% raw %}{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}{% endraw %}'
            send_resolved: true
        email_configs:
          - to: 'payments-team@yourcompany.com'
            subject: 'Payment Alert: {% raw %}{{ .GroupLabels.alertname }}{% endraw %}'

    inhibit_rules:
      - source_match:
          severity: 'sev1'
        target_match:
          severity: 'sev2'
        equal: ['alertname', 'instance']
```

Apply the configuration:

```bash
# Create secret with your actual values
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK"
export SMTP_PASSWORD="your-smtp-password"
export PAGERDUTY_SERVICE_KEY="your-pd-key"

envsubst < alertmanager-config.yaml | kubectl apply -f -
```

### PagerDuty Integration

For Sev 1 alerts, add to your `receivers`:

```yaml
      - name: 'pagerduty-critical'
        pagerduty_configs:
          - service_key: '${PAGERDUTY_SERVICE_KEY}'
            severity: critical
            description: '{% raw %}{{ .CommonAnnotations.summary }}{% endraw %}'
            details:
              firing: '{% raw %}{{ template "pagerduty.default.instances" .Alerts.Firing }}{% endraw %}'
              resolved: '{% raw %}{{ template "pagerduty.default.instances" .Alerts.Resolved }}{% endraw %}'
```

### Email Notifications

```yaml
      - name: 'email-alerts'
        email_configs:
          - to: 'sre-team@yourcompany.com'
            from: 'alerts@yourcompany.com'
            smarthost: 'smtp.gmail.com:587'
            auth_username: 'alerts@yourcompany.com'
            auth_password: '${SMTP_PASSWORD}'
            subject: '[{% raw %}{{ .Status | toUpper }}{% endraw %}] {% raw %}{{ .GroupLabels.alertname }}{% endraw %}'
            html: |
              {% raw %}{{ range .Alerts }}
              <h3>{{ .Annotations.summary }}</h3>
              <p><strong>Severity:</strong> {{ .Labels.severity }}</p>
              <p><strong>Description:</strong> {{ .Annotations.description }}</p>
              <p><strong>Time:</strong> {{ .StartsAt }}</p>
              <hr/>
              {{ end }}{% endraw %}
```

---

## Validation Steps

Verify your monitoring setup is working correctly.

### Step 1: Verify Prometheus Targets

```bash
# Port-forward to Prometheus
kubectl port-forward svc/prometheus-server 9090:9090 -n monitoring

# Open http://localhost:9090/targets in browser
# All Hyperswitch targets should show as UP
```

**Expected outcome:** All targets in `UP` state, no `DOWN` or `UNKNOWN`.

---

### Step 2: Verify Metrics Collection

```bash
# Query a basic metric in Prometheus UI
curl "http://localhost:9090/api/v1/query?query=up"

# Check Hyperswitch-specific metrics
curl "http://localhost:9090/api/v1/query?query=http_requests_total"
```

**Expected outcome:** JSON response with metric data and values.

---

### Step 3: Verify Log Collection

```bash
# Port-forward to Loki
kubectl port-forward svc/loki 3100:3100 -n monitoring

# Query logs via Loki API
curl "http://localhost:3100/loki/api/v1/query_range?query={namespace=\"Hyperswitch\"}&limit=10"
```

**Expected outcome:** JSON response with log entries from Hyperswitch pods.

---

### Step 4: Verify Grafana Datasources

```bash
# Port-forward to Grafana
kubectl port-forward svc/grafana 3000:3000 -n monitoring

# Login and check:
# Configuration > Datasources
# - Prometheus: Test should pass
# - Loki: Test should pass
```

**Expected outcome:** All datasources show green "Data source is working".

---

### Step 5: Test Alertmanager Configuration

```bash
# Check Alertmanager config is valid
kubectl exec -it deploy/prometheus-alertmanager -n monitoring -- amtool check-config /etc/alertmanager/alertmanager.yml

# View Alertmanager UI
kubectl port-forward svc/prometheus-alertmanager 9093:9093 -n monitoring
# Open http://localhost:9093
```

**Expected outcome:** No config errors, Alertmanager UI loads.

---

### Step 6: Trigger Test Alert

Create a temporary test alert:

```yaml
# test-alert.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: test-alert
  namespace: monitoring
spec:
  groups:
    - name: test
      rules:
        - alert: TestAlertAlwaysFiring
          expr: vector(1)  # Always returns 1 (true)
          for: 0m
          labels:
            severity: sev3
            team: test
          annotations:
            summary: "Test alert - monitoring is working"
            description: "This alert confirms your alerting pipeline is functional"
```

Apply and verify:

```bash
kubectl apply -f test-alert.yaml

# Check alert is firing in Prometheus
# http://localhost:9090/alerts

# Check alert received in Alertmanager
# http://localhost:9093/#/alerts

# Verify notification received in Slack/email

# Clean up
kubectl delete -f test-alert.yaml
```

**Expected outcome:** Test alert appears in Prometheus, Alertmanager, and notification channels.

---

### Step 7: Load Dashboards

Import the following dashboards in Grafana:

1. **Kubernetes Cluster** (ID: 7249)
2. **Node Exporter Full** (ID: 1860)
3. **Payment Processing Overview** (custom — import from your team)

**Steps:**
- Grafana > Create > Import
- Enter dashboard ID or paste JSON
- Select Prometheus datasource
- Click Import

**Expected outcome:** Dashboards load with data populated.

---

## Troubleshooting

### Issue: Prometheus Not Scraping Targets

**Symptoms:** Targets page shows `DOWN` or no targets listed.

**Diagnosis:**
```bash
# Check pod annotations
kubectl get pods -n Hyperswitch -o yaml | grep -A 5 prometheus.io

# Check Prometheus config is loaded
kubectl exec -it deploy/prometheus-server -n monitoring -- cat /etc/prometheus/prometheus.yml

# Check Prometheus logs
kubectl logs deploy/prometheus-server -n monitoring --tail=50
```

**Resolution:**
- Ensure pods have `prometheus.io/scrape: "true"` annotation
- Verify service discovery is configured for the correct namespace
- Check network policies allow Prometheus to reach pods

---

### Issue: No Logs in Loki

**Symptoms:** Log queries return empty results.

**Diagnosis:**
```bash
# Check Promtail pods are running
kubectl get pods -n monitoring -l app.kubernetes.io/name=promtail

# Check Promtail logs
kubectl logs -l app.kubernetes.io/name=promtail -n monitoring --tail=50

# Verify Promtail can reach Loki
kubectl exec -it daemonset/promtail -n monitoring -- wget -qO- http://loki:3100/ready
```

**Resolution:**
- Ensure Promtail daemonset is running on all nodes
- Check Loki is running and ready
- Verify Promtail configuration includes Hyperswitch namespace
- Check for network connectivity issues between Promtail and Loki

---

### Issue: Alerts Not Firing

**Symptoms:** Metric query returns data but alert doesn't trigger.

**Diagnosis:**
```bash
# Check alert rule is loaded
curl "http://localhost:9090/api/v1/rules" | jq '.data.groups[].rules[] | select(.name=="HighCPUUtilisation")'

# Check alert state
curl "http://localhost:9090/api/v1/alerts"

# Review Prometheus logs
kubectl logs deploy/prometheus-server -n monitoring | grep -i alert
```

**Resolution:**
- Verify `for` duration — alert must be active for this duration before firing
- Check `expr` query returns data when evaluated manually
- Ensure alert rule labels match routing configuration
- Check Prometheus has sufficient data (alerts may need 5-10 minutes of history)

---

### Issue: Notifications Not Received

**Symptoms:** Alerts show as firing in Alertmanager but no Slack/email received.

**Diagnosis:**
```bash
# Check Alertmanager logs
kubectl logs deploy/prometheus-alertmanager -n monitoring --tail=50

# Verify receiver configuration
curl http://localhost:9093/api/v1/status | jq '.config.receivers'

# Test alert routing
kubectl exec -it deploy/prometheus-alertmanager -n monitoring -- \
  amtool config routes test --config.file=/etc/alertmanager/alertmanager.yml severity=sev1
```

**Resolution:**
- Verify webhook URL and credentials in Alertmanager secret
- Check routing labels match alert labels exactly
- Ensure `continue: true` is set if multiple receivers should fire
- Review Alertmanager logs for delivery errors

---

### Issue: High Cardinality Metrics

**Symptoms:** Prometheus slow to query, high memory usage.

**Diagnosis:**
```bash
# Check label cardinality
curl "http://localhost:9090/api/v1/label/__name__/values" | jq '.data | length'

# Identify high-cardinality metrics
curl "http://localhost:9090/api/v1/status/tsdb" | jq '.data.headStats'
```

**Resolution:**
- Drop high-cardinality labels in relabel configs
- Increase scrape interval for less critical metrics
- Add recording rules for frequently queried aggregations
- Consider metric retention policies

---

### Issue: Grafana Datasource Errors

**Symptoms:** Dashboards show "DatasourceError" or no data.

**Diagnosis:**
```bash
# Test datasource connectivity
kubectl exec -it deploy/grafana -n monitoring -- \
  wget -qO- http://prometheus-server:9090/api/v1/status/targets

# Check Grafana logs
kubectl logs deploy/grafana -n monitoring --tail=50
```

**Resolution:**
- Verify datasource URL is correct (use cluster DNS names)
- Check network policies allow Grafana to reach Prometheus/Loki
- Ensure datasources are configured with correct access mode (Server)
- Re-import dashboards after fixing datasource

---

## Remote Monitoring (Enterprise)

For Enterprise Edition merchants:

- Metrics exported via Prometheus Remote Write
- Juspay Hyperswitch team provides proactive support
- Performance analysis and recommendations

Contact your account representative to enable remote monitoring.

---

## Logging Best Practices

- **Centralise logs** using ELK, Splunk, or Loki
- **Define retention policies** for compliance (typically 30-90 days)
- **Enable log rotation** to prevent disk exhaustion
- **Secure logs** with encryption and access control
- **Review logs periodically** for anomalies and security events
- **Structure logs** as JSON for easier parsing and querying
- **Include correlation IDs** across request flows for traceability

---

## Next Steps

After completing setup and validation:

1. [Configure custom dashboards](grafana-setup.md) for your specific use cases
2. [Review alert runbooks](runbooks.md) for each alert type
3. [Set up log aggregation](log-aggregation.md) for long-term storage
4. [Schedule regular monitoring reviews](sre-handbook.md) with your SRE team

---

## Quick Reference Commands

```bash
# Port forwards for debugging
kubectl port-forward svc/prometheus-server 9090:9090 -n monitoring
kubectl port-forward svc/grafana 3000:3000 -n monitoring
kubectl port-forward svc/loki 3100:3100 -n monitoring
kubectl port-forward svc/prometheus-alertmanager 9093:9093 -n monitoring

# Check pod status
kubectl get pods -n monitoring
kubectl get pods -n Hyperswitch

# View logs
kubectl logs -l app.kubernetes.io/name=prometheus -n monitoring --tail=100
kubectl logs -l app.kubernetes.io/name=grafana -n monitoring --tail=100

# Reload Prometheus config
kubectl exec -it deploy/prometheus-server -n monitoring -- kill -HUP 1

# Check metrics endpoints
curl http://localhost:9090/api/v1/targets
curl http://localhost:9090/api/v1/alerts
curl http://localhost:9090/api/v1/rules
```

---

## Document Information

| Field | Value |
|-------|-------|
| **Task** | TASK-010 Monitoring and Alerts |
| **Last Updated** | 2026-03-10 |
| **Applicable Versions** | Juspay Hyperswitch 1.0+ |
| **Maintainer** | SRE Team |