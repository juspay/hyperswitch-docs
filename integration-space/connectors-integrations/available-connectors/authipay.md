---
description: Accept card payments through Authipay.
metaLinks:
  alternates:
    - authipay.md
---

# Authipay

Accept Visa and Mastercard credit and debit cards through Authipay. Hyperswitch sends Authipay requests to Fiserv's EMEA payments gateway API (see the [production base URL](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/production.toml#L45)). Payments support automatic, manual, and sequential automatic capture, and refunds are supported. 3DS and mandates are not supported.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, sequential automatic, manual | not supported | Mastercard, Visa | - | - |
| card | Debit Card | not supported | supported | automatic, sequential automatic, manual | not supported | Mastercard, Visa | - | - |

### Authentication

Supply an **API Key** and **API Secret**. Hyperswitch sends the API Key in the `Api-Key` header. It concatenates `API Key + client request ID + timestamp + payload` without delimiters, signs that string with HMAC-SHA256 using the API Secret, Base64-encodes the result, and sends it in `Message-Signature`. Each request also carries the generated request ID in `Client-Request-Id`, the Unix timestamp in milliseconds in `Timestamp`, and `Auth-Token-Type: HMAC`. See [`AuthipayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay/transformers.rs#L164-L180), [`generate_authorization_signature()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs#L63-L80), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs#L102-L142).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **API Key** and **API Secret** ready.
3. The connector form also shows a **Source verification key** field for webhooks. You can leave it blank: Authipay webhooks are not supported, so the value has no effect (see [Webhooks](#webhooks) and the [connector form configuration](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/connector_configs/toml/production.toml#L481-L494)).

To connect Authipay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Authipay supports.

### Webhooks

Authipay webhooks are not supported. Use payment sync and refund sync for status updates. The connector's webhook handlers all return `WebhooksNotImplemented`; see [`IncomingWebhook for Authipay`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs#L757-L781).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Authipay connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs) and [Authipay transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay/transformers.rs).
