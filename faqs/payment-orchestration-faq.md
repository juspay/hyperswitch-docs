---
description: Find answers to common questions about payment orchestration faq and payment best practices
hidden: true
noIndex: true
---

# Payment Orchestration FAQ

## What is payment orchestration?

Payment orchestration is a control layer that sits between your application and multiple payment processors or acquirers. It provides a unified API while enabling routing, retries, failover, observability, and optimization across providers.

Processors continue to handle authorization, clearing, and settlement. The orchestration layer determines how and where transactions are processed.

If you're new to Juspay Hyperswitch, start here:

- [What is Juspay Hyperswitch?](https://docs.hyperswitch.io/about-hyperswitch/readme-2)
- [Architecture Overview](https://hyperswitch.io/blog/building-hyperswitch-the-world-s-first-open-source-payments-platform)

## Does orchestration replace my payment processor?

No. Orchestration complements processors.

Processors:

- Connect to card networks
- Authorize and settle transactions
- Provide risk tooling

Orchestration:

- Routes transactions
- Applies retry and failover logic
- Normalizes responses
- Centralizes configuration
- Enables cross-PSP reporting

For implementation details, see:

- [Connector Integration](https://docs.hyperswitch.io/explore-hyperswitch/connectors)
- [Payments API Reference](https://api-reference.hyperswitch.io/introduction)

## Why would I need orchestration if I already use a PSP?

A single PSP may be sufficient early on. Orchestration becomes relevant when payments materially impact revenue, cost, or availability.

Common triggers include:

- Improving authorization rates
- Reducing processing costs
- Expanding to multiple regions
- Avoiding single-provider dependency
- Supporting marketplace or ISV complexity

For routing and configuration examples:

- [Routing Documentation](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing)

## How does orchestration improve authorization rates?

Approval improvements typically come from:

- BIN or country-based routing
- Local acquirer selection
- Success-rate-aware routing
- Automated retry with alternate processors

For technical details:

- [Routing Rules Configuration](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing)

## How does orchestration reduce processing costs?

Cost optimization may involve:

- Routing to lower-cost processors
- Domestic versus cross-border optimization
- Negotiating across multiple providers
- Intelligent retry strategies

To configure cost-based routing:

- [Connector Matrix](https://juspay.io/integrations)

## How complex is it to implement?

Implementation typically involves:

1. Integrating with the Payments API
2. Configuring one or more connectors
3. Defining routing rules
4. Testing in sandbox

Start here:

- [Your First Payment Guide](https://docs.hyperswitch.io/#your-first-payment)
- [Unified Local Setup Using Docker](https://docs.hyperswitch.io/hyperswitch-open-source/readme-1/unified-local-setup-using-docker)

For API details:

- [API Reference](https://api-reference.hyperswitch.io/introduction)

## Can I migrate gradually?

Yes. Migration can be done incrementally using routing rules or traffic splitting.

Common strategies:

- Route a small percentage of traffic
- Pilot by geography or BIN range
- Run A/B comparisons across processors
- Enable instant rollback

## What happens if the orchestration layer fails?

High availability depends on deployment architecture.

Best practices include:

- Horizontal scaling
- Load balancing
- Health checks
- Observability and alerting

See:

- [Deployment Guide](https://docs.hyperswitch.io/hyperswitch-open-source/readme-1)

## How does orchestration affect PCI compliance?

Compliance impact depends on deployment model and integration pattern.

Considerations include:

- Card data handling
- Tokenization strategy
- Encryption key management
- Self-hosted versus SaaS responsibilities

For more details:

- [Security and Compliance Overview](https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance)

## How does orchestration handle multiple payment methods?

Orchestration normalizes payment methods across connectors while preserving connector-specific capabilities.

Supported methods may include:

- Cards
- ACH
- Wallets
- Buy Now Pay Later
- Alternative payment methods

See:

- [Supported Payment Methods](https://juspay.io/integrations)
- [Connector Documentation](https://docs.hyperswitch.io/explore-hyperswitch/connectors)

## How does reporting and reconciliation work?

Juspay Hyperswitch centralizes transaction metadata and routing decisions, enabling unified reporting across processors.

For logging and monitoring:

- Observability Documentation
- Log Export and Storage

This simplifies:

- [Cross-PSP reconciliation](https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product)
