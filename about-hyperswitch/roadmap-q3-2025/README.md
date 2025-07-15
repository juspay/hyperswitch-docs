---
description: Jul '25 to Sep '25
icon: road
---

# Roadmap - Q3 2025

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

#### Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

#### Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

Earlier this year, Hyperswitch was made more modular to provide businesses with focused solutions to specific payment-related problems. Hence, our roadmap, starting this quarter, will be published under each module. A summary of the 8 product modules is provided below :

1. **Vault:** Simplifying PCI compliance and data privacy regulations through a standalone Card Vault
2. **Cost Observability:** Tracking and reducing payment processing costs via PSP reports.
3. **Authentication:** Data driven 3DS routing decision system and unified authentication SDK to encompass the diversity of authentication products.
4. **Intelligent Routing:** Routing service to dynamically select the most optimal PSP/ network in real time exploring/exploiting/managing multiple objectives simultaneously.
5. ​​**Alternate Payment Method Widgets:** Embracing the ever expanding diversity of payment methods and payment experiences through orchestration, and a simple add-on button to Checkout.
6. **Orchestration:** The core module supporting workflows unifying various connector
7. **Revenue Recovery:** A payment recovery sub-system with a customizable retry engine that reduces passive churn to recover failed subscription payments.
8. **Reconciliation:** Improving Finops efficiency in multi-acquirer settlement reconciliation.

#### Roadmap <a href="#roadmap" id="roadmap"></a>

**Vault**

* Make Hyperswitch interoperable with any third party card vault.
* Merchants self-hosting Hyperswitch stack will be able to outsource PCI compliance as a managed service to Hyperswitch managed card vault, or other third party card vaults.
* Single-use PCI token generation for guest checkout use cases.

**Authentication**

* 3DS Intelligence engine to provide 3DS step-up/ step-down decisions, to optimize for (i) Authentication success rate, and (ii) Overall transaction success rate
* Enhanced Authentication Analytics to deeply understand the cardholder’s authentication journey, 3DS failures, 3DS performance, etc. across issuers, markets, and 20+ other payment dimensions.

**Revenue Recovery**

* **Open source Revenue Recovery:** Merchant will be able to self deploy our integrations and intelligence service on to their stack
* **Multi-card retries:** System will Intelligently utilise payments methods present with the customer to perform retries on a given invoice
* System will Intelligently retry invoices which have been declined due to hard decline error codes based on the budget specified by the merchant
* **Custom subscription support:** Ability to integrate with merchant's in-house subscription management platform to recover failed payments
* **Account Updater:** Ability to automatically update the stored card information when a customer’s card details change

**Intelligent Routing**

* Audit Trail and observability dashboard to monitor the performance of various routing modules
* Extending Least Cost Routing to wallet payments such as Apple Pay and Google Pay
* Multi-objective routing modules to simultaneously optimise for objectives like auth rate, cost and volume commitments (Stretch Target)

**Cost Observability**

* **Smarter Fee Attribution Engine:** Enhancing our system’s ability to accurately derive fee names from fragmented or ambiguous reports, fee rates and attribute costs across key dimensions such as card variants, acquirers, and funding sources.
* **Advanced Fee Auditing Capabilities**
  * Audit applied interchange and scheme fees against both standard and contracted rates.
  * Benchmark or compare processing fees applied by different providers to identify savings opportunities.
  * Estimate expected interchange and scheme fees per transaction and reconcile them against actual applied rates.
* **Conversational AI Interface:** Introducing an intuitive, AI-powered chat experience that allows users to explore their payment processing fees through a rich, context-aware interface, making cost observability more interactive, insightful, and user-friendly.
* **AI-Powered Self-Serve Uploads & Instant Insights:** Empowering users to upload any report or transaction data, structured or unstructured and instantly receive meaningful insights, summaries, and potential optimization actions.
* **Expanded Acquirer Coverage:** Adding support for five or more new acquirer report formats, enabling broader compatibility and faster onboarding for merchants working with a variety of providers.

**Core Orchestration**

* New Connector integrations: Worldpay Vantiv(cnpAPI), Payload, Dwolla , Bluecode, GoMobi, Sift, [Checkbook.io](http://checkbook.io/),Trust Payments , Nordea
* Extending payment methods for existing integrations: Multisafe, Airwallex, Braintree, Fiserv
* Support for co-branded cards through direct integration with issuers
* Support for Split Payments
  * Gift cards
  * Long term lending/leasing providers
* Support for Offers module

**Want to contribute to the roadmap?**

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
