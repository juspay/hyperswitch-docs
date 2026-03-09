# System Requirements

### **Hardware**

The capacity is defined in terms of RPS or Requests per second.&#x20;

A single transaction may require 4 requests on average, and hence 40 RPS will approximately equal to a capacity of 10 transactions per second (TPS) and 25 million transactions per month.

However, the RPS to TPS ratio might vary based on various factors such as type of integration between merchant app and hyperswitch and variability in transaction patterns. It is recommended to provision for the peak TPS capacity expected from the users.

The production configuration recommended for 40 RPS capacity is as follows (excluding monitoring services).

#### **Baseline Requirements for 40 RPS -**&#x20;

| **HARDWARE REQUIREMENTS (40 RPS)** |                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes Cluster                 | <ul><li>Compute: 4 CPU cores </li><li>Memory: 16GB RAM </li><li>Nodes: 2 (Min)</li><li>Processor: Intel Xeon Platinum 8124M or equivalent (e.g., any modern multi-core x86_64 processor with similar performance capabilities)</li></ul> |
| Database Server                    | <ul><li>Compute: 2 CPU cores</li><li>Read: 8GB RAM</li><li>Storage: 1TB</li></ul>                                                                                                                                                        |
| Redis Cache                        | <ul><li>Compute: 1 CPU core</li><li>Read: 4GB RAM</li></ul>                                                                                                                                                                              |

{% hint style="info" %}
**Note:** For enterprise deployments, scaling without a buffer is not recommended. The following additional capacity should be provisioned:

* 30–50% headroom for traffic spikes and retries
* N+1 redundancy for node-level failures
* Additional margin for rolling deployments
* Autoscaling thresholds set below maximum utilization

For planning purposes, a 40% buffer for the application layer and 50% buffer for stateful components (Database and Redis) is recommended.

Detailed guidance for scaling Hyperswitch for enterprise payment systems can be found in the [**Scale & Reliability**](https://docs.hyperswitch.io/production-deployment/scale-and-reliability) section.&#x20;
{% endhint %}

### **Software**

Due to necessary time and cost considerations, only the Hyperswitch build compatible with specific operating systems, relational SQL and no-SQL databases has gone through the stringent PCI Software Security Standards (SSS) validation process.

It is strongly recommended to use the following software to ensure easy external validation such as PCI DSS certification and achieve the required performance from the installation.

Operating system

Linux version Ubuntu is 24.04 LTS is recommended.

Database

PostgreSQL version 14.x is recommended for persistent storage.&#x20;

Redis version 7.x is recommended for caching

Versioning

The [hyperswitch-suite](https://github.com/juspay/hyperswitch-suite) is a singular reference repository to be followed for application updates. This is to ensure compatibility across application components. Semantic versioning is followed across all application components.

The approved and listed software version appears as "Hyperswitch, Version: 1.x" on the [PCI SSC List of Validated Payment Software](https://listings.pcisecuritystandards.org/assessors_and_solutions/payment_software?agree=true), with the major version clearly indicated. Major version components only change when there are significant feature changes, or the changes impact any part of a security standard.

The stable releases are announced on a monthly basis on the [Releases page](https://github.com/juspay/hyperswitch-suite/releases). This will include notes on each application component which includes

* New features
* Bug fixes
* Database migrations
* Breaking changes (if any)<br>

A Continuous deployment engine automatically updates the nightly releases on a daily/ weekly basis. The nightly releases are developer builds which are not officially tested, nor deployed for production use (alpha).&#x20;

{% hint style="info" %}
**Note:** It is strongly recommended to not use the nightly releases in the production environment.
{% endhint %}

#### Devops software

Installing and managing Hyperswitch requires a good operational expertise on Kubernetes, Helm and Kubectl.

The minimum recommended versions for the devops software as follows:

* Kubernetes v1.22+
* Helm v3+
* Kubectl v1.28+
