---
description: >-
  Accept card, bank redirect, wallet, and pay-later payments.
metaLinks:
  alternates:
    - aci.md
---

# ACI

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/ACILogo.svg" alt=""></div>

ACI provides payment services. Its card methods support recurring charges and optional 3DS, while the other declared methods do not support mandates. Refunds and automatic or manual capture are available across the declared methods.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | EFT | not supported | supported | automatic, manual | not applicable | - | - | - |
| bank redirect | EPS | not supported | supported | automatic, manual | not applicable | - | AUT | EUR |
| bank redirect | Giropay | not supported | supported | automatic, manual | not applicable | - | DEU | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, manual | not applicable | - | NLD | EUR |
| bank redirect | Interac | not supported | supported | automatic, manual | not applicable | - | CAN | CAD, USD |
| bank redirect | Przelewy24 | not supported | supported | automatic, manual | not applicable | - | POL | CZK, EUR, GBP, PLN |
| bank redirect | Sofort | not supported | supported | automatic, manual | not applicable | - | 9 ([full list](https://hyperswitch.io/pm-list)) | CHF, EUR, GBP, HUF, PLN |
| bank redirect | Trustly | not supported | supported | automatic, manual | not applicable | - | 12 ([full list](https://hyperswitch.io/pm-list)) | CZK, DKK, EUR, GBP, NOK, SEK |
| card | Credit Card | supported | supported | automatic, manual | supported, optional | American Express, Diners Club, Discover, JCB, Maestro, Mastercard, UnionPay, Visa | 67 ([full list](https://hyperswitch.io/pm-list)) | 58 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual | supported, optional | American Express, Diners Club, Discover, JCB, Maestro, Mastercard, UnionPay, Visa | 67 ([full list](https://hyperswitch.io/pm-list)) | 58 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | Klarna | not supported | supported | automatic, manual | not applicable | - | 22 ([full list](https://hyperswitch.io/pm-list)) | 11 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Alipay | not supported | supported | automatic, manual | not applicable | - | CHN | CNY |
| wallet | Apple Pay | not supported | supported | automatic, manual | not applicable | - | 77 ([full list](https://hyperswitch.io/pm-list)) | 9 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual | not applicable | - | 74 ([full list](https://hyperswitch.io/pm-list)) | - |
| wallet | MB WAY | not supported | supported | automatic, manual | not applicable | - | ESP, EST, PRT | EUR |
| wallet | Samsung Pay | not supported | supported | automatic, manual | not applicable | - | 31 ([full list](https://hyperswitch.io/pm-list)) | 9 ([full list](https://hyperswitch.io/pm-list)) |

### Connector-specific notes

* **Form-encoded requests:** ACI payment requests use `application/x-www-form-urlencoded`, not JSON. See [`common_get_content_type()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci.rs#L73-L86).

### Authentication

Supply an API Key and Entity ID in the connector configuration. Hyperswitch places the API Key in the `Authorization` header with the Bearer scheme and maps the second credential to `entity_id` in connector requests. See [`AciAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci/transformers.rs#L99-L109) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci.rs#L88-L99).

### Webhooks

The source handles one wire event, `PAYMENT`. Depending on the result code and payment type, it updates a payment as successful, processing, or failed, or a refund as successful or failed; pending refunds and unknown result codes are not handled as status updates. See [`AciWebhookEventType`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci/transformers.rs#L1869-L1873) and [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci.rs#L928-L968).

Webhook processing requires `X-Authentication-Tag`, `X-Initialization-Vector`, and the connector webhook secret. Hyperswitch uses HMAC-SHA256 for source verification. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci.rs#L825-L889).

### Activate ACI with Hyperswitch

#### Before you start

1. You need to be registered with ACI. Sign up at [aciworldwide.com](https://www.aciworldwide.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect ACI to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what ACI supports.

***

### Troubleshooting

**Webhook decryption failure**
Symptom: A webhook reaches Hyperswitch but is not processed. Fix: verify the configured webhook secret and confirm that `X-Initialization-Vector` and `X-Authentication-Tag` are present. The key must be 32 bytes and the tag must be 16 bytes. See [`decrypt_aci_webhook_payload()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci.rs#L751-L820).

***

### Source reference

[ACI connector implementation](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/aci.rs)
