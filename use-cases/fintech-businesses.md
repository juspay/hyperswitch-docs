---
description: >-
  Augment fintech payment stacks to enable seamless global expansion with smart
  routing, vaulting, and observability
icon: watch-calculator
---

# Fintech Businesses

## TL;DR

Juspay Hyperswitch is an open-source payment orchestration platform designed for Fintech enterprises that need to augment existing payment stacks. It provides modular capabilities—Smart Routing, Network Tokenization, and unified observability—without requiring a full platform migration. Deploy the [connector service](https://github.com/juspay/connector-service) as a stateless integration layer, or self-host within your own infrastructure for complete data sovereignty.

***

## Why do Fintechs need payment orchestration?

Fintech enterprises rarely build payment stacks from scratch. Most established players already operate mature internal ledgers, risk engines, and reconciliation systems. The challenge isn't replacing these systems; it's augmenting them to support new markets, APMs, and compliance requirements without accruing technical debt.

Hyperswitch is designed as a modular middleware layer that injects specific capabilities into your existing stack. The sections below outline the architectural patterns for augmenting a Fintech payment stack.

***

## How can fintechs expand into new geographies faster?

Expanding into new geographies (e.g., adding Pix in Brazil or UPI in India) typically requires months of engineering time to build and maintain new PSP integrations. This slows down market entry and diverts resources from core product work.

Hyperswitch acts as a stateless integration layer. You can utilise our [Connector Crate](https://github.com/juspay/hyperswitch/tree/main/crates/router/src/connector) to instantly access 300+ processor APIs across 50+ global processors without writing a single line of integration code.

| Capability        | Description                                                                                     | Reference                                                                                                |
| ----------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Unified Schema    | Maps disparate upstream APIs (Stripe, Adyen, Checkout.com) into a single Request/Response Model | [Payment Intent Flow](https://api-reference.hyperswitch.io/v1/payments/payments--create#payments-create) |
| Rapid Expansion   | Enable local payment methods (LPMs) like Klarna, WeChat Pay, or Afterpay via configuration      | [Supported Connectors](https://juspay.io/integrations)                                                   |
| Open Contribution | Fork the repo, add a connector, and run it locally or contribute back                           | [Open Source](https://github.com/juspay/hyperswitch)                                                     |

***

## How can fintechs maintain data sovereignty with self-hosted deployment?

Fintechs dealing with high-value transactions or strict regulatory requirements (e.g., CCPA, GDPR) often need full control over their payment infrastructure. While Hyperswitch's SaaS offering is PCI-DSS compliant, self-hosting gives you complete ownership of your data and infrastructure.

Hyperswitch supports a "Bring Your Own Cloud" model. You can deploy the entire stack (Router, Vault, Analytics) as a set of microservices within your own Kubernetes cluster or VPC—without the operational overhead of managing a payment platform from scratch.

| Capability         | Description                                                                                                                            | Reference                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Zero Data Egress   | Sensitive card data (PAN) never leaves your infrastructure; you maintain full ownership of logs and database                           | [Self-Managed Guide](https://docs.hyperswitch.io/explore-hyperswitch/account-management/self-managed-deployment) |
| Compliance Control | Define TLS Termination (the point where encrypted traffic is decrypted) and key management strategies using AWS KMS or HashiCorp Vault | [Security Architecture](https://github.com/juspay/hyperswitch/blob/main/docs/architecture.md#security)           |
| No Vendor Lock-in  | You host the code, so you are not dependent on an external vendor's uptime or roadmap                                                  | [Open Source](https://github.com/juspay/hyperswitch)                                                             |

***

## How can fintechs boost authorisation rates without rebuilding routing logic?

Internal routing engines often struggle to scale. Hardcoding rules like _"If transaction > $500, route to Adyen"_ creates a fragile codebase. Implementing Smart Retries (e.g., retrying a soft decline on a secondary processor) requires complex state management.

Insert Hyperswitch downstream of your Risk Engine to act as a dynamic Smart Router.

| Capability        | Description                                                                                                                               | Reference                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| DSL-Based Routing | Configure complex logic based on BIN, Currency, Amount, or Metadata using our Routing DSL                                                 | [Intelligent Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) |
| Auto-Retries      | Automatically identify Soft Declines (e.g., generic failures) and retry on a secondary connector, potentially boosting auth rates by 2-5% | [Smart Retries](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/smart-retries) |
| A/B Testing       | Run traffic experiments (e.g., "Send 10% of traffic to Worldpay") to benchmark processor performance in real-time                         | [Routing Rules](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing)       |

***

## How can fintechs avoid processor lock-in when storing saved cards?

Relying on PSP-specific tokens (like Stripe `cus_` objects) creates vendor lock-in. Migrating millions of saved cards to a new processor is a high-risk operation that often causes churn.

Hyperswitch provides a [standalone Vault Service](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards) that detaches the stored credential from the processor.

**Centralize card storage across all processors with a single vault.**

**Key benefits:**

1. **PSP-agnostic storage**: Cards are tokenized independently of any specific processor, enabling true portability
2. **Standalone offering**: Use the Vault Service as a standalone component without adopting the full orchestration platform
3. **External vault support**: Already have a vault? Configure Hyperswitch to pass-through tokens or integrate with external providers like VGS or Forter

| Capability        | Description                                                                                                                                             | Reference                                                                                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Network Tokens    | Integrate directly with schemes (Visa/Mastercard) to provision Network Tokens, which offer higher authorisation rates and auto-update for expired cards | [Network Tokenisation](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation)          |
| Token Portability | A card saved during a transaction on Processor A can be seamlessly charged via Processor B                                                              | [Vault Service](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards)                                      |
| External Vaults   | Already have a vault? Configure Hyperswitch to pass-through tokens or integrate with external VGS/Forter setups                                         | [External Vault Setup](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/external-sdk-+-external-vault-setup/processing-payments-with-external-vault) |

***

## How can fintechs manage payment operations without replacing their checkout flow?

Some Fintechs only need to control specific parts of the lifecycle—like issuing refunds or capturing authorized funds—without routing the initial checkout through Hyperswitch.

Use our [Relay APIs](https://api-reference.hyperswitch.io/v1/relay/relay#relay-create) to interact with underlying processors directly. This "passthrough" mode lets you leverage Hyperswitch's unified API for post-payment operations while keeping your existing checkout flow intact.

| Capability           | Description                                                                                                               | Reference                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Unified Refunds      | Issue a refund by passing the `connector_resource_id`; we handle the upstream API call and return a standardised response | [Relay APIs](https://api-reference.hyperswitch.io/v1/relay/relay#relay-create)                              |
| State Reconciliation | Poll the status of any transaction across any connected processor using a single API endpoint                             | [Transaction Status](https://api-reference.hyperswitch.io/v1/payments/payments--retrieve#payments-retrieve) |

***

## How can fintechs maintain consistent retry logic across multiple processors?

Handling error codes from 10+ different processors is a maintenance nightmare. A "Do Not Honor" from one bank might be a "suspected\_fraud" from another, making it impossible to build consistent retry logic or user feedback.

Hyperswitch normalises the chaos of the global payment ecosystem into a strict schema.

**Error Code Unification Example:**

| Source          | Error Code | Error Message               |
| --------------- | ---------- | --------------------------- |
| PSP 1           | `101`      | "Invalid card number"       |
| PSP 2           | `1314`     | "Invalid card"              |
| **Hyperswitch** | `US_1000`  | "Issue with payment method" |

This shows how disparate PSP error codes are mapped to a unified, intelligible standard—enabling consistent retry logic and clearer user feedback.

| Capability       | Description                                                                                                | Reference                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Canonical Errors | Maps thousands of upstream error codes to a Standardised Enum (e.g., `insufficient_funds`, `expired_card`) | [Error Codes](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/web/error-codes) |

***

## How can fintechs detect payment anomalies before they impact revenue?

Blind spots in processor performance can lead to lost revenue. If a specific BIN range is failing on a processor, you need to know promptly—not when the monthly report comes out.

Hyperswitch provides observability capabilities to help monitor payment operations.

| Capability           | Description                                                                                                              | Reference                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| OpenTelemetry (OTel) | The Router can emit OTel Traces for API calls; integrate with observability tools like Datadog, Prometheus, or Honeycomb | [Monitoring Architecture](https://github.com/juspay/hyperswitch/blob/main/docs/architecture.md#monitoring)              |
| Granular Metrics     | Monitor latency and success rates per Connector, Account, or Region; set alerts for anomalies                            | [Analytics and Operations](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations) |

***

## What's next?

Ready to augment your payment stack? Here are the next steps:

- [Explore intelligent routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing) — Set up smart routing rules
- [Configure smart retries](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/smart-retries) — Improve authorisation rates automatically
- [Implement webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks) — Standardise event handling across processors
- [View supported connectors](https://juspay.io/integrations) — See the full list of integrated payment providers
- [Try it in sandbox](https://docs.hyperswitch.io/explore-hyperswitch/account-management/sandbox-environment) — Test your integration without touching production
- [Deploy self-managed](https://docs.hyperswitch.io/explore-hyperswitch/account-management/self-managed-deployment) — Run Hyperswitch in your own infrastructure
