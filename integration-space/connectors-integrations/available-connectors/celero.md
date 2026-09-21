---
description: Connect Celero through Hyperswitch.
metaLinks:
  alternates:
    - celero.md
---

# Celero

Celero lets merchants route credit and debit card payments through its API. Celero is not offered in the Hyperswitch control center, so contact the Hyperswitch team to arrange setup instead of looking for a Celero activation form. Payment status should be checked through payment sync because Celero does not implement incoming webhooks.

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

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | - | - |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | - | - |

### Authentication

Celero requires one credential: the **Celero API Key**, obtained when you set up an account at [https://celerocommerce.com/](https://celerocommerce.com/). The key is sent as the `Authorization` header value without a `Bearer` prefix. The dashboard label is defined in [`[celero.connector_auth.HeaderKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml#L7256-L7258); the accepted auth shape is [`CeleroAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero/transformers.rs#L358-L373), and the header is built in [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero.rs#L118-L129).

### Before you start

1. Set up a Celero account at [https://celerocommerce.com/](https://celerocommerce.com/) and obtain the **Celero API Key**.
2. Contact the Hyperswitch team to configure Celero because it is not listed in the control center.

### Webhooks

Webhooks are **not supported** for Celero — the connector does not implement incoming webhook handling, so there are no callbacks to configure or verify. To track payment status, use the payment sync (status check) API through Hyperswitch, or query Celero's API directly. See the [webhook interface stubs](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero.rs#L707-L731) in the connector source.

### Source reference

Authentication, dashboard availability, and webhook behavior on this page are tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Celero connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero.rs) and [Celero transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero/transformers.rs).
