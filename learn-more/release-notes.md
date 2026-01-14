---
description: >-
  This page is a central archive of Hyperswitch release notes. It summarises
  recent product updates.
---

# Release Notes

Hyperswitch is a fast-moving open source payments orchestration platform. We ship improvements across routing, vaulting, reconciliation, connectors, SDKs, and developer experience.

This page serves as a central place to track what is shipping in Hyperswitch.

These release notes help you:

1. Understand what is new or improved across Hyperswitch.
2. Track connector and SDK updates in one place.
3. Follow product evolution across core orchestration, routing, vault, reconciliation, and customer capabilities.
4. Stay aligned with ongoing improvements in reliability and developer experience.

With these sections:

1. Connector expansions and enhancements
2. Customer and access management
3. Routing and core improvements<br>

<details>

<summary>December 10th - 16th, 2025</summary>

#### Highlights

* Advanced Routing: Introduced new routing capabilities based on transaction initiators and issuer countries to optimize payment success rates.
* Expanded Connector Support: Added specialized flows including Peach Payments Pre-Auth, Braintree 3DS pass-through, and WorldpayWPG payouts.
* UCS Tunnel Enhancements: Significant progress on the Hyperswitch <> UCS tunnel with new support for sessions, PayPal Post-Auth, and granular authentication.
* Identity & Security: Launched OIDC infrastructure and discovery endpoints, alongside improved user role validation and a generic Locker API.
* Standardized Error Handling: Implemented GSM (Global Status Monitoring) schema updates to provide more consistent error codes and messages across the platform.

#### Connector expansions and enhancements

* Peach Payments: Added support for Pre-Auth flows with full reversal capabilities. \[[#10590](https://github.com/juspay/hyperswitch/pull/10590)]
* Braintree: Introduced support for external 3DS pass-through authentication. \[[#10591](https://github.com/juspay/hyperswitch/pull/10591)]
* WorldpayWPG: Implemented "Fast Access" feature for payout processing. \[[#10647](https://github.com/juspay/hyperswitch/pull/10647)]
* Zift: Streamlined integration by removing redundant billing fields and adding account verification (mandate setup) support. \[[#10665](https://github.com/juspay/hyperswitch/pull/10665)]
* Stripe: Expanded zero-amount mandate support and refined `setup_future_usage` configurations for Affirm and Klarna. \[[#10644](https://github.com/juspay/hyperswitch/pull/10644), [#10610](https://github.com/juspay/hyperswitch/pull/10610)]
* NMI: Fixed an issue where `merchant_defined_fields` were being double encoded. \[[#10603](https://github.com/juspay/hyperswitch/pull/10603)]
* J.P. Morgan: Refactored capture and void requests to ensure proper field mapping. \[[#10617](https://github.com/juspay/hyperswitch/pull/10617)]

#### Customer and access management

* OIDC Infrastructure: Launched OpenID Connect (OIDC) infrastructure including discovery endpoints for standardized identity provider integration. \[[#10145](https://github.com/juspay/hyperswitch/pull/10145), [#10678](https://github.com/juspay/hyperswitch/pull/10678)]
* User Roles: Enhanced security by adding entity type validation in user role lineage queries and inviter-invitee role hierarchy checks. \[[#10608](https://github.com/juspay/hyperswitch/pull/10608), [#10667](https://github.com/juspay/hyperswitch/pull/10667)]
* Locker API: Implemented a generic Locker API handler to unify sensitive data management. \[[#10242](https://github.com/juspay/hyperswitch/pull/10242)]
* Payouts: Added fallback logic for name fields when processing payouts via PSP tokens. \[[#10502](https://github.com/juspay/hyperswitch/pull/10502)]

#### Routing and core improvements

* Euclid Routing: Enabled advanced routing rules based on `transaction_initiator` and `issuer_country`. \[[#10658](https://github.com/juspay/hyperswitch/pull/10658), [#10638](https://github.com/juspay/hyperswitch/pull/10638)]
* HS <> UCS Tunnel: Significant enhancements including Session flow support, Pre-Auth for NMI, PayPal Post-Auth, and granular authentication interfaces. \[[#10552](https://github.com/juspay/hyperswitch/pull/10552), [#10632](https://github.com/juspay/hyperswitch/pull/10632), [#10640](https://github.com/juspay/hyperswitch/pull/10640), [#10622](https://github.com/juspay/hyperswitch/pull/10622)]
* Global Status Monitoring (GSM): Standardized error fields across database schemas and refined the lookup logic for GSM codes and messages. \[[#10600](https://github.com/juspay/hyperswitch/pull/10600), [#10585](https://github.com/juspay/hyperswitch/pull/10585)]
* Webhooks & Analytics: Added `requires_capture` to default webhook statuses and improved event tracking for payment method flows and refund filters. \[[#10660](https://github.com/juspay/hyperswitch/pull/10660), [#10549](https://github.com/juspay/hyperswitch/pull/10549)]
* CIT Payments: Added support for Customer Initiated Transactions (CIT) using saved ACH payment methods. \[[#10592](https://github.com/juspay/hyperswitch/pull/10592)]

</details>

<details>

<summary>December 17th - 23th, 2025</summary>

#### Highlights

* Advanced Error Insights: Enhanced Shift4 error mapping to propagate specific issuer error codes, enabling more precise troubleshooting for failed transactions.
* Expanded Payment Capabilities: Introduced PayJustNow In-Store and OpenBanking support for the Hyperswitch <> UCS integration, broadening global payment method availability.
* Optimized Data Retrieval: Launched a new batch retrieval endpoint for payment methods and refined metadata propagation from the locker to payment responses.
* Decryption Enhancements: Added support for Apple Pay decryption on Braintree and NMI (via WASM), streamlining the checkout experience for digital wallets.
* Architectural Consolidation: Refactored gateway routing into a unified execution path and introduced a comparison service to improve system reliability and performance.

#### Connector expansions and enhancements

* Shift4: Enhanced error mapping to support and propagate granular issuer error codes. \[[#10748](https://github.com/juspay/hyperswitch/pull/10748)]
* Gigadat: Added support for storing Interac customer information within the connector's additional data fields. \[[#10749](https://github.com/juspay/hyperswitch/pull/10749)]
* Braintree: Introduced Apple Pay HS-Decryption support and expanded UCS wallet support for PayPal, Apple Pay, and Google Pay SDKs. \[[#10734](https://github.com/juspay/hyperswitch/pull/10734), [#10513](https://github.com/juspay/hyperswitch/pull/10513)]
* PayJustNow: Implemented the PayJustNow In-Store payment method and template code. \[[#10745](https://github.com/juspay/hyperswitch/pull/10745), [#10716](https://github.com/juspay/hyperswitch/pull/10716)]
* Novalnet: Updated SEPA requirements to make billing email a mandatory field. \[[#10720](https://github.com/juspay/hyperswitch/pull/10720)]
* Nuvei: Implemented a passthrough payout flow for faster processing. \[[#10463](https://github.com/juspay/hyperswitch/pull/10463)]
* WorldpayWPG: Fixed an issue with PSync deserialization in error responses. \[[#10764](https://github.com/juspay/hyperswitch/pull/10764)]

#### Customer and access management

* Metadata Propagation: Improved core logic to propagate metadata from the locker response directly to the payment method response. \[[#10645](https://github.com/juspay/hyperswitch/pull/10645)]
* Payment Method Service: Added support for guest checkout flows and introduced a batch data retrieval endpoint. \[[#10487](https://github.com/juspay/hyperswitch/pull/10487), [#10663](https://github.com/juspay/hyperswitch/pull/10663)]
* Authentication Models: Introduced new domain models for authentication and added Kafka-based filters to the dashboard for better monitoring. \[[#10446](https://github.com/juspay/hyperswitch/pull/10446)]
* API Consistency: Aligned `ApiEvent` status codes with HTTP responses when the proxy connector status code feature is enabled. \[[#10680](https://github.com/juspay/hyperswitch/pull/10680)]

#### Routing and core improvements

* Unified Routing: Consolidated payment gateway routing into a single execution path to improve maintainability and speed. \[[#10710](https://github.com/juspay/hyperswitch/pull/10710)]
* HS <> UCS Tunnel: Introduced PostAuth for Nexixpay and PreAuth flows for Redsys and Nuvei. \[[#10706](https://github.com/juspay/hyperswitch/pull/10706), [#10727](https://github.com/juspay/hyperswitch/pull/10727), [#10726](https://github.com/juspay/hyperswitch/pull/10726)]
* NMI WASM: Added Apple Pay decryption flow via WASM for enhanced frontend security. \[[#10740](https://github.com/juspay/hyperswitch/pull/10740), [#10686](https://github.com/juspay/hyperswitch/pull/10686)]
* Network Tokens: Enabled the passing of network tokens directly in payment requests. \[[#9975](https://github.com/juspay/hyperswitch/pull/9975)]
* Infrastructure Fixes: Increased `RUST_MIN_STACK` size to prevent stack overflow errors in heavy environments and improved error handling for 3DS authentication strategies. \[[#10730](https://github.com/juspay/hyperswitch/pull/10730), [#10722](https://github.com/juspay/hyperswitch/pull/10722)]

</details>

<details>

<summary>December 24th - 30th, 2025</summary>

{% hint style="info" %}
This will be deployed in production on or before 8th January 2025
{% endhint %}

#### Highlights

* Advanced Error Structuring: Introduced structured error details to `payment_attempts`, allowing for a more granular breakdown of failures at each stage of the transaction attempt.
* Redirection & SDK Session Support: Refactored the order creation interface to support seamless redirection and SDK session tokens for Trustpay and Payme, improving high-conversion checkout flows.
* Proxy V2 Volatile ID Support: Added support for volatile payment method IDs within Proxy V2, enabling more flexible and secure handling of temporary payment method tokens.
* Unified Payment Architecture: Transitioned core logic from "Preprocessing" to "Granular Flow" and unified gateway context handling to simplify payment processing and improve overall system reliability.
* Payout Transparency: Enhanced connector event logging to propagate `payout_id`, providing better audit trails and visibility for payout lifecycle management.

#### Connector expansions and enhancements

* Zift: Updated transaction logic to use `Ecommerce` industry type categorization instead of simple card-present/not-present flags for more accurate processing. \[[#10775](https://github.com/juspay/hyperswitch/pull/10775)]
* FINIX: Added comprehensive support for webhooks and statement descriptors to improve reconciliation and transaction clarity on bank statements. \[[#10758](https://github.com/juspay/hyperswitch/pull/10758)]
* Finix (WASM): Enhanced security for the WASM integration by adding merchant source verification keys. \[[#10792](https://github.com/juspay/hyperswitch/pull/10792)]
* Trustpay & Payme: Refactored the create order interface to better handle redirection and SDK-based session tokens. \[[#10779](https://github.com/juspay/hyperswitch/pull/10779)]
* WorldpayWPG: Fixed a critical bug in the 3DS challenge endpoint to ensure smooth cardholder authentication. \[[#10772](https://github.com/juspay/hyperswitch/pull/10772)]

#### Customer and access management

* Proxy V2 Enhancement: Integrated volatile payment method ID support, allowing for more dynamic management of temporary payment identifiers in proxy-based workflows. \[[#10597](https://github.com/juspay/hyperswitch/pull/10597)]
* Platform Trackers: Added support for update trackers within the platform payment models, enabling better state monitoring across different entities. \[[#10691](https://github.com/juspay/hyperswitch/pull/10691)]
* Payout Updates: Introduced a manual update API for payouts, giving merchants more control over modifying payout statuses when automated syncs are unavailable. \[[#10539](https://github.com/juspay/hyperswitch/pull/10539)]

#### Routing and core improvements

* Granular Flow Architecture: Successfully migrated core preprocessing logic to the new Granular Flow, optimizing how requests are handled before authorization. \[[#10778](https://github.com/juspay/hyperswitch/pull/10778)]
* Error Detail Framework: Enhanced the `payment_attempts` model to include structured error details, which helps in identifying whether failures originated from the issuer, network, or connector. \[[#10646](https://github.com/juspay/hyperswitch/pull/10646)]
* Unified Context Handling: Simplified the payment processing logic by unifying gateway context handling (v2), reducing technical debt and improving performance. \[[#10774](https://github.com/juspay/hyperswitch/pull/10774)]
* Connector Event Enrichment: Enabled the propagation of `payout_id` within connector events to ensure end-to-end traceability for every payout attempt. \[[#10518](https://github.com/juspay/hyperswitch/pull/10518)]

</details>

<details>

<summary>December 31st 2025 - January 6th, 2026</summary>

{% hint style="info" %}
This will be deployed in production on or before 15th January 2025
{% endhint %}

#### **Highlights**

1. Expanded analytics coverage for payouts with new audit and reporting capabilities.
2. Improved platform visibility with richer payment response fields and better processor tracking.
3. Strengthened connector support for Google Pay, mandates, and authentication flows.
4. Continued improvements in tokenisation, routing accuracy, and API reliability.

#### Connector expansions and enhancements

1. Adyen and Barclaycard: authentication and wallet improvements
   * Added Google Pay pre-decryption support for Adyen, improving wallet processing reliability ([#10806](https://github.com/juspay/hyperswitch/pull/10806))
   * Introduced authentication flows for Barclaycard, enabling stronger step-up handling where required ([#10810](https://github.com/juspay/hyperswitch/pull/10810))
2. Airwallex, Redsys, and Stripe: mandate and request handling fixes
   * Fixed order creation consistency across all Airwallex flows ([#10768](https://github.com/juspay/hyperswitch/pull/10768))
   * Resolved base64 padding and 3DS transaction ID mapping issues for Redsys ([#10757](https://github.com/juspay/hyperswitch/pull/10757), [#10784](https://github.com/juspay/hyperswitch/pull/10784))
   * Added support for customer-initiated mandate payments and ensured `setup_future_usage` is passed for tokenised cards in Stripe flows ([#10815](https://github.com/juspay/hyperswitch/pull/10815))
3. Paysafe and JPMorgan: token and request correctness
   * Introduced a PaymentMethodToken flow for Paysafe connectors ([#10541](https://github.com/juspay/hyperswitch/pull/10541))
   * Ensured correct field propagation in capture and void requests for JPMorgan ([#10617](https://github.com/juspay/hyperswitch/pull/10617))

#### Customer and access management

1. Platform-connected customer access
   * Added support to retrieve customer details in platform-based payment flows, improving visibility in multi-merchant setups ([#10684](https://github.com/juspay/hyperswitch/pull/10684))
2. Authentication model improvements
   * Restructured authentication to use a unified platform model with initiator tracking, laying groundwork for more consistent auth handling across flows ([#10746](https://github.com/juspay/hyperswitch/pull/10746))

#### Routing and core improvements

1. Analytics and reporting
   * Added compatibility for payouts in the Analytics API and introduced a payout audit table to support richer payout reporting and reconciliation ([#10479](https://github.com/juspay/hyperswitch/pull/10479), [#10842](https://github.com/juspay/hyperswitch/pull/10842), [#10588](https://github.com/juspay/hyperswitch/pull/10588))
2. Payment response enrichment
   * Added `processor_merchant_id` and `initiator` fields to payment responses, improving downstream observability and debugging ([#10804](https://github.com/juspay/hyperswitch/pull/10804))
   * Updated post-update tracking to accept processor information for better lifecycle visibility ([#10743](https://github.com/juspay/hyperswitch/pull/10743))
3. Tokenisation and payment method APIs
   * Introduced CVC token payment method APIs (v2) and updated token generation and consumption logic to align with newer payment flows ([#10787](https://github.com/juspay/hyperswitch/pull/10787), [#10835](https://github.com/juspay/hyperswitch/pull/10835))
4. Network and error handling
   * Added `connector_response_reference_id` to error responses, improving traceability across failed requests ([#10816](https://github.com/juspay/hyperswitch/pull/10816))
   * Began passing network tokens directly in payment requests for supported flows ([#9975](https://github.com/juspay/hyperswitch/pull/9975))
5. Routing correctness and stability
   * Ensured `setup_future_usage` is populated using intent data within router state, reducing inconsistencies in saved payment behaviour ([#10829](https://github.com/juspay/hyperswitch/pull/10829))

</details>
