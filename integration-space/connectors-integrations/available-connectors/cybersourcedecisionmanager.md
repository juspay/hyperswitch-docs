---
description: Cybersource Decision Manager runs fraud screening. It does not process payments.
metaLinks:
  alternates:
    - cybersourcedecisionmanager.md
---

# Cybersource Decision Manager

{% hint style="warning" %}
**This connector does not process payments.** Decision Manager is Cybersource's fraud screening service, and that is all this connector implements. The matrix labels it a live payment gateway, which is a declaration rather than a capability.
{% endhint %}

Cybersource Decision Manager screens transactions for fraud. Only the fraud-check flows are implemented, [checkout](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L439) and [transaction](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L533). Every payment flow behind the block is an empty implementation: [`Authorize`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L405-L408), [`PSync`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L410-L413), [`Capture`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L414-L417), [`Void`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L419-L422), refund [`Execute`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L424-L427) and [`RSync`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L429) all fall through to the interface default, which builds no request. Sending a payment to this connector does nothing.

It is also not offered in the control center, so there is no activation form and the shared activation guide does not apply. Arrange setup with the Hyperswitch team.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

_This connector declares no payment methods. It is a payment gateway rather than a payment processor._


### Authentication

The connector accepts three credentials as a `SignatureKey` triple, mapped by [`CybersourcedecisionmanagerAuthType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager/transformers.rs#L68-L92): an API key, a merchant account, and an API secret.

There are no control-center labels to quote for them. Cybersource Decision Manager has no entry in `crates/connector_configs/toml/`, in any environment, which is the same reason it does not appear in the connector list. Ask the Hyperswitch team which values to supply and in what form.

### Before you start

Contact the Hyperswitch team. There is no dashboard setup for this connector, and no connector configuration defines its credential labels, so there is nothing to prepare in the control center. Have your Cybersource Decision Manager account details to hand for that conversation.

### Webhooks

Webhooks are not supported, so there is no event list and nothing to configure. All three handlers return `WebhooksNotImplemented`: [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L630-L635), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L637-L643) and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs#L645-L650).

There is nothing to fall back on either, since the payment and sync flows are unimplemented too. This connector reports no status of its own.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Cybersource Decision Manager connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager.rs) and [Cybersource Decision Manager transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/cybersourcedecisionmanager/transformers.rs).
