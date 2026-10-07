---
description: Configure GivePayments card payments with Hyperswitch.
metaLinks:
  alternates:
    - givepayments.md
---

# GivePayments

{% hint style="warning" %}
**Alpha connector.** Confirm current availability with the Hyperswitch team before relying on GivePayments in production.
{% endhint %}

GivePayments processes credit and debit card payments through Hyperswitch. Its card routes support mandates and refunds with automatic capture. 3DS is not supported for either route.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | supported | supported | automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | - | - |


### Authentication

Provide the **API Key** from [`givepayments.connector_auth.HeaderKey`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L9217-L9218); [`GivepaymentsAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/givepayments/transformers.rs#L72-L82) maps it. The form also shows **Source verification key**, but webhooks are not implemented, so it is unused and can be left blank ([`givepayments.connector_webhook_details`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L9219-L9220)).

### Before you start

GivePayments appears in the control center list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). Confirm alpha availability with the Hyperswitch team, then follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).

### Webhooks

GivePayments webhooks are not supported. Payment sync and refund sync cannot build a URL, so check status in the provider portal. See [`IncomingWebhook for Givepayments`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/givepayments.rs#L573-L597), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/givepayments.rs#L273-L336), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/givepayments.rs#L505-L571).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [GivePayments connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/givepayments.rs) and [GivePayments transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/givepayments/transformers.rs).
