---
description: Connect Breadpay through Hyperswitch.
metaLinks:
  alternates:
    - breadpay.md
---

# Breadpay

Breadpay gives merchants a pay-later redirect flow through Hyperswitch. The connector is in alpha, so confirm availability with the Hyperswitch team before using it in production. Payment status is retrieved through the API because Breadpay does not implement incoming webhooks.

To connect Breadpay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

This connector is in alpha status. Check with the Hyperswitch team before enabling it in production.


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

### Authentication

Enter the control-center fields **API Key** and **API Secret**. Breadpay sends them as HTTP Basic authentication in the `Authorization` header; the header builder also adds `Content-Type: application/json`. See [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L134-L148) and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L99-L110). The control-center labels come from [`[breadpay.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml#L7898-L7901).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Open Breadpay in the connector configuration form.
3. Enter the **API Key** and **API Secret** from your Breadpay account.

No provider registration URL was verified for this page.

### Webhooks

Breadpay does not support incoming webhooks. The object-reference, event-type, and resource handlers all return `WebhooksNotImplemented`, so use payment API syncs for status instead of waiting for callbacks. See [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs#L780-L804).

### Source reference

Authentication, capture, and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Breadpay connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay.rs) and [Breadpay transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/breadpay/transformers.rs).
