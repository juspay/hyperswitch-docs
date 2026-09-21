---
description: Connect Boku through Hyperswitch.
metaLinks:
  alternates:
    - boku.md
---

# Boku

{% hint style="warning" %}
**Alpha connector.** Boku is at alpha integration status and has no production configuration: the connector is defined in the sandbox and development configs only. Manual capture is declared but not implemented, and webhooks are not implemented at all.

If you want to use this connector, reach out on the [Slack Community](https://inviter.co/hyperswitch-slack) first so someone on the Hyperswitch team can tell you where it stands.
{% endhint %}

Boku reaches mobile wallets across Southeast and East Asia: DANA and GoPay in Indonesia, GCash in the Philippines, KakaoPay in Korea, and MoMo in Vietnam. Each pays in its own local currency, refunds are supported, and a saved wallet cannot be reused for a later payment.

To connect Boku to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.


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

Supply **API KEY** and **MERCHANT ID**, the labels shown in the Hyperswitch control center. Those are the only two credentials Boku authenticates with: [`BokuAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku/transformers.rs#L219-L235) accepts a `BodyKey` pair and rejects every other shape. Hyperswitch signs each request from them in [`build_headers()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L94-L113), so you do not assemble a signature yourself.

The control center also shows a **Source verification key** field. It is not a credential: the configuration files list it under webhook details rather than connector authentication, and because Boku webhooks are not implemented, a value there does nothing today. Leave it blank.

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Enter **API KEY** and **MERCHANT ID** during connector activation, and leave **Source verification key** blank.
3. Enable only the wallets your Boku account covers, and select automatic capture.
4. Expect sandbox only. Boku has no entry in the production configuration, so there is no production base URL to point at yet.

### Webhooks

Boku webhooks are not supported, so there is no event list and nothing to configure. Use payment sync and refund sync for status updates.

All three incoming-webhook handlers return `WebhooksNotImplemented`: [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L644-L649), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L651-L657), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs#L659-L665).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Boku connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku.rs) and [Boku transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/boku/transformers.rs).
