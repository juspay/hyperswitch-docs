---
description: Connect Finix through Hyperswitch.
metaLinks:
  alternates:
    - finix.md
---

# Finix

Finix supports Apple Pay, Google Pay, debit cards, and credit cards. Refunds, mandates, and manual capture are declared for its payment methods.

To connect Finix to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Finix supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual | not supported | American Express, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 249 | 160 |
| card | Debit Card | supported | supported | automatic, manual | not supported | American Express, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 249 | 160 |
| wallet | Apple Pay | supported | supported | automatic, manual | not applicable | - | - | CAD, USD |
| wallet | Google Pay | supported | supported | automatic, manual | not applicable | - | 221 | CAD, USD |


{% hint style="warning" %}
Finix rejects 3DS card payments outright. A card request sent with the authentication type set to 3DS fails with a "not supported" error before anything reaches Finix. See [the guard in `FinixPaymentsRequest`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L133-L144). The table's "3DS: not supported" means the connector errors on 3DS attempts rather than falling back to non-3DS, so route cards to another connector if your profile enables 3DS.
{% endhint %}

### Authentication

Finix needs four credentials, not two. Enter **Username**, **Password**, **Merchant Id**, and **Merchant Identity Id**; activation will not complete without all four. The labels come from [`[finix.connector_auth.MultiAuthKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml#L8341-L8345).

They are not used the same way. **Username** and **Password** are combined as `username:password`, base64-encoded, and sent as HTTP Basic authentication in the `Authorization` header. See [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs#L307-L328). **Merchant Id** and **Merchant Identity Id** are not authentication values: they travel in the request body as the `merchant` and `merchant_identity` fields, so a wrong value there fails the payment rather than the login. The mapping is [`FinixAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L511-L529).

### Before you start

Finix is available in the control center connector list. Have the four credentials from the Authentication section ready before configuring the connector.

Cards and wallets both go through Finix's own tokenization step, so the payment must carry a Finix token rather than raw or decrypted payment data. Wallet flows that hand Hyperswitch decrypted data are not supported: Apple Pay in Simplified mode, Google Pay decrypt, and Paze each fail with an unimplemented error ([`FinixPaymentsRequest`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L146-L164)). Configure Apple Pay and Google Pay for the tokenized path.

### Webhooks

The matrix declares no webhook flow, but the handler processes authorization, transfer, dispute, and evidence payloads. It maps authorization states to authorization, processing, cancellation, or failure events; debit transfers to payment events; reversal transfers to refund events; and dispute states to dispute events. Evidence payloads are recognized but return `EventNotSupported`, so they apply no update. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L779-L848).

Unlike the event mapping, webhook verification is configured rather than automatic. Set **Source verification key** on the connector, the label from [`[finix.connector_webhook_details]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml#L8505-L8506), to the signing secret Finix issues. Callbacks are then verified with HMAC-SHA256: Hyperswitch reads the `Finix-Signature` header, which carries comma-separated `key=value` pairs including a timestamp and a hex signature, and checks the signature over `timestamp:body`. See [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs#L1159-L1173) and [`decode_finix_signature()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs#L1103-L1139).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Finix connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs) and [Finix transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs).
