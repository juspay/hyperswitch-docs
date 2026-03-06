---
icon: monitor-waveform
---

# Monitoring and Alerts

Reliable operation of a production Hyperswitch deployment requires comprehensive observability across **infrastructure, application behavior, and transaction performance**.

Observability in a Hyperswitch installation is based on two primary data sources:

| Element     | Description                                                                                          | Purpose                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Logs**    | Logs provide a chronological record of events and operations occurring within the system.            | Used for debugging, auditing, troubleshooting failures, and security analysis.          |
| **Metrics** | Metrics are numerical measurements collected over time representing system performance and behavior. | Used for performance monitoring, capacity planning, alerting, and operational analysis. |

Both logs and metrics together provide the necessary visibility to maintain **operational reliability, detect anomalies, and troubleshoot incidents** in production environments.

### Observability Stack

Hyperswitch integrates with a standard observability stack that combines logging, metrics collection, and visualization.

| Component                                             | Function                                                    |
| ----------------------------------------------------- | ----------------------------------------------------------- |
| Promtail                                              | Log scraping agent that collects logs from application pods |
| Grafana Loki                                          | Centralized log storage and query engine                    |
| OpenTelemetry Collector                               | Collects and exports application metrics                    |
| CloudWatch (or equivalent system monitoring platform) | Collects infrastructure and system metrics                  |
| Grafana                                               | Visualization platform used to build monitoring dashboards  |

This stack enables unified dashboards where operators can correlate:

* application metrics
* system resource utilization
* transaction behavior
* error patterns
* application logs

This correlation significantly reduces the time required to diagnose issues in production systems.

### Monitoring Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#ffffff',
  'primaryBorderColor': '#333333',
  'lineColor': '#333333',
  'secondaryColor': '#f5f5f5',
  'tertiaryColor': '#ffffff',
  'textColor': '#000000'
}}}%%

flowchart TD

A[Hyperswitch Application Pods] --> B[OpenTelemetry Collector]
A --> C[Promtail]

B --> D[Prometheus / VictoriaMetrics]
C --> E[Loki]

F[Node & Infrastructure Metrics] --> G[CloudWatch / Node Exporter]

D --> H[Grafana Dashboards]
E --> H
G --> H

D --> I[Remote Write]
I --> J[Hyperswitch Monitoring Environment]

H --> K[Operations & Engineering Teams]
J --> L[Hyperswitch Support Team]
```

#### Application Metrics

Hyperswitch services emit **application metrics** such as:

* request rates
* latency
* authorization success rates
* error rates

These metrics are collected through the **OpenTelemetry Collector**, which forwards them to a **metrics backend such as Prometheus**.

#### Infrastructure Metrics

Infrastructure metrics such as:

* node CPU usage
* memory consumption
* disk utilization
* network usage

are typically collected from the **cloud provider monitoring system** (for example CloudWatch or equivalent).

#### Log Collection

Application and system logs are collected by **Promtail**, which:

* scrapes logs from containers and nodes
* sends them to **Loki** for centralized log storage.

#### Visualization Layer

**Grafana** serves as the unified observability interface and provides:

* infrastructure dashboards
* application performance dashboards
* transaction success rate monitoring
* latency analysis
* error analysis

Grafana can visualize both:

* metrics (Prometheus / cloud metrics)
* logs (Loki)

#### Optional Enterprise Remote Monitoring

For **Enterprise Edition merchants**, a subset of metrics may be exported using **Prometheus Remote Write** to a **Hyperswitch-managed monitoring environment** to enable:

* proactive operational support
* performance analysis
* infrastructure optimization recommendations.

### Monitoring Dashboards

The monitoring package includes **pre-built Grafana dashboards** that provide real-time visibility into infrastructure health and payment processing performance.

The dashboards typically cover the following areas.

#### Kubernetes Cluster Monitoring

Infrastructure-level monitoring ensures that the underlying cluster remains healthy and capable of handling transaction workloads.

Tracked metrics include:

* CPU utilization by pods
* Memory utilization by pods
* CPU utilization by nodes
* Memory utilization by nodes
* Pod restart counts
* Node health status

These metrics help detect:

* resource exhaustion
* pod instability
* infrastructure bottlenecks

before they affect transaction processing.

#### Application Monitoring

Application dashboards provide visibility into API behavior and system performance.

Tracked metrics include:

* API route performance
* Request throughput by endpoint
* API latency (P95 / P99)
* HTTP status code distribution
* Error rates across services

These metrics allow operators to quickly identify:

* degraded API performance
* abnormal error patterns
* traffic spikes

#### Payment and Transaction Monitoring

Hyperswitch dashboards also provide deep insight into payment processing performance.

Tracked metrics include:

* Total transactions initiated
* Total transactions processed
* Authorization success rate
* Transaction status distribution
* Error codes returned by processors
* Payment method distribution
* Payment method level authorization rate
* Acquirer level authorization rate
* Metric segmentation by organization, account, and profile

These dashboards allow operators to detect:

* processor outages
* authorization rate degradation
* routing inefficiencies
* payment method performance issues

### Monitoring Configuration

Grafana dashboards are deployed as part of the Hyperswitch Helm installation.

The deployment process involves the following steps:

1. Deploy the monitoring stack components as part of the Kubernetes cluster.
2. Import the provided Grafana dashboard JSON files.
3. Configure the appropriate data sources for each dashboard.

Each dashboard requires selecting the appropriate data source at the top of the dashboard configuration.

<figure><img src="../.gitbook/assets/unknown (3).png" alt=""><figcaption></figcaption></figure>

Once configured, data typically begins appearing within a few minutes, provided that the monitoring agents are running correctly and metrics are being collected.

### Remote Monitoring (Enterprise Edition)

For merchants using the Enterprise Edition of Hyperswitch, optional **remote monitoring support** is available.

In this configuration, selected operational metrics are exported from the merchant's environment to a monitoring system maintained by the Hyperswitch team.

This allows the Hyperswitch team to:

* monitor transaction patterns and infrastructure utilization
* assist in troubleshooting production issues
* identify performance optimization opportunities
* provide proactive recommendations to improve authorization rates

### Remote Monitoring Configuration

Remote monitoring is implemented using the **Prometheus Remote Write API**.

The merchant's Prometheus server (or compatible monitoring system such as VictoriaMetrics) pushes selected metrics to a Prometheus instance maintained by the Hyperswitch team.

This configuration allows merchants to retain full control over which metrics are shared externally.

#### Setup Process

Before configuring remote monitoring, ensure that:

* Prometheus is running correctly in the Kubernetes cluster
* application metrics are visible in Grafana dashboards

The configuration process typically involves:

1. Obtaining the Prometheus remote-write configuration snippet from the Hyperswitch team.
2. Updating the Prometheus configuration to export selected metrics.
3. Reloading the Prometheus configuration.

Configuration reload can be triggered by sending a **SIGHUP signal** to the Prometheus process.

Infrastructure rules may also need to be updated to allow outbound connections to the Hyperswitch monitoring endpoint.

After configuration, verify that:

* remote write metrics are being exported successfully
* the Hyperswitch team confirms receipt of the metrics

Note: Remote monitoring is available only for merchants subscribing to the Enterprise Edition.

### Alerting

Alerting should be configured to proactively notify operators about abnormal system conditions.

Alerts should be categorized into **Infrastructure Alerts**, **Application Alerts**, and **Business Alerts**.

#### Infrastructure Alerts

Infrastructure alerts monitor system health and resource utilization.

| Condition                               | Severity |
| --------------------------------------- | -------- |
| CPU or memory usage > 80%               | Sev 1    |
| CPU or memory usage > 70%               | Sev 2    |
| CPU or memory usage > 60%               | Sev 3    |
| Health check endpoint returning non-2xx | Sev 1    |

Infrastructure alerts should apply to:

* application pods
* database instances
* Redis instances
* cluster nodes

#### Application Alerts

Application alerts monitor API behavior.

| Condition                  | Severity                               |
| -------------------------- | -------------------------------------- |
| 5xx API responses          | Sev 1 (if >1 request)                  |
| Abnormal 4xx response rate | Configurable based on merchant traffic |

These alerts help identify:

* application crashes
* integration failures
* misconfigurations

#### Business Alerts

Business alerts monitor the performance of payment processing.

| Condition               | Severity |
| ----------------------- | -------- |
| Success rate drop > 30% | Sev 1    |
| Success rate drop > 20% | Sev 2    |
| Success rate drop > 10% | Sev 3    |

These alerts should be configured for:

* overall authorization success rate
* payment method level success rate
* processor/acquirer level success rate

### Logging and Log Archival

Logging is essential for production environments for the following purposes:

* troubleshooting and debugging
* security monitoring
* compliance and auditing
* operational analysis

It is recommended to centralize logs using platforms such as:

* Elasticsearch / Logstash / Kibana (ELK Stack)
* Splunk
* Grafana Loki

The following practices should be implemented in production environments.

#### Log Retention

Application logs must be archived and retained in accordance with compliance requirements such as PCI DSS.

Retention policies should be defined based on organizational security policies.

#### Log Rotation

Automated log rotation must be configured to prevent excessive disk usage and ensure long-term system stability.

#### Security and Access Control

Logs should be protected through:

* encryption at rest
* encryption in transit
* restricted access for authorized personnel only

Although Hyperswitch does not log sensitive payment data, logs must still be handled securely to maintain compliance and prevent information leakage.

#### Log Review

Access logs and operational logs should be periodically reviewed to detect:

* unauthorized access
* suspicious system activity
* operational anomalies

This process is commonly required during security audits and PCI compliance reviews.
