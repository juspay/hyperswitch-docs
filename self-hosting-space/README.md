---
description: >-
  Deploy and operate Hyperswitch within your own infrastructure. Start here to
  choose your preferred support model, your cloud provider, and how your
  infrastructure gets provisioned.
icon: globe
---

# Running Hyperswitch on your own cloud

***

### How to get started?

Hyperswitch can be deployed inside any Kubernetes compatible cloud provider or on-premise setup. You can retain full control of your payment stack soveriegnity, data residency, your compliance boundary, and your infrastructure spend.&#x20;

Infra-as-code recipes using Terraform are readily available for AWS, GCP, Azure and Oracle. The framework is extensible to alternative cloud providers like Digital Ocean, OVH cloud, Stack IT, Tencent and more.

This section helps you make three decisions before you begin production certification process for you self-hosted hyperswitch stack. Each takes a few minutes and determines which guide you will follow next.

{% hint style="info" %}
**Just exploring?**&#x20;

You can try [Run Hyperswitch locally with Docker Compose](enterprise-self-hosting-byoc/readme-1/unified-local-setup-using-docker/) or [Quickstart on your cloud using Helm charts](enterprise-self-hosting-byoc/readme/). This is is the quickest path to a proof of concept.&#x20;

Both are options are for evaluation only, and neither is a production path.
{% endhint %}

***

### Decision 1 — How much do you want to operate?

Juspay provides three flexible tiers of Enterprise support models to enable enterprises to self-host Hyperswitch. Each support tiers determine who operates the stack, who monitors it, and what Juspay commits to, and you can choose your preferred model.

|                                                   | Tier 1 : Managed                         | Tier 2 : Co-Managed                      | Tier 3 : Self-Managed                          |
| ------------------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------------- |
| **Who operates the stack?**                       | Juspay                                   | Merchant                                 | Merchant                                       |
| **Who manages uptime?**                           | Juspay                                   | Merchant                                 | Merchant                                       |
| **Who owns observability plane software?**        | Juspay                                   | Juspay                                   | Merchant                                       |
| **Who detects issues?**                           | Juspay, 24×7                             | Juspay and Merchant, 24×7                | Merchant, 24×7                                 |
| **Who diagnoses and recommends**                  | Juspay, 24×7 support for severity issues | Juspay, 24×7 support for severity issues | Merchant; Juspay consult during business hours |
| **Who deploys changes**                           | Juspay                                   | Merchant                                 | Merchant                                       |
| **Who adds feature enhancements to the software** | Juspay                                   | Juspay                                   | Juspay                                         |

#### What each side commits to?

<table><thead><tr><th width="158.2890625"></th><th width="186.21875">Tier 1 — Juspay Managed</th><th width="200.3671875">Tier 2 — Co-Managed</th><th>Tier 3 — Self-Managed</th></tr></thead><tbody><tr><td><strong>Juspay commits to</strong></td><td>Full uptime guarantee, with response and recovery targets</td><td>Issue detection, response and recommendation — proactive and on demand</td><td>Best-effort support during business hours — on demand only</td></tr><tr><td><strong>You commit to</strong></td><td>Full on-premise access and ownership for the Juspay team</td><td>Technical SPOC available 24×7, on-call team, adherence to prerequisites and deployment runbooks</td><td>Managing the deployment end to end</td></tr></tbody></table>

{% hint style="info" %}
**The distinction that matters most in the above models is uptime ownership, issue detection and change ownership.**&#x20;

In Tiers 1 and 2 Juspay owns the observability plane and watches your platform around the clock, whether or not we deploy the fix. In Tier 3 detection is yours, and we assist on request during business hours.&#x20;

* **Tier 1 is the best model**, if you do not have an in-house payments team but wish to self host, by fully outsourcing the ownership to Juspay team
* **Tier 2 is the best model**, if you prefer your in-house payments team to fully manage the stack, with Juspay team's expert support to complement your inhouse payments team. The juspay support will be in terms of installation, ongoing monitoring, feature developments and solution consultation.
* **Tier 3 is the best model**, if you are fully confident on fully managing the stack, but need Juspay team' support for installion, ongoing agile feature addition and solution consultation.
{% endhint %}

***

### Decision 2 — Which cloud provider?

Hyperswitch is cloud-agnostic by design — the application, its Helm charts and its container images are identical on every cloud provider. The surrounding infrastructure automation varies across cloud providers and enhanced regularly.

Terraform provisions the infrastructure your cluster runs on. Helm deploys Hyperswitch onto that cluster. This is the recommended approach for every production deployment. The coverage of infra  structure automation across cloud providers as below.

<table><thead><tr><th width="145.2578125">Cloud</th><th width="261.421875">Infrastructure as Code approach</th><th width="187.0234375">Automation coverage</th><th>Status</th></tr></thead><tbody><tr><td><strong>AWS</strong></td><td>Terraform + Helm</td><td>90%</td><td>Validated</td></tr><tr><td><strong>GCP</strong></td><td>Terraform + Helm</td><td>80%</td><td>Validated</td></tr><tr><td><strong>Azure</strong></td><td>Terraform + Helm</td><td>80%</td><td>In beta</td></tr><tr><td><strong>Oracle Cloud</strong></td><td>Terraform + Helm</td><td>80%</td><td>In beta</td></tr><tr><td><strong>Other / On-premise</strong></td><td>Helm on any managed Kubernetes setup</td><td>Varies</td><td>-</td></tr></tbody></table>

***

### Decision 3 — Strategy to provisions the infrastructure

The final decision you will have to take is, how much of infrastructure to be created with reference Terraform scripts and, how much you bring in.

If you are an enterprise user, you will not be starting from an empty cloud account. You have a landing zone, an account hierarchy, network standards, an IAM model, and a dedicated platform team that owns them. However, **that does not mean you should hand-build the Hyperswitch stack.** Our Terraform modules are designed to be adopted inside your existing infrastructure, not only alongside a clean account.

#### Path A — Provision Hyperswitch stack using reference Terraform modules _(recommended)_

Our Terraform modules can create the resources Hyperswitch needs. Helm then deploys the application onto them. This is the path assumed for our Enterprise self hosting production certification process.&#x20;

It represents the exact reference architecture, production blue print, PCI scoping guidance, infra sizing approach, relability configurations models which is leveraged by Juspay team on the Hyperswich Cloud offering.

Path A comes in two shapes. **Most enterprises use A2.**

<table><thead><tr><th width="223.42578125">Shape</th><th>What our terraform modules create?</th><th>What you will provide?</th></tr></thead><tbody><tr><td><strong>Greenfield (A1)</strong></td><td>Basically everything for a production grade stack: Network, cluster, database, cache, edge, key management</td><td>A cloud account and a domain</td></tr><tr><td><strong>Inside your landing zone (A2)</strong></td><td>Only the Hyperswitch specific layers: Cluster workloads, database, cache, card vault, key management, edge</td><td>Your existing accounts, VPC, subnets, transit routing, IAM boundary, logging destinations, CMKs</td></tr></tbody></table>

Every module accepts externally-created resources as inputs. And adoption will be module by module.

You can pass in your own VPC and subnet IDs, your own KMS key ARNs, your own IAM roles, your own log destinations, and our modules will build on them rather than replacing them.&#x20;

In Path A,

* **The PCI boundary is expressed in code you can hand to a QSA.** The cardholder-data environment, vault isolation, key custodianship and network segmentation are module boundaries and variables, not prose your team has to interpret and then evidence from scratch. This is the single largest time saving at certification and at every annual reassessment.
* **Reliability defaults are already correct.** Multi-AZ, point-in-time recovery, failover, backup retention and node spread ship as defaults tied to your required workload, RTO and RPO targets.
* **Upgrades stay tractable.** Each module version maps to specific application component versions. When a release requires an infrastructure change — a new managed service, a parameter change, a migration — it arrives as a module bump rather than a change request your platform team has to reverse-engineer.
* **Support can reproduce your environment.** When something breaks at 2am, a known topology is the difference between a fast root cause and a long detection call. Our detection and response commitments in Tiers 1 and 2 assume a topology we recognize very well.
* **Production certification is faster.** Sizing, blueprint, validation and readiness artifacts all reference these modules. On Path A you inherit that sequence; otherwise you rebuild it.
* **Drift is reviewable.** Infrastructure changes arrive as pull requests against pinned module versions, which is what your change-control process almost certainly already requires.

#### Path B — Bring your own infrastructure, deploy Helm only

You provision every resource yourself under your own IaC and point our Helm charts at the result.

**Choose this path only if** a hard organizational constraint rules out running third-party Terraform in your accounts — for example a mandated single-tool IaC estate, or a security policy that permits no external IaC artefacts.

Compared to Path A, if you choose to go with Path B,

* **The PCI evidence burden is significant:** You will have to reproduce the CDE boundary, vault isolation, key custodianship and segmentation yourself, and you produce the QSA evidence for each.
* **Reliability properties are not inherited as defaults:** Multi-AZ, failover behaviour and backup retention are yours to establish.
* **Upgrades become projects:** There is no module version to bump. Infrastructure changes required by new releases must be identified from release notes and implemented by your team, on your schedule, at your risk.
* **Detection and diagnosis could be slower:** In Tiers 1 and 2, diagnosis begins with establishing what your topology actually is. Root-cause analysis takes materially longer, and Tier 1 is generally not available on Path B.
* **Production certification takes longer:** Because each artifact must be produced against your architecture rather than validated against a known one.

{% hint style="info" %}
**Note:** In case you are considering Path B because our modules seem to conflict with your standards, raise it before to support@juspay.io for further guidance.
{% endhint %}

***

### Path to production

Once the three decisions are taken, the production certification process shall be commenced. The Juspay Enterprise support team will work with your payments team across four stages (as shown below) with clear outcomes signed off at each stage.

<table><thead><tr><th width="40">#</th><th width="265.05859375">Milestone</th><th>What you get?</th></tr></thead><tbody><tr><td>1</td><td>Architecture finalization</td><td>Stack blueprint from ingress to egress, with applicable hyperswitch components finalized. Any custom requirements on the infrastructure side shall also be addressed.</td></tr><tr><td>2</td><td>Sizing &#x26; deployment</td><td>Infrastructure sized to your TPS, RTO and RPO requirements. <br>Terraform scripts and helm are finalized.<br>Any customization requirements such as theme, domain mapping, email configuration; feature modules and service configuarations are also addressed.</td></tr><tr><td>3</td><td>Deploy and health check</td><td>Validated deployment with smoke tests passed, observability plane wiring metrics and alerts to Juspay team and your Payments team.<br>Working payment flow test on production.</td></tr><tr><td>4</td><td>Reliability, Security and Change management</td><td><p>Chaos testing and Load testing signed off, with remediations (if any)</p><p>Security controls pending, PCI scope and actionables will be documented for PCI audits (if applicable)<br>Dry run of the change management process, with remediations (if any)<br>On-call ownership and technical SPOCs for production stack maintainance are designated</p></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>

Completing all the above four stages results in a production certified Hyperswitch stack adhering to your requirements and compliance policies.

***

### Prerequisites

Whichever path you choose, you will need:

* A cloud account, or a subscription within your existing organisation, with permissions to create networking, Kubernetes and managed database resources
* A team member who can make infrastructure decisions, because some steps require choices only your organization can make
* A domain and TLS certificate for your Hyperswitch endpoints
* At least one payment processor credential to connect for payment processing
* On Path A2, also have ready:&#x20;
  * your VPC and subnet IDs
  * your IAM permissions boundary
  * your CMK ARNs if you manage your own keys, and&#x20;
  * your logging and monitoring destinations.

