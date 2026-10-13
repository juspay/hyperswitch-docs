---
description: Connect Facilitapay through Hyperswitch.
metaLinks:
  alternates:
    - facilitapay.md
---

# Facilitapay

Facilitapay supports Pix bank transfers in the sandbox, with refunds and automatic capture. Payment webhook processing is declared.

To connect Facilitapay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Facilitapay supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank transfer | Pix | not supported | supported | automatic, sequential automatic | BRA | BRL |


The table says refunds are supported, which is true only for the full amount. A refund whose amount differs from the payment amount is rejected before any request is sent, with "Partial refund not supported by Facilitapay". See [`build_request()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs#L686-L709). Refund the whole payment or not at all.

### Authentication

Activation needs three values. [`[facilitapay.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml#L7209-L7211) supplies the first two labels, and the connector metadata supplies the third:

| Field | Required |
| --- | --- |
| **Username** | yes |
| **Password** | yes |
| **Merchant Account Number** | yes, from `facilitapay.metadata.destination_account_number` |

All three are required, so activation will not complete with the username alone.

### Before you start

1. Obtain your **Username**, **Password** and **Merchant Account Number** from Facilitapay.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) and open Facilitapay, which is offered in the connector list.
3. Enter all three during connector activation.
4. Read the webhook warning below before you rely on callbacks.

### Webhooks

{% hint style="warning" %}
**Facilitapay callbacks are weakly authenticated. Do not treat one as proof of payment.**

Verification compares a secret carried in the callback body against your configured value as plain text, at [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs#L812-L841). Nothing is computed over the payload, so the check says only that the sender knew the secret, and the source comment describes it as "a simple 4-digit secret".

Two things make that weaker still. When no webhook secret is configured the comparison falls back to the literal string `default_secret` ([`facilitapay.rs:836`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs#L836)), rather than failing closed, so a connector with no secret set accepts any callback carrying that value.

And the default path leaves it unset. No `connector_webhook_details` block exists for Facilitapay in any connector configuration, so the control center offers no field for it. The value can still be set through the connector-account API, as `merchant_secret` in `connector_webhook_details`, but a connector configured through the dashboard alone will not have one.

Confirm with payment sync before you release goods or mark an order paid, and treat a callback only as a signal to go and check.
{% endhint %}

The events below are what the connector does with a callback once it accepts it.

| Wire value | Effect |
| --- | --- |
| `exchange_created` | Payment is processing |
| `identified` | Payment succeeds |
| `payment_approved` | Payment succeeds |
| `wire_created` | Payment succeeds |
| `payment_expired` | Payment fails |
| `payment_failed` | Payment fails |
| `payment_refunded` | Refund succeeds |
| `wire_waiting_correction` | Payment needs action |

The eight wire values come from [`FacilitapayWebhookEventType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay/responses.rs#L278-L287); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs#L879-L913). The match is exhaustive, so every declared value maps to an outcome and there is no unknown fallback.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Facilitapay connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay.rs) and [Facilitapay transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/facilitapay/transformers.rs).
