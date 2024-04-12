---
description: Hyperswitch roadmap (Jan to Mar' 24)
---

# 🛣️ Previous roadmap - Q1 2024

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, [previous roadmap](roadmap-1.md), findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

## Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

<table data-header-hidden><thead><tr><th width="125"></th><th></th></tr></thead><tbody><tr><td><strong>Legend</strong></td><td><strong>Description</strong></td></tr><tr><td>🟩</td><td>Feature completed</td></tr><tr><td>🟧</td><td>Feature in progress</td></tr><tr><td>🟥</td><td>Work not started</td></tr><tr><td>💪</td><td>Stretch target</td></tr><tr><td>🚛</td><td>Backlog feature from Q4 2023</td></tr></tbody></table>

## Roadmap <a href="#roadmap" id="roadmap"></a>

### Community Feature Requests <a href="#community-feature-requests" id="community-feature-requests"></a>

* 🟩 Card vault enhancements to support more use cases - enable vaulting before payment, card fingerprinting
* 🟩 Enhance MIT payments (Merchant Initiated Transactions) to accept `raw card data` and `network_reference_id.` This will allow for payment gateway agnostic MIT payments
* _(removed from the Q1 roadmap)_ Enabling card transactions using `payment gateway token` to ensure business continuity for merchants with card vaulted with payment gateways&#x20;
*   🟩 New connector and payment method Integrations&#x20;

    * 🟩 Place2Pay
    * 🟩 Billwerk
    * 🟩 Pix and Boleto via Adyen

    _(the list of connectors will keep expanding as we receive more requests from the community!!! )_

### Developer Experience <a href="#developer-experience" id="developer-experience"></a>

* 🚛 Code restructuring for enhancing readability and ease of contributions
* 🟩 Helm charts enhancement to enable easy installation on Azure, Google Cloud and within existing Kubernetes clusters
* 🟩 Helm charts will support installation of `hyperswitch-card-vault`
* 🚛  PCI Software Security Standard (S3) certification. At the moment, Hyperswitch application is battle tested for PCI L1 compliance. While PCI Software Security Standard (S3) is not mandatory for Hyperswitch related functionalities, we are undertaking the certification to further augment our security standards
* 🟩Adding more developer help videos and improving developer documentations for Hyperswitch features, components and usage
* 💪🚛 Open sourcing the Native Unified Checkout SDK (Android and iOS)
* 🟩 Diagnostics tool to determine health of your on-cloud Hyperswitch stack setup

### Reduce Payment Costs <a href="#reduce-payment-costs" id="reduce-payment-costs"></a>

* 🟩 Enabling surcharge for specific payment methods to promote low cost payment methods
* 🚛 🟩 Hyperswitch API supports for Plaid for ACH account verification

### Improving Payment Authorization Rates <a href="#improving-payment-authorization-rates" id="improving-payment-authorization-rates"></a>

* 🟩Decoupled 3DS authentication and authorization using EMVCo certified 3DS connectors, for improving payment authorization rates and customer experience.
* 🚛 Paypal Vault flows for improving repeat user payment experience

### Reducing Payment Operations <a href="#reducing-payment-operations" id="reducing-payment-operations"></a>

* 🟩 Enhanced Audit trail visibility for Payments, Refunds, Disputes on Hyperswitch Control Centre
* 🟩 Support for Hosted Checkout Page on Web&#x20;
* 🟩 Mitigating fraud by defining Block List rules to block transactions from specific customer ID, card bins, card numbers and more parameters
* 🟩 Enhanced search using Global Identifiers for improved discoverability. Hyperswitch Cloud users can use the Control Center to search for payments, customers, refunds, connector transaction IDs and get all related data
* 🟩 Dispute management and evidence submission workflow on Hyperswitch Control Centre
* 🟩 Hyperswitch Control Centre will allow to customize payment methods at country and currency&#x20;
* 🟩 Create custom roles for Identity and Access Management

### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
