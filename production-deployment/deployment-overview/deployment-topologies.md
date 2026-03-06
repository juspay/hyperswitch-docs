# Deployment Topologies

There are two primary deployment topologies to enhance the reliability of enterprise setups:

1. Multi Region Active - Active Setup
2. Multi Region Active - Passive Setup

### Multi-Region Active-Active Setup

In an Active-Active setup, the merchant would deploy Hyperswitch instances in multiple geographically separate regions, with both regions actively processing traffic simultaneously. A CDN distributes incoming requests across both regions.&#x20;

This setup offers the highest level of availability and can also improve performance by routing users to the nearest available instance.

<figure><img src="../../.gitbook/assets/ChatGPT Image Mar 6, 2026 at 01_06_10 PM.png" alt=""><figcaption></figcaption></figure>

#### Implementation

1. Infrastructure Duplication: Identical infrastructure in multiple regions.
2. Database Synchronization: This is the most complex part. Introducing KV (Redis) and a drainer, which helps in keeping the database sync across the regions.
3. Affinity Proxy: This service helps in the stickiness part. A transaction which started in one stack should always go to the same stack, because of the delayed sync in the data.

#### Pros:

* Extremely Low Downtime: Near-zero downtime (RTO: 30 secs, RPO: 30 secs) as traffic is automatically routed away from failing instances or regions.
* Highest Availability: Provides the highest level of resilience against regional outages.
* Potential Cost Optimization: While initial setup is costly, it can be more cost-effective than Active-Passive if both regions are fully utilized, as there's no idle infrastructure.

#### Cons:

* Complexity: The most complex option to implement and manage, primarily due to database synchronization and affinity control.

Initial Cost: Requires upfront investment in infrastructure.

### Multi Region Active - Passive Setup

In an Active - Passive setup, the merchant would deploy two identical Hyperswitch stacks in geographically separate regions. Active region handles all live traffic, while Passive remains on standby. The passive instance is kept in sync with the active instance, typically through database replication and configuration management. In the event of a failure in the active region, traffic is switched over to the passive region with a DB flip.

<figure><img src="../../.gitbook/assets/ChatGPT Image Mar 6, 2026 at 01_23_20 PM.png" alt=""><figcaption></figcaption></figure>

#### Implementation

1. Infrastructure Duplication: Provision identical server infrastructure (VMs, networking, storage) in a secondary, geographically distinct region.
2. Database Replication: Implement Asynchronous database replication from the active region's database to the passive region's database. This is critical for data consistency.
3. Failover Mechanism: Implement a mechanism (DNS failover, load balancer failover, or manual switch) to redirect traffic to the passive region upon detection of an active region failure. This involves updating DNS records and a DB flip.

#### **Pros:**

* Very Low Downtime: In case of a regional outage, downtime is limited to the failover time (RTO: <10 mins, RPO: 30 secs)
* Disaster Recovery: Provides excellent protection against regional disasters.

#### **Cons:**

* High Cost: Requires duplicating the entire infrastructure stack.
* Operational Overhead: Maintaining two identical environments, including database replication and configuration synchronization
