---
description: Accept Amazon Pay wallet payments.
---

# Amazon Pay

Amazon Pay supplies a wallet checkout route as an alternative payment method. Payments use automatic capture and can be refunded. Mandates and webhook flow classes are not declared for this connector.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** beta

**Category:** alternative payment method

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| wallet | Amazon Pay | not supported | supported | automatic | USA | USD |

### Authentication

Supply a **Public Key** and **Private Key**. Hyperswitch hashes the canonical request with SHA-256, signs the algorithm line and request hash with RSA-PSS-SHA256 using the Private Key, Base64-encodes the signature, and places the Public Key plus the signature in the `Authorization` header. See [`AmazonpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay/transformers.rs#L323-L339), [`create_authorization_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L92-L130), [`create_signature()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L132-L184), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L205-L278).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **Public Key** and **Private Key** ready.
3. If the activation flow requests wallet details, provide only artifacts produced for the Amazon Pay wallet configuration.
4. Select Amazon Pay during activation only when it is enabled for your connector account.

To connect Amazon Pay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Amazon Pay supports.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. Object lookup, event classification, and resource parsing each return `WebhooksNotImplemented`; see [`IncomingWebhook for Amazonpay`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L725-L749).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Amazon Pay connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay.rs) and [Amazon Pay transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/amazonpay/transformers.rs).
