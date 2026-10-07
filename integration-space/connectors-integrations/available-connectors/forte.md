---
description: Configure Forte card payments with Hyperswitch.
metaLinks:
  alternates:
    - forte.md
---

# Forte

Forte processes credit and debit card payments in Canada and the United States. Both routes support refunds and automatic, manual, and sequential automatic capture. Mandates and 3DS are not available for these card payments.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d03f8547d6367fab56690e4f5043590be4935dcd; host http://127.0.0.1:8080; fetched 2026-10-02; matrix canonical-json-v1 sha256 8b92b42f08eb323a31ea974c99ac67dc4972774ab49bda767a79da9d2992fd5b; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | CAN, USA | CAD, USD |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | CAN, USA | CAD, USD |

3DS is not supported. A card request sent with 3DS set is rejected with a "not supported" error before anything reaches Forte ([`FortePaymentsRequest`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte/transformers.rs#L98-L105)), so route cards to another connector if your profile enables 3DS.

Capture method changes what the create response reports. A manual-capture authorization returns `Authorized`, and a capture returns `Charged`. An automatic-capture sale returns `Pending` even when Forte approved it, and the payment moves to `Charged` only when a sync reports Forte's status as complete or settled ([`get_status`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte/transformers.rs#L217-L227), [status mapping](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte/transformers.rs#L205-L215)). Sync after every automatic payment before treating it as paid.

### Authentication

Provide the **API Access ID**, **Organization ID**, **API Secure Key**, and **Location ID** shown in the connector form. The labels and accepted multi-auth fields are defined by the [`forte.connector_auth.MultiAuthKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L2759-L2763) and [`ForteAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte/transformers.rs#L174-L192).

They are not all used the same way. The **API Access ID** and **API Secure Key** are combined and sent as HTTP Basic authentication in the `Authorization` header. The **Organization ID** is sent in the `X-Forte-Auth-Organization-Id` header and, together with the **Location ID**, forms the request path, `/organizations/{organization id}/locations/{location id}/transactions` ([`get_auth_header`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs#L123-L146), [`get_url`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs#L220-L225)). A wrong Access ID or Secure Key fails authentication; a wrong Organization ID or Location ID sends the request to the wrong endpoint.

### Before you start

Have the API Access ID, Organization ID, API Secure Key, and Location ID ready. To connect Forte to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Forte supports.

### Webhooks

Forte webhooks are not currently supported. Event lookup returns `EventNotSupported`, while object and resource lookup return `WebhooksNotImplemented`; use payment sync for payment status and refund sync for refund status. See [`IncomingWebhook for Forte`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs#L710-L733), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs#L296-L357), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs#L635-L694).

The connector form exposes a **Source verification key**, but the current webhook implementation does not consume it because callbacks are unsupported. See [`forte.connector_webhook_details`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L2764-L2765) and [`IncomingWebhook for Forte`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs#L710-L733).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. See [Forte connector source](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte.rs) and [Forte transformers](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/forte/transformers.rs).
