---
description: Connect Coingate through Hyperswitch.
metaLinks:
  alternates:
    - coingate.md
---

# Coingate

Coingate gives merchants an alternative payment method integration in Hyperswitch. It declares crypto support in the capability block below, with method-specific capture, refund, mandate, region, and currency details there. Use the status and webhook declaration in that block when deciding whether to enable it.

To connect Coingate to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** alternative payment method

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | supported | automatic, sequential automatic | 59 | EUR, GBP, USD |

{% hint style="warning" %}
Although the capability table lists sequential automatic capture, the connector does not implement the capture flow — capture requests return a "flow not supported" error. Only **automatic** capture works with CoinGate.
{% endhint %}

### Authentication

Enter the connector credentials **API Key** and **Merchant Token**. The API key is sent as `Authorization: Bearer <API key>`; the merchant token is used to verify CoinGate webhook requests. These labels come from [`[coingate.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml); the auth mapping is [`CoingateAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate/transformers.rs#L119-L135), and the header is built in [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate.rs#L122-L133).

### Refund metadata

Refunds require three additional values in the connector metadata — `currency_id`, `platform_id`, and `ledger_account_id` — which are consumed by refund requests, not authentication. They are not currency-scoped credentials. See [`CoingateConnectorMetadataObject`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate/transformers.rs#L38-L42).

### Before you start

1. Create or sign in to your CoinGate account and obtain the **API Key** and **Merchant Token**.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) and open CoinGate.
3. Enter the two connector credentials.

No provider dashboard path beyond account setup was verified for this page.

### Webhooks

CoinGate maps webhook statuses to payment outcomes: `Pending` becomes processing, `Confirming` and `New` require payment action, `Paid` succeeds, and `Invalid`, `Expired`, and `Canceled` fail. It verifies the webhook by comparing the request token with the configured **Merchant Token**. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate.rs#L569-L595) and [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate.rs#L596-L618).

### Source reference

Authentication, refund metadata, capture, and webhook behavior on this page are tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Coingate connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate.rs) and [Coingate transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/coingate/transformers.rs).
