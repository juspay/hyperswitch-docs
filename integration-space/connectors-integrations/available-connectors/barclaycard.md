---
description: Accept card and wallet payments through BarclayCard SmartPay Fuse.
---

# BarclayCard SmartPay Fuse

BarclayCard SmartPay Fuse combines card acceptance with Apple Pay and Google Pay as a bank acquirer connection. Card routes support optional 3DS and refunds, while wallet routes keep the same capture choices. Mandates are not available across the declared methods.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** bank acquirer

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, PLN, SEK, USD |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, PLN, SEK, USD |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 22 |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 23 |

### Authentication

Supply a **Key**, **Merchant ID**, and **Shared Secret**. Hyperswitch Base64-decodes the Shared Secret, signs the ordered `host`, `date`, request-target, optional digest, and merchant ID lines with HMAC-SHA256, then Base64-encodes the result. It sends the Key as `keyid` inside the `Signature` header and the Merchant ID in `v-c-merchant-id`; POST and PUT requests also carry a SHA-256 `Digest` header. See [`BarclaycardAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs#L51-L75), [`generate_signature()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L92-L132), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L159-L215).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **Key**, **Merchant ID**, and **Shared Secret** ready.
3. If activation asks for wallet artifacts, provide them only after the corresponding wallet setup produces them.
4. Choose only the payment methods enabled for your connector account.

To connect BarclayCard SmartPay Fuse to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what BarclayCard SmartPay Fuse supports.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. Object lookup, event classification, and resource parsing each return `WebhooksNotImplemented`; see [`IncomingWebhook for Barclaycard`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1518-L1542).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [BarclayCard SmartPay Fuse connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/barclaycard.rs) and [BarclayCard SmartPay Fuse transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs).
