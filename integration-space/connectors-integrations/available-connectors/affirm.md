---
description: Offer Affirm pay later payments.
metaLinks:
  alternates:
    - affirm.md
---

# Affirm

Offer Affirm pay later payments in USD through a direct connection to Affirm. Checkout is a redirect: the customer completes the Affirm checkout and returns to Hyperswitch, which then confirms the transaction. Payments support sequential automatic or manual capture, and refunds are supported. Mandates are not supported.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** beta

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| pay later | Affirm | not supported | supported | sequential automatic, manual | - | USD |

The Countries column is empty because the direct Affirm connector's payment method filter restricts currency to USD but sets no country. Hyperswitch calls Affirm's US API (`api.affirm.com`), so use this connector for US Affirm merchant accounts. See the [payment method filter](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/production.toml#L420-L421) and the [production base URL](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/production.toml#L40).

### Authentication

Supply a **Public Key** and **Private Key**. Hyperswitch joins them in that order as `<Public Key>:<Private Key>`, Base64-encodes the pair, and sends `Authorization: Basic <encoded value>`. See [`AffirmAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/affirm/transformers.rs#L215-L230), [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/affirm.rs#L90-L107), and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/affirm.rs#L127-L144).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Get your **Public Key** and **Private Key** from **API keys** in the Affirm merchant portal: [sandbox](https://sandbox.affirm.com/dashboard/apikeys) or [production](https://www.affirm.com/dashboard/apikeys). Keep the Private Key server-side only. See [Affirm API keys](https://docs.affirm.com/developers/docs/api-keys).

To connect Affirm to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Affirm supports.

### Webhooks

Affirm webhooks are not supported. Use payment sync and refund sync for status updates. The connector's webhook handlers all return `WebhooksNotImplemented`; see [`IncomingWebhook for Affirm`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/affirm.rs#L797-L821).

### Source reference

Checkout, authentication, and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Affirm connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/affirm.rs) and [Affirm transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/affirm/transformers.rs).
