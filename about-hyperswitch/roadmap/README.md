---
description: Hyperswitch roadmap (Apr to Jun'24)
---

# 🛣️ Roadmap - Q2 2024

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, [previous roadmap](roadmap-1.md), findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

## Recap of Q1 2024 <a href="#recap-of-q4-2023" id="recap-of-q4-2023"></a>

Lets start with a short recap on what was released new in Q1 2024

* New connector integrations
  * Cybersource support for ApplePay, GooglePay
  * PlacetoPay support for card payments
  * [3Dsecure.io](http://3dsecure.io) integration for 3DS authentication
  * Pix and Boleto via Adyen
* Card vault was enhanced to support fingerprinting and MIT recurring payments
* Payment gateway agnostic MIT payments through Stripe, Adyen and Cybersource
* Upgraded helm charts to support cloud agnostic installation of Hyperswitch
* Enhanced audit trail for visibility into payment flows
* Decoupled 3DS authentication for smoother payment experience and better conversion rates authorization rates
* Customs roles on Control center for identity & access management
* Retries for failed webhooks
* Enabling surcharge for specific payment methods to promote low cost payment methods
* Control center can manage support tracking, submitting evidences for disputes (via Stripe) - we will be extending to more processors in the upcoming quarters.
* Global ID based search in control center to quickly access a payment record
* Block lists to prevent fraudulent card payments based on card issuers and fingerprints
* Interface to dynamically select components (Storage Backend, Secrets Manager) during runtime

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

<table data-header-hidden><thead><tr><th width="125"></th><th></th></tr></thead><tbody><tr><td><strong>Legend</strong></td><td><strong>Description</strong></td></tr><tr><td>🟩</td><td>Feature completed</td></tr><tr><td>🟧</td><td>Feature in progress</td></tr><tr><td>🟥</td><td>Work not started</td></tr><tr><td>💪</td><td>Stretch target</td></tr><tr><td>🚛</td><td>Backlog feature from Q1 2024</td></tr></tbody></table>

## Roadmap <a href="#roadmap" id="roadmap"></a>

### Community Feature Requests <a href="#community-feature-requests" id="community-feature-requests"></a>

* 🟧 🚛 Vaulting payment methods in non-payment flows
* 🟥 Support business continuity for MIT payment through PSP tokens
* 🟥 Card vaulting enhancements - support nickname updation
* 🟧 Hyperswitch Widgets for Quick Checkout experience - Paypal, Applepay and Googlepay
* 🟥 New connector and payment method Integrations
  * [Planet.com](http://planet.com) for card payments
  * Netcetera for 3DS service

_(list of connectors will keep expanding as we receive more requests from the community!!! )_

### Developer Experience <a href="#developer-experience" id="developer-experience"></a>

* 🟧 🚛 Code restructuring for enhancing readability, reducing compile & build times
* 🟧 PCI Software Security Standard (S3) certification. At the moment, Hyperswitch application is battle tested for PCI L1 compliance. While PCI Software Security Standard (S3) is not mandatory for Hyperswitch related functionalities, we undertook the certification starting Feb 2024 to further augment our security standards. _Expected closure by June 2024_
* 🟥 Open sourcing the Native Unified Checkout SDK (Android and iOS)

### Improving Payment Authorization Rates <a href="#improving-payment-authorization-rates" id="improving-payment-authorization-rates"></a>

* 🟧 🚛 Enable scanning of cards to reduce manual entry of card details by the customer
* 🟧 Native 3DS on Android and iOS apps
* 🚛 🟥 Paypal Vault flows for improving repeat user payment experience
* 🟥 Customer initiated payment retries on Hyperswitch Unified Checkout
* 🟥 Account verification for bank payment methods like ACH and SEPA

### Reducing Payment Operations <a href="#reducing-payment-operations" id="reducing-payment-operations"></a>

* 🟥 Payment audit trail will carry more information for Hyperswitch Cloud users - Consolidated API logs, Webhook and State change events on the Control Centre
* 🟧 Hyperswitch Headless SDK methods to support payment account management experience for users - this will allow customers to add, update, edit and delete payment methods
* 🟥 Enhance the functionality of the analytics module in the control center by adding additional features such as expanded filter options, currency conversion capabilities, granular timeline views and a broader range of analytical views

### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
