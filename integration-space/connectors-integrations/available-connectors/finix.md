---
description: Finix connector for payment gateway.
metaLinks:
  alternates:
    - finix.md
---

# Finix

Finix supports Apple Pay, Google Pay, debit cards, and credit cards. Refunds, mandates, and manual capture are declared for its payment methods.

To connect Finix to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Finix supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fd; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

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

Supply Merchant Id and Merchant Identity Id. The dashboard labels come from the connector configuration; implementation details are defined in the connector source.

### Before you start

Finix is available in the control center connector list. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

The matrix declares no webhook flow, but the handler processes authorization, transfer, dispute, and evidence payloads. It maps authorization states to authorization, processing, cancellation, or failure events; debit transfers to payment events; reversal transfers to refund events; and dispute states to dispute events. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix/transformers.rs#L779-L848).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Finix connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/finix.rs) and [Finix transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/transformers.rs).
