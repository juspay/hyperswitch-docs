---
description: Connect Breadpay through Hyperswitch.
metaLinks:
  alternates:
    - breadpay.md
---

# Breadpay

{% hint style="warning" %}
**Alpha connector.** Breadpay is at alpha integration status, and refunds are declared but not implemented. Reach out on the [Slack Community](https://inviter.co/hyperswitch-slack) to check where it stands before you build on it.
{% endhint %}

Breadpay offers a pay-later redirect: the customer leaves your checkout to arrange financing with Breadpay and returns once it is settled. There are no webhooks, so payment status comes from syncing rather than callbacks.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| pay later | Breadpay | not supported | supported | automatic, manual, sequential automatic | - | - |

The matrix declares refunds, but neither refund flow is implemented: `get_url()` returns `NotImplemented` for [refund execute](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L642-L648) and for [refund sync](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L726-L732), and both `build_request()` implementations call it, so a refund fails before it is sent. Capture is unaffected and works as declared.

### Authentication

Supply **API Key** and **API Secret**, the labels shown in the Hyperswitch control center. Breadpay sends them as HTTP Basic authentication in the `Authorization` header; the header builder also adds `Content-Type: application/json`. See [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L134-L148) and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L99-L110). The labels come from [`[breadpay.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml#L7898-L7901).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Open Breadpay in the connector configuration form.
3. Enter the **API Key** and **API Secret** from your Breadpay account.

To connect Breadpay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

No provider registration URL was verified for this page.

### Webhooks

Breadpay does not support incoming webhooks. The object-reference, event-type, and resource handlers all return `WebhooksNotImplemented`, so use payment API syncs for status instead of waiting for callbacks. See [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L780-L804).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Breadpay connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs) and [Breadpay transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay/transformers.rs).
