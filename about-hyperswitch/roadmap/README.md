---
description: April '26 to June '26
icon: road
---

# Roadmap - Q2 2026

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, and what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

#### Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

### Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

Last year, Hyperswitch was made more modular to provide businesses with focused solutions to specific payment-related problems. Hence, our roadmap includes updates for each module. A summary of these product modules is provided below:

🧱 **Composability:** Enabling users to independently augment Juspay Hyperswitch platform modules of choice to create a tailored, high-performance payment stack. Such modules could be payment processors (or) PCI vaults (or) intelligent routing (or) reconciliation, cost observability, revenue recovery, or card network certified services (like 3DS, network tokenization)

🌐 **Connectedness:** Increasing connectedness of the Juspay Hyperswitch operating system into more and more connectors for - Payins, Vaults, Payouts, Fraud, Subscriptions, Tokenization. And also keeping the connections up-to-date.

🎯 **Reducing Payment Operations:** Managing payments across multiple countries, currencies and processors should not add to the administrative burden on businesses. Hence, Hyperswitch intends to eliminate all such operational burdens so that businesses can focus on the core activities.

🛡️ **Reliability:** Building capabilities for Fault, Capacity and Change tolerance into the payment platform.

🚀 **Developer Experience:** Providing a great self-service and self-installation experience for developers who wish to use or contribute back to Hyperswitch.


## Roadmap <a href="#roadmap" id="roadmap"></a>

### Composability

**Decoupling the Connectors**: The connector integrations layer for payments will be decoupled into a stateless, embeddable payment integration library with multi-language SDK support. This will be done for payment connectors and further extended to payout connectors and vault connectors in the future.

**Compatibility with Cashier Platforms for Gaming and Gambling businesses**: The payment platform will be enhanced with more events to improve composability with cashier platforms used by gaming and gambling businesses. This is to support regulatory-level compliance and configurability - payment method blocking, user notification for responsible gambling, deposit amount controls.

**Enhancements to Platform and Connected merchants:** The Platform and Connected merchants setup will be enhanced with more feature modules - profile acquirer, async operations (process tracker), external vault, external authentication, card blocking, surcharge, Apple Pay merchant registration, analytics and relay.

**Enhancements to External Vault**: External vault support for VGS will be extended to the Hyperswitch native SDKs.

**Enhancements to Intelligent routing module:** Enhancement with a dashboard to visualize the module performance and uplift.

### Connectedness

**New Integrations**
- EFT Debit Order: Support for bank debit payment method popular in South Africa for recurring collections.
- iMerchant Solutions:	Payment processor with full payment + webhook flow. Supports retrieving webhook reference IDs for async payment tracking.
- Santander: Pix Automatico (Brazil's recurring Pix payments) with push notifications, QR code generation, CIT, MIT, and webhook flows.
- Interpayments for surcharging

**Enhancements to Existing Connectors**
- ACI: Apple Pay and Google Pay wallet support
- Worldpay XML: Apple Pay pre-decrypted flow
- Stripe: Google Pay pre-decrypted flow
- Finix: Support for external 3DS
- Peach Payments: COF Data for CardWithLimitedDetails CIT and No-3DS Cards CIT
- Checkout: Network token payment support for CIT and MIT NTID support
- Stripe: on_behalf_of support for Stripe Connect split payments
- Loonio: Manual capture support
- Gigadat: Manual capture support

[Learn more about the existing connectors supported in Hyperswitch here.](https://docs.hyperswitch.io/explore-hyperswitch/connectors)


### Reducing payment operations

**Reconciliation Enhancements**: 
- **Tolerance Rules** support to reduce manual effort and improve operational visibility. Merchants can define variance thresholds for automatic reconciliation, with any residual differences routed to a dedicated tolerance account for tracking and auditability. 
- **Aging** provides visibility into unmatched transactions and enables configurable time-based thresholds to proactively identify stale items.
- **Manual corrections** will enable merchants to fix recon mismatches with an audit trail.
- **SFTP support** for fetching settlement files for Adyen, Amex

[Learn more about the existing Reconciliation features and workflows here](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/reconciliation).

### Reliability & Systems

**Multi-Region Active Passive Setup**: Production environment drills will be conducted on the active-passive setup for the US and EU regional stacks.

**Configuration Management**: Juspay Hyperswitch will adopt a context-based configuration management system to facilitate safe and flexible rollout of config changes. Configurations on the platform will be made more granular for merchants to control at a profile, merchant and organization level through adoption.

### Developer Experience

**Agentic interface for juspay hyperswitch**: Deploying and running Juspay hyperswitch Enterprise Edition is bound to become easier with a Specialized Agentic Interface to explore, trace, analyse. We will be launching a beta version supporting Bring-your-own-LLM support.

[Learn more about the existing Revenue Recovery features and workflows here.](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/revenue-recovery)

**Want to contribute to the roadmap?**

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.