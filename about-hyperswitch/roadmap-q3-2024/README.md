---
icon: road
description: Hyperswitch roadmap (Oct to Dec'24)
---

# Roadmap - Q4 2024

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

### Recap of Q3 2024 <a href="#recap-of-q2-2024" id="recap-of-q2-2024"></a>

* Hyperswitch is now PCI Software Security Standard (S3) certified
* Network Tokenization capability with Visa, Master and Amex card networks. This shall enable merchant to use network tokens to improve auth rates for one-time/ recurring payments and reduce the interchange fee
* Payment Method Management experience to view, add and delete payment methods (for Web platform)
* New connector and payment method integrations
  * Datatrans ([Planet.com](http://planet.com/)) for card payments
  * Wells Fargo (US) for card payments
  * Deutsche Bank (DE) for SEPA direct debits
  * Novalnet for card payments
  * Fiuu for cards, bank transfer and inter-operable QR based payments
  * Itau Bank for instant payments
  * Payouts via PayOne, and Wells Fargo
  * Razorpay UPI payments
* Pay by Bank Experience through [Plaid Open banking](../../explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup/banks/open-banking.md). This is to allow merchants to enable instant bank transfer (push payments) in the UK and EU via with support for app2app redirection experience
* Account verification via Plaid for pull payments (ACH, SEPA) in the EU and US
* React Native SDK was Open Sourced
* Native 3DS Authentication Experience via Netcetera for mobile
* Merchant Initiated Transactions (MIT) were made PSP agnostic with Network Transaction ID (NTI)
* User management and dashboard analytics views at entity level granularity (org to profile)
* Payment plugin for Saleor - headless commerce platform to facilitate faster integrations
* Localisation support for Payouts across 17 languages
* Control Centre - Enable SSO sign in with Okta

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

* 🟧  More payment authorization workflows - split payments and incremental authorization
* New integrations -&#x20;
  * 🟥[ Paymentwall for cards and alternate payment methods](#user-content-fn-1)[^1] _(Expected Closure by Mar'2025)_
  * 🟥 ~~Digital Virgo integration for Direct Carrier Billing~~
  * 🟧 SamsungPay
  * 🟩 Nexi Xpay card payments
  * 🟥 ~~Deutche Bank for card payins and SEPA payouts~~
  * 🟩 PAZE for card payments in the US
* 🟩 Dynamic Tax updater for express checkout wallets (Paypal, Applepay, Googlepay and Klarna) using Taxjar integration

#### Improving Authorization Rates <a href="#improving-authorization-rates" id="improving-authorization-rates"></a>

* 🟧 Smart retry enhancements using Clear PAN as fallback for Network Tokens/ Gateway tokens to improve auth rates
* 🟩 Extending smart retries to 7 more PSPs: Adyen, Worldpay, Braintree, Deutsche Bank, Novalnet, Fiuu and Nexi Xpay
* 🟧 Implement MPAN (merchant tokens) for Applepay recurring payments
* 🟥  [Secure Card on File (SCOF) with Passkeys](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/token-authentication/tas_scof/use-case1/) with Mastercard cards. This is to provide seamless payment authentication experience (with Biometrics) and liability shift for merchants _(Expected Closure by Mar'2025)_
* 🟩  Enabling guest checkout flow with [Click to Pay](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/use-cases/click-to-pay/)&#x20;

#### Reducing Payments Cost <a href="#reducing-payments-cost" id="reducing-payments-cost"></a>

* More direct bank acquirer integrations
  * 🟧 JP Morgan

#### Reducing Payment Operations <a href="#reducing-payment-operations" id="reducing-payment-operations"></a>

* 🟩  Data reporting at an organization, merchant and profile level for easier reconciliation
* 🟩  Enhancements in analytics module for Refunds, Disputes and Smart Retries
* 🟥  Add support for bulk network tokenization _(Expected Closure by Mar'2025)_
* 🟩 Migration of Network Tokens for business continuity

#### Developer Experience <a href="#developer-experience" id="developer-experience"></a>

* 🟩  Hyperswitch widgets to support Alternate payment methods, express checkout payment methods and Authentication solutions

#### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.

[^1]: 
