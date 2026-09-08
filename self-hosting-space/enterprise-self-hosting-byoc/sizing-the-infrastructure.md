---
description: >-
  A worked out reference for 25 million transactions per month, with the sizing
  rationale for each layer using AWS instances as a reference.
icon: ruler-combined
---

# Sizing the infrastructure

***

## Reference architecture

This is complete, per-service footprint at a common entry-level production volume for enterprise self-hosting. You may use it as a starting point and adjust against your own inputs.

### Traffic assumptions

The sizign approach on this page derives from these three numbers.

| Metric                     | Value                    |
| -------------------------- | ------------------------ |
| Monthly transaction volume | 25 million               |
| Transactions per second    | \~10 TPS                 |
| Requests per second        | \~70 RPS (1 TPS = 7 RPS) |
| Traffic spikes             | Not applicable.          |

The request rate assumes **7 requests per transaction**.&#x20;

While the ratio is a standard, it may also be affected based on your integration pattern, business use cases.

### Application cluster

**Hyperswitch OLTP application running on 1 pod with 1 vCPU can handle approximately 40 RPS**. Hence it needs a minimum of 2 vCPUs — the minimums below are higher because two pods is a capacity floor, not an availability posture.

Three principles shape this table:

* **Every service runs at least two pods:** With additional buffer on critical services. The writer path carries the most.
* **Maximum pods and nodes are set high for critical services:** These are ceilings for spiky traffic, not provisioned capacity. Setting them low saves nothing and caps your ability to absorb a surge. Superposition is the exception: it does not scale with traffic, so its ceiling stays low.
* **Node instance types are deliberately diverse:** Listing several instance types prevents a chokepoint if one type cannot be provisioned due to regional or technical unavailability. This is a real failure mode during a scale-up event, and it is free to avoid.

Services fall into three classes, and the class determines how you size it:

* **Traffic-scaled:** Footprint tracks TPS directly. Size from the 40 RPS-per-vCPU figure and give the critical ones extra minimum pods.
* **Stateless:** Scales horizontally without constraint, since there is no session or persistent state to coordinate.
* **Operator-scaled:** Load comes from the number of users using it, not necessarily from payment volume. It can stay small regardless of TPS.

<table><thead><tr><th>Service</th><th>Class</th><th width="100.96484375">Min pods</th><th width="84.1953125">Max pods</th><th>CPU request/limit</th><th>Memory request/limit</th></tr></thead><tbody><tr><td>OLTP Router</td><td>Traffic-scaled</td><td>5</td><td>50</td><td>1 / 1.5 core</td><td>1 / 1.5 GB</td></tr><tr><td>OLAP Router</td><td>Traffic-scaled</td><td>3</td><td>50</td><td>1 / 1.5 core</td><td>1 / 1.5 GB</td></tr><tr><td>Payment Methods</td><td>Traffic-scaled</td><td>To be added</td><td>To be added</td><td>To be added</td><td>To be added</td></tr><tr><td>Decision Engine</td><td>Traffic-scaled</td><td>2</td><td>50</td><td>0.4 / 1 core</td><td>400 MB / 1 GB</td></tr><tr><td>Connector Service</td><td>Stateless</td><td>To be added</td><td>To be added</td><td>To be added</td><td>To be added</td></tr><tr><td>Superposition</td><td>Operator-scaled</td><td>2</td><td>5</td><td>1 / 1.5 core</td><td>2 / 3 GB</td></tr><tr><td>Control Center</td><td>Operator-scaled</td><td>To be added</td><td>To be added</td><td>To be added</td><td>To be added</td></tr></tbody></table>

**Payment Methods** is deployed as a separate release of the same chart and image as the router, so it can scale independently of it. Expect a traffic-scaled profile similar to the router's, if the payment flows are significantly saved card payments or recurring transactions.

**Connector Service** is stateless. It carries payment processor integrations, so its load tracks outbound call volume rather than inbound TPS. If your transaction mix weighted toward connectors that need multiple calls per payment will push it harder than the transaction count suggests. However, being stateless, it takes a high ceiling safely.

**Control Center** serves the operator dashboard. Its load comes from concurrent operators, not from payment volume. If the control center is only for your internal use, two pods for availability is usually sufficient; raise it with the Juspay support team, only if you distribute the dashboard across 1000s of users, or have significant analytics use.

**Node pool**, shared across all the above services shall be:

|                                             | Value                                                                                  |
| ------------------------------------------- | -------------------------------------------------------------------------------------- |
| Minimum nodes                               | 3                                                                                      |
| Maximum nodes                               | 50                                                                                     |
| Instance types (AWS instances as reference) | `c5.2xlarge`, `c5a.2xlarge`, `c6a.2xlarge`, `c5.4xlarge`, `c5a.4xlarge`, `c6a.4xlarge` |

**Payment processing is not the only consumer of cluster compute.** The service mesh, Kubernetes management overhead and telemetry daemon sets all require vCPU on every node.&#x20;

These are routinely omitted from first-pass estimates, and cross validated during the load testing in Milestone IV.

### Application database

**Both writer and reader are sized at 4 vCPU.** The workload is write-heavy, and the reader sits on the failover path — undersizing it means failing over into an instance that cannot carry the load.

**IOPS is derived at 20 per transaction**, extrapolated to 10 TPS with a 5× safety factor to absorb connection spikes up to 1,000 concurrent connections.

The database shall run on Multi-AZ with a primary writer and a secondary read replica.

| Service         | vCPU        | Memory      | IOPS        | Instance    |
| --------------- | ----------- | ----------- | ----------- | ----------- |
| OLTP Service    | 4           | \~64 GB     | 1,000       | `r5.xlarge` |
| Superposition   | 2           | \~16 GB     | —           | `r5.large`  |
| Decision engine | To be added | To be added | To be added | To be added |

#### How the databases are grouped?

Two deliberate decisions here, and both save cost without compromising isolation where it matters.

**OLTP Router, Payment Methods and Decision Engine share one physical database** with logical separation — three schemas, one per service. They have compatible access patterns and a shared failure domain is acceptable between them.

**Connector Service needs no database or cache** — it is stateless by design. **Control Center** reads through the reader database (replica) rather than holding its own. However, payment. list, analtiucs may demands heavy read workload. In such case it is advisable to not use the reader and have a dedicated database instance with replication.

**Superposition runs standalone.** It is not a critical-path service as it can run from cache, and its usage pattern should not be able to interfere with Hyperswitch. It needs no read replica either.&#x20;

### Cache

Redis runs in **cluster mode** with a multi-shard, multi-node setup, at least one replica per node, and Multi-AZ enabled.

<table><thead><tr><th width="172.0703125">Services</th><th width="91.2890625">vCPU</th><th width="89.3984375">Memory</th><th width="120.296875">Nodes per shard</th><th width="84.69921875">Shards</th><th>Instance</th></tr></thead><tbody><tr><td>Rate limiter, OLTP Router, Superposition, Decision Engine, Card Vault</td><td>2</td><td>>6 GB</td><td>2 — master and replica</td><td>3</td><td><code>m5.large</code></td></tr></tbody></table>

Three shards with a master and replica each gives **six nodes in total**. Cluster mode allows shards to be added later without re-architecting.

### Card vault

{% hint style="info" %}
Note:[ ](#user-content-fn-1)[^1]Deploy this only if you store card data yourself — the decision is made in the blueprint and it determines your PCI scope.
{% endhint %}

**Roughly 50% of transactions are assumed to touch the vault**, so 10 TPS translates to about 5 TPS of vault traffic.

<table data-header-hidden><thead><tr><th width="313.65625"></th><th>10 TPS</th></tr></thead><tbody><tr><td>Vault traffic</td><td>~5 TPS</td></tr><tr><td>Compute</td><td>~8 vCPU</td></tr><tr><td>Memory</td><td>16 GB</td></tr><tr><td>Instance</td><td>2 × <code>c5.xlarge</code></td></tr></tbody></table>

**The vault is not operated on Kubernetes and cannot autoscale.** The key custodian model means a new instance cannot join the pool without human intervention, so capacity cannot expand when traffic surges.  Hence, replicas and capacity must be provisioned for your **peak**, deliberately over-provisioned for safety.

### Card vault database

Multi-AZ with a writer and reader, on the same write-heavy reasoning as the application database.

| Compute  | \~4 vCPU — writer 4, reader 2 |
| -------- | ----------------------------- |
| Memory   | \~48 GB                       |
| IOPS     | To be added                   |
| Storage  | To be added                   |
| Instance | To be added                   |

### Monitoring and logging

| Compute  | To be added |
| -------- | ----------- |
| Memory   | To be added |
| Instance | To be added |

**This layer does not scale linearly with TPS.** Its footprint is driven by the number of components emitting telemetry, metric cardinality and log retention. The sizing is dependent on component count and retention policy instead.

### What this does not include?

Size the below components seperately.

* **Analytics and data processing** **service** — ClickHouse, Kafka, OpenSearch and the Sessionizer.
* **Ingress, egress and content delivery** **service** — Sized separately, and often already provided at organization level.

### Scaling from the baseline setup of 10 TPS

The 10 TPS architecture is a baseline, not a ceiling. When your inputs differ:

<table><thead><tr><th width="354.90234375">If</th><th>Then</th></tr></thead><tbody><tr><td>Your requests-per-transaction ratio is higher</td><td>Scale pod counts and database IOPS proportionally. This ratio drives both</td></tr><tr><td>Peaks are frequent or sustained</td><td>Raise minimum pods rather than relying on the ceiling; autoscaling has a lag the payment path may not tolerate</td></tr><tr><td>You deploy the card vault</td><td>Add its footprint, provisioned for peak, and its own Multi-AZ database</td></tr><tr><td>You need dashboard analytics at volume</td><td>Add the data processing stack, manually provisioned</td></tr><tr><td>Exptected throughput grows past roughly 400 TPS</td><td>Treat it as an architecture conversation — the data layer reaches single-instance limits.</td></tr></tbody></table>

{% hint style="info" %}
The infra sizing is verified in Milestone IV during the load test and in Milestone V by monitoring the saturation limits. The sixing figure may get tweaked as the traffic proves the estimates.
{% endhint %}



[^1]: 
