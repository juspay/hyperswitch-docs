---
description: Accept cryptocurrency payments through Bitpay.
---

# Bitpay

Bitpay provides cryptocurrency checkout as an alternative payment method. Crypto payments use automatic capture and support refunds. Payment webhooks can move an invoice through processing, success, or failure outcomes.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** alternative payment method

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | supported | automatic | 30 | 8 |

### Authentication

Configure an **API Key** for the connector. The current `build_headers()` override sends only content type and `X-Accept-Version: 2.0.0`; it does not call `get_auth_header()`, so the API Key is not placed in the `Authorization` header on connector requests. See [`BitpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay/transformers.rs#L67-L81), [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay.rs#L83-L107), and the unused [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay.rs#L126-L137).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **API Key** ready.
3. If the activation flow asks for cryptocurrency payment methods, select only those enabled for your connector account.
4. Account for the authentication limitation described above before testing connector requests.

To connect Bitpay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Bitpay supports.

### Webhooks

The connector does not override webhook source verification, so callback signatures are not checked. Configure the endpoint only if that limitation is acceptable for your integration.

Handled event wire values: **8**.

| Wire value | Effect |
|---|---|
| `invoice_paidInFull` | Payment is processing |
| `invoice_confirmed` | Payment succeeds |
| `invoice_completed` | Payment succeeds |
| `invoice_expired` | No payment update is applied |
| `invoice_failedToConfirm` | No payment update is applied |
| `invoice_declined` | Payment fails |
| `invoice_refundComplete` | No payment update is applied |
| `invoice_manuallyNotified` | No payment update is applied |

Any other event value uses the unknown fallback and applies no payment update. The eight wire values and fallback come from [`WebhookEventType`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay/transformers.rs#L294-L325); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay.rs#L399-L420).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Bitpay connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay.rs) and [Bitpay transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/bitpay/transformers.rs).
