---
description: Hyperswitch roadmap (Jan to Mar'24)
---

# 🛣 Roadmap - Q1 2024

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, [previous roadmap](roadmap.md), findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

## Recap of Q4 2023 <a href="#recap-of-q4-2023" id="recap-of-q4-2023"></a>

Lets start with a short recap of Q4 2023

:new: More new features and experiences

* 3DS Smart Retries for Fraud detected payments
* Easy installation of Hyperswitch using Helm charts and AWS Cloud formation setup
* New Processor integrations - `GoCardless`, `Bank of America`, `Helcim`, `Prophetpay`, `Volt`
* Upgrades to existing processor integrations - `Cybersource`, `Paypal`, `Braintree`
* Fraud checks with `Signifyd` and `Riskified` to reduce Chargebacks

:open\_hands: Changed our policy from `Open Core` to `100% Open Source`. So previously commercial, enterprise features such as Control Centre, Smart Routing, Web Checkout, Card Vault, Fraud & Risk Integrations an many more were made available in the open source project.

:two\_men\_holding\_hands:Active code contributors to Hyperswitch Open Source doubled from 70 to 150. There are  product and business audience contributing with ideas.

:face\_with\_hand\_over\_mouth:Last but not least. We were overwhelmed !!! At the beginning of Q4 2023, we allocated 30% of bandwidth for community feature requests and managing community contributions. But we were surprised by the overwhelming response and passion from the community in terms of `Feature requests` and `contributions`.

> Hence, Q1 2024 is “For the Community”. Because, we will be dedicating 50% of our bandwidth for community feature requests.&#x20;

## Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

## Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

There are a lot of problems to be solved in payments, but our majority of our current focus falls under 5 themes below.

🌎 **Community Feature Requests:** Most of our community feature requests falls under one of the above themes, but we still keep this as a separate theme, because we intend to actively explore new problem statements and themes from the community before scheduling actual feature work.

👨‍💻 **Developer Experience:** Providing a great self-service and self-installation experience for developers who wish to use or contribute back to Hyperswitch.

💰 **Reducing Payment Costs:** Payments should be like a free utility for digital businesses. Any business should be able reduce payment processing costs by embracing the diversity in payments.

📈 **Improving Authorization Rates:** Ensuring a best-in-class payment experience and access to latest innovations in the payments ecosystem for all businesses.

👍 **Reducing Payment Operations:** Managing payments across multiple countries, currencies and processors should not add to the administrative burden on businesses. Hence, Hyperswitch intends to eliminate all such operational burdens so that businesses can focus on the core activities.

<table data-header-hidden><thead><tr><th width="125"></th><th></th></tr></thead><tbody><tr><td><strong>Legend</strong></td><td><strong>Description</strong></td></tr><tr><td>🟩</td><td>Feature completed</td></tr><tr><td>🟧</td><td>Feature in progress</td></tr><tr><td>🟥</td><td>Work not started</td></tr><tr><td>💪</td><td>Stretch target</td></tr><tr><td>🚛</td><td>Backlog feature from Q4 2023</td></tr></tbody></table>

## Roadmap <a href="#roadmap" id="roadmap"></a>

### Community Feature Requests <a href="#community-feature-requests" id="community-feature-requests"></a>

* 🟥 Card vault enhancements to support more use cases - enable vaulting before payment, card fingerprinting and optional 3DS verification before vaulting
* 🟧 Enhance MIT payments (Merchant Initiated Transactions) to accept `raw card data` and `network_reference_id.` This will allow for payment gateway agnostic MIT payments
* _(removed from the Q1 roadmap)_ Enabling card transactions using `payment gateway token` to ensure business continuity for merchants with card vaulted with payment gateways&#x20;
*   🟥 New connector and payment method Integrations&#x20;

    * Place2Pay
    * Billwerk
    * Pix and Boleto via Adyen

    _(the list of connectors will keep expanding as we receive more requests from the community!!! )_

### Developer Experience <a href="#developer-experience" id="developer-experience"></a>

* 🟧 Code restructuring for enhancing readability and ease of contributions
* 🟧 Helm charts enhancement to enable easy installation on Azure, Google Cloud and within existing Kubernetes clusters
* 🟩 Helm charts will support installation of `hyperswitch-card-vault`
* 🟧 PCI Software Security Standard (S3) certification. At the moment, Hyperswitch application is battle tested for PCI L1 compliance. While PCI Software Security Standard (S3) is not mandatory for Hyperswitch related functionalities, we are undertaking the certification to further augment our security standards
* 🟧 Adding more developer help videos and improving developer documentations for Hyperswitch features, components and usage
* 💪 Open sourcing the Native Unified Checkout SDK (Android and iOS)
* 🟧  Diagnostics tool to determine health of your on-cloud Hyperswitch stack setup

### Reduce Payment Costs <a href="#reduce-payment-costs" id="reduce-payment-costs"></a>

* 🚛 🟧 Enabling surcharge for specific payment methods to promote low cost payment methods
* 🚛 🟧 Support Plaid for ACH account verification

### Improving Payment Authorization Rates <a href="#improving-payment-authorization-rates" id="improving-payment-authorization-rates"></a>

* 🟧 Decoupled 3DS authentication and authorization using EMVCo certified 3DS connectors, for improving payment authorization rates and customer experience.
* 🚛 🟥 Paypal Vault flows for improving repeat user payment experience

### Reducing Payment Operations <a href="#reducing-payment-operations" id="reducing-payment-operations"></a>

* 🚛 🟧 Enhanced Audit trail visibility for Payments, Refunds, Disputes on Hyperswitch Control Centre
* 🟩 Support for Hosted Checkout Page on Web&#x20;
* 🟧 Mitigating fraud by defining Block List rules to block transactions from specific customer ID, card bins, card numbers and more parameters
* 🟥 Payment audit trail will carry more information for Hyperswitch Cloud users - Consolidated API logs, Webhook and State change events on the Control Centre
* 🟥 Enhanced search using Global Identifiers for improved discoverability. Hyperswitch Cloud users can use the Control Center to search for payments, customers, refunds, connector transaction IDs and get all related data
* 🟥 Create and manage payment links from the Hyperswitch control centre
* 🟥 Dispute management and evidence submission workflow on Hyperswitch Control Centre
* 🟥 Hyperswitch Control Centre will allow to customize payment methods at country and currency level and support more configurations
* 💪🟥 Create custom roles for Identity and Access Management

### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
