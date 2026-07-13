---
description: July'26 to Sep'26
icon: road
---

# Roadmap – Q3 2026

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

#### Account Updater

Adding support for Juspay's Account Updater as a modular service that automatically keeps stored card credentials up to date, helping recurring payments succeed without customer intervention.

#### Offers Engine

Introducing a native Offers Engine within Hyperswitch that enables merchants to configure and manage discounts and cashback campaigns directly from the Hyperswitch Control Center.

#### Decoupling Connector Integrations

The connector integration layer is being decoupled into [**hyperswitch-prism**](https://github.com/juspay/hyperswitch-prism)**:** a stateless, embeddable payment integration library with multi-language SDK support.

Today, hyperswitch-prism powers **97 payment connectors** and **5 payout connectors**. During the coming quarter, we will continue expanding payment and payout coverage while adding support for additional connector categories, including:

* Vault connectors
* &#x20;Fraud & Risk Management (FRM) connectors
* Surcharge connectors

#### Intelligent Routing Enhancements

Enhancing the intelligent routing engine with **multi-objective routing** to optimize both authorization rates and payment processing costs. Also adding support for A/B Testing to compare different routing configurations.

#### Vault Service Enhancements

Expanding the Hyperswitch Vault / Payment Method Service with:

* Support for custom tokens
* Enhanced analytics and observability
* Network Tokenization support for External vaults
* Supporting additional request types for Proxy flows

#### Headless Vault SDK

Decoupling the Vault UI from the SDK, enabling teams to build fully customized payment method experiences while leveraging the underlying vault capabilities.

***

### 🌐 Connectedness

#### New Integrations

* TSYS Transit (Cards)
* Givepayments (Cards)

#### Enhancements to Existing Integrations

* Deutsche Bank - Payouts
* TrueLayer - Returning customer flow
* Checkout.com - TLID handling
* dLocal - GCash recurring payments
* Paysafe - Google Pay
* Payload - Payouts
* Payload - Split Payments
* Barclaycard - 3DS Payments
* PayPal - Returning customer flow

[Learn more about the existing connectors supported by Hyperswitch](https://docs.hyperswitch.io/explore-hyperswitch/connectors)

***

### 🎯 Reducing Payment Operations

#### Reconciliation Enhancements

**Improved Cashflow Visibility**

Revamping reconciliation analytics to provide a clearer view of how money moves through every stage of reconciliation. Teams will be able to trace cashflows end-to-end, identify matched, pending, delayed, and mismatched transactions, and investigate exceptions faster.

**Better Control Over Uploaded Data**

Introducing stronger validation and review workflows before reconciliation begins. Merchants will be able to preview uploaded files, inspect potential records and errors, discard incorrect uploads, and resolve issues before processing.

**Revamped User Experience**

Redesigning the reconciliation experience to make day-to-day operations faster and more intuitive, with improved workflows, better exception handling, clearer navigation, and more actionable operational insights.

[Learn more about existing reconciliation features](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/reconciliation)

***

### 🛡️ Reliability & Systems

#### Multi-Region Active-Passive Setup

Conducting production disaster recovery drills across the US and EU regional active-passive deployments to further validate operational readiness and resilience.

#### Automated Regression Testing

Major enhancements to our regression testing framework to replay production traffic against every code change before release, deterministically validating behavior, surfacing precise divergence reports, and giving teams greater confidence that changes won't introduce regressions before they reach production.

***

### 🚀 Developer Experience

#### Agentic Interface for Hyperswitch

Deploying and operating Hyperswitch Enterprise Edition will become significantly easier with a specialized agentic interface for exploring deployments, tracing requests, debugging issues, and analyzing system behavior.

A beta release with **Bring Your Own LLM (BYO-LLM)** support will be available during the quarter.

[Learn more about Revenue Recovery](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/revenue-recovery)

***

### Want to contribute to the roadmap?

Have an idea or feature request?

[Submit it here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests)

When submitting an idea, include a brief explanation of:

• **What** you'd like to see

• **Why** it would be valuable
