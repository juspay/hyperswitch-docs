---
description: Dwolla connector for payment gateway.
metaLinks:
  alternates:
    - dwolla.md
---

# Dwolla

Dwolla supports ACH direct debit in the sandbox, with refunds and automatic capture. Payment and refund webhook flows are declared.

To connect Dwolla to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Dwolla supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank debit | ACH Direct Debit | not supported | supported | automatic, sequential automatic | USA | USD |


### Authentication

Activation needs three values, not two. [`[dwolla.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/connector_configs/toml/sandbox.toml) supplies the first two labels and the connector metadata supplies the third:

| Field | Required |
| --- | --- |
| **Client ID** | yes |
| **Client Secret** | yes |
| **Funding Source ID** | yes, from `dwolla.metadata.merchant_funding_source` |

If you take webhooks, also set **Source verification key**. It is not an authentication credential; it is the HMAC key the webhook check runs on, from `dwolla.connector_webhook_details`. See [Webhooks](#webhooks).

### Before you start

1. Obtain your **Client ID**, **Client Secret** and **Funding Source ID** from Dwolla.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) and open Dwolla, which is offered in the connector list.
3. Enter all three during connector activation. Activation will not complete without the funding source ID.
4. If you take webhooks, enter your Dwolla webhook secret in **Source verification key**.

### Webhooks

Dwolla's event enum carries 22 wire values ([`DwollaWebhookEventType`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla/transformers.rs#L550-L574)), but only six of them change a payment or refund. Everything else resolves to `EventNotSupported` and applies no update.

What a handled event means depends on whether the callback belongs to a refund, which the connector decides from the correlation id: an id beginning `refund_` makes it a refund event.

| Wire value | On a payment | On a refund |
| --- | --- | --- |
| `CustomerTransferCreated`, `CustomerBankTransferCreated` | Payment is processing | No update |
| `CustomerTransferCompleted`, `CustomerBankTransferCompleted` | Payment succeeds | Refund succeeds |
| `CustomerTransferFailed`, `CustomerBankTransferFailed` | Payment fails | Refund fails |

The mapping is at [`TryFrom<DwollaWebhookDetails> for IncomingWebhookEvent`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla/transformers.rs#L576-L608). The other sixteen values, the customer and funding-source and microdeposit events, parse but do nothing.

Callbacks are verified with a real HMAC-SHA256 over the request body, keyed on your **Source verification key**, at [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla.rs#L888-L915). A callback that fails the check is rejected.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Dwolla connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla.rs) and [Dwolla transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla/transformers.rs).
