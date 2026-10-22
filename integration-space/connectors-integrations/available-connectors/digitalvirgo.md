---
description: Digital Virgo connector for alternative payment method.
metaLinks:
  alternates:
    - digitalvirgo.md
---

# Digital Virgo

Digital Virgo supports direct carrier billing for mobile payments. Refunds and automatic capture are declared, while mandates are not supported.

Digital Virgo is not offered in the control center, so the shared [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md) guide does not apply: it begins by picking a connector from a list this one is not on. See [Before you start](#before-you-start).

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
Although the capability table lists sequential automatic capture, the connector does not implement the capture flow. A capture request returns a flow-not-supported error, so only automatic capture works with Digital Virgo.
{% endhint %}

### Authentication

Digital Virgo requires two credentials, which Digital Virgo provides when you set up your account with them: **Username** and **Password**. They are sent as HTTP Basic authentication, not in the request body: [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L124-L140) joins them as `<username>:<password>`, Base64-encodes the pair, and sends `Authorization: Basic <encoded value>`.

[`DigitalvirgoAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo/transformers.rs#L86-L101) maps them from Hyperswitch's `BodyKey` credential schema, which names how the two values are stored rather than how they reach Digital Virgo.

### Before you start

Dashboard setup is not offered for this connector in the current connector list; contact the Hyperswitch team. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

Webhooks are not supported, so there is no event list and nothing to configure. All three handlers return `WebhooksNotImplemented`: [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L517-L522), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L524-L530) and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L532-L538).

Payment status can be tracked through the payment sync API, which Digital Virgo implements against its payment state endpoint. See the [payment sync implementation](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L314-L354).

Refunds are a different matter. The table above marks them supported, but neither refund flow works: [refund execute](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L487-L499) returns `FlowNotSupported` from `build_request`, so a refund fails before a request is sent, and [refund sync](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs#L501-L512) is unimplemented too. There is nothing to reconcile out of band, because no refund reaches Digital Virgo through Hyperswitch in the first place. 

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Digital Virgo connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo.rs) and [Digital Virgo transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/digitalvirgo/transformers.rs).
