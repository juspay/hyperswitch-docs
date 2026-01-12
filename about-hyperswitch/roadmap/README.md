---
description: Jan '26 to March '26
icon: road
---

# Roadmap - Q1 2026

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

### Recap of Q4 2025 <a href="#recap-of-q2-2024" id="recap-of-q2-2024"></a>

**Connectors**

* **New PSP integrations** – Gigadat and Loonio for Interac e Transfer; Tesouro for Cards, Apple Pay, and Google Pay; Paysafe for Cards, Apple Pay, Skrill, Interac e Transfer, and Paysafecards; Finix for Cards, Apple Pay, and Google Pay
* **Integration depth** – Expanded wallet and alternative rail coverage across new connectors, adding broader support for Apple Pay and Google Pay, plus regional payment rails like Interac e Transfer, and additional tender types like Skrill and Paysafecards through Paysafe

**Core orchestration**

* **Platform Merchants support:** Support for Platform merchant use-cases to share customers and payment methods across their managed-merchants
* **Split Payments:** Support for split payments with gift cards to enable combined payments within a single transaction
* **Error code enhancements** – Issuer error codes added to the Gateway Status Mapping table to improve response mapping and retry decisions; unified error codes expanded to generate clearer, consistent user facing error messages across channels
* **Real time payment method eligibility** – Merchant level risk based eligibility checkpoints added before payment confirmation to reduce fraud exposure and improve authorization performance

**Vault**

* **Guest checkout tokenization** – Token creation without customer creation in Hyperswitch, enabling secure and PCI compliant handling of guest one time and repeat transactions, with flexibility to map tokens to merchant owned identifiers
* **Volatile tokenization** – Support for time bound temporary tokens for PAN and network token flows, enabling secure session based authorizations and one time payment experiences without long term vault storage

**Revenue recovery**\
\
Account Updater to automatically refresh stored card credentials for expired, replaced, or reissued cards, improving continuity for stored payment methods and recovering failures tied to outdated card data

#### Core Values <a href="#core-values" id="core-values"></a>

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, and at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

### Themes for Roadmap <a href="#themes-for-roadmap" id="themes-for-roadmap"></a>

Last year, Hyperswitch was made more modular to provide businesses with focused solutions to specific payment-related problems. Hence, our roadmap includes updates for each module. A summary of these product modules is provided below :

1. **Orchestration:** The core module supporting workflows unifying various connector
2. **Vault:** Simplifying PCI compliance and data privacy regulations through a standalone Card Vault
3. **Authentication:** Data driven 3DS routing decision system and unified authentication SDK to encompass the diversity of authentication products.
4. **Revenue Recovery:** A payment recovery sub-system with a customizable retry engine that reduces passive churn to recover failed subscription payments.
5. **Reconciliation:** Improving Finops efficiency in multi-acquirer settlement reconciliation.
6. **Cost Observability:** Tracking and reducing payment processing costs via PSP reports.

## Roadmap <a href="#roadmap" id="roadmap"></a>

#### Core Orchestration

**Platform Managed Payments**

We plan to introduce platform capabilities that allow platforms to trigger and manage key payment operations on behalf of their managed merchants. This will include Payments, Refunds, Webhooks, and Disputes.

**Recurring Payments Expansion**

We plan to expand recurring payment capabilities across cards and bank-based methods, and improve lifecycle handling for recurring flows. This will include support for storing payment credentials and enabling recurring payments across ACH and other APMs, enabling PSP triggered recurring payments with lifecycle handling and reconciliation support, and supporting recurring payment flows using only card PAN and expiry without requiring Network Tokenization (NTI).

**Retry Enhancements to Improve Authorization Rates**

We plan to enhance retry tooling across APMs and merchant-initiated flows to help improve approval rates and reduce avoidable drop-offs. This will include automatic retries support for Google Pay and other APMs, support for manual retries in MIT flows, and support for merchants to configure retry rules for different error codes.

**Relay for Post Payment Actions**

We plan to enable Hyperswitch to act as a relay to orchestrate incremental and post payment actions on the original order across PSPs. This will support workflows such as incremental authorization, capture, refund, void, and churn recovery.

**Instalments**

We plan to support installment-based payments across supported payment methods, enabling merchants to offer flexible payment options without changing their orchestration setup.

#### Connectors

**New Integrations**

We plan to expand connector coverage with new PSP integrations including Banco Do Brasil, Cielo, Caixa, Bradesco, Bancoob, Worldpay Access Modular, and HyperPG.

**Enhancing Existing Integrations**

We also plan to enhance existing integrations to expand payment method coverage and improve reliability. This will include Payload (ACH), Itau Bank (Pix, Boleto), Stripe Connect (Apple Pay, Google Pay), Dwolla (ACH recurring), Worldpay WPG (3DS cards with fraud ID), Xendit (QRIS), and Deutsche Bank.

[Learn more about the existing Connectors supported in Hyperswitch here.](https://docs.hyperswitch.io/explore-hyperswitch/connectors)

### Vault

**Multi Vault Support**

We plan to expand Vault capabilities to enable seamless use of both Juspay-hosted and external vaults across self-hosted and SaaS Hyperswitch deployments.

**Alt ID Network Tokenization for Guest Checkout**

We plan to enable alternate identifier-based flows for network tokenization in guest checkout scenarios, allowing tokenization without requiring full customer creation.

**Extended Proxy API Payload Support**

We plan to extend Proxy APIs to support non-JSON request formats such as application/x-www-form-urlencoded, XML, and other upstream formats, to improve compatibility with legacy gateway patterns.

**Custom Token Formats**

We plan to support configurable and merchant-defined token formats across Vault and payment flows, giving merchants more control over token design and interoperability.

**Vault Observability and Auditability**

We plan to add analytics, audit trails, and observability capabilities for the Vault service, improving traceability, governance, and operational debugging.

[Learn more about the existing Vault Services and workflows here.](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault)

### Authentication and Checkout Experience

**SDK Accessibility Enhancements**

We are enhancing the checkout SDK to ensure accessibility compliance and inclusivity for all users. Updates will include improved keyboard navigation, screen reader support, and visual contrast adjustments aligned with WCAG accessibility standards.

**Framework Compatibility Upgrades**

We plan to add compatibility upgrades across Web and Native experiences. This will include support for React 19 for Web and support for React Native's new architecture for Native.

**Swift Package Manager Migration (iOS)**

We plan to migrate iOS integration to Swift Package Manager to consolidate all frameworks into a unified and modular package with clear dependency boundaries. This will replace CocoaPods for simpler merchant integration and cleaner versioning.

**Optional OTA Support for SDKs**

We plan to introduce optional OTA (Airborne) support for Hyperswitch SDKs. Merchants will be able to opt into Hyperswitch-managed updates, approval-gated releases, self-hosted OTA, or fully disable OTA based on governance, compliance, and risk requirements.

**Apple Pay Beyond Safari**

We plan to enable Apple Pay support across non-Safari browsers where supported, improving reach and checkout conversion without changing existing integrations.

**Subscription Based SDK Events**

We plan to enable subscription-based events across SDK flows, allowing merchants to subscribe to granular lifecycle signals for real time decisioning, observability, and tighter integration with merchant systems. Examples include BIN, field validation outcomes, and button clicks.

**Custom In SDK Messaging**

We plan to support custom in SDK messaging so merchants can configure and display contextual messages (info, warnings, errors, compliance text) within the Hyperswitch SDK UI, with an optional fallback to default SDK messaging for a consistent user experience.

[Learn more about the existing Authentication and Checkout Experience capabilities here.](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls)

### Revenue Recovery

**Advanced Retry Logic for Hard Declines**

We plan to introduce smarter recovery for hard declines, where the system identifies transactions that were falsely marked as hard declines and retries them intelligently.

**Recovery Analytics in the Dashboard**

We plan to add analytics that provide merchants with real-time visibility into recovery performance through the dashboard.

**Hosted Recovery with Self-Hosted Orchestration**

We plan to support using self-hosted orchestration with Juspay-hosted revenue recovery, enabling merchants to adopt recovery improvements without changing their orchestration deployment model.

[Learn more about the existing Revenue Recovery features and workflows here.](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/revenue-recovery)

### Reconciliation

**Aging**

We plan to provide visibility into transactions awaiting a match and allow time-based threshold monitoring to help teams track stale reconciliation items.

**Tolerance Rules**

We plan to enable merchants to establish tolerance rules for automatic reconciliation when transaction amounts fall within a specified variance threshold.

**Linked Analytics**

We plan to offer a comprehensive end-to-end reconciliation view of a transaction across multiple systems, improving auditability and issue triage.

[Learn more about the existing Reconciliation features and workflows here](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/reconciliation).

### Control Centre

**Developer Observability & Self-Service Diagnostics**

We plan to expose real-time technical metrics and system health insights for platforms, enabling faster self-diagnosis and reducing dependency on support.

**Contextual Alerts & Configurable Automation**

We plan to add a configurable, multi-merchant alerting system to detect PSP downtimes, error spikes, and emerging failure patterns.

**Embeddable Components**

We plan to introduce widgets for payment configuration and operations that can be integrated directly into platform dashboards. This will enable platforms to manage payments, connector integrations, and refunds within their own dashboard experience.

**Theme Management UI**

We plan to build a dedicated UI to configure and manage dashboard and email themes across organization, merchant, and profile levels. The UI will support brand colors, logos, favicons, and email branding with clear theme precedence and live preview.<br>

**Want to contribute to the roadmap?**

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
