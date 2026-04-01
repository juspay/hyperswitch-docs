---
description: Hyperswitch roadmap (Apr to Jun'25)
icon: road
---

# Previous Roadmap - Q2 2025

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

### Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

### Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

Earlier this year, Hyperswitch was made more modular to provide businesses with focused solutions to specific payment-related problems. Hence, our roadmap, starting this quarter, will be published under each module. A summary of the 8 product modules is provided below :

1. **Vault:** Simplifying PCI compliance and data privacy regulations through a standalone Card Vault
2. **Cost Observability:** Tracking and reducing payment processing costs via PSP reports.
3. **Authentication:** Data driven 3DS routing decision system and unified authentication SDK to encompass the diversity of authentication products.
4. **Intelligent Routing:** Routing service to dynamically select the most optimal PSP/ network in real time exploring/exploiting/managing multiple objectives simultaneously.
5. ​​**Alternate Payment Method Widgets:** Embracing the ever expanding diversity of payment methods and payment experiences through orchestration, and a simple add-on button to Checkout.
6. **Orchestration:** The core module supporting workflows unifying various connector
7. **Revenue Recovery:** A payment recovery sub-system with a customizable retry engine that reduces passive churn to recover failed subscription payments.
8. **Reconciliation:** Improving Finops efficiency in multi-acquirer settlement reconciliation.

### Roadmap <a href="#roadmap" id="roadmap"></a>

#### Vault <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

* Make Hyperswitch interoperable with any third party card vault.
* Merchants self-hosting Hyperswitch stack will be able to outsource PCI compliance as a managed service to Hyperswitch managed card vault, or other third party card vaults.
* Single-use PCI token generation for guest checkout use cases.

#### Authentication <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

* 3DS Intelligence engine to provide 3DS step-up/ step-down decisions, to optimize for (i) Authentication success rate, and (ii) Overall transaction success rate
* Enhanced Authentication Analytics to deeply understand the cardholder’s authentication journey, 3DS failures, 3DS performance, etc. across issuers, markets, and 20+ other payment dimensions.

#### Revenue Recovery <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

* Support rule-based as well as intelligent retries&#x20;

#### Intelligent Routing <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

* Making decision-engine a standalone offering to enable merchants to use it along side any payment authorization system (vendor agnostic).
* Multi-objective routing system to allow (i) Auth Rate Uplift (already available), and (ii) Cost Optimization through Debit routing (to be added)

#### Cost Observability <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

* Solve the data challenges across PSPs fee report formats. For example, achieve standardisation across PSP fee names and field names by building standard mapper that can scale for multiple PSPs
* Capability to display aggregated fee data in reports, including chargebacks, refunds, and backdated adjustments.

#### Core Orchestration <a href="#modular-and-composable-payments" id="modular-and-composable-payments"></a>

* Connector integrations - Facilitapay, Global Payments, Tranzilla, Paytm, Razorpay

#### **Want to contribute to the roadmap?** <a href="#want-to-contribute-to-the-roadmap" id="want-to-contribute-to-the-roadmap"></a>

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
