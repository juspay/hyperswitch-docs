---
description: Connect Boku through Hyperswitch.
metaLinks:
  alternates:
    - boku.md
---

# Boku

{% hint style="warning" %}
**Boku cannot be set up from the control center.** The dashboard keeps its own list of connectors, and Boku is not in it, so Boku does not appear at app.hyperswitch.io in any mode and there is no activation form to fill in. The connector itself exists in the router and is configured for sandbox, so talk to the Hyperswitch team about how to enable it.

Boku is also at alpha integration status, with two gaps worth knowing before you build on it: manual capture is declared but not implemented, and webhooks are not implemented at all.

If you want to use this connector, reach out on the [Slack Community](https://inviter.co/hyperswitch-slack) first so someone on the Hyperswitch team can tell you where it stands.
{% endhint %}

Boku reaches mobile wallets across Southeast and East Asia: DANA and GoPay in Indonesia, GCash in the Philippines, KakaoPay in Korea, and MoMo in Vietnam. Each pays in its own local currency, refunds are supported, and a saved wallet cannot be reused for a later payment.

The shared [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md) guide does not apply here, because it begins by picking a connector in the control center and Boku is not offered there. See Before you start below.


### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** alpha

**Category:** alternative payment method

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| wallet | DANA | not supported | supported | automatic, manual, sequential automatic | IDN | IDR |
| wallet | GCash | not supported | supported | automatic, manual, sequential automatic | PHL | PHP |
| wallet | GoPay | not supported | supported | automatic, manual, sequential automatic | IDN | IDR |
| wallet | KakaoPay | not supported | supported | automatic, manual, sequential automatic | KOR | KRW |
| wallet | MoMo | not supported | supported | automatic, manual, sequential automatic | VNM | VND |

The feature matrix declares manual capture, but the capture flow is not implemented: [`get_url()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L400-L406) and [`get_request_body()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L408-L414) both return `NotImplemented`, and [`build_request()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L416-L434) calls them, so a capture request fails before it is sent. Use automatic capture.

### Authentication

Boku authenticates with two credentials, named **API KEY** and **MERCHANT ID** in the connector configuration. Those are the only two: [`BokuAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku/transformers.rs#L219-L235) accepts a `BodyKey` pair and rejects every other shape. Hyperswitch signs each request from them in [`build_headers()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L94-L113), so you do not assemble a signature yourself.

The connector configuration carries a third field, **Source verification key**, which is not a credential: it sits under webhook details rather than connector authentication, and because Boku webhooks are not implemented, it has no effect. Nothing needs to be supplied for it.

### Before you start

Boku is not offered in the control center, so the usual activation flow does not apply. Work through the Hyperswitch team instead, and have the following ready.

1. Your Boku **API KEY** and **MERCHANT ID**. Those are the only two credentials the connector authenticates with.
2. The wallets your Boku account covers, from DANA, GCash, GoPay, KakaoPay and MoMo.
3. Automatic capture. Manual capture is declared in the matrix but not implemented, so do not plan around it.

You will not be asked for a source verification key. It is a webhook field, and Boku webhooks are not implemented.

### Webhooks

Boku webhooks are not supported, so there is no event list and nothing to configure. Refund sync is available for refund status. Payment sync is not implemented, so do not rely on it for payment status.

All three incoming-webhook handlers return `WebhooksNotImplemented`: [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L644-L649), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L651-L657), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L659-L665).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Boku connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs) and [Boku transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku/transformers.rs).
