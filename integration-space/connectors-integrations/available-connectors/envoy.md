---
description: Envoy connector for payment gateway.
metaLinks:
  alternates:
    - envoy.md
---

# Envoy

{% hint style="warning" %}
**Envoy is a payout processor.** Although Envoy is registered as a payment gateway connector, its payment-side flows are unimplemented stubs: the connector declares no payment methods, and every payment flow (authorize, sync, capture, refund) fails with a "not implemented" error. What Envoy actually implements is payouts — it is one of the [`PayoutConnectors`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/api_models/src/enums.rs#L48-L70), and payout fulfillment has a working implementation. Use Envoy through [Hyperswitch Payouts](../payouts/README.md), not for accepting payments.
{% endhint %}

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fd; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

_This connector declares no payment methods. Its payment flows are stubs; see the warning above._

### Authentication

Envoy requires two credentials, which Envoy provides when you set up your account with them: **Username** and **Password**. Both are sent with each API request as body-key fields — see [`EnvoyAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy/transformers.rs#L83-L98) in the connector source.

### Before you start

1. Set up an Envoy account and obtain the **Username** and **Password**.
2. Envoy is not offered in the control-center payment connector list (it appears only as a payout connector), so contact the Hyperswitch team to arrange setup.
3. Configure Envoy as a payout connector and initiate payouts through the [Payouts API](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts). Note that payout create eligibility checks are not implemented; the working flow is payout fulfillment.

### Webhooks

Webhooks are not currently supported. All three webhook handlers return `WebhooksNotImplemented`; see [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy.rs#L683-696). Payout status must be tracked through payout sync or by checking Envoy directly.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Envoy connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy.rs) and [Envoy transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy/transformers.rs).
