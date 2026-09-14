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

<!-- generated from GET /feature_matrix; hyperswitch e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
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
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, Mastercard, Visa | 247 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, Mastercard, Visa | 247 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |

### Authentication

Worldline requires **API Key ID**, **Secret API Key**, and **Merchant ID**. Its [`build_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L96-L128) override builds the transport headers directly: [`generate_authorization_token()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L64-L88) joins the HTTP method, content type, date, and endpoint with newline delimiters, signs the string with HMAC-SHA256 using Secret API Key, and returns `GCS v1HMAC:<API Key ID>:<signature>` for the `Authorization` header. Merchant ID is placed in request URLs after [`WorldlineAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs#L501-L519) maps the credentials.

### Before you start

1. Register with Worldline at [worldline.com](https://worldline.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key ID**, **Secret API Key**, and **Merchant ID** under **API Keys** in the Worldline dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Worldline-specific behavior.

### Webhooks

Hyperswitch verifies the Base64-decoded `X-GCS-Signature` value with HMAC-SHA256 over the raw request body. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L721-L731) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L733-L740).

Object lookup parses the embedded payment and returns its connector transaction ID; see [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L742-L760). Resource extraction returns the embedded payment object and fails when it is absent; see [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L790-L804). Event dispatch maps endpoint checks to `EndpointVerification`, maps the three wire values below to payment outcomes, and treats unknown event types as unsupported; see [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L763-L788).

Handled event wire values: **3**.

| Wire value | Effect |
|---|---|
| `payment.paid` | Payment succeeds |
| `payment.rejected` | Payment fails |
| `payment.rejected_capture` | Payment fails |

The wire names come from [`WebhookEvent`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs#L772-L782). Endpoint verification requests are echoed through [`get_webhook_api_response()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs#L806-L831).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0`. See [Worldline connector source](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline.rs) and [Worldline transformers](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldline/transformers.rs).
