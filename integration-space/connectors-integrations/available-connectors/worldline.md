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

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | Giropay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | DEU | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, manual, sequential automatic | not applicable | - | NLD | EUR |
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, Mastercard, Visa | 247 | 154 |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, Mastercard, Visa | 247 | 154 |

### Authentication

Worldline requires **API Key ID**, **Secret API Key**, and **Merchant ID**. Hyperswitch signs each request: it joins the HTTP method, content type, date, and endpoint into one string, signs it with HMAC-SHA256 using the Secret API Key, and sends `Authorization: GCS v1HMAC:<API Key ID>:<signature>`. The Merchant ID is part of the request URL. Details: [`build_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L96-L128) builds the transport headers via [`generate_authorization_token()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L64-L88), and [`WorldlineAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs#L501-L519) maps the credentials.

### Before you start

1. Register with Worldline at [worldline.com](https://worldline.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key ID**, **Secret API Key**, and **Merchant ID** under **API Keys** in the Worldline dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Worldline-specific behavior.

### Webhooks

Hyperswitch verifies the Base64-decoded `X-GCS-Signature` value with HMAC-SHA256 over the raw request body. Configure Worldline's webhook secret key in Hyperswitch's connector `merchant_secret` (the **Source Verification Key**); Hyperswitch uses it as the HMAC key when checking the signature. Worldline's own SDKs choose the key using the `X-GCS-KeyId` header; Hyperswitch always uses the single secret you configure. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L721-L731) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L733-L740).

Hyperswitch reads the payment embedded in the callback to get the transaction ID and status, and answers Worldline's endpoint verification checks. Event types other than the three below are treated as unsupported. Object lookup: [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L742-L760). Resource extraction: [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L790-L804). Event dispatch: [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L763-L788).

Handled event wire values: **3**.

| Wire value | Effect |
|---|---|
| `payment.paid` | Payment succeeds |
| `payment.rejected` | Payment fails |
| `payment.rejected_capture` | Payment fails |

The wire names come from [`WebhookEvent`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs#L772-L782). Endpoint verification requests are echoed through [`get_webhook_api_response()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L806-L831).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0`. See [Worldline connector source](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs) and [Worldline transformers](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs).
