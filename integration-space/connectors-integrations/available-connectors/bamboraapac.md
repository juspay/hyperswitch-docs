---
description: Accept card payments through Bambora Asia-Pacific.
metaLinks:
  alternates:
    - bamboraapac.md
---

# Bambora Asia-Pacific

Accept credit and debit cards through Bambora Asia-Pacific. Cards support mandates and refunds, with automatic or manual capture. 3DS is not supported.

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
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 185 ([full list](https://hyperswitch.io/pm-list)) | 76 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 185 ([full list](https://hyperswitch.io/pm-list)) | 76 ([full list](https://hyperswitch.io/pm-list)) |

Use automatic or manual capture. The connector declares sequential automatic capture, but the payment request builder accepts only automatic and manual, so a payment with sequential automatic capture fails with `CaptureMethodNotSupported` before any request is sent. See [`get_transaction_type()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac/transformers.rs#L173-L179) and the [declared capture methods](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac.rs#L736-L740).

Voiding a payment is not implemented: the connector has no request for the void flow, so a cancel request never reaches Bambora Asia-Pacific. If you use manual capture, do not rely on Hyperswitch to cancel an uncaptured authorization. See [`ConnectorIntegration<Void>`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac.rs#L527).

### Authentication

Supply a **Username**, **Password**, and **Account Number**. Hyperswitch maps the connector API Key to Username, API Secret to Password, and the second key to Account Number. These values are written to the XML request as `<UserName>`, `<Password>`, and `<AccountNumber>`; the transport adds no authorization header. See [`BamboraapacAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac/transformers.rs#L181-L203), [`get_transaction_body()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac/transformers.rs#L73-L102), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac.rs#L86-L101).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **Username**, **Password**, and **Account Number** ready.

To connect Bambora Asia-Pacific to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Bambora Asia-Pacific supports.

### Webhooks

Bambora Asia-Pacific webhooks are not supported. Use payment sync and refund sync for status updates. The connector's webhook handlers all return `WebhooksNotImplemented`; see [`IncomingWebhook for Bamboraapac`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac.rs#L704-L728).

### Source reference

Capture, void, authentication, and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Bambora Asia-Pacific connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac.rs) and [Bambora Asia-Pacific transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bamboraapac/transformers.rs).
