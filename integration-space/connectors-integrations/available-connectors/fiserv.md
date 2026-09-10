---
description: >-
  Accept card and wallet payments.
metaLinks:
  alternates:
    - fiserv.md
---

# Fiserv

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/fiservLogo.svg" alt=""></div>

Fiserv operates as a payment gateway. Its declared card and wallet methods support refunds but not mandates; 3DS is not supported for card payments and does not apply to wallets. Payments can use automatic, manual, or sequential automatic capture, while webhooks are not implemented in this connector.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, sequential automatic, manual | not supported | American Express, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 27 ([full list](https://hyperswitch.io/pm-list)) | 156 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | not supported | supported | automatic, sequential automatic, manual | not supported | American Express, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 27 ([full list](https://hyperswitch.io/pm-list)) | 156 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, sequential automatic, manual | not applicable | - | 85 ([full list](https://hyperswitch.io/pm-list)) | 22 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, sequential automatic, manual | not applicable | - | 11 ([full list](https://hyperswitch.io/pm-list)) | 10 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | PayPal | not supported | supported | automatic, sequential automatic, manual | not applicable | - | 20 ([full list](https://hyperswitch.io/pm-list)) | 15 ([full list](https://hyperswitch.io/pm-list)) |

### Authentication

Supply an API Key, API Secret, and Merchant ID in the connector configuration. Hyperswitch uses the API Secret to compute a fresh HMAC-SHA256 authorization signature for each request, and sends the signature with the API key, client request ID, timestamp, and HMAC token type. See [`FiservAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/fiserv/transformers.rs#L733-L749) and [`generate_authorization_signature()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/fiserv.rs#L67-L127).

### Webhooks

Fiserv webhooks are not currently processed by this connector. Do not configure Fiserv webhooks as the source of status updates in Hyperswitch. The incoming webhook implementation returns `EventNotSupported` and `WebhooksNotImplemented`; see [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/fiserv.rs#L910-L934).

### Activate Fiserv with Hyperswitch

#### Before you start

1. You need to be registered with Fiserv. Sign up at [fiserv.com](https://www.fiserv.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect Fiserv to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Fiserv supports.

***

### Source reference

[Fiserv connector implementation](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/fiserv.rs)
