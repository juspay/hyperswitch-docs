---
description: >-
  AbsaSanlam connector status: payment flows are not yet implemented, so payments cannot be processed.
metaLinks:
  alternates:
    - absa_sanlam.md
---

# AbsaSanlam

AbsaSanlam is an EFT debit order connector, but Hyperswitch cannot currently process payments with it: every payment and refund flow in the connector is unimplemented, so no payment request ever reaches AbsaSanlam. The capability block below reflects what the connector's code declares, not what currently works. We are working on it; see [the tracking issue](https://github.com/juspay/hyperswitch/issues/14234).

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** live (declared in code; the payment flows are not implemented, see below)

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank debit | EFT Debit Order | not supported | not supported | automatic | - | - |

This table is the connector's declared capability set. Every flow behind it (`Authorize`, `PSync`, `Capture`, `Void`, refund `Execute`, refund `RSync`, and the rest) returns `FlowNotSupported`, so none of these capabilities can currently be used. See [`ConnectorIntegration<Authorize>`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L198-L210) and the [full set of stubbed flows](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L138-L301).

### Authentication

Supply an **API Key** and **Merchant ID**. Hyperswitch sends the API Key unchanged in the `Authorization` header and the Merchant ID in the `Merchant-Id` header. See [`AbsaSanlamAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam/transformers.rs#L22-L38), [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L69-L86), and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L106-L123).

The authentication code is implemented, but it only runs as part of the payment flows, which are not implemented. There is currently nothing to authenticate against.

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **API Key** and **Merchant ID** ready.
3. If the activation flow asks you to select payment methods, choose only the methods enabled for your connector account.

To connect AbsaSanlam to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what AbsaSanlam supports.

You can create the connector account, but payments against it will fail until the payment flows are implemented.

### Webhooks

The connector's webhook code is implemented (HMAC-SHA256 over the raw body via the `X-Signature` header, verified with the connector `merchant_secret`), but it has no payments to report on: webhooks update payment attempts, and no payment attempt can be created through this connector. Do not rely on AbsaSanlam webhooks until the payment flows are implemented.

Two further gaps for when payments do work: `dispute.opened` is mapped in the event type code, but the dispute details extraction (`get_dispute_details`) is not implemented, so dispute events cannot be processed. And the wire values below come from the connector's own type definitions and tests, not from captured AbsaSanlam callbacks; treat them as the expected shape rather than a verified external contract. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L303-L329) and [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L353-L378).

Expected event wire values:

| Wire value | Effect |
|---|---|
| `payment.succeeded` | Payment succeeds |
| `payment.failed` | Payment fails |
| `dispute.opened` | Not processable: dispute details extraction is not implemented |

The wire values come from [`AbsaSanlamWebhookEventType`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam/transformers.rs#L60-L68); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs#L353-L378).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [AbsaSanlam connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam.rs) and [AbsaSanlam transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/absa_sanlam/transformers.rs).
