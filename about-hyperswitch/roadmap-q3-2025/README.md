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

### Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

Earlier this year, Hyperswitch was made more modular to provide businesses with focused solutions to specific payment-related problems. Hence, our roadmap, starting this quarter, will be published under each module. A summary of the 8 product modules is provided below :

1. **Core Orchestration:** The core module supporting workflows unifying various connector
2. **Vault:** Simplifying PCI compliance and data privacy regulations through a standalone Card Vault
3. **Cost Observability:** Tracking and reducing payment processing costs via PSP reports.
4. **Authentication:** Data driven 3DS routing decision system and unified authentication SDK to encompass the diversity of authentication products.
5. **Intelligent Routing:** Routing service to dynamically select the most optimal PSP/ network in real time exploring/exploiting/managing multiple objectives simultaneously.
6. ​​**Alternate Payment Method Widgets:** Embracing the ever expanding diversity of payment methods and payment experiences through orchestration, and a simple add-on button to Checkout.
7. **Revenue Recovery:** A payment recovery sub-system with a customizable retry engine that reduces passive churn to recover failed subscription payments.
8. **Reconciliation:** Improving Finops efficiency in multi-acquirer settlement reconciliation.

## Roadmap <a href="#roadmap" id="roadmap"></a>

### **Core Orchestration**

* Expand Hyperswitch with new payment connector integrations including Worldpay Vantiv, Payload, Dwolla, Bluecode, Checkbook.io, Trust Payments, Nordea, and Silverflow.
* Extend support for additional payment methods across existing integrations such as Multisafe, Airwallex, Braintree, and Fiserv.
* Enable gift card support through direct provider integrations.
* Support co-branded card acceptance via direct issuer integrations.
* Integrate long-term lending options through solution partners.
* Introduce split payment support across
  * Gift cards
  * Long-term lending/leasing providers
* Implement an asynchronous chargeback handling solution for connectors without webhook support.

### **Vault**

* Make Hyperswitch interoperable with any third-party card vault
* Enable merchants self-hosting Hyperswitch to outsource PCI compliance as a managed service to Hyperswitch’s managed card vault or other third-party vaults
* Single-use PCI token generation for guest checkout use cases

### **Authentication**

* AI based 3DS Intelligence Engine for step-up/step-down decisions to optimize:
  * Authentication success rate
  * Overall transaction success rate
  * Fraud rate
* Authentication/Exemption Analytics to deeply understand the cardholder’s authentication journey, including:
  * 3DS failures
  * 3DS performance
  * Variability across issuers, markets, and 20+ other payment dimensions
* ML Based 3DS Intelligence engine to provide 3DS step-up/ step-down decisions, to optimize for&#x20;
  * Authentication success rate
  * Overall transaction success rate
* Authentication Observability to provide analytics and insights to merchants with tightly coupled Acquirer 3DS for better authentication and authorization results.

### **Revenue Recovery**

* Open-source revenue recovery: Merchants will be able to self-deploy Hyperswitch's integrations and intelligence services onto their own stack
* Multi-card retries: The system will intelligently utilize payment methods already present with the customer to perform retries on a given invoice
* Intelligent invoice retrying: Automatically retries invoices declined due to hard decline error codes, within the retry budget specified by the merchant
* Custom subscription support: Enables integration with the merchant’s in-house subscription management platform to recover failed payments
* Account Updater: Automatically updates stored card information when a customer's card details change

### **Intelligent Routing**

* Audit Trail and observability dashboard: Allows monitoring of performance across various routing modules
* Extension of Least Cost Routing to wallet payments: Includes Apple Pay and Google Pay
* Multi-objective routing modules: Simultaneously optimize for authentication rate, cost, and volume commitments (Stretch Target)

### **Cost Observability**

* Smarter Fee Attribution Engine: Enhancing our system’s ability to accurately derive fee names from fragmented or ambiguous reports, fee rates and attribute costs across key dimensions such as card variants, acquirers, and funding sources.
* Advanced Fee Auditing Capabilities
  * Audit applied interchange and scheme fees against both standard and contracted rates.
  * Benchmark or compare processing fees applied by different providers to identify savings opportunities.
  * Estimate expected interchange and scheme fees per transaction and reconcile them against actual applied rates.
* Conversational AI Interface: Introducing an intuitive, AI-powered chat experience that allows users to explore their payment processing fees through a rich, context-aware interface, making cost observability more interactive, insightful, and user-friendly.
* AI-Powered Self-Serve Uploads & Instant Insights: Empowering users to upload any report or transaction data, structured or unstructured and instantly receive meaningful insights, summaries, and potential optimization actions.
* Expanded Acquirer Coverage: Adding support for five or more new acquirer report formats, enabling broader compatibility and faster onboarding for merchants working with a variety of providers.



**Want to contribute to the roadmap?**

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
