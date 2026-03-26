---
description: Scale Hyperswitch deployments to handle high transaction volumes with enterprise-grade reliability
icon: arrows-maximize
---

# Scale and Reliability

This section provides reference guidance for scaling Hyperswitch deployments and ensuring their reliability in production environments.

The models presented here outline how compute, memory, database capacity, and caching layers should scale with increasing throughput. These guidelines assist operators in planning infrastructure capacity, designing resilient architectures, and validating system behavior through structured testing methodologies.

The sizing models are derived from internal testing and production observations. Actual requirements may vary depending on workload characteristics, payment method mix, infrastructure configuration, and database usage patterns.&#x20;

Merchants should validate all sizing assumptions through load testing before production deployment.

### Production Sizing and Node Architecture Model

Infrastructure at higher throughput must scale **horizontally**. Increasing memory or concentrating large numbers of pods on a single node is not recommended for production payment systems.

CPU generally scales approximately linearly with throughput, while memory scales per pod and per node. System stability depends heavily on maintaining controlled pod density and minimizing failure blast radius across worker nodes.

#### Terminology

* **RPS (Requests Per Second)** Number of API requests handled by the Hyperswitch Router.
* **TPS (Transactions Per Second)** Number of payment transactions processed by the system.

A single transaction may involve multiple internal API calls. As a result, **RPS is typically higher than TPS**.

For reference models in this document, an approximate conversion of:

**1 TPS ≈ \~7 API calls (RPS)**

is assumed.

Actual ratios may vary depending on payment flow configuration and enabled services.

#### 1. Application Layer (Kubernetes)

#### Architectural Assumptions

The reference scaling model assumes the following application characteristics:

* Services are **stateless**
* **Horizontal Pod Autoscaler (HPA)** is enabled
* Safe sustained throughput per pod is determined via load testing
* Reference baseline: **\~15 RPS per pod**
* **3 GB RAM requested per pod**
* **20% cluster memory headroom**
* Worker nodes sized at **64 GB RAM**
* Pod density maintained well below Kubernetes default limits

These assumptions provide predictable scaling behavior while maintaining operational stability.

#### Throughput-Based Scaling Formula

Let:

```
Safe_RPS_per_Pod = validated via load testing
Reference Example: 15 RPS
```

Then:

```
Required Pods = Peak_RPS / Safe_RPS_per_Pod

Total Application Memory =
Pods × 3 GB × 1.2 (memory safety buffer)

Total Application CPU =
Peak_RPS × 0.1 × 1.4 (CPU safety buffer)

Node Count =
Determined by memory, CPU, and pod density constraints
```

These calculations provide a baseline estimate for cluster sizing.

#### Pod Density Guidelines

Kubernetes allows up to **110 pods per node by default**, however operating close to this limit is not recommended for production systems.

Maintaining lower pod density improves:

* node stability
* resource isolation
* failure blast radius containment
* scheduling reliability during autoscaling events

**Recommended Pod Density Ranges:**

| Node Size | Recommended Pod Range |
| --------- | --------------------- |
| 32 GB     | 20–40 pods            |
| 64 GB     | 30–60 pods            |
| 128 GB    | 50–90 pods            |

Best practices:

* Maintain pod count below **\~70% of configured `maxPods`**
* Distribute pods across **multiple nodes and availability zones**
* Avoid high pod concentration on a single node

Even if technically possible through configuration adjustments, placing **150–200 pods on a single node is strongly discouraged**.

#### Autoscaling Recommendations

The **Horizontal Pod Autoscaler (HPA)** should be configured to scale application pods based on CPU utilization and request throughput.

Recommended baseline thresholds:

| Metric                 | Recommendation             |
| ---------------------- | -------------------------- |
| Target CPU Utilization | 60–65%                     |
| Scale Up Trigger       | Sustained utilization >70% |
| Scale Down Threshold   | Sustained utilization <40% |

Autoscaling should be configured with sufficient headroom to absorb sudden traffic bursts without triggering aggressive scaling oscillations.

#### Availability Zone Distribution

All production deployments should span **at least two availability zones**, with **three zones recommended** for high availability.

Application pods should be distributed using:

* Kubernetes **topology spread constraints**
* **Pod anti-affinity rules**
* Node groups distributed across zones

This design reduces the impact of node failures or zone-level outages.

#### Reference Sizing Table (Application Layer)

Assumptions:

* 15 RPS per pod
* 3 GB RAM per pod
* 20% memory buffer
* 64 GB worker nodes
* Target pod density: \~40–50 pods per node

| Peak RPS | Pods Required | App CPU (vCPU) | Total App RAM (GB) | Recommended Nodes (64 GB) |
| -------- | ------------- | -------------- | ------------------ | ------------------------- |
| 40       | 3             | 6              | 11                 | 2                         |
| 100      | 7             | 14             | 25                 | 2                         |
| 200      | 14            | 28             | 50                 | 2                         |
| 500      | 34            | 70             | 122                | 3                         |
| 1000     | 67            | 140            | 241                | 5                         |
| 2000     | 134           | 280            | 482                | 10                        |
| 3000     | 200           | 420            | 720                | 14                        |

Notes:

* Node count reflects balanced memory usage and safe pod density.
* CPU limits must also be validated against chosen node types.
* All production clusters should span **multiple availability zones**.
* Autoscaling thresholds should avoid sustained utilization above **65–70%**.

#### 2. Database Capacity Planning Model

The following model provides baseline guidance for scaling the primary transactional database.

Baseline reference deployment:

* **Writer node:** 4 vCPU
* **Reader node:** 2 vCPU
* **20 IOPS per transaction**
* **2.5× IOPS safety factor**
* **16 KB per transaction**
* **5× storage safety factor**

#### Reference Sizing Table

| Peak TPS | Writer vCPU (Aggregate) | Reader vCPU (Aggregate) | Recommended RAM     | Required IOPS (TPS × 50) |
| -------- | ----------------------- | ----------------------- | ------------------- | ------------------------ |
| 40       | 4                       | 2                       | 16–32 GB            | 2,000                    |
| 100      | 10                      | 5                       | 32–64 GB            | 5,000                    |
| 200      | 20                      | 10                      | 64–128 GB           | 10,000                   |
| 500      | 50                      | 25                      | 128–256 GB          | 25,000                   |
| 1000     | 100                     | 50                      | 256–512 GB          | 50,000                   |
| 2000     | 200                     | 100                     | 512 GB – 1 TB       | 100,000                  |
| 3000     | 300                     | 150                     | 1 TB+ (partitioned) | 150,000                  |

{% hint style="info" %}
#### Important Clarifications

The vCPU numbers above represent **aggregate compute capacity**, not a recommendation to deploy a single large instance.

Example:

At **1000 TPS**, instead of a single 100-vCPU writer:

Use **multiple 16–32 vCPU nodes** through partitioning or sharding strategies.
{% endhint %}

#### RAM Scaling Considerations

RAM requirements do not scale strictly linearly.

Memory usage depends on:

* working set size
* index size
* active connections
* cache hit ratio
* replication overhead

Beyond **256–512 GB per node**, vertical scaling becomes inefficient.

At this stage, horizontal strategies are recommended:

* read replicas
* logical sharding
* partitioned datasets

#### Storage and IOPS

IOPS requirements are derived as:

```
IOPS = TPS × 50
```

Recommendations:

* Provisioned IOPS storage is recommended beyond **10,000 sustained IOPS**
* Burst-credit storage classes should **not be used for production payment workloads**

#### Connection Pooling

High throughput deployments should use **connection pooling** to prevent excessive database connections from application pods.

Recommended approaches include:

* PgBouncer
* built-in connection pooling solutions
* managed pooling layers provided by database platforms

#### 4. Redis Scaling Model

Redis is typically used for caching, session management, and high-frequency lookups.

Baseline deployment for **40 TPS / \~280 RPS**:

* **3 primary shards**
* **1 replica per shard**
* **6 total nodes**
* **2 vCPU per node**
* **\~8 GB RAM per node**

#### Reference Scaling Table

| Peak RPS | Equivalent TPS | Primary Shards | Replicas per Shard | Total Nodes | vCPU per Node | Memory per Node | Total Primary Memory |
| -------- | -------------- | -------------- | ------------------ | ----------- | ------------- | --------------- | -------------------- |
| 280      | 40             | 3              | 1                  | 6           | 2             | \~8 GB          | \~24 GB              |
| 500      | \~70           | 4–5            | 1                  | 8–10        | 2             | \~8 GB          | 32–40 GB             |
| 1000     | \~140          | 8–9            | 1                  | 16–18       | 2             | \~8 GB          | 64–72 GB             |
| 2000     | \~285          | 12–15          | 1                  | 24–30       | 4             | \~16 GB         | 192–240 GB           |

Redis clustering is preferred over large single-node deployments.



### System Testing

Production systems must be validated under controlled testing scenarios to ensure both performance and resilience.

Two critical testing methodologies should be performed before production deployment.

#### Load Testing

Load testing validates system throughput capacity and resource utilization under sustained traffic.

#### Implementation Steps

**1. Download Load Test Script**

Clone the repository:

```
https://github.com/juspay/hyperswitch-suite/tree/main/load-test
```

Extract the contents to a local directory.

**2. Verify Prerequisites**

Ensure the following tools are installed:

Python ≥ 3.7

```
python3 --version
```

pip

```
pip3 --version
```

PostgreSQL client ≥ 13

```
psql --version
```

Ensure the Hyperswitch server is running.

**3. Navigate to Load Test Directory**

```
cd load-test
```

**4. Run Setup Script**

```
bash setup.sh
```

This installs required Python dependencies.

**5. Provide Required Configuration**

You will be prompted to enter:

* Hyperswitch server URL
* Admin API key

**6. Enable Grafana Monitoring**

To monitor system behavior during testing:

Provide:

* Grafana URL
* Service token
* Username
* Password

If using the internal Grafana service:

```
Username: admin
Password: admin
```

**7. Enable Storage Monitoring**

Provide PostgreSQL credentials:

* username
* password
* database name
* host
* port

If skipped, the script will generate a SQL query which can be executed manually.

**8. Load Test Report**

The generated report can be found at:

```
output/report.pdf
```

#### Chaos Testing and Fault Tolerance Validation

Chaos testing validates the system’s resilience under partial service outages.

#### Objective

Ensure the **Hyperswitch Router** continues processing payment requests even when dependent services become unavailable.

#### Services That May Be Disrupted

Core services:

* Token service
* Consumer
* Producer

Analytics stack:

* Grafana
* Loki
* ClickHouse
* Kafka
* OpenSearch
* Prometheus / Vector

#### Implementation Guidelines

**Graceful Degradation**

Dependent services may fail without affecting core routing functionality.

**Health Checks**

Services should report failures without blocking request processing.

**Observability**

All failures should be logged for operational visibility.

#### Success Criteria

The system is considered resilient if:

* Router continues processing payment requests normally
* No customer-facing impact occurs
* Core routing logic remains operational
* Router latency and error rates remain within acceptable operational thresholds

### Infrastructure Segmentation & Isolation

Production deployments should isolate core application workloads from supporting services to improve both reliability and security.

Recommended isolation principles:

* Monitoring services should run in a **separate node group**
* Event and logging systems should run in **separate node groups**
* Remote monitoring and observability components should not share compute resources with the core router

This segmentation prevents non-critical workloads from affecting payment processing performance.
