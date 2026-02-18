---
description: All the payment use-cases for SaaS providers
icon: desktop
---

# SaaS Platforms

SaaS platforms operating in commerce, bookings, and professional services face a unique challenge: they must act as the central nervous system for thousands of distinct merchants.

A recurring theme we observe is the friction between scalability (standardizing payments) and flexibility (allowing merchants to bring their own processors). Hyperswitch resolves this by providing a composable payment mesh that standardizes these differences without requiring custom engineering for each merchant.

The sections below outline the architectural patterns required to scale a multi-tenant payment infrastructure.

#### Pattern 1: "Bring Your Own Processor" (BYOP)

The Business Friction: High-value merchants often refuse to migrate their payment processing to the SaaS platform because they have pre-negotiated rates or historical data with specific providers (e.g., Stripe, Adyen, Worldpay). Supporting these "brownfield" merchants usually requires building and maintaining dozens of custom integrations.

The Hyperswitch Advantage: Decoupled Connectivity

Hyperswitch acts as a Connector Abstraction Layer. You integrate our SDK once, and we dynamically route the transaction to the merchant’s preferred processor based on their configuration.

* Unified API: We normalize 50+ processor APIs into a single [Payment Intent Flow](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration).
* Zero-Code Integration: New processors are added via configuration, not code. See our [Supported Connectors](https://juspay.io/integrations) list.
* Deployment Models: Choose between Full-Stack Mode (we handle UI & Tokenization) or Backend-Only (you own the UI).

#### Pattern 2: Multi-Tenant Data Isolation

The Business Friction: SaaS platforms must ensure that one merchant's routing rules, API keys, and customer data never leak to another. Building this "tenancy logic" from scratch is risky and delays time-to-market.

The Hyperswitch Advantage: Native Hierarchy

We provide a built-in [Organization → Merchant → Profile](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles) data model designed specifically for platforms.

* Granular Control: Isolate API keys and routing rules at the Merchant ID level.
* Business Unit Segmentation: Use Profiles to manage regional splits (e.g., "Merchant A - US Store" vs. "Merchant A - EU Store").
* Team Access: Map your dashboard users to specific levels of the hierarchy using our [User Management](https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team) controls.

#### Pattern 3: Automated Merchant Provisioning

The Business Friction: Manual onboarding via a dashboard is an operational bottleneck. To scale, platforms need to provision sub-merchants, inject credentials, and configure webhooks programmatically at the moment of signup.

The Hyperswitch Advantage: Infrastructure-as-Code

Treat merchant onboarding as an API call, not a support ticket. Hyperswitch exposes [Management APIs](https://api-reference.hyperswitch.io/v1/merchant-account/merchant-account--create#merchant-account-create) to fully automate the lifecycle.

* Instant Onboarding: Create a new merchant entity and inject their Stripe/Adyen keys via the [Connector Configuration API](https://api-reference.hyperswitch.io/merchant-connector-account/merchant-connector--create).
* Flexible Liability: Support both Merchant of Record (MoR) models (platform holds funds) and Connected Account models (merchant holds funds).

#### Pattern 4: Standardizing Complex Payment Flows

The Business Friction: Different verticals require different flows (e.g., $0 Auth for hotels, 3DS for EU retail, Recurring for subscriptions). Fragmentation across PSP capabilities (e.g., "Stripe supports 3DS, but does Authorize.net?") often forces platforms to write "spaghetti code."

The Hyperswitch Advantage: The Universal State Machine

We normalize complex flows into a standard state machine. Your frontend handles a single response type, regardless of the underlying complexity.

* Compliance Ready: We automatically handle [3D Secure (3DS)](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/payment-features/3d-secure-3ds) challenges across all processors.
* Unified Lifecycle: Perform [Auth, Capture, and Void](https://docs.hyperswitch.io/learn-more/hyperswitch-architecture/connector-payment-flows) operations using a single API syntax, even if the underlying PSP (e.g., Klarna vs. Visa) behaves differently.

#### Pattern 5: Vendor-Agnostic Vaulting (Tokenization)

The Business Friction: If a merchant stores card data in a PSP-specific vault (e.g., Stripe Customer ID), they are vendor-locked. Switching providers means losing all saved customer cards, which destroys recurring revenue.

The Hyperswitch Advantage: Portable Tokenization

We offer a neutral [Payment Vault (Locker)](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault) that exists independently of the processor.

* Ownership: You or the merchant own the tokens, not the PSP.
* Interoperability: A card saved during a Stripe transaction can be seamlessly charged via Adyen later using our [Network Tokenization](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards) logic.
* Security: Offload PCI-DSS compliance by using our certified secure storage.

#### Pattern 6: Operational Efficiency & Unified Support

The Business Friction: Support teams struggle when every PSP returns different error codes (e.g., "Do Not Honor" vs. "Refusal" vs. "Error 402"). Debugging requires deep knowledge of 10+ different vendor systems.

The Hyperswitch Advantage: Normalized Observability We translate the chaos of vendor responses into a clean, standardized language for your support and engineering teams.

* Unified Errors: We map thousands of PSP error codes into a [Standardized Error Reference](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/web/error-codes) (e.g., `card_expired`), so your UI can show consistent messages.
* Single Source of Truth: Use the [Operations Dashboard](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations) to view transaction logs, refunds, and disputes across all merchants and processors in one view.

#### Pattern 7: Unified Post-Payment Operations

The Business Friction: The payment lifecycle doesn't end at "Checkout." SaaS platforms must also build portals for their merchants to handle Refunds, Disputes, and Webhooks. Building these operational interfaces is painful because every processor has a different API schema for refunds and a different JSON payload for webhooks.

The Hyperswitch Advantage: Normalized Event Streams

We standardize the chaotic "Day 2" operations into a clean, unified interface. Your engineering team builds one refund handler and one webhook listener, and it works for all connected processors.

* Universal Webhooks: We ingest disparate events and transform them into a [Standardized Webhook Schema](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks). You receive the same JSON structure regardless of the upstream provider.
* Dispute Management: Manage chargebacks centrally. We normalize the [Disputes Lifecycle](https://docs.hyperswitch.io/explore-hyperswitch/account-management/disputes) so you can surface evidence submission flows directly in your SaaS dashboard.
* Stateless Operations: Use our [Relay APIs](https://api-reference.hyperswitch.io/v1/relay/relay#relay-create) to trigger refunds or voids by passing the `connector_resource_id`, even if the original payment wasn't processed through Hyperswitch.

#### Pattern 8: Platform Reliability & SLA Monitoring

The Business Friction: Global SaaS platforms cannot afford downtime. When a processor like Stripe US-East experiences latency, your merchants blame _you_, not Stripe. Without granular visibility into processor performance, your engineering team is flying blind, unable to reroute traffic or uphold SLAs for VIP merchants.

The Hyperswitch Advantage: Real-Time Observability We treat payments as "Critical Infrastructure." Hyperswitch provides deep visibility into the health of your payment mesh, allowing you to proactively manage reliability.

* Connector Health: We continuously monitor the success rates and latency of every connected processor. If a provider degrades, our [Smart Router](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) can automatically failover traffic to a healthy alternative.
* Open Telemetry: We emit standard OTel Traces for every request. You can pipe these directly into Datadog, Prometheus, or Grafana to visualize P99 latency per merchant.
* System Status: Access the System Health API to build your own internal status pages, giving your support team instant context during incidents.
