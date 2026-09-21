---
description: Connect Celero through Hyperswitch.
metaLinks:
  alternates:
    - celero.md
---

# Celero

Celero gives merchants a payment gateway integration in Hyperswitch. It declares card support in the capability block below, with method-specific capture, refund, mandate, region, and currency details there. Use the status and webhook declaration in that block when deciding whether to enable it.

To connect Celero to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

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

Celero requires a single credential, the **Celero API Key**, which Celero provides when you set up your account with them at [https://celerocommerce.com/](https://celerocommerce.com/). It is sent as the `Authorization` header value on every API request (no `Bearer` prefix). Enter it through the connector configuration form in the control center — see [`CeleroAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero/transformers.rs#L358-L373) and the [auth header construction](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero.rs#L119-L130) in the connector source.

### Before you start

1. Set up a Celero account at [https://celerocommerce.com/](https://celerocommerce.com/) to obtain the Celero API Key.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Open the connector configuration form and provide the fields named in Authentication.
4. Use the configured base URL for the environment you are enabling.

### Webhooks

Webhooks are **not supported** for Celero — the connector does not implement incoming webhook handling, so there are no callbacks to configure or verify. To track payment status, use the payment sync (status check) API through Hyperswitch, or query Celero's API directly. See the [webhook interface stubs](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero.rs#L707-L731) in the connector source.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Celero connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero.rs) and [Celero transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/celero/transformers.rs).
