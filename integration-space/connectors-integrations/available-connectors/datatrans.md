---
description: Datatrans connector for payment gateway.
metaLinks:
  alternates:
    - datatrans.md
---

# Datatrans

Datatrans supports credit and debit card payments with refunds, mandates, manual capture, and optional 3DS. It covers a broad European country set and multiple currencies.

To connect Datatrans to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Datatrans supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 49 | 26 |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 49 | 26 |


### Authentication

Supply **datatrans MerchantId** and **Passcode**, the two labels the control center shows. Both are required: [`DatatransAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/datatrans/transformers.rs#L449-L460) takes them as a `BodyKey` pair and rejects any other shape, and the labels come from [`[datatrans.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml).

The form also offers **Acquirer Bin** and **Acquirer Merchant ID**. Both are marked optional in the connector configuration, and the Datatrans connector reads neither, so leave them blank unless the Hyperswitch team tells you otherwise.

### Before you start

1. Obtain your **datatrans MerchantId** and **Passcode** from Datatrans.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) and open Datatrans, which is offered in the connector list.
3. Enter both credentials during connector activation.

### Webhooks

Webhooks are not supported, so there is no event list and nothing to configure. All three handlers return `WebhooksNotImplemented`: [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/datatrans.rs#L782-L787), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/datatrans.rs#L789-L795) and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/datatrans.rs#L797-L803).

Use payment sync and refund sync for status instead. Both are implemented, unlike the webhook handlers.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Datatrans connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/datatrans.rs) and [Datatrans transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/datatrans/transformers.rs).
