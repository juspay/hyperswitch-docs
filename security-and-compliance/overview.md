---
description: >-
  A brief summary of Hyperswitch infrastructure ensuring compliance and data
  privacy
---

# 🔏 Overview

## Data center locations <a href="#docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715" id="docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715"></a>

Hyperswitch Cloud is hosted on the AWS platform and served out of the US (N.Virginia region) by default. Hyperswitch is listed partner on [AWS Partner Network](https://partners.amazonaws.com/partners/0018W00001wtpU1QAI/Juspay#solutions--tech-product).

We support deployments in more geographies for merchants who wish to restrict data transfer across geographies. Each deployment is supported with at least two redundant Availability Zones for ensuring reliability.

<table><thead><tr><th width="180"></th><th width="304">Global Server (US)</th><th>EU Residency Server</th></tr></thead><tbody><tr><td>Live endpoints</td><td><code>api.hyperswitch.io</code></td><td>Available on request</td></tr></tbody></table>

{% hint style="success" %}
**Note:** Hyperswitch is a super lightweight payment switch with Infrastructure-as-Code capability. So we can quickly deploy in new geographies (AWS regions) as data residency requirements emerge across countries around the world.
{% endhint %}

## Latency

The application latency of Hyperswitch is optimized to `sub-30 milliseconds` (90 percentile) to ensure that the application by itself does not add any latency cost. [Read here](https://docs.hyperswitch.io/learn-more/hyperswitch-architecture/a-payments-switch-with-virtually-zero-overhead) to know more about it.

Inter-regional network latency is optimized by fronting the API endpoints with Cloud Delivery Network (AWS Cloudfront).

{% hint style="info" %}
**Note:** In case you are opting for the Hyperswitch Open Source offering, you will be able to run the software like a microservice within your own deployment.
{% endhint %}

## Reliability

Reliability is ensured as a primitive in each component of Hyperswitch to offer 99.99% uptime guarantee.

All infrastructure components are deployed across multiple Availability Zones. This includes:

* Load Balancers
* Proxy instances for incoming and outgoing APIs
* Kubernetes clusters powering core application, analytics and async services
* Aurora PSQL Database (primary storage)
* Elasticache storage (cache)
* Vault service

## Scalability

Hyperswitch support for 80 RPS per merchant account and rate limits applicable beyond. Higher enterprise workloads can be processed on request basis.

### Scaling Infrastructure components

Scaling of each component in the Hyperswitch setup is achieved as follows

* Incoming proxy layer is deployed using Auto Scaling Group (ASG)
* Application layer is managed using Kubernetes with Horizontal Pod Autoscaler (HPA)&#x20;
* Outgoing Proxy is deployed using Auto Scaling Group (ASG)

### Handling traffic spikes

Database provides consistency, but it more often becomes a bottleneck and a failure point in case of sudden traffic spikes. Hyperswitch can be configured (on request basis) to use Cache as Data storage in case of sudden spikes in the traffic to reduce the friction of database latency. All the data is drained from cache to the database.

