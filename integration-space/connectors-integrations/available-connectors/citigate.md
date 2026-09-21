---
description: Connect Citigate through Hyperswitch.
metaLinks:
  alternates:
    - citigate.md
---

# Citigate

Citigate is available in Hyperswitch for its declared integration category. The capability block below is the source of truth for its current status and declarations. The connector currently declares no payment method rows, so do not infer payment support beyond that declaration.

To connect Citigate to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

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

The feature matrix declares live status but no payment-method rows for Citigate. This declaration gap is left visible rather than padded with unsupported methods; verify the connector implementation before relying on it.


### Authentication

The control-center configuration exposes these connector fields: Merchant Name; Merchant Password. Enter them through the connector configuration form. Authentication transport and flow-specific headers are implemented in [`Citigate connector source`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs#L85-L136) and the [`Citigate transformers`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate/transformers.rs#L1-L20).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Open the connector configuration form and provide the fields named in Authentication.
3. Use the configured base URL for the environment you are enabling.

### Webhooks

The matrix declares no webhook flow; status updates should be checked against the API. The exact event list and verification mechanism require code-level review of [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs#L580-L606) and the connector transformers before callbacks are used as payment confirmation.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Citigate connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate.rs) and [Citigate transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/citigate/transformers.rs).
