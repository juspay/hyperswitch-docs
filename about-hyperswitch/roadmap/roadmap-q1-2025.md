---
description: Jan'25 - Mar'25
icon: road
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/about-hyperswitch/roadmap/roadmap-q1-2025
---

# Previous Roadmap - Q1 2025

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

### Recap of Q4 2024 <a href="#recap-of-q2-2024" id="recap-of-q2-2024"></a>

* [Dynamic Tax updater for express checkout wallets (Paypal, Applepay, Googlepay and Klarna) using Taxjar](https://docs.hyperswitch.io/explore-hyperswitch/e-commerce-platform-plugins/automatic-tax-calculation-for-express-checkout-wallets)
* [Smart retries extended to 7 more PSPs: Adyen, Worldpay, Braintree, Deutsche Bank, Novalnet, Fiuu and Nexi Xpay](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/smart-retries)
* Implementation of MPAN (merchant tokens) flow for Applepay recurring payments
* [Enablement of guest checkout flow with Click to Pay](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/click-to-pay#easier-and-customizable-integration)
* [Pass through Split payments through Stripe Connect and Adyen Platforms](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/split-payments)
* [New connector and payment method integrations](https://hyperswitch.io/pm-list)
  * Nexixpay (Cards)
  * Fiuu (Duitnow QR, Apple Pay, Google Pay)
  * Cybersource (Paze Wallet, Samsung Pay)
  * Bankofamerica (Samsung Pay)
  * Novalnet (Paypal, Google Pay)
  * Paypal Vaulting (via Cards and Paypal Wallet)
  * Adyen (Paze Wallet)
  * Elavon (Cards)
  * Klarna Kustom Checkout
  * JPMorgan (Cards)
  * Deutsche Bank(Cards 3DS)
* Data reporting at an organization, merchant and profile level for easier reconciliation
* Enhancements in analytics module for Refunds, Disputes and Smart Retries
* [Support for migration of Network Tokens for business continuity](https://docs.hyperswitch.io/explore-hyperswitch/account-management/data-migration/import-data-to-hyperswitch)

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

#### Modular and Composable Payments <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

In Q1’25, Hyperswitch will be offering the following composable services as standalone modules on Hyperswitch SaaS version. This activity would be the major focus for the team and each of these modules address one or more of the above roadmap themes

* 🟧 **Payment Methods Service (includes Vault):** Merchants will be able use the standalone Payment methods service to do various levels of tokenization \[PCI tokenization, Network tokenization, PSP tokenization - one-time/multi-use]. PCI compliant merchants will be able to leverage server-to-server flow for tokenization. _(Larger-scope initiative extending into Q2)_
* 🟧 **Reconciliation Service:** Reconciliation module will have an upgraded user experience; and allow FinOps teams to use the module independently without having to use Hyperswitch as the transaction processing technology _(Larger-scope initiative extending into Q2)_
* 🟧 **Cost observability service:** For merchants on interchange+ pricing, HyperSense will ingest their PSP invoices and reports to present the cost - trends, drill-downs, auto RCAs for any anomalies and audit of the report _(Larger-scope initiative extending into Q2)_
* 🟧 **Churn Recovery Service:** For merchants with recurring payment use cases and working with an external subscription engine, Churn recovery service will get notified about all recurring transactions and retry those transactions that have failed _(Larger-scope initiative extending into Q2)_

#### Community Feature Requests <a href="#community-feature-requests" id="community-feature-requests"></a>

* New integrations
  * 🟩 Deutsche Bank for card payments
  * 🟩 Redsys
  * 🟩 Inespay
  * 🟩 Xendit
  * 🟧 Amazon Pay _(moved to Q2)_
* 🟥 Scan Card Feature for MWeb _(moved to Q2)_

#### Improving Authorization Rates <a href="#improving-authorization-rates" id="improving-authorization-rates"></a>

* 🟧 **Intelligent Routing:** Intelligent Routing module tracks the auth rates of various processor in realtime at a granular level to select the most optimal processor to boost conversions
  * 🟥 **Outages and acute failures:** Provides a failsafe system that proactively identifies incidents and holds off traffic to processors that are facing temporary downtimes or failures _(Larger-scope initiative extending into Q2)_
  * 🟥 **Volume Commitments:** Helps select the appropriate PSP for getting volume tier benefits from the processor by routing sufficient payments volume to necessary processors in accordance with their SLA or contracts _(Larger-scope initiative extending into Q2)_
* **🟧 Churn Recovery Service:** For all merchants with recurring payment use cases and working with an external subscription engine, Churn recovery service will get notified about all recurring txns and retry only those transactions that have failed _(Larger-scope initiative extending into Q2)_
  * 🟩 **Split retries -** Merchants will be able to split retries between their subscription engine and the Passive retry service
  * 🟩 **Single PSP -** The Churn Recovery service will interact with only a single PSP for a transaction
  * 🟩 **Basic Retry logic -** The Churn Recovery service will have a very basic error code & region based logic to retry transactions
* 🟧 Secure Card on File (SCOF) with Passkeys - For Mastercard cards, provide Biometric authentication to the customers _(extending to Q2)_
* 🟧 **One time tokenization:** During CIT payments, merchants will be able to do collect, validate and do one-time tokenization of cards & other PMs and use these one-time tokens later in the checkout flow once the customer confirms their purchase _(extending to Q2)_
* 🟩 Smart retry enhancements using Clear PAN as fallback for Network Tokens/ Gateway tokens to improve auth rates
* 🟩 More payment authorization workflows - Estimated auth and Over-capture

#### Reducing Payments Cost <a href="#reducing-payments-cost" id="reducing-payments-cost"></a>

* **🟧** PINless Debit routing - enable cost savings through regulated/ unregulated transactions in US _(extending to Q2)_

#### Reducing Payment Operations <a href="#reducing-payment-operations" id="reducing-payment-operations"></a>

* **🟧 Revamped Recon module** to support self exploration with transaction source agnostic recon and 2-way or 3-way level capabilities _(Larger-scope initiative extending into Q2)_
* **🟧 Cost observability service:** For merchants on interchange+ pricing, HyperSense will ingest their PSP invoices and reports to present the cost - trends, drill-downs, auto RCAs for any anomalies and audit of the report _(Larger-scope initiative extending into Q2)_
* 🟩 Data reporting on an organisation, merchant and profile level for easier reconciliation

#### Developer Experience <a href="#developer-experience" id="developer-experience"></a>

* 🟧 Enhancing Hyperswitch's self-deployment process to be even more seamless and self-serve, enabling merchants to deploy a fully compliant payments stack independently _(Larger-scope initiative extending into Q2)_
* 🟧 Revamped connector <> payment method matrix view _(extending to Q2)_

#### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
