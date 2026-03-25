---
description: All the payment use-cases for SaaS providers
icon: desktop
---

# SaaS Platforms

### TL;DR

Juspay Hyperswitch is an open-source payment orchestration platform that helps SaaS platforms scale multi-tenant payment infrastructure. It provides connector abstraction, hierarchical tenant isolation, and unified operations. You can onboard accounts programmatically, support BYOP (Bring Your Own Processor), and maintain unified observability across all connected payment providers.

***

### Why do SaaS platforms struggle with multi-tenant payments?

SaaS platforms face a unique challenge: they must act as the central nervous system for thousands of distinct accounts. A recurring friction exists between scalability (standardising payments) and flexibility (allowing accounts to bring their own processors). Juspay Hyperswitch resolves this by providing a composable payment mesh that standardises these differences without requiring custom engineering for each account.

The sections below outline the architectural patterns required to scale a multi-tenant payment infrastructure.

***

### How can SaaS platforms support high-value accounts that demand their own processors?

High-value accounts often refuse to migrate their payment processing to the SaaS platform because they have pre-negotiated rates or historical data with specific providers. Supporting these "brownfield" accounts usually requires building and maintaining dozens of custom integrations.

Juspay Hyperswitch acts as a Connector Abstraction Layer. You integrate our checkout once, and we dynamically route the transaction to the account's preferred processor based on their configuration.

| Feature               | Description                                                          | Reference                                                                                                        |
| --------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Unified API           | Normalises 300+ processor APIs into a single Payment Intent Flow     | [Payment Intent Flow](https://api-reference.hyperswitch.io/v1/payments/payments--create#payments-create)         |
| Zero-Code Integration | New processors added via configuration, not code                     | [Supported Connectors](https://juspay.io/integrations)                                                           |
| Deployment Model      | Self-hosted (run in your infrastructure) or SaaS (managed by Juspay) | [Deployment Options](https://docs.hyperswitch.io/explore-hyperswitch/account-management/self-managed-deployment) |
| Integration Model     | SDK (embedded checkout UI) or API (backend-only integration)         | [Platform Capabilities](https://docs.hyperswitch.io/explore-hyperswitch)                                         |

***

### How can SaaS platforms ensure data isolation between accounts?

SaaS platforms must ensure that one account's routing rules, API keys, and customer data never leak to another. Building this "tenancy logic" from scratch is risky and delays time-to-market.

Juspay Hyperswitch provides a built-in [Organisation → Account → Profile](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles) data model designed specifically for platforms.

| Level        | Purpose                              | Benefit                                                                           |
| ------------ | ------------------------------------ | --------------------------------------------------------------------------------- |
| Organisation | Top-level container for the platform | Centralised governance                                                            |
| Account      | Individual account entity            | Isolates API keys and routing rules                                               |
| Profile      | Business unit segmentation           | Manages regional splits (e.g., "Account A - US Store" vs. "Account A - EU Store") |

Additional capabilities:

- **Platform Setup**: Configure hierarchical organizations with programmatic merchant onboarding. See [Platform Org and Merchant Setup](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles/platform-org-and-merchant-setup).
- **Granular Control**: Isolate API keys and routing rules at the Account ID level.
- **Team Access**: Map your control center users to specific levels of the hierarchy using our [User Management](https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team) controls.

***

### How can I onboard accounts programmatically?

Manual onboarding via a control center is an operational bottleneck. To scale, platforms need to provision sub-accounts, inject credentials, and configure webhooks programmatically at the moment of signup.

Treat account onboarding as an API call, not a support ticket. Juspay Hyperswitch exposes [Management APIs](https://api-reference.hyperswitch.io/v1/merchant-account/merchant-account--create#merchant-account-create) to fully automate the lifecycle.

| Capability         | Description                                                                                  | API Reference                                                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Instant Onboarding | Create a new account entity and inject their processor API keys                              | [Connector Configuration API](https://api-reference.hyperswitch.io/v1/merchant-connector-account/merchant-connector--create#merchant-connector-create) |
| Flexible Liability | Support MoR models (platform holds funds) and Connected Account models (account holds funds) | [Account Management](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles)                                |

#### Example: Create an account

```bash
## Note: Use sandbox endpoint for testing
curl --request POST \
  --url https://api.hyperswitch.io/accounts \
  --header 'api-key: YOUR_API_KEY' \
  --header 'content-type: application/json' \
  --data '{
    "merchant_id": "merchant_abc123",
    "merchant_name": "Acme Store",
    "merchant_details": {
      "primary_contact_person": "John Doe",
      "primary_email": "john@acmestore.com"
    },
    "metadata": {
      "saas_tenant_id": "tenant_456"
    }
  }'
```

> **Try it in sandbox:** Use `https://sandbox.hyperswitch.io` for testing. See our [Sandbox Guide](https://docs.hyperswitch.io/explore-hyperswitch/account-management/sandbox-environment) for details.

***

### How can SaaS platforms standardise complex payment flows across processors?

Different verticals require different flows (e.g., $0 Auth for hotels, 3DS for EU retail, Recurring for subscriptions). Fragmentation across PSP capabilities (e.g., some processors support 3DS, others don't) often forces platforms to write "spaghetti code."

Juspay Hyperswitch normalises complex flows into a standard state machine. Your frontend handles a single response type, regardless of the underlying complexity.

| Feature           | Description                                                            | Reference                                                                                                           |
| ----------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Compliance Ready  | Automatically handles 3D Secure (3DS) challenges across all processors | [3D Secure (3DS)](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/payment-features/3d-secure-3ds) |
| Unified Lifecycle | Perform Auth, Capture, and Void operations using a single API syntax   | [Connector Payment Flows](https://docs.hyperswitch.io/learn-more/hyperswitch-architecture/connector-payment-flows)  |

***

### How can I help accounts avoid vendor lock-in with their saved cards?

If an account stores card data in a PSP-specific vault (e.g., a processor-specific Customer ID), they are vendor-locked. Switching providers means losing all saved customer cards, which destroys recurring revenue.

Use the [Payment Vault](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards) to provide accounts with processor-independent token storage.

| Benefit          | Description                                                                                               |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| Ownership        | You or the account own the tokens, not the PSP.                                                           |
| Interoperability | A card saved during a transaction on one processor can be seamlessly charged via another processor later. |
| Security         | Offload PCI-DSS compliance by using certified secure storage.                                             |

**Reference**: [Network Tokenisation](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation)

***

### How can SaaS platforms simplify support workflows across multiple providers?

Support teams struggle when every PSP returns different error codes (e.g., "Do Not Honour" vs. "Refusal" vs. "Error 402"). Debugging requires deep knowledge of 10+ different vendor systems.

Juspay Hyperswitch translates the chaos of vendor responses into a clean, standardised language for your support and engineering teams.

| Capability             | Description                                                                                  | Reference                                                                                                               |
| ---------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Unified Errors         | Maps thousands of PSP error codes into a Standardised Error Reference (e.g., `card_expired`) | [Error Codes](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/web/error-codes)               |
| Single Source of Truth | View transaction logs, refunds, and disputes across all accounts and processors in one view  | [Analytics and Operations](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations) |

***

### How can SaaS platforms build unified operational interfaces for refunds, disputes, and webhooks?

The payment lifecycle doesn't end at "Checkout." SaaS platforms must also build portals for their accounts to handle Refunds, Disputes, and Webhooks. Building these operational interfaces is painful because every processor has a different API schema for refunds and a different JSON payload for webhooks.

Juspay Hyperswitch standardises the chaotic "Day 2" operations into a clean, unified interface. Your engineering team builds one refund handler and one webhook listener, and it works for all connected processors.

| Feature              | Description                                                                                                         | Reference                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Universal Webhooks   | Ingests disparate events and transforms them into a Standardised Webhook Schema                                     | [Webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks) |
| Dispute Management   | Normalises the Disputes Lifecycle so you can surface evidence submission flows in your SaaS control center          | [Disputes](https://docs.hyperswitch.io/explore-hyperswitch/account-management/disputes)               |
| Stateless Operations | Trigger refunds or voids using Relay APIs, even if the original payment wasn't processed through Juspay Hyperswitch | [Relay APIs](https://api-reference.hyperswitch.io/v1/relay/relay#relay-create)                        |

***

### How can SaaS platforms maintain payment uptime during processor outages?

Global SaaS platforms cannot afford downtime. When a processor in a specific region experiences latency or outages, your accounts blame _you_, not the processor. Without granular visibility into processor performance, your engineering team is flying blind, unable to reroute traffic or uphold SLAs for Enterprise accounts.

Juspay Hyperswitch treats payments as "Critical Infrastructure" and provides deep visibility into the health of your payment mesh, allowing you to proactively manage reliability.

| Feature          | Description                                                                                                              | Reference                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Connector Health | Continuously monitors success rates and latency of every connected processor; automatic failover to healthy alternatives | [Smart Router](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) |
| Open Telemetry   | Emits standard OTel Traces for every request; pipe into Datadog, Prometheus, or Grafana                                  | [Monitoring](https://github.com/juspay/hyperswitch/blob/main/docs/architecture.md#monitoring) |
| System Status    | Access the System Health API to build internal status pages for your support team                                        | [System Health API](https://live.hyperswitch.io/api/health)                                   |

***

### What's next?

Ready to get started? Here are the next steps:

- [Set up multiple accounts and profiles](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles) — Configure your platform hierarchy
- [Configure intelligent routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) — Set up smart routing rules for your accounts
- [Configure smart retries](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/smart-retries) — Improve authorisation rates automatically
- [Implement webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks) — Listen for payment events across all processors
- [View supported connectors](https://juspay.io/integrations) — See the full list of integrated payment providers
- [Try it in sandbox](https://docs.hyperswitch.io/explore-hyperswitch/account-management/sandbox-environment) — Test your integration without touching production
