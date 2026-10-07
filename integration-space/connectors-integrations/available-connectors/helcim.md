---
description: Configure Helcim card payments with Hyperswitch.
metaLinks:
  alternates:
    - helcim.md
---

# Helcim

Helcim processes credit and debit card payments through Hyperswitch. Its card routes support mandates, refunds, and manual capture. 3DS is not supported.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
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
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | CAN, USA | CAD, USD |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | CAN, USA | CAD, USD |


### Authentication

Provide the **Api Key** from [`helcim.connector_auth.HeaderKey`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L6106-L6107); [`HelcimAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/helcim/transformers.rs#L312-L322) maps it.

### Before you start

Helcim appears in the control center list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). Have the Api Key ready and follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).

### Webhooks

Helcim webhooks are not supported; use payment sync and refund sync for status. See [`IncomingWebhook for Helcim`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/helcim.rs#L816-L840), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/helcim.rs#L389-L477), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/helcim.rs#L732-L814).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [Helcim connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/helcim.rs) and [Helcim transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/helcim/transformers.rs).
