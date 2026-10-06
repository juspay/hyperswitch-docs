---
description: Configure Flexiti pay-later payments with Hyperswitch.
metaLinks:
  alternates:
    - flexiti.md
---

# Flexiti

{% hint style="warning" %}
**Alpha connector.** Flexiti is at alpha integration status. The payment status mapping from Flexiti is incomplete: a completed purchase currently reports as authorized rather than captured, so a successful payment may show a `requires_capture` status even though no capture call is needed or possible. Manual capture, refunds, mandates, and webhooks are not supported. Use payment sync to check payment status, and confirm current behavior with the Hyperswitch team before relying on this connector in production.
{% endhint %}

Flexiti provides a redirected pay-later checkout through Hyperswitch. The payment is captured automatically when the customer completes checkout, so no separate capture call is needed. Manual capture is not supported. Refunds and mandates are not available for this payment route.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d03f8547d6367fab56690e4f5043590be4935dcd; host http://127.0.0.1:8080; fetched 2026-10-02; matrix canonical-json-v1 sha256 8b92b42f08eb323a31ea974c99ac67dc4972774ab49bda767a79da9d2992fd5b; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead.
     Manually corrected 2026-10-05: the feature matrix still declares
     manual capture at hyperswitch d03f8547, but Flexiti does not
     support manual capture (confirmed in
     https://github.com/juspay/hyperswitch/issues/14610). The capture
     method and CA/CAD availability below reflect the confirmed
     behavior, not the current matrix output. Regenerate this block
     once the hyperswitch fix lands and the matrix reports automatic
     capture. Countries and currencies come from pm_filters in
     config/development.toml (flexiti = CA, CAD). -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| pay later | Klarna | not supported | not supported | automatic | CA | CAD |

### Authentication

Provide the **Client id** and **Client secret** shown in the connector form. The labels and accepted body-key fields are defined by the [`flexiti.connector_auth.BodyKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L7994-L7996) and [`FlexitiAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/flexiti/transformers.rs#L188-L199).

### Before you start

Confirm availability with the Hyperswitch team before enabling Flexiti. Have the Client id and Client secret ready. To connect Flexiti to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Flexiti supports.

### Webhooks

Flexiti webhooks are not currently supported. The object lookup, event lookup, and resource lookup methods all return `WebhooksNotImplemented`; use payment sync for payment status. See [`IncomingWebhook for Flexiti`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/flexiti.rs#L701-L724) and [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/flexiti.rs#L391-L452).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. See [Flexiti connector source](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/flexiti.rs) and [Flexiti transformers](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/flexiti/transformers.rs).
