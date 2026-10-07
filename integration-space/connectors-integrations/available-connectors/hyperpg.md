---
description: Configure HyperPG card payments with Hyperswitch.
metaLinks:
  alternates:
    - hyperpg.md
---

# HyperPG

HyperPG processes credit and debit card payments through Hyperswitch. Its routes support mandates, refunds, automatic capture, and optional 3DS. The connector is not available for self-service setup in the control center.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, INR, USD |
| card | Debit Card | supported | supported | automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, INR, USD |


### Authentication

The sandbox form defines **Username** and **Password** ([`hyperpg.connector_auth.BodyKey`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L8089-L8091)), while [`HyperpgAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/hyperpg/transformers.rs#L72-L88) also requires merchant ID. Contact the Hyperswitch team for a path that supplies all three values.

### Before you start

HyperPG is absent from the control center list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)) and from the rendered connector screen. Contact the Hyperswitch team instead of attempting self-service activation.

### Webhooks

HyperPG webhooks are not supported. Payment sync and refund sync cannot build a URL, so check status in the provider portal. See [`IncomingWebhook for Hyperpg`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/hyperpg.rs#L561-L585), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/hyperpg.rs#L263-L326), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/hyperpg.rs#L493-L559).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [HyperPG connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/hyperpg.rs) and [HyperPG transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/hyperpg/transformers.rs).
