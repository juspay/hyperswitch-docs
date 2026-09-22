---
description: Facilitapay connector for payment gateway.
metaLinks:
  alternates:
    - facilitapay.md
---

# Facilitapay

Facilitapay supports Pix bank transfers in the sandbox, with refunds and automatic capture. Payment webhook processing is declared.

To connect Facilitapay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Facilitapay supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fd; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank transfer | Pix | not supported | supported | automatic, sequential automatic | BRA | BRL |


### Authentication

Supply Username. The dashboard labels come from the connector configuration; implementation details are defined in the connector source.

### Before you start

Facilitapay is available in the control center connector list. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

Facilitapay maps eight webhook event values: ExchangeCreated, Identified, PaymentApproved, PaymentExpired, PaymentFailed, PaymentRefunded, WireCreated, and WireWaitingCorrection. Source verification compares the notification secret. See [`FacilitapayWebhookEventType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay/responses.rs#L278-L287) and [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs#L879-L908).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Facilitapay connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs) and [Facilitapay transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/transformers.rs).
