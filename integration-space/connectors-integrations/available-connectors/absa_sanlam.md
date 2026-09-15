---
description: Process EFT debit order payments through AbsaSanlam.
---

# AbsaSanlam

AbsaSanlam provides a payment gateway path for EFT debit orders. Transactions use automatic capture, while mandates and refunds are unavailable. The connector declaration does not expose webhook flow classes.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank debit | EFT Debit Order | not supported | not supported | automatic | - | - |

### Authentication

Supply an **API Key** and **Merchant ID**. Hyperswitch sends the API Key unchanged in the `Authorization` header and the Merchant ID in the `Merchant-Id` header. See [`AbsaSanlamAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam/transformers.rs#L22-L38), [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L69-L86), and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L106-L123).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **API Key** and **Merchant ID** ready.
3. If the activation flow asks you to select payment methods, choose only the methods enabled for your connector account.

To connect AbsaSanlam to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what AbsaSanlam supports.

### Webhooks

The status block declares no webhook flows, but the connector implements payment and dispute event processing. Configure the connector `merchant_secret`, shown as the **Source Verification Key**, in Hyperswitch. The shared verifier supplies that value as the HMAC key; AbsaSanlam verifies the hexadecimal `X-Signature` header with HMAC-SHA256 over the raw request body. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L303-L329) and [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_interfaces/src/webhooks.rs#L265-L301).

Handled event wire values: **3**.

| Wire value | Effect |
|---|---|
| `payment.succeeded` | Payment succeeds |
| `payment.failed` | Payment fails |
| `dispute.opened` | A dispute opens |

The three wire values come from [`AbsaSanlamWebhookEventType`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam/transformers.rs#L60-L68); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L353-L378).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [AbsaSanlam connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs) and [AbsaSanlam transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam/transformers.rs).
