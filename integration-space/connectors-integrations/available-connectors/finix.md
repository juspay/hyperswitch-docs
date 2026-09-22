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


### Authentication

Finix needs four credentials, not two. Enter **Username**, **Password**, **Merchant Id**, and **Merchant Identity Id**; activation will not complete without all four. The labels come from [`[finix.connector_auth.MultiAuthKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml#L8341-L8345).

They are not used the same way. **Username** and **Password** are combined as `username:password`, base64-encoded, and sent as HTTP Basic authentication in the `Authorization` header — see [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs#L307-L328). **Merchant Id** and **Merchant Identity Id** are not authentication values: they travel in the request body as the `merchant` and `merchant_identity` fields, so a wrong value there fails the payment rather than the login. The mapping is [`FinixAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L511-L529).

### Before you start

Finix is available in the control center connector list. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

The matrix declares no webhook flow, but the handler processes authorization, transfer, dispute, and evidence payloads. It maps authorization states to authorization, processing, cancellation, or failure events; debit transfers to payment events; reversal transfers to refund events; and dispute states to dispute events. Evidence payloads are recognized but return `EventNotSupported`, so they apply no update. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L779-L848).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Finix connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs) and [Finix transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs).
