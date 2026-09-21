---
description: Connect Cryptopay through Hyperswitch.
metaLinks:
  alternates:
    - cryptopay.md
---

# Cryptopay

Cryptopay gives merchants a payment gateway integration in Hyperswitch. It declares crypto support in the capability block below, with method-specific capture, refund, mandate, region, and currency details there. Use the status and webhook declaration in that block when deciding whether to enable it.

To connect Cryptopay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

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

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | not supported | automatic, sequential automatic | - | - |

### Authentication

The control-center configuration exposes these connector fields: API Key; Secret Key; Source verification key. Enter them through the connector configuration form. Authentication transport and flow-specific headers are implemented in [`Cryptopay connector source`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs#L91-L181) and the [`Cryptopay transformers`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay/transformers.rs#L1-L20).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Open the connector configuration form and provide the fields named in Authentication.
3. Use the configured base URL for the environment you are enabling.

### Webhooks

The matrix declares a payments webhook flow. Event names, source verification, and handler outcomes are tied to the connector source and should be verified before relying on callbacks. The exact event list and verification mechanism require code-level review of [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs#L477-L505) and the connector transformers before callbacks are used as payment confirmation.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Cryptopay connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs) and [Cryptopay transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay/transformers.rs).
