---
description: Accept card payments through Authipay.
---

# Authipay

Authipay handles card payments as a payment gateway. Credit and debit paths cover Visa and Mastercard without 3DS or mandate support. Refunds work with automatic, manual, and sequential automatic capture choices.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
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

Supply an **API Key** and **API Secret**. Hyperswitch sends the API Key in the `Api-Key` header. It concatenates `API Key + client request ID + timestamp + payload` without delimiters, signs that string with HMAC-SHA256 using the API Secret, Base64-encodes the result, and sends it in `Message-Signature` with the request ID and timestamp headers. See [`AuthipayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay/transformers.rs#L164-L180), [`generate_authorization_signature()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs#L63-L80), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs#L102-L142).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **API Key** and **API Secret** ready.
3. If activation asks for payment methods, choose only the card types enabled for your connector account.

To connect Authipay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Authipay supports.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. Object lookup, event classification, and resource parsing each return `WebhooksNotImplemented`; see [`IncomingWebhook for Authipay`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs#L757-L781).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Authipay connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay.rs) and [Authipay transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/authipay/transformers.rs).
