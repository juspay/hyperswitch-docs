---
description: Oct'26 - Dec'26
icon: road
---

# Roadmap - Q4 2026

🗺️ Our roadmap typically spans a three-month period. Before the start of every quarter, we come together to define what we'll work on next based on our core values, progress from the previous roadmap, learnings from the past quarter, and feedback from the community.

👂 As always, we continue to listen to your feedback and adapt our plans as needed.

### Core Values

Our core values have remained largely unchanged since the early days:

• Make payments more **accessible** and **affordable** for every digital business.

• Stay **simple** and **lightweight**, while remaining **reliable** and **scalable** as a payment switch.

• Be **community-first** in the ideation, planning, and execution of features.

***

### Roadmap Themes

While there are many problems to solve in payments, our current focus is centered around five key themes.

#### 🧱 Composability

Enable businesses to independently adopt and compose the Hyperswitch modules they need to build a tailored, high-performance payments stack. These modules include payment processing, PCI vaults, intelligent routing, reconciliation, cost observability, revenue recovery, and card-network-certified services such as 3DS and network tokenization.

#### 🌐 Connectedness

Expand the Hyperswitch operating system through broader integrations across payment processors, vaults, payouts, fraud providers, subscription platforms, tokenization services, and more—while continuously improving and maintaining existing integrations.

#### 🎯 Reducing Payment Operations

Managing payments across multiple countries, currencies, and processors should not increase operational complexity. Hyperswitch aims to eliminate this overhead so businesses can focus on their core products and customers.

#### 🛡️ Reliability

Build fault tolerance, capacity resilience, and change tolerance into the payment platform to maximize uptime and confidence in production.

#### 🚀 Developer Experience

Provide a best-in-class self-service and self-hosting experience for developers adopting or contributing to Hyperswitch.

***

## Roadmap

### 🧱 Composability

#### Fraud Management Enhancements

BIN blocking support for both Pay-ins and Payouts, with configuration and management capabilities available through the dashboard.

#### Decoupling Connector Integrations

The connector integration layer is being decoupled into [**hyperswitch-prism**](https://github.com/juspay/hyperswitch-prism)**:** a stateless, embeddable payment integration library with multi-language SDK support.

Today, hyperswitch-prism powers **118 payments connectors** and **14 payouts connectors**,. During the coming quarter, we will continue expanding payment and payout coverage while adding support for additional connector categories, including:

* Vault connectors
* Fraud & Risk Management (FRM) connectors
* Surcharge connectors

#### Intelligent Routing Enhancements

Enhancing Intelligent Routing with **Volume Commitment Routing**, enabling merchants to continue benefiting from authorization rate optimization and rule-based routing while meeting committed transaction volume or GMV targets with PSPs to unlock off-ledger discounts and rebates on processing fees.

#### Vault Service Enhancements

Expanding the Hyperswitch Vault / Payment Method Service with:

1. **External Vault Integrations**
   * Extend support for external vault tokens across additional payment flows.
   * Enable Network Tokenization for external vault integrations.
2. **Modular Vault Enhancements**
   * Support digital wallets, including Apple Pay and Google Pay, through Modular Vault.
   * Extend Modular Vault capabilities to support Payouts.
3. **Proxy Enhancements**
   * Expand Proxy support to additional payment flows.
   * Support additional HTTP request types through Proxy.
4. **Analytics & Observability**
   * Enhance analytics and observability across vault and proxy operations.

#### Headless Vault SDK

Decoupling the Vault UI from the SDK, enabling teams to build fully customized payment method experiences while leveraging the underlying vault capabilities.

***

### 🌐 Connectedness

#### New Integrations

* Worldpay RAFT
* Mifinity Payout
* Paysafe Payouts

#### Enhancements to Existing Integrations

* DataTrans - Accepting connector metadata
* Paypal - Returning Customer Flow
* Mifinity Payout - Pay by any bank
* JP Morgan - Recurring payments
* JP Morgan - MITs using NTID
* JP Morgan - 3DS and pass through 3DS
* Envoy - Webhooks handling
* Adyen - Version upgrade
* JP Morgan Orbital - Enhancement for flows
* Worldpay WPG - Recurring cards

[Learn more about the existing connectors supported by Hyperswitch](https://docs.hyperswitch.io/explore-hyperswitch/connectors)

***

### 🎯 Reducing Payment Operations

#### Reconciliation Enhancements

**Linked Reconciliation View**

Bringing all legs of a reconciliation together in one place. Merchants will be able to open an expanded report that links related transactions across every source, so they can trace a payment's full journey and find where it breaks.

**Reconciliation Status APIs**

Adding GET APIs, authenticated with API keys, so merchants can fetch the latest reconciliation status for their transactions. Teams can pull results straight into their own systems and workflows without exporting from the dashboard.

**Embeddable Recon Dashboard**

Making the full reconciliation dashboard embeddable, so merchants and platforms can place it inside their own products and internal tools with the same views, workflows and exception handling.

[Learn more about existing reconciliation features](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/reconciliation)

***

### 🛡️ Reliability & Systems

#### Multi-Region Active-Passive Setup

Conducting production disaster recovery drills across the US and EU regional active-passive deployments to further validate operational readiness and resilience.

#### Multi-cloud support enhancement

Equal reliability, provisioning, and support depth across on-prem, AWS, GCP, Azure, Oracle

#### Observability & Alerting for Self-Hosted Hyperswitch

Observability and alerting will be shipped **as part of the Hyperswitch product**, deployed by the merchant into their own environment. Only **alerts** cross the boundary to Juspay — never metrics, logs, or transaction data.

#### Automated Regression Testing

Major enhancements to our regression testing framework to replay production traffic against every code change before release, deterministically validating behavior, surfacing precise divergence reports, and giving teams greater confidence that changes won't introduce regressions before they reach production.

***

### 🚀 Developer Experience

#### Agentic Interface for Hyperswitch

Deploying and operating Hyperswitch Enterprise Edition will become significantly easier with a specialized agentic interface for exploring deployments, tracing requests, debugging issues, and analyzing system behavior.

***

### Want to contribute to the roadmap?

Have an idea or feature request?

[Submit it here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests)

When submitting an idea, include a brief explanation of:

• **What** you'd like to see

• **Why** it would be valuable
