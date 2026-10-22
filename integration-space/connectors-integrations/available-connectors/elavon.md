---
description: Connect Elavon through Hyperswitch.
metaLinks:
  alternates:
    - elavon.md
---

# Elavon

Elavon supports debit and credit card payments with refunds, mandates, and manual capture. Card payments are declared without 3DS.

To connect Elavon to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Elavon supports.

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
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | USA | 157 |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | USA | 157 |


### Authentication

Elavon requires three credentials, which Elavon provides when you set up your account with them at [https://www.elavon.com/](https://www.elavon.com/): **Account Id**, **User ID**, and **Pin**. All three are sent with each API request as signature-key fields. See [`ElavonAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/elavon/transformers.rs#L148-L168) in the connector source. The labels come from [`[elavon.connector_auth.SignatureKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml#L6923-L6926).

{% hint style="warning" %}
Elavon rejects 3DS card payments outright. Requests with 3DS enabled fail with a "not supported" error. The capability table's "3DS: not supported" means the connector errors on 3DS attempts, not that it falls back to non-3DS.
{% endhint %}

### Before you start

Elavon is available in the control center connector list. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

Webhooks are not currently supported. All three webhook handlers return `WebhooksNotImplemented`; see [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/elavon.rs#L565-L588).

Since there are no callbacks, track status through the sync APIs: both payment sync and refund sync are implemented for Elavon, so use the payment and refund status check APIs through Hyperswitch to confirm outcomes.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Elavon connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/elavon.rs) and [Elavon transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/elavon/transformers.rs).
