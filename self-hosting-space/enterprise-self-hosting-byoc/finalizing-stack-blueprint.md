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

The stack blueprint is the Milestone I of the production certification process.

<figure><img src="../.gitbook/assets/Juspay hyperswitch (Self hosted) - Architecture blueprint.png" alt=""><figcaption></figcaption></figure>

### How to read it?

Components are colored marked based ownership and customization possibility.

<table><thead><tr><th width="93.75390625">Colour</th><th width="262.08984375">Meaning</th><th>How to customize?</th></tr></thead><tbody><tr><td><strong>Blue</strong></td><td>Juspay or open-source software components which are central to operating Hyperswitch stack</td><td><p>Choose the components applicable for your use case. </p><p>Removing an optional component is a trade-off in features, reliability or Juspay's SLAs.</p></td></tr><tr><td><strong>Orange</strong></td><td>Mandatory open-source tooling the stack depends upon for continuos operations</td><td>Customization requires code changes in the application core — treat these as fixed choices.</td></tr><tr><td><strong>Teal</strong></td><td>Components you may build and manage yourself</td><td>Yours to provide, or to share from an existing organization-level service</td></tr></tbody></table>

**Note:**&#x20;

* The networking layer, load balancers, firewalls are not shown in the blue print. Since these are standard for any stack, it will be covered in the final milestone of the production certification.
* Native SDK (Android, iOS, React etc.,) are not included in the blue print, since they are served from specific package manager, the approach to host it could be very flexible as you may need.

***

### Entry points

The hyperswitch stack will server three distinct traffic patterns:

* Users hit the content delivery layer. This is the shoppers loading the checkout experience in a browser or app.
* Merchants hit the API path directly. This is the server-to-server API traffic — payment creation, refunds, status queries; or through the control center which the merchant team will use to configure and operate the payment stack.
* Payment processors sending webhook notification to the hyperswitch endpoint directly. This is for various functionality like updating payment status, disputes etc.,

### Content delivery

This is the layer most often already provided at organization level. If you have a CDN and Cloud object storages as Global services within your organization, you can use it as-is.

<table><thead><tr><th width="162.0625">Component</th><th width="113.59765625">Required?</th><th>Why it exists?</th></tr></thead><tbody><tr><td><strong>Content Delivery Network</strong></td><td>Mandatory</td><td>Serves checkout assets from an edge location near the shopper. Removing it puts your own cluster on the checkout critical path.</td></tr><tr><td><strong>SDK Resources</strong></td><td>Conditional</td><td>Hosts the checkout SDK and its assets which will be embedded in your app and directly exposed to the users. The optionality depends on your PCI strategy. Consider this optional, only if you are not using the hosted checkout experience.</td></tr></tbody></table>

### Ingress

<table><thead><tr><th width="161.5234375">Component</th><th width="117.59765625">Required?</th><th>Why it exists?</th></tr></thead><tbody><tr><td><strong>Envoy</strong></td><td>Mandatory</td><td>The edge proxy: terminates and routes inbound traffic before it reaches the mesh.</td></tr><tr><td><strong>Auth Proxy</strong></td><td>Optional</td><td><p>Enforces authentication at the edge rather than in the application. The benefits are two in terms of reliability with agility:</p><ul><li>Critical application processing resources are safe guarded from high throughput authentication system.</li><li>Moving authentication to the edge can help create an isolating agile application changes for a closed user group (CUG) of merchants. This could be very valuable if you would want to deploying changes continuously across 'm' merchants coming up with 'n' requirements.</li></ul></td></tr><tr><td><strong>Rate limiter</strong></td><td>Mandatory</td><td>Protects the API paths from abuse and traffic spikes. It is important to enforce API level and merchant level rate limits as per promised SLAs to the merchants.</td></tr></tbody></table>

### Application core

The core application running on Kubernetes for payment processing services and other associated functionalities. A lot of services here could be optional depending on your use cases to be served.

<table><thead><tr><th width="160.99609375">Component</th><th width="118.68359375">Required?</th><th>Why it exists?</th></tr></thead><tbody><tr><td><strong>Istio</strong></td><td>Mandatory</td><td>Service mesh: maps hostnames and paths to services and applies mesh policy across the core.</td></tr><tr><td><strong>OLTP Router</strong></td><td>Mandatory</td><td>The payment engine — authorisation, capture, refunds, routing decisions. The one component nothing runs without.</td></tr><tr><td><strong>OLAP Router</strong></td><td>Mandatory</td><td>Serves read and analytical queries so reporting load never touches the transaction path.</td></tr><tr><td><strong>Payment methods</strong></td><td>Mandatory</td><td>The payment-methods API surface, deployed separately so it scales independently of the router.</td></tr><tr><td><strong>Connector Service</strong></td><td>Mandatory</td><td>Runs processor integrations as their own service, so adding or updating a connector does not mean redeploying the router.</td></tr><tr><td><strong>Producer / Consumer</strong></td><td>Mandatory</td><td>Handles asynchronous work — webhooks, refunds, retries, scheduled payments — off the synchronous request path.</td></tr><tr><td><strong>Control Center</strong></td><td>Conditional</td><td>The operator dashboard: routing rules, transaction operations, connector configuration, analytics. If you prefer to build your own interface for the control center, this becomes optional.</td></tr><tr><td><strong>Card Vault</strong></td><td>Conditional</td><td>Tokenizes and stores card data. Deploying it makes you the holder of a cardholder data environment. <strong>This single choice determines your PCI scope, certification effort and annual reassessment cost.</strong></td></tr><tr><td><strong>Encryption Service</strong></td><td>Conditional</td><td>Encrypts and decrypts sensitive data in transit between components. Required alongside the card vault.</td></tr><tr><td><strong>Decision Engine</strong></td><td>Conditional</td><td>Cost-aware and success-rate-aware routing decisions.</td></tr><tr><td><strong>Revenue Recovery</strong></td><td>Optional</td><td>Recovers failed recurring payments through intelligent retries.</td></tr><tr><td><strong>Reconciliation</strong></td><td>Optional</td><td>Matches processor settlement files against internal records.</td></tr></tbody></table>

**The card vault is the highest-consequence decision on this page.** Not deploying it means using a third-party vault or a processor's tokenization, and staying outside PCI scope for cardholder data. Deploying it means owning a CDE. Decide deliberately, not by default.

### OLTP storage

<table><thead><tr><th width="163.28125">Component</th><th width="117.4296875">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>PostgreSQL</strong></td><td>Mandatory</td><td>Transactional store. Separate instances for the OLTP Router, Card Vault, Encryption Service, Superposition and Decision Engine — separation is deliberate, and it is what keeps the vault's data isolated from everything else.</td></tr><tr><td><strong>Redis</strong></td><td>Mandatory</td><td>Cache and session tier, with matching per-service instances.</td></tr></tbody></table>

The exact instance counts will depend on the application core components you wish to include in your deployment.

### Management

<table><thead><tr><th width="164.43359375">Component</th><th width="127.828125">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Terraform</strong></td><td>Mandatory</td><td>Provisions cloud infrastructure.</td></tr><tr><td><strong>Helm</strong></td><td>Mandatory</td><td>Packages the application components for deployment.</td></tr><tr><td><strong>ArgoCD</strong></td><td>Mandatory</td><td>Reconciles the cluster against Git continuously, so what runs is always what is declared.</td></tr><tr><td><strong>Superposition</strong></td><td>Mandatory</td><td>Context-based configuration management — roll out routing rules, retry ladders and feature flags across environments or tenants without redeploying.</td></tr></tbody></table>

### Monitoring

<table><thead><tr><th width="167.0078125">Component</th><th width="129.07421875">Required?</th><th>Why it exists?</th></tr></thead><tbody><tr><td><strong>OpenTelemetry</strong></td><td>Mandatory</td><td>Collects metrics, logs and traces from every component in one standard.</td></tr><tr><td><strong>Victoria Metrics</strong></td><td>Mandatory</td><td>Stores metrics.</td></tr><tr><td><strong>Loki</strong></td><td>Mandatory</td><td>Stores logs.</td></tr><tr><td><strong>Promtail</strong></td><td>Mandatory</td><td>Ships logs into Loki.</td></tr><tr><td><strong>Grafana</strong></td><td>Mandatory</td><td>Dashboards over all of the above.</td></tr><tr><td><strong>Alerts Manager</strong></td><td>Conditional</td><td>Routes alerts to Juspay and your internal on-call system. Optional depending on the Juspay support model you choose (Tier 1/ Tier 2/ Tier 3)</td></tr></tbody></table>

This layer is orange for a reason: substituting a different observability stack means code changes in the application core, not configuration. If your organization mandates a different tool, raise it during the blueprint rather than after deployment.

It is also a prerequisite for support. Tier 1 and Tier 2 both depend on Juspay owning the observability plane — see Enterprise Edition Support.

### Data processing

<table><thead><tr><th width="177.83203125">Component</th><th width="122.953125">Required?</th><th>Why it exists</th></tr></thead><tbody><tr><td><strong>Kafka</strong></td><td>Mandatory</td><td>Streams events out of the transaction path into analytics without adding latency to payments.</td></tr><tr><td><strong>ClickHouse</strong></td><td>Mandatory</td><td>Columnar store powering dashboard analytics and reporting at volume.</td></tr><tr><td><strong>Cassandra</strong></td><td>Mandatory</td><td>Backing datastore for sessionizer.</td></tr><tr><td><strong>OpenSearch</strong></td><td>Optional</td><td>Lookup by identifier in the dashboard.</td></tr><tr><td><strong>Sessionizer</strong></td><td>Optional</td><td>Processes data for A/B testing and analytics insight.</td></tr></tbody></table>

{% hint style="info" %}
**The data processing layer is not covered by the Terraform modules on any cloud today.** ClickHouse, Kafka, OpenSearch and the sessionizer will have to be manually provisioned, to support dashboard analytics, reporting.
{% endhint %}

### Egress

<table><thead><tr><th width="183.98046875">Component</th><th width="133.3359375">Required?</th><th>Why it exists?</th></tr></thead><tbody><tr><td><strong>Squid</strong></td><td>Mandatory</td><td>Forward proxy giving controlled, allow-listed outbound access to processors and external endpoints. In a PCI environment, unrestricted egress from the CDE is not acceptable — this is how you will have to constrain it.</td></tr></tbody></table>

