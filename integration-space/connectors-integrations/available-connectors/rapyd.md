---
description: Configure Rapyd card and wallet payments with Hyperswitch.
metaLinks:
  alternates:
    - rapyd.md
---

# Rapyd

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/rapydLogo.svg" alt=""></div>

Across Rapyd's payment gateway routes, card payments sit alongside Apple Pay and Google Pay. Credit and debit cards can use automatic, manual, or sequential automatic capture, while wallets use the same capture options without a 3DS step. Mandates are not supported, and refunds cover every listed method.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** disputes, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | 246 ([full list](https://hyperswitch.io/pm-list)) | 76 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | 246 ([full list](https://hyperswitch.io/pm-list)) | 76 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 59 ([full list](https://hyperswitch.io/pm-list)) | 40 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 50 ([full list](https://hyperswitch.io/pm-list)) | 36 ([full list](https://hyperswitch.io/pm-list)) |

### Activate Rapyd with Hyperswitch
#### Before you start
1. Register with Rapyd.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) or create your Hyperswitch account.
3. In the Rapyd dashboard, go to **Developers > Access & Secret Keys** and copy your Access Key and Secret Key.
4. Enable the same payment methods in Rapyd and in your Hyperswitch connector configuration.

To connect Rapyd to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Rapyd supports.

### Connector-Specific Notes

Every API request carries a fresh signature. Hyperswitch concatenates the HTTP method, URL path, salt, timestamp, access key, secret key, and request body in that order with no delimiter. It signs that value with HMAC-SHA256 using the secret key, hex-encodes the result, then URL-safe Base64-encodes it. See [`generate_signature()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs#L76-L100).

### Authentication

Provide an `<access key>` and `<secret key>`. The `BodyKey` mapping assigns `api_key` to the access key and `key1` to the secret key. Rapyd does not use an `Authorization` header; each request sends `access_key`, `salt`, `timestamp`, and `signature` headers. See [`RapydAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd/transformers.rs#L199-L217), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs#L120-L126), and the [authorization request headers](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs#L223-L255).

### Webhooks

Rapyd webhook signatures use HMAC-SHA256. Hyperswitch reads the URL-safe Base64 value from the `signature` header and constructs the signed message by concatenating the webhook URL, salt, timestamp, access key, secret key, and body in that order with no delimiter. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs#L746-L763) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs#L765-L836).

The connector maps 8 webhook event values:

| Wire event value | Effect |
|---|---|
| `PAYMENT_COMPLETED` | Payment succeeds |
| `PAYMENT_CAPTURED` | Payment succeeds |
| `PAYMENT_FAILED` | Payment fails |
| `REFUND_COMPLETED` | Refund succeeds |
| `PAYMENT_REFUND_REJECTED` | Refund fails |
| `PAYMENT_REFUND_FAILED` | Refund fails |
| `PAYMENT_DISPUTE_CREATED` | Dispute opens |
| `PAYMENT_DISPUTE_UPDATED` | Dispute follows the status mapping below |

For dispute updates, 4 status values change the dispute state:

| Wire status value | Effect |
|---|---|
| `ACT` | Dispute opens |
| `RVW` | Dispute is challenged |
| `LOS` | Dispute is lost |
| `WIN` | Dispute is won |

The wire values come from [`RapydWebhookObjectEventType`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd/transformers.rs#L542-L566) and [`RapydWebhookDisputeStatus`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd/transformers.rs#L568-L590). Their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs#L869-L900).

### Source reference

The connector implementation is [`rapyd.rs`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/rapyd.rs).
