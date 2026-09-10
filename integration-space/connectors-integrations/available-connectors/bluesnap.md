---
description: Accept card and wallet payments through BlueSnap.
metaLinks:
  alternates:
    - bluesnap.md
---

# BlueSnap

BlueSnap is a payment gateway for card and digital wallet payments. Card payments support optional 3DS and several card networks, while Apple Pay and Google Pay provide wallet options. Refunds and automatic, manual, or sequential automatic capture apply to every declared method. Webhooks cover payment, refund, and dispute updates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** disputes, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, JCB, Maestro, Mastercard, RuPay, Visa | 185 ([full list](https://hyperswitch.io/pm-list)) | 94 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 88 ([full list](https://hyperswitch.io/pm-list)) | 52 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 74 ([full list](https://hyperswitch.io/pm-list)) | 54 ([full list](https://hyperswitch.io/pm-list)) |

### Authentication

Supply an API Username and API Password in the connector configuration. Hyperswitch combines them for HTTP Basic authentication and sends `Authorization: Basic <base64 API username and API password>` on connector requests. See [`BluesnapAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/bluesnap/transformers.rs#L768-L786) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/bluesnap.rs#L130-L143).

### Webhooks

Configure a webhook merchant secret in Hyperswitch; the shared webhook verifier uses that value as the signature key. See [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_interfaces/src/webhooks.rs#L266-L301). BlueSnap webhooks use HMAC-SHA256 verification: Hyperswitch reads the hex signature from `bls-signature` and verifies the `bls-ipn-timestamp` value followed by the request body. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/bluesnap.rs#L1105-L1129).

The connector recognizes six webhook event values:

| Event | Effect in Hyperswitch |
|---|---|
| `DECLINE` | Payment is marked failed |
| `CC_CHARGE_FAILED` | Payment is marked failed |
| `CHARGE` | Payment is marked successful |
| `REFUND` | Refund is marked successful |
| `CHARGEBACK` | Dispute state follows `cbStatus` |
| `CHARGEBACK_STATUS_CHANGED` | Dispute state follows `cbStatus` |

For chargeback events, `NEW` and `WORKING` open the dispute, `CLOSED` expires it, `COMPLETED_LOST` marks it lost, `COMPLETED_PENDING` marks it challenged, and `COMPLETED_WON` marks it won. The wire names and mappings are defined by [`BluesnapWebhookEvents`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/bluesnap/transformers.rs#L992-L1053).

### Activate BlueSnap with Hyperswitch

#### Before you start

1. Register with BlueSnap.
2. Create a Hyperswitch account.
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect BlueSnap to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what BlueSnap supports.

### Source reference

[BlueSnap connector implementation](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/bluesnap.rs) and [BlueSnap data mappings](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/bluesnap/transformers.rs)
