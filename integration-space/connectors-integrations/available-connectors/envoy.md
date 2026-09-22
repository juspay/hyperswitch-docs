---
description: >-
  Envoy is a payout processor. It is registered as a payment gateway connector, but
  its payment-side flows are not implemented.
metaLinks:
  alternates:
    - envoy.md
---

# Envoy

{% hint style="warning" %}
**Envoy is a payout processor.** Although Envoy is registered as a payment gateway connector, its payment-side flows are unimplemented stubs: the connector declares no payment methods, and every payment flow (authorize, sync, capture, refund) fails with a "not implemented" error. What Envoy actually implements is payouts — it is one of the [`PayoutConnectors`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/api_models/src/enums.rs#L48-L70), and payout fulfillment has a working implementation. Use Envoy through [Hyperswitch Payouts](../payouts/README.md), not for accepting payments.
{% endhint %}

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

_This connector declares no payment methods. Its payment flows are stubs; see the warning above._

### Authentication

Envoy requires two credentials, which Envoy provides when you set up your account with them: **Username** and **Password**. Both are sent with each API request as body-key fields — see [`EnvoyAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy/transformers.rs#L83-L98) in the connector source. The labels come from [`[envoy_payout.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml#L8731-L8733); note that the configuration key is `envoy_payout`, because Envoy is registered for payouts rather than payments.

### Before you start

1. Set up an Envoy account and obtain the **Username** and **Password**.
2. Envoy is not offered in the control-center payment connector list (it appears only as a payout connector), so contact the Hyperswitch team to arrange setup.
3. Configure Envoy as a payout connector and initiate payouts through [Hyperswitch Payouts](../payouts/README.md). Payout fulfillment is the only implemented flow; see the note under Webhooks.

### Webhooks

Webhooks are not currently supported. All three webhook handlers return `WebhooksNotImplemented`; see [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy.rs#L675-L698).

Payout status cannot be tracked through Hyperswitch either. Of the payout flows, only fulfillment is implemented: [payout create](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy.rs#L86-L98) returns a not-implemented error for the eligibility check, and payout sync has no implementation at all, so it never reaches Envoy. Check payout status with Envoy directly.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Envoy connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy.rs) and [Envoy transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/envoy/transformers.rs).
