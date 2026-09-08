---
description: >-
  Every component in a self-hosted Hyperswitch stack, what it does, and why it
  exists? So you can decide what to deploy and what to leave out.
icon: ruler-combined
---

# Finalizing Stack Blueprint

***

## Stack blueprint

The blueprint exists to answer two questions before you provision anything:

1. **Which components does your stack actually need?** Several are optional, based on your feature requirements and devops strategy to operate the Hyperswitch stack.
2. **Which layers are dedicated to Hyperswitch, and which are shared organization-wide?** For example the ingress, egress and content delivery could be commonly provided centrally. If yours are, plug into them instead of duplicating them.

Finalizing your own version of the stack blueprint will be Milestone I of the production certification process.

<figure><img src="../.gitbook/assets/Juspay hyperswitch (Self hosted) - Architecture blueprint (1).png" alt=""><figcaption></figcaption></figure>

### How to read it?

Components are colored marked based ownership and customization possibility.

<table><thead><tr><th width="93.75390625">Colour</th><th width="262.08984375">Meaning</th><th>How to customize?</th></tr></thead><tbody><tr><td><strong>Blue</strong></td><td>Juspay or open-source software components which are central to operating Hyperswitch stack</td><td>Choose the components applicable for your use case. Removing an optional component is a trade-off in features, reliability or Juspay's SLAs.<br><strong>For example:</strong> Removing Superposition will disable runtime configuration management for hyperswitch; makes hyperswitch more reliable while rolling out config changes. </td></tr><tr><td><strong>Orange</strong></td><td>Mandatory tooling the stack depends upon for continuous operations</td><td>Can be extended or replaced with alternatives, if needed. <br><strong>For example:</strong> Key manager services could be substituted with Hashicorp</td></tr><tr><td><strong>Teal</strong></td><td>Components you may build and manage yourself</td><td>Yours to provide, or to share from an existing organization-level service.<br><strong>For example:</strong> You can choose to use your own ingress/ egress at an org level.</td></tr></tbody></table>

**Note:**&#x20;

* The networking layer, load balancers, firewalls are not shown in the blue print. Since these are standard for any stack, it will be covered in the final milestone of the production certification.
* Native SDK (Android, iOS, React etc.,) are not included in the blue print, since they are served from specific package manager, the approach to host it could be very flexible as you may need.

***

### Entry points

The hyperswitch stack will serve four distinct traffic patterns:

* Users hit the content delivery layer. This is the shoppers loading the checkout experience in a browser or app.
* Merchants hit the API path directly. This is the server-to-server API traffic — payment creation, refunds, status queries; or through the control center which the merchant team will use to configure and operate the payment stack.
* Payment processors sending webhook notification to the hyperswitch endpoint directly. This is for various functionality like updating payment status, disputes etc.,
* Scheduler which takes care of refunds and other Async process.

### Content delivery and Object Storage

This is the layer most often already provided at organization level. If you have a CDN as global services within your organization, use them as-is.

<table><thead><tr><th width="167.21484375">Component</th><th width="124.32421875">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Content Delivery Network</strong></td><td>Mandatory</td><td><p></p><p>Serves checkout assets from edge locations near the shopper. Caches static assets, results in cheap and faster content delivery.</p></td></tr></tbody></table>

### Object storage

This is where the checkout SDK and its assets live, served to shoppers through the CDN. Small in footprint, but on the critical path for every hosted checkout session.

<table><thead><tr><th width="163.7421875">Component</th><th width="127.765625">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>SDK Resources</strong></td><td>Conditional</td><td>Hosts the checkout SDK and its assets, served through the CDN. This may be optional based on your PCI strategy.</td></tr></tbody></table>

### Ingress

The front door for all inbound traffic, merchant and shopper alike. It terminates, optionally authenticates and throttles requests before anything reaches the application.

<table><thead><tr><th width="167.15625">Component</th><th width="115.3984375">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Envoy</strong></td><td>Required</td><td>The edge proxy: terminates and routes inbound traffic before it reaches the mesh.</td></tr><tr><td><strong>Rate limiter</strong></td><td>Required</td><td>Protects the payment path from abuse and traffic spikes. Not optional in practice for an internet-facing payments API.</td></tr><tr><td><strong>Auth Proxy</strong></td><td>Optional</td><td>Enforces authentication at the edge rather than in the application. Moving authentication to the edge can help create an isolating agile application changes for a closed user group (CUG) of merchants. This could be very valuable if you would want to deploying changes very frequently across 'm' merchants coming up with 'n' requirements.</td></tr></tbody></table>

### Application core

The core application running on Kubernetes: payment processing and its associated functionality. Many services here are optional depending on the use cases you need to serve.

<table><thead><tr><th width="154.8359375">Component</th><th width="132.46484375">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Istio</strong></td><td>Required</td><td>Service mesh: maps hostnames and paths to services and applies mesh policy across the core.</td></tr><tr><td><strong>OLTP Router</strong></td><td>Required</td><td>The payment engine — authorisation, capture, refunds, routing decisions. Nothing runs without it.</td></tr><tr><td><strong>OLAP Router</strong></td><td>Required</td><td>Serves read and analytical queries so reporting load never touches the transaction path.</td></tr><tr><td><strong>Payment methods</strong></td><td>Required</td><td>The payment-methods API surface, deployed separately so it scales independently of the router.</td></tr><tr><td><strong>Connector Service</strong></td><td>Required</td><td>Runs processor integrations as their own service, so adding or updating a connector does not mean redeploying the router.</td></tr><tr><td><strong>Producer / Consumer</strong></td><td>Required</td><td>Handles asynchronous work — webhooks, refunds, retries, scheduled payments — off the synchronous request path.</td></tr><tr><td><strong>Control Center</strong></td><td>Required</td><td>The operator dashboard: routing rules, transaction operations, connector configuration, analytics.</td></tr><tr><td><strong>Card Vault</strong></td><td>Conditional</td><td>Tokenises and stores card data. The applicability of the module depends on your PCI strategy.</td></tr><tr><td><strong>Decision Engine</strong></td><td>Optional</td><td>Rule based, Cost-aware and Auth-rate-aware routing decisions to uplift conversion rates and achieve routing business goals</td></tr><tr><td><strong>Revenue Recovery</strong></td><td>Optional</td><td>Recovers failed recurring MIT payments through intelligent retries.</td></tr><tr><td><strong>Reconciliation</strong></td><td>Optional</td><td>Matches processor settlement files against internal records.</td></tr></tbody></table>

### Online Transaction Processing (OTLP) storage

The transactional data layer behind the application core. Instances are isolated per service for the critical services to ensure reliability and compliance. The exact instance counts depend on which application core components you include in your deployment.

<table><thead><tr><th width="144.19921875">Component</th><th width="124.578125">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>PostgreSQL</strong></td><td>Required</td><td>Transactional store, with separate instances for the OLTP Router, Card Vault, Superposition and Decision Engine. The separation is deliberate — it is what keeps the vault's data isolated from everything else.</td></tr><tr><td><strong>Redis</strong></td><td>Required</td><td>Cache and session tier, with separate instances for the Rate Limiter, OLTP Router, Card Vault, Superposition, Decision Engine and Reconciliation.</td></tr></tbody></table>

### Managed services

These are cloud provider or third-party services the Hyperswitch stack depends on, rather than components you deploy yourself.

<table><thead><tr><th width="152.95703125">Component</th><th width="120.93359375">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Key manager service</strong></td><td>Required</td><td>Generates and manages the encryption and decryption keys used across the stack — Router, Card vault, Superposition.</td></tr><tr><td><strong>Secrets Manager</strong></td><td>Required</td><td>Holds credentials outside the application cluster, synced in at runtime rather than living in Helm values or Git.</td></tr><tr><td><strong>SMTP email service</strong></td><td>Required</td><td>Sends dashboard signup verification and operational email. Without it, Control Center signup cannot complete.</td></tr></tbody></table>

### Management layer

The is component defines how the stack gets provisioned, deployed and configured. These run alongside Hyperswitch rather than serving any payment traffic.

<table><thead><tr><th width="157.34765625">Component</th><th width="124.18359375">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Terraform/Terragrunt (Devops tool)</strong></td><td>Required</td><td>Provisions cloud infrastructure with the required provisioning, PCI controls, reliability defaults.</td></tr><tr><td><strong>Helm charts</strong><br><strong>(Devops tool)</strong></td><td>Required</td><td>Packages the application components for deployment.</td></tr><tr><td><strong>ArgoCD (Devops tool)</strong></td><td>Required</td><td>Reconciles the cluster against Git continuously, so what runs is always what is declared.</td></tr><tr><td><strong>Superposition</strong></td><td>Required</td><td>Context-based configuration management — roll out routing rules, retry ladders and feature flags across environments or tenants without redeploying.</td></tr></tbody></table>

### Monitoring

The monitoring and observability plane covering every component in the stack. It is how your team — or Juspay, on Tier 1 and Tier 2 — find out the platform is unhealthy before your customers do. It also provides you with the developer telemetry to deepdive and resolve issues.

<table><thead><tr><th width="149.87109375">Component</th><th width="128.7578125">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>OpenTelemetry</strong></td><td>Required</td><td>Collects metrics, logs and traces from every component in one standard.</td></tr><tr><td><strong>Victoria Metrics</strong></td><td>Required</td><td>Handles metrics.</td></tr><tr><td><strong>Loki</strong></td><td>Required</td><td>Handles logs.</td></tr><tr><td><strong>Vector</strong></td><td>Required</td><td>Ships pod and node logs into Loki.</td></tr><tr><td><strong>Grafana</strong></td><td>Required</td><td>Dashboards over all of the above for monitoring the Infrastructure and Application performance. The Juspay team will also have read access to select metrics to be able to support your team.</td></tr><tr><td><strong>Alerts Manager</strong></td><td>Conditional</td><td>Routes alerts to your on-call system. Skip it only if you already have one. Required if you are on the Tier 1 or Tier 2 plan.</td></tr></tbody></table>

### Data processing

The analytics pipeline behind dashboard reporting, insights and ID based search. All events stream out of the transaction path so analytical load never touches live payments.

<table><thead><tr><th width="154.66796875">Component</th><th width="124.66796875">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Kafka</strong></td><td>Required</td><td>Streams events out of the transaction path into analytics without adding latency to payments.</td></tr><tr><td><strong>ClickHouse</strong></td><td>Required</td><td>Columnar store powering dashboard analytics and reporting at volume.</td></tr><tr><td><strong>Vector</strong></td><td>Required</td><td>Ships events into the data processing pipeline.</td></tr><tr><td><strong>OpenSearch</strong></td><td>Optional</td><td>Lookup by identifier in the dashboard.</td></tr><tr><td><strong>Sessionizer</strong></td><td>Optional</td><td>Processes data for A/B testing and advanced analytics insights on the dashboard.</td></tr><tr><td><strong>Cassandra</strong></td><td>Conditional</td><td>Backing datastore for the sessioniser.</td></tr></tbody></table>

{% hint style="info" %}
**The data processing layer is not covered by the Terraform modules on any cloud today.** ClickHouse, Kafka, OpenSearch and the sessionizer will have to be manually provisioned to enable the hyperswitch control center with dashboard analytics, reporting, ID based search features.
{% endhint %}

### Egress

The single controlled exit from the stack to processors and other external endpoints. Everything outbound goes through here, by design rather than by convention.

<table><thead><tr><th width="153.1328125">Component</th><th width="131.1484375">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Squid</strong></td><td>Required</td><td>Forward proxy giving controlled, allow-listed outbound access to processors and external endpoints. In a PCI environment, unrestricted egress from the CDE is not acceptable — this is how you constrain it.</td></tr></tbody></table>

