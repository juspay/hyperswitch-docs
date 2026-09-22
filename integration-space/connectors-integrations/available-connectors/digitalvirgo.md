---
description: Digital Virgo connector for alternative payment method.
metaLinks:
  alternates:
    - digitalvirgo.md
---

# Digital Virgo

Digital Virgo supports direct carrier billing for mobile payments. Refunds and automatic capture are declared, while mandates are not supported.

To connect Digital Virgo to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Digital Virgo supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fd; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** alpha

**Category:** alternative payment method

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| mobile payment | Direct Carrier Billing | not supported | supported | automatic, sequential automatic | 48 | 37 |

{% hint style="warning" %}
Although the capability table lists sequential automatic capture, the connector does not implement the capture flow — capture requests return a "flow not supported" error. Only **automatic** capture works with Digital Virgo.
{% endhint %}

### Authentication

Digital Virgo requires two credentials, which Digital Virgo provides when you set up your account with them: **Username** and **Password**. Both are sent with each API request as body-key authentication — see [`DigitalvirgoAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo/transformers.rs#L86-L102) in the connector source.

### Before you start

Dashboard setup is not offered for this connector in the current connector list; contact the Hyperswitch team. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

Webhooks are not currently supported. All three webhook handlers return `WebhooksNotImplemented`; see [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L524-537).

Payment status can be tracked through the payment sync (status check) API, which Digital Virgo implements against its payment state endpoint. Refund status cannot be synced through Hyperswitch: refund sync is not implemented, so refunds marked supported in the table above must be reconciled with Digital Virgo out of band. See the [payment sync implementation](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L314-L354) and the [refund sync stub](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L501-L512) in the connector source.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Digital Virgo connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs) and [Digital Virgo transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo/transformers.rs).
