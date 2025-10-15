---
description: Oct '25 to Dec '25
icon: road
---

# Roadmap - Q4 2025

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, previous roadmap, findings over the previous quarter, what we heard from the community as feature requests.

👂And as always, we listen to your feedback and adapt our plans if needed.

### Recap of Q3 2025 <a href="#recap-of-q2-2024" id="recap-of-q2-2024"></a>

* **Connectors**
  * **New PSP integrations** - Worldpay Vantiv, Payload, Dwolla, Bluecode, Checkbook, Trust Payments, Nordea, and Silverflow
  * **Integration enhancements** - Multisafe, Airwallex, Braintree, and Fiserv
  * **New category of integration** - Support for subscription management providers to augment the plan management and record-keeping capabilities of the subscription engine with payment orchestration
  * **Feature depth** - L2/L3 data standardization across PSPs, support merchant decryption and decrypted payload for Apple Pay and Google Pay, return MAC codes in API response, chargeback support for PSPs with no webhook support, and MIT category fields
* **Core orchestration** - Support for over-capture, extended authorization, and manual/user-triggered retries
* **Standalone Network Tokenization** Service with support for Visa, Mastercard, and Amex\
  Standalone EMVCo-certified Juspay 3DS Server and 3DS SDK
* **Revenue recovery** - New capabilities to handle partial capture, support in-house billing engines, invoice queuing or grouping of all pending invoices, hard decline smart retry
* **Intelligent routing** analytics added to offer real-time insights into transaction flow and gateway performance
* **Reconciliation** - New capabilities to support transaction-level audit logs to ensure every transaction can be traced from initiation to settlement, strengthening compliance and operational accountability
* **Cost observability** - New capabilities to accurately derive fee names from fragmented or ambiguous reports, fee rates and attribute costs, advanced fee auditing capabilities, estimate expected interchange and scheme fees per transaction and reconcile them against actual applied rates, conversational AI interface, and expanded acquirer coverage: adding support for five or more new acquirer report formats (AIBMS, Elavon, PayPal, Stripe, and Amex)
* **Control Centre** - Support for platform org and merchant to allow programmatic API-driven merchant account creation, management, and configuration

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

**Vault**

*   **Guest Checkout Tokenization in Hyperswitch Vault**

    We plan to extend our vault capabilities to support guest checkout tokenization. This will allow merchants to create tokens without generating a customer ID in Hyperswitch, enabling secure and PCI-compliant handling of one-time or repeat transactions. Merchants will also have the flexibility to map these tokens to their own unique identifiers as needed.
*   **Alt ID Flow for Network Tokenization in Guest Checkout**

    We plan to support Alt ID–based network tokenization for guest checkout, allowing merchants to tokenize cards without customer creation. The Alt ID issued by the network replaces PAN in all downstream operations, ensuring PCI and network compliance while simplifying secure guest transactions.
*   **Volatile Tokenization for PAN and Network Tokens**

    We plan to add support for volatile tokenization, allowing merchants to generate temporary tokens valid for a limited time. This will be particularly useful for transient payment flows such as session-based authorizations or one-time payments, providing enhanced flexibility and security without long-term storage in the vault.
*   **Proxy API for Vault-Only Integrations**

    We are expanding the Proxy API to support merchants who choose to integrate solely with Hyperswitch Vault services. This will allow merchants to pass a card token in their requests, which Hyperswitch will substitute with the actual card details before routing the call to the target connector.

    Additionally, the Proxy API will support multiple request formats, including form-URL-encoded and XML, to ensure easier interoperability with existing gateway or legacy systems.

Learn more about the existing Vault Services and workflows [here](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault)

**Authentication and Checkout Experience**

*   **Authentication Observability**\
    We plan to introduce Authentication Observability, a dedicated analytics layer that provides merchants with detailed visibility into authentication performance across acquirers, issuers, and 3DS flows.

    This will include insights such as 3DS success ratios, challenge vs. frictionless breakdowns, and issuer response patterns, allowing merchants to identify friction points and optimize their authentication strategies.
*   **Authorization Uplift**

    We are introducing a set of enhancements aimed at improving authorization success rates and overall checkout reliability. These features are designed to create a more adaptive, resilient, and insight-driven payment experience:

    * **Payment Method Prioritization**: The checkout SDK will automatically prioritize payment methods based on a customer’s most recently used or highest-success options, improving the likelihood of first-attempt approvals.
    * **Real-Time Outage Awareness**: SDK-level alerts will notify merchants of ongoing payment method or network outages, enabling them to hide or reorder affected options dynamically.
    * **Fallback Recommendations**: In the event of a failed payment attempt, customers will be prompted with alternate payment methods such as wallets, BNPL, or UPI to complete their transaction seamlessly.
*   **Integration with Cardinal SDK**

    We are integrating the CardinalCommerce SDK to strengthen 3DS authentication across global transactions.
*   **SDK Accessibility Enhancements**

    We are enhancing the checkout SDK to ensure accessibility compliance and inclusivity for all users. Updates will include improved keyboard navigation, screen reader support, and visual contrast adjustments aligned with WCAG accessibility standards.
*   **Payout Links Enhancements**

    We plan to enhance Payout Links with an improved user experience. We will add advanced customization support to payout links so that the payout links are in line with the merchant's branding and styling.

**Revenue Recovery**

* **Advanced retry logic for Hard declines**\
  The system intelligently identifies and retries transactions that were falsely marked as hard declines. This feature aims to recover transactions that were previously considered unrecoverable. Merchants will be able to manage these retries by setting a configurable budget that limits the number retry attempts.
* **Account Updater:**\
  The system will automatically refresh stored card credentials when a customer’s card information changes. This capability ensures continuity in payment processing by updating expired, replaced, or reissued cards in real time. As a result, payment failures caused by expired, closed, or lost/stolen cards can be effectively recovered.

Learn more about the existing Revenue Recovery and workflows [here](../payments-modules/revenue-recovery.md)

**Intelligent Routing**

*   **Multi-Objective Routing Modules**

    We plan to introduce multi-objective routing capabilities that enable Hyperswitch to optimize transaction routing across multiple business goals simultaneously — such as authorization rate, processing cost, and volume commitments. This will allow merchants to configure and balance routing priorities dynamically, ensuring optimal performance and cost efficiency across connectors.
*   **Expanded LCR (Least Cost Routing) Based on Acquirer Costs**

    We are extending the scope of Least Cost Routing (LCR) to incorporate acquirer-specific cost structures. This enhancement will allow routing decisions to factor in interchange, scheme, and acquirer fees in real time, ensuring each transaction is processed through the most cost-efficient path without compromising reliability or compliance.
*   **Routing Savings and Benefits Reporting**

    We plan to introduce savings and benefits reporting for routing, providing merchants with detailed visibility into the financial and operational impact of their routing configurations. The reporting will include insights into cost savings, authorization uplift, and volume distribution across acquirers, helping merchants measure the tangible benefits of intelligent routing and refine their strategies over time.

**Cost Observability**

* **Payment fees estimation using transaction data:** Estimate expected interchange and scheme fees for every transaction of merchant and reconcile them against actual applied rates from transaction fee reports from Acquirers.
* **Conversational AI Interface:** Enhance the AI-powered chat experience that allows users to explore questions and information on payment processing fees. In addition making cost observability more interactive, insightful, and highly contextual for logged in users to interact with their data using AI powered chat.

#### Reconciliation

* **Revamped Exception Resolution Interface**\
  Instantly resolve mismatches in transaction amounts, status, or other metadata through a clean, side-by-side interface. The system highlights exact discrepancies across multiple sources and provides guided resolution options while maintaining a full audit trail for every action
* **Smarter Rules for Advanced Businesses**\
  Support for one-to-many and many-to-one reconciliation rules, enabling flexible handling of complex payment and payout scenarios (e.g., one payout covering many sales or vice versa)
* **Forex Handling**\
  Support for merchant-provided exchange rates in cross-currency reconciliation. This enables automatic alignment of settlements and deposits across currencies, eliminating manual conversions
* **Exceptions Aging & Tolerance Handling**\
  Monitor how long each exception remains unresolved and surface those breaching SLA thresholds to drive faster closure.Configure tolerance levels for acceptable amount variances so minor differences don’t block reconciliation.
* **AI-Driven Exception Handling**\
  AI-powered recommendations to automatically analyze mismatches and suggest likely matches based on amounts, dates, and references — dramatically reducing exception resolution time
* **Advanced Data Management**\
  Dedicated ingestion integrity module to isolate problematic records, prevent data contamination, and enable review and correction before reprocessing

Learn more about the existing Reconciliation features and workflows [here](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/reconciliation-product)

**Core Orchestration and Connectors**

* **Connectors**\
  We plan to expand connector coverage with new integrations including
  * **New integrations:** Gigadat (Interac e-transfer), Loonio (Interac e-transfer), Tesouro (Cards,Applepay,Googlepay), Paysafe (Cards, Applepay, Skrill, Interac e-transfer, Paysafecards), Finix (Cards, Applepay, Googlepay), Sift (FRM)
  * **Enhancing existing integrations:** Stripe (Mobilepay, Sofort, Paypal,Blik) , Braintree(Venmo)
* **Core Orchestration**
  * We plan to introduce split-payment support for gift cards, enabling combined payments within a single transaction for greater flexibility across customer use cases.
* Su**bscriptions enhancements**
  *   **Coupons Handling**

      We plan to enhance the subscriptions module with coupon handling capabilities, allowing merchants to define, apply, and manage promotional discounts for recurring billing plans.
  *   **Outgoing Webhooks**

      We’re introducing outgoing webhooks to enable real-time communication with merchant systems during key subscription lifecycle events
  *   **Entitlements Management**

      We plan to add entitlements management to help merchants link subscription plans to feature access or service tiers.
  *   **Lifecycle Management**

      We’re enhancing subscription lifecycle management to handle complex state transitions such as trial activation, pausing, resuming, renewal, and cancellation.
  *   **Plans SDK**

      We plan to introduce a Plans SDK to provide merchants with a unified interface for displaying subscription plans and collecting payments.
* **Improve Auth rate**
  *   **Error Code Enhancements**

      We plan to enhance our error-handling framework to improve visibility and precision in transaction outcomes.

      *   **Issuer Error Codes in GSM Table**: Issuer-specific error codes will be added to the GSM (Gateway Status Mapping) table to improve accuracy in mapping responses. These will be leveraged to make better retry decisions during payment flows, helping merchants reduce unnecessary retries and improve approval rates.

          **Unified Error Codes and User-Facing Messages**: We will expand the existing unified error code system to generate clearer, user-focused error messages. This ensures consistency in how payment failures are communicated across channels, improving transparency for both merchants and end users.
*   **Real-Time Payment Method Eligibility Checks**

    We plan to introduce real-time eligibility validation for payment methods during checkout. This will include:

    * **Card Eligibility by BIN**: Verifying card eligibility upfront based on BIN (Bank Identification Number) data to prevent declines related to unsupported networks, regions, or card types.
    * **Risk-Based Eligibility Checkpoints**: Adding merchant-level risk evaluation before payment confirmation. This will allow merchants to assess potential transaction risks in real time, reducing fraud exposure and improving overall authorization performance.

**Community Requests**

Based on popular community requests, we plan to take up the following features this quarter:

* **Chase Connector Integration**: Addition of card processing support through Chase.
* **Agentic Shopping Framework**: Enable merchants to embed payments within chatbots and AI-driven commerce experiences, aligned with emerging standards like Stripe’s agentic commerce and Google's AP2 initiatives.

**Want to contribute to the roadmap?**

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
