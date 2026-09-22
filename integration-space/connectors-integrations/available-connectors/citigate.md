---
description: Connect Citigate through Hyperswitch.
metaLinks:
  alternates:
    - citigate.md
---

# Citigate

Citigate appears in the Hyperswitch control center, but it is not currently usable for payment processing: its payment request conversion returns `NotImplemented`, including for cards. Do not activate Citigate for live payment traffic until the connector implements a payment method and the Hyperswitch team confirms setup.

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

_This connector declares no payment methods. It is a payment gateway rather than a payment processor._

The feature matrix declares live status but no payment-method rows. The connector implementation also does not process payments, so the live label does not mean a merchant can send a payment through Citigate.


### Authentication

Citigate takes two credentials, shown in the control center as **Merchant Name** and **Merchant Password**, from [`[citigate.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml#L9145-L9147).

[`CitigateAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate/transformers.rs#L65-L85) accepts them as a `BodyKey` pair and rejects any other shape. Only the first is sent in `Authorization` by [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs#L121-L132), with the remaining transport headers assembled by [`build_headers()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs#L82-L95).

Citigate is a UCS-only connector: Hyperswitch forwards the credentials to the Unified Connector Service rather than calling Citigate directly, which the source notes alongside the auth type. None of this is reachable today, since no payment method is implemented.

### Before you start

1. Do not enable Citigate for payment processing; the pinned connector does not implement payment requests.
2. Contact the Hyperswitch team if you need to track the implementation or request setup.

No provider registration URL or dashboard credential path was verified for this page.

### Webhooks

Citigate does not support incoming webhooks. The object-reference, event-type, and resource handlers all return `WebhooksNotImplemented`, so there are no events or source-verification steps to configure. See [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs#L568-L587).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Citigate connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs) and [Citigate transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate/transformers.rs).
