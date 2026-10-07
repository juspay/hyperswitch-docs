---
description: Configure Deutsche Bank card and SEPA Direct Debit payments with Hyperswitch.
metaLinks:
  alternates:
    - deutschebank.md
---

# Deutsche Bank

Deutsche Bank supports card acquisition and SEPA Direct Debit through Hyperswitch. Card payments require 3DS, while SEPA Direct Debit supports mandate-based payments. Refund and capture options are listed by payment route below.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
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
| bank debit | SEPA Direct Debit | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | required | Mastercard, Visa | - | - |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | required | Mastercard, Visa | - | - |


### Authentication

Provide the **Client ID**, **Merchant ID**, and **Client Key** shown in the connector form. The labels come from [`deutschebank.connector_auth.SignatureKey`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L2362-L2365), and [`DeutschebankAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/deutschebank/transformers.rs#L59-L95) maps all three values.

### Before you start

Deutsche Bank appears in the control center payment-processor list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). Have all three credentials ready. Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector behavior.

### Webhooks

Deutsche Bank webhooks are not supported. The webhook methods return `WebhooksNotImplemented`; use payment sync for payment status and refund sync for refund status. See [`IncomingWebhook for Deutschebank`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/deutschebank.rs#L985-L1009), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/deutschebank.rs#L577-L648), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/deutschebank.rs#L916-L983).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [Deutsche Bank connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/deutschebank.rs) and [Deutsche Bank transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/deutschebank/transformers.rs).
