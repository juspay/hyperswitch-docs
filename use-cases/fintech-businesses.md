---
description: >-
  Common payment augmentation patterns for FinTech enterprises, from adding
  processors to improving routing, vaulting, and operational visibility.
icon: watch-calculator
---

# Fintech Businesses

## TL;DR

Juspay Hyperswitch is an open-source payment orchestration platform designed for Fintech enterprises that need to augment existing payment stacks. It provides modular capabilities—Smart Routing, Network Tokenization, and unified observability—without requiring a full platform migration. Deploy it as a stateless integration layer or self-manage it within your own infrastructure for complete data sovereignty.

---

## Why do Fintechs need payment orchestration?

Fintech enterprises rarely build payment stacks from scratch. Most established players already operate mature internal ledgers, risk engines, and reconciliation systems. The challenge isn't replacing these systems; it's augmenting them to support new markets, APMs, and compliance requirements without accruing technical debt.

Hyperswitch is designed as a modular middleware layer that injects specific capabilities into your existing stack. The sections below outline the architectural patterns for augmenting a Fintech payment stack.

---

## How can I add new processors instantly?

Expanding into new geographies (e.g., adding Pix in Brazil or UPI in India) typically requires months of engineering time to build and maintain new PSP integrations. This slows down market entry and diverts resources from core product work.

Hyperswitch acts as a stateless integration layer. You can utilise our [Connector Crate](https://github.com/juspay/hyperswitch/tree/main/crates/router/src/connector) to instantly access 300+ processor APIs across 50+ global processors without writing a single line of integration code.

| Capability | Description | Reference |
|------------|-------------|-----------|
| Unified Schema | Maps disparate upstream APIs (Stripe, Adyen, Checkout.com) into a single Request/Response Model | [Payment Intent Flow](https://api-reference.hyperswitch.io/v1/payments/payments--create#payments-create) |
| Rapid Expansion | Enable local payment methods (LPMs) like Klarna, WeChat Pay, or Afterpay via configuration | [Supported Connectors](https://juspay.io/integrations) |
| Open Contribution | Fork the repo, add a connector, and run it locally or contribute back | [Open Source](https://github.com/juspay/hyperswitch) |

---

## How does self-managed deployment work?

Fintechs dealing with high-value transactions or strict regulatory bodies (e.g., CCPA, GDPR) often cannot use shared SaaS infrastructure due to Data Sovereignty and PCI-DSS requirements.

Hyperswitch supports a "Bring Your Own Cloud" model. You can deploy the entire stack (Router, Vault, Analytics) as a set of microservices within your own Kubernetes cluster or VPC.

| Capability | Description | Reference |
|------------|-------------|-----------|
| Zero Data Egress | Sensitive card data (PAN) never leaves your infrastructure; you maintain full ownership of logs and database | [Self-Managed Guide](https://docs.hyperswitch.io/explore-hyperswitch/account-management/self-managed-deployment) |
| Compliance Control | Define TLS Termination (the point where encrypted traffic is decrypted) and key management strategies using AWS KMS or HashiCorp Vault | [Security Architecture](https://github.com/juspay/hyperswitch/blob/main/docs/architecture.md#security) |
| No Vendor Lock-in | You host the code, so you are not dependent on an external vendor's uptime or roadmap | [Open Source](https://github.com/juspay/hyperswitch) |

---

## How does Smart Routing improve authorisation rates?

Internal routing engines often struggle to scale. Hardcoding rules like *"If transaction > $500, route to Adyen"* creates a fragile codebase. Implementing Smart Retries (e.g., retrying a soft decline on a secondary processor) requires complex state management.

Insert Hyperswitch downstream of your Risk Engine to act as a dynamic Smart Router.

| Capability | Description | Reference |
|------------|-------------|-----------|
| DSL-Based Routing | Configure complex logic based on BIN, Currency, Amount, or Metadata using our Routing DSL | [Intelligent Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) |
| Auto-Retries | Automatically identify Soft Declines (e.g., generic failures) and retry on a secondary connector, potentially boosting auth rates by 2-5% | [Smart Retries](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/smart-retries) |
| A/B Testing | Run traffic experiments (e.g., "Send 10% of traffic to Worldpay") to benchmark processor performance in real-time | [Routing Rules](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) |

---

## Why should I use vendor-agnostic vaulting?

Relying on PSP-specific tokens (like Stripe `cus_` objects) creates vendor lock-in. Migrating millions of saved cards to a new processor is a high-risk operation that often causes churn.

Hyperswitch provides a [standalone Vault Service](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards) that detaches the stored credential from the processor.

| Capability | Description | Reference |
|------------|-------------|-----------|
| Network Tokens | Integrate directly with schemes (Visa/Mastercard) to provision Network Tokens, which offer higher authorisation rates and auto-update for expired cards | [Network Tokenisation](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation) |
| Token Portability | A card saved during a transaction on Processor A can be seamlessly charged via Processor B | [Vault Service](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards) |
| External Vaults | Already have a vault? Configure Hyperswitch to pass-through tokens or integrate with external VGS/Forter setups | [External Vault Setup](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/external-sdk-+-external-vault-setup/processing-payments-with-external-vault) |

---

## How can I manage payments without routing checkout?

Some Fintechs only need to control specific parts of the lifecycle—like issuing refunds or capturing authorized funds—without routing the initial checkout.

Use our [Relay APIs](https://api-reference.hyperswitch.io/v1/relay/relay#relay-create) to interact with underlying processors in a "Headless" mode.

| Capability | Description | Reference |
|------------|-------------|-----------|
| Unified Refunds | Issue a refund by passing the `connector_resource_id`; we handle the upstream API call and return a standardised response | [Relay APIs](https://api-reference.hyperswitch.io/v1/relay/relay#relay-create) |
| State Reconciliation | Poll the status of any transaction across any connected processor using a single API endpoint | [Transaction Status](https://api-reference.hyperswitch.io/v1/payments/payments--retrieve#payments-retrieve) |

---

## How does unified error handling reduce complexity?

Handling webhooks and error codes from 10+ different processors is a maintenance nightmare. A "Do Not Honor" from one bank might be a "suspected_fraud" from another, making it impossible to build consistent retry logic or user feedback.

Hyperswitch normalises the chaos of the global payment ecosystem into a strict schema.

| Capability | Description | Reference |
|------------|-------------|-----------|
| Canonical Errors | Maps thousands of upstream error codes to a Standardised Enum (e.g., `insufficient_funds`, `expired_card`) | [Error Codes](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/web/error-codes) |
| Unified Webhooks | Listen to One Webhook Format; we ingest raw PSP webhooks, parse them, and forward a clean JSON payload to your ledger | [Webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks) |

---

## How does real-time observability protect revenue?

Blind spots in processor performance lead to lost revenue. If a specific BIN range is failing on Adyen, you need to know immediately—not when the monthly report comes out.

Hyperswitch treats observability as a first-class citizen.

| Capability | Description | Reference |
|------------|-------------|-----------|
| OpenTelemetry (OTel) | The Router emits high-cardinality OTel Traces for every API call; pipe directly into Datadog, Prometheus, or Honeycomb | [Monitoring Architecture](https://github.com/juspay/hyperswitch/blob/main/docs/architecture.md#monitoring) |
| Granular SLAs | Monitor latency and success rates per Connector, Account, or Region; set alerts for anomalies (e.g., "Latency > 2s on Stripe US") | [Analytics and Operations](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations) |

---

## What's next?

Ready to augment your payment stack? Here are the next steps:

- [Explore intelligent routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) — Set up smart routing rules
- [Configure smart retries](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/smart-retries) — Improve authorisation rates automatically
- [Implement webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks) — Standardise event handling across processors
- [View supported connectors](https://juspay.io/integrations) — See the full list of integrated payment providers
- [Try it in sandbox](https://docs.hyperswitch.io/explore-hyperswitch/account-management/sandbox-environment) — Test your integration without touching production
- [Deploy self-managed](https://docs.hyperswitch.io/explore-hyperswitch/account-management/self-managed-deployment) — Run Hyperswitch in your own infrastructure
