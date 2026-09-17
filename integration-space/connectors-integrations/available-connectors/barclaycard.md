---
description: Accept card and wallet payments through BarclayCard SmartPay Fuse.
---

# BarclayCard SmartPay Fuse

BarclayCard SmartPay Fuse combines card acceptance with Apple Pay and Google Pay. Card routes support optional 3DS, refunds, and multiple capture choices. Mandate reuse is not declared for these payment routes.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 9e5dd70d1cb4011bbcca3114862406008a0b61f8; host http://localhost:8080; fetched 2026-09-17; matrix canonical-json-v1 sha256 25db1ecc45c5b9c7; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

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

Supply **Key**, **Merchant ID**, and **Shared Secret**, the labels shown in the Hyperswitch control center. Hyperswitch Base64-decodes the Shared Secret, signs the ordered `host`, `date`, request-target, optional digest, and Merchant ID lines with HMAC-SHA256, then Base64-encodes the result. It sends the Key as `keyid` inside the `Signature` header and the Merchant ID in `v-c-merchant-id`; POST and PUT requests also carry a SHA-256 `Digest` header. See [`BarclaycardAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs#L51-L75), [`generate_signature()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L92-L132), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L159-L215).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Enter **Key**, **Merchant ID**, and **Shared Secret** during connector activation.
3. Enable only the card and wallet methods available on your connector account.

To connect BarclayCard SmartPay Fuse to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

### Webhooks

BarclayCard SmartPay Fuse webhooks are not supported. Use payment sync and refund sync for status updates. [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1520-L1525), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1527-L1533), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1535-L1541) each return `WebhooksNotImplemented`.

### Source reference

Authentication and webhook behavior on this page follows [BarclayCard connector source](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs) and [BarclayCard transformers](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs).
