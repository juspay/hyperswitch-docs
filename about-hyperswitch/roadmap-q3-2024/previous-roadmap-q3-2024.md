---
description: Hyperswitch roadmap (July to Sept'24)
---

# 🛣️ Previous Roadmap - Q3 2024

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

### Recap of Q2 2024 <a href="#recap-of-q2-2024" id="recap-of-q2-2024"></a>

* Payouts support with Adyen Platform, Cybersource, Ebanx, Payone and Paypal and instant payout methods&#x20;
* Vaulting payment methods with Hyperswitch for on-session payments
* Natively authenticating payments using Third party 3DS service providers - Netcetra, 3dsecure.io
* Integrations for alternate payment methods via Mifinity and ZSL
* Scan a card experience on Unified Checkout
* Open-sourced the Native SDK for Unified Checkout
* Control Centre support for Two Factor Authentication for user login
* One-click Express Checkout through Applepay, Klarna, GooglePay
* Secure payout iframe to collect payout details and trigger payouts

### Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

### Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

There are a lot of problems to be solved in payments, but our majority of our current focus falls under 5 themes below.

🌎 **Community Feature Requests:** Most of our community feature requests falls under one of the above themes, but we still keep this as a separate theme, because we intend to actively explore new problem statements and themes from the community before scheduling actual feature work.

👨‍💻 **Developer Experience:** Providing a great self-service and self-installation experience for developers who wish to use or contribute back to Hyperswitch.

💰 **Reducing Payment Costs:** Payments should be like a free utility for digital businesses. Any business should be able reduce payment processing costs by embracing the diversity in payments.

📈 **Improving Authorization Rates:** Ensuring a best-in-class payment experience and access to latest innovations in the payments ecosystem for all businesses.

👍 **Reducing Payment Operations:** Managing payments across multiple countries, currencies and processors should not add to the administrative burden on businesses. Hence, Hyperswitch intends to eliminate all such operational burdens so that businesses can focus on the core activities.

| **Legend** | **Description**     |
| ---------- | ------------------- |
| 🟩         | Feature completed   |
| 🟧         | Feature in progress |
| 🟥         | Work not started    |
| 💪         | Stretch target      |
| 🚛         | Backlog feature     |

### Roadmap <a href="#roadmap" id="roadmap"></a>

#### Community Feature Requests <a href="#community-feature-requests" id="community-feature-requests"></a>

* 🟧 Payment Method Management experience to enabled customer and payment method related operations in non-purchase user journeys&#x20;
* New connector and payment method Integrations (more will be added as we progress)
  * 🟩 🚛 Datatrans ([Planet.com](http://planet.com/)) for card payments&#x20;
  * 🟧 Razorpay for UPI payments&#x20;
  * 🟧 PAZE checkout
  * 🟩 TaxJar for dynamic tax calculations



#### Improving Authorization Rates <a href="#improving-authorization-rates" id="improving-authorization-rates"></a>

* 🟩 Network Tokenization with account updater to (a) improve auth rates for one-time/ recurring payments and (b) reducing scheme fee&#x20;

#### Reducing Payments Cost <a href="#reducing-payments-cost" id="reducing-payments-cost"></a>

* Direct integrations with banks acquirers to reduce cost (will be extended for EU banks)
  * 🟧 Wells Fargo (US)
  * 🟩 Deutsche Bank (DE)
* 🟩 Pay by Bank Experience through Plaid Open banking to enable instant bank transfer (push payments) in the UK and EU via with support for app2app redirection experience&#x20;

#### Reducing Payment Operations <a href="#reducing-payment-operations" id="reducing-payment-operations"></a>

* 🟩 🚛 Account verification for pull payments like Direct Debits in the EU and US (ACH, SEPA) via Plaid&#x20;
* 🟧  User management and dashboard analytics views at entity level granularity (org to profile)

#### Developer Experience <a href="#developer-experience" id="developer-experience"></a>

* 🟧 Payment plugins for Commerce Tools Headless commerce platform to facilitate faster integrations&#x20;
* 🟩 🚛 PCI Software Security Standard (S3) certification&#x20;

#### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
