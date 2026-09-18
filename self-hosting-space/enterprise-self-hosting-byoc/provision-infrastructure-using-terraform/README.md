---
description: >-
  How a production grade Hyperswitch stack is provisioned using Terraform? An
  explanation of steps involved and infra automation coverage across cloud
  providers.
icon: code
---

# Provision Infrastructure using Terraform

***

## Deploy with Terraform

This page covers Milestone III of the production certification process. The approach is same across every cloud: how the code is organized, the steps to reach a working production stack, and how much of each layer is automated. The per-cloud pages cover the detailed devops installation engineering steps to be done on specific cloud provider.

### Approach

**Terraform provisions cloud infrastructure.** It builds the cloud resources Hyperswitch needs, including the workload identities and encryption keys the pods assume

**ArgoCD acts application management layer.** It installs Hyperswitch related applications using the helm charts. It provides the release management tooling like staggered rollouts, A/B during and rollback to ensure reliability during the change management process.

**Terragrunt to manage multiple environments or stacks.** It runs Terraform underneath and adds the things Terraform lacks once you have more than one environment. It include composing whole environments, passing output from one state to another, keeping the modules external and pinned.

<table><thead><tr><th width="186">Layer</th><th width="252.28125">Owns</th><th>Tool</th><th>Lives in</th></tr></thead><tbody><tr><td><strong>Infrastructure</strong></td><td>Network, Kubernetes cluster, databases, cache, identity, keys, load balancers</td><td>Terraform via Terragrunt</td><td>Your infrastructure repo</td></tr><tr><td><strong>Applications</strong></td><td>Router, payment methods, connector service, card vault, Control Center, Superposition, monitoring</td><td>Helm charts reconciled by ArgoCD</td><td>Your GitOps repo</td></tr></tbody></table>

**The reference Terraform lives in the public `juspay/hyperswitch-suite` repo.** Your infrastructure repo shall not copy it. Instead it shall reference each unit references it by pinned tag:

```hcl
terraform {
  source = "git::https://github.com/juspay/hyperswitch-suite.git//terraform/<cloud>/modules/<module>?ref=<pinned-tag>"
}
```

**Terragrunt composes those modules. You do not write Terraform.** The layout will be identical on every cloud:

```
terraform/
├── catalog/
│   ├── units/<name>/     Reusable building blocks
│   └── stacks/<name>/    Compose units into a full environment, in order
└── <cloud>/
    ├── modules/          A few internal-only application modules
    └── live/<env>/<region>/<component>/
                          Real deployments — thin configs pointing at a unit
```

A new region or environment means adding a `live/<env>/<region>/` directory following the existing pattern.&#x20;

Primary regions are hand-authored unit by unit.&#x20;

DR regions are generated from a stack with `terragrunt stack generate`.

{% hint style="info" %}
**Terragrunt is required, and tags are not optional.** If your team standardized on plain Terraform, raise it before you start. And never change `?ref=<tag>` to a branch — that means your infrastructure changes on someone else's merge, with no pull request in your repo.
{% endhint %}

### Greenfield or Brownfield?

Lets revisit Decision III. The choice, will impact how much work steps 6 and 7 below involve.

<table><thead><tr><th width="192.3671875"></th><th width="267.21875">Greenfield  Installation (Path A1)</th><th>Brownfield Installation (Path A2)</th></tr></thead><tbody><tr><td>Starting point</td><td>A fresh cloud account</td><td>An existing landing zone inside your existing cloud account</td></tr><tr><td>Network, routing, keys</td><td>Provisioned for you</td><td>You supply them as inputs</td></tr><tr><td>Customization step</td><td>Everything is pre-configured for production.</td><td>Required, and external resources must be wired into the IaC</td></tr></tbody></table>

Most organizations deploying Hyperswitch already have a landing zone, an account hierarchy and network standards. The units are built to attach to what you already run rather than duplicate it.

***

### Steps to install production-grade stack

The production installation to health verification take approximately **12 hours of hands-on work.**&#x20;

It involves 12 steps across 4 phases to install hyperswitch and test a payment flow working end-to-end.

{% hint style="info" %}
The stated time assumes that the Milestones I and II of the production certification process are already completed; and prerequisites stated in&#x20;

is a working estimates including a buffer for misconfiguration and debugging.&#x20;

The stated time does not include additional time for your own infra change approval cycles.
{% endhint %}

### Phase 1: Prepare

<table><thead><tr><th width="44.56640625">#</th><th width="175.25">Step</th><th width="80.953125">Time</th><th>What it does?</th></tr></thead><tbody><tr><td>1</td><td><strong>Arrange the prerequisites</strong></td><td>—</td><td><ul><li>Cloud account and organization permissions, domain and TLS certificate, at least one payment processor credential is arranged</li><li>On brownfield installation your network and subnet identifiers are arranged. See prerequisites below for complete list.</li></ul></td></tr><tr><td>2</td><td><strong>Install and verify local tooling</strong></td><td>0.5 h</td><td><ul><li>Helm, kubectl, Terraform, Terragrunt and your cloud provider CLI on the operator's work device. All verified before proceeding</li></ul></td></tr></tbody></table>

### Phase 2: Provision the infrastructure

<table><thead><tr><th width="47.91796875">#</th><th width="177.27734375">Step</th><th width="82.48046875">Time</th><th>What it does?</th></tr></thead><tbody><tr><td>3</td><td><strong>Bring up the cloud infrastructure with Terragrunt</strong></td><td>4.0 h</td><td><ul><li>This cover bulk of the infra automation. </li><li>Network, Kubernetes cluster, databases, cache, card vault infrastructure, workload identity, keys and load balancers, object storage resources - all applied in dependency order. </li></ul></td></tr><tr><td>4</td><td><strong>Verify the infrastructure components</strong></td><td>0.5 h</td><td><ul><li>Confirm the cluster is reachable and nodes are spread across zones, the databases and cache are reachable from the cluster and only from the cluster, and state is remote, encrypted and lock-protected.</li></ul></td></tr><tr><td>5</td><td><strong>Install the application management layer — ArgoCD</strong></td><td>0.5 h</td><td><ul><li>Installs the GitOps controller and the platform components it depends on: the cloud ingress controller, External Secrets Operator, and the ArgoCD app-of-apps that will manage everything else.</li></ul></td></tr><tr><td>6</td><td><strong>Set up External Secrets Operator</strong></td><td>0.5 h</td><td><ul><li>Points the cluster at your managed secret store and declares which secrets to sync. Credentials never enter Helm values or Git; ESO pulls them at runtime and materializes them as ordinary Kubernetes secrets</li></ul></td></tr></tbody></table>

### Phase 3: Deploy and verify the applications

<table><thead><tr><th width="47.26953125">#</th><th width="180.5078125">Step</th><th width="86.32421875">Time</th><th>What it does?</th></tr></thead><tbody><tr><td>7</td><td><strong>Apply customizations for your infra landing zone</strong></td><td>2.0 h</td><td><ul><li><strong>Brownfield only.</strong> Wire externally created resources into the application values: ingress and egress paths, database and cache URLs, payment connector URLs, domain mapping and SMTP.</li><li>This could be the step requiring more iterations in the sequence, since it is manual, and it touches every component. <strong>Greenfield deployments typically skip it</strong>.</li></ul></td></tr><tr><td>8</td><td><strong>Deploy all Hyperswitch components using ArgoCD</strong></td><td>2.0 h</td><td><ul><li>ArgoCD applications pointing at the public Helm charts bring up the router, payment methods, connector service, card vault, Control Center, Superposition, encryption service and monitoring.</li></ul></td></tr><tr><td>9</td><td><strong>Verify with deep health checks</strong></td><td>0.5 h</td><td><ul><li>Confirm Helm releases and pod status across every component. This checks that the installation is healthy, not that the product works.</li></ul></td></tr><tr><td>10</td><td><strong>Test the backend application with APIs</strong></td><td>0.1 h</td><td><ul><li>Generate an API key and call the payment-create API. </li><li>First proof that the stack processes a request end to end.</li></ul></td></tr></tbody></table>

### Phase 4: Configure and test the production stack

<table><thead><tr><th width="45.44921875">#</th><th width="178.36328125">Step</th><th width="89.23046875">Time</th><th>What it does?</th></tr></thead><tbody><tr><td>11</td><td><strong>Update Control Center and SDK environment configuration</strong></td><td>0.1 h</td><td>Applied through ArgoCD so the change is declared in Git rather than made by hand.</td></tr><tr><td>12</td><td><strong>Configure the payment stack and test end to end</strong></td><td>0.5 h</td><td>Configure connectors, routing and payment methods through the Control Center, then test both the APIs and the SDK checkout flow.</td></tr></tbody></table>

After step 12 you have a working deployment and Milestone III, is completed.

{% hint style="warning" %}
Completion of Milestone III, does not result in a production-grade setup. Complete Milestone IV to be completed for hardening — proving recovery, proving capacity, closing PCI items.
{% endhint %}

***

#### Prerequisites

**Milestone I and II artifacts**

* A signed-off blueprint with no open architectural decisions.
* Custom Terraform chart and Helm values for your production deployments.

**Tooling**

<table><thead><tr><th width="206.9375">Tool</th><th>Version</th></tr></thead><tbody><tr><td>Terraform</td><td>1.12.1</td></tr><tr><td>Terragrunt</td><td>1.1.1</td></tr><tr><td>kubectl</td><td>1.33+</td></tr><tr><td>Helm</td><td>3.0+</td></tr><tr><td>Kubernetes</td><td>1.34+</td></tr><tr><td>Cloud provider CLI</td><td><p>AWS CLI: v2.35.x </p><p>Google Cloud CLI: 583.0.0 </p><p>Oracle OCI CLI: v3.91.0</p></td></tr></tbody></table>

**Access & credentials**

* **Cloud access** — an apply identity able to create network, Kubernetes, database, cache, identity and key management resources. **Not an administrator role.** For CI, use workload identity federation rather than long-lived credentials.
* **Network and DNS** — a domain you control with DNS management access, and TLS certificates or the ability to issue them.
* **In case of brownfield installation**
  * Network and subnet identifiers,&#x20;
  * routing model,&#x20;
  * permissions boundary,&#x20;
  * existing key identifiers,&#x20;
  * logging destinations, and&#x20;
  * Egress or proxy restrictions.
* **Payment processor credentials** — at least one processor account with production credentials, will be needed at Step 12.

**People**

* This could take the longest lead time, and critical as much as any tool:
  * **Key custodians** — named individuals to generate and hold custodian keys, and to unlock the vault
  * **A change approver**, if production applies require sign-off
  * **A security reviewer**, if account access needs approval
  * **A single technical SPOC**, to work with Juspay team and co-ordinate across the above owners
