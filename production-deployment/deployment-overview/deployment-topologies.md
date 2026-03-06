# Deployment Topologies

There are two primary deployment topologies to enhance the reliability of enterprise setups:

1. Multi Region Active - Active Setup
2. Multi Region Active - Passive Setup

### Multi-Region Active-Active Setup

In an Active-Active setup, the merchant would deploy Hyperswitch instances in multiple geographically separate regions, with both regions actively processing traffic simultaneously. A CDN distributes incoming requests across both regions.&#x20;

This setup offers the highest level of availability and can also improve performance by routing users to the nearest available instance.

<figure><img src="../../.gitbook/assets/ChatGPT Image Mar 6, 2026 at 05_53_52 PM.png" alt=""><figcaption></figcaption></figure>

#### Implementation

1. **Infrastructure Duplication:** Identical infrastructure in multiple regions.
2. **Database Synchronization:** This is achieved by introducing a **distributed key-value store (Redis)** and a **drainer service**. The application publishes database change events to Redis, which are then consumed by the drainer to replicate the corresponding updates to the secondary region. This mechanism ensures near real-time propagation of state changes between regions while minimizing coupling between the primary transaction flow and cross-region replication.
3. **Affinity Proxy:** Ensures request stickiness by maintaining transaction-level routing affinity. Once a transaction begins processing in a specific region, all subsequent requests related to that transaction are directed to the same region. This prevents inconsistencies that could arise if requests are routed to a region where the latest transaction state has not yet been replicated.

#### Pros:

* **Extremely Low Downtime:** Near-zero downtime **(RTO ≈ 30 seconds, RPO ≈ 30 seconds)** as traffic can be automatically routed to healthy regions during failures.
* **High Availability:** Active-Active deployments provide strong resilience against infrastructure or regional outages.
* **Efficient Infrastructure Utilization:** Both regions actively process production traffic, improving infrastructure utilization compared to Active-Passive architectures.

#### Cons:

* **Operational Complexity:** Requires careful management of cross-region database synchronization, transaction affinity, and distributed system behavior.
* **Higher Initial Setup Effort:** Implementing Active-Active infrastructure requires additional routing, synchronization, and monitoring components compared to simpler deployment models.

### Multi Region Active - Passive Setup

In an Active - Passive setup, the merchant would deploy two identical Hyperswitch stacks in geographically separate regions. Active region handles all live traffic, while Passive remains on standby. The passive instance is kept in sync with the active instance, typically through database replication and configuration management. In the event of a failure in the active region, traffic is switched over to the passive region with a DB flip.

<figure><img src="../../.gitbook/assets/ChatGPT Image Mar 6, 2026 at 01_23_20 PM.png" alt=""><figcaption></figcaption></figure>

#### Implementation

1. **Infrastructure Duplication:** Provision identical infrastructure in a secondary, geographically separate region. This includes compute resources, networking configuration, storage, and all supporting platform components to ensure environment parity.
2. **Database Replication:** Configure **asynchronous database replication** from the primary region to the secondary region to maintain data continuity. Replication lag determines the achievable Recovery Point Objective (RPO).
3. **Failover Mechanism:** Implement a controlled failover mechanism to redirect traffic to the secondary region when a primary region outage is detected. This can be achieved through **DNS failover, load balancer failover, or an operational failover procedure**, typically accompanied by a database role switch (DB flip).

#### Pros

* **Low Downtime During Failover:** In the event of a regional outage, service restoration time is limited to the failover window (**RTO < 10 minutes, RPO ≈ 30 seconds** **depending on replication delay)**.
* **Strong Disaster Recovery Posture:** Provides effective protection against regional failures by maintaining a ready standby environment.

#### Cons

* **Higher Infrastructure Cost:** Requires provisioning and maintaining a fully replicated infrastructure stack in a secondary region.
* **Operational Management Overhead:** Requires ongoing management of environment parity, database replication health, and failover readiness procedures.
