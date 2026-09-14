---
description: >-
  Accept card and bank-redirect payments through Worldline with HMAC-signed requests.
metaLinks:
  alternates:
    - worldline.md
---

# Worldline

Worldline combines card checkout with bank-redirect payment paths. Refunds and delayed capture options apply across the declared methods. Payment callbacks distinguish successful and rejected outcomes.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | Giropay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | DEU | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, manual, sequential automatic | not applicable | - | NLD | EUR |
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, Mastercard, Visa | 247 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, Mastercard, Visa | 247 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |


### Authentication

Worldline requires **API Key ID**, **Secret API Key**, and **Merchant ID**. Hyperswitch joins the HTTP method, content type, date, and endpoint with newline delimiters, signs that string with HMAC-SHA256 using Secret API Key, then sends `Authorization: GCS v1HMAC:<API Key ID>:<signature>`. Merchant ID is placed in each request URL. See [`WorldlineAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs#L501-L519), [`generate_authorization_token()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs#L64-L88), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs#L100-L127).

### Webhooks

Hyperswitch verifies the Base64-decoded `X-GCS-Signature` value with HMAC-SHA256 over the raw request body. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs#L721-L731) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs#L733-L740).

Handled event wire values: **3**.

| Wire value | Effect |
|---|---|
| `payment.paid` | Payment succeeds |
| `payment.rejected` | Payment fails |
| `payment.rejected_capture` | Payment fails |

The wire names come from [`WebhookEvent`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs#L772-L782); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs#L763-L788). Endpoint verification requests are echoed through the response path described by [`get_webhook_api_response()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs#L806-L831).

### Activate Worldline with Hyperswitch

#### Before you start

1. Register with Worldline at [worldline.com](https://worldline.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key ID**, **Secret API Key**, and **Merchant ID** under **API Keys** in the Worldline dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Worldline-specific behavior.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Worldline connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline.rs) and [Worldline transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs).
