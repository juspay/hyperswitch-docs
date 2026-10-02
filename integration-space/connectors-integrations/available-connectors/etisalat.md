---
description: Configure Etisalat card payments with Hyperswitch.
metaLinks:
  alternates:
    - etisalat.md
---

# Etisalat

Etisalat processes credit and debit card payments through Hyperswitch. Both card routes support refunds and manual capture alongside automatic capture. Mandates and 3DS are not available for these routes.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d03f8547d6367fab56690e4f5043590be4935dcd; host http://127.0.0.1:8080; fetched 2026-10-02; matrix canonical-json-v1 sha256 8b92b42f08eb323a31ea974c99ac67dc4972774ab49bda767a79da9d2992fd5b; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual | not supported | Mastercard, Visa | 7 | 9 |
| card | Debit Card | not supported | supported | automatic, manual | not supported | Mastercard, Visa | 7 | 9 |

### Authentication

Provide the **EPG Password**, **EPG UserName**, and **EPG Customer** shown in the connector form. The labels and accepted signature-key fields are defined by the [`etisalat.connector_auth.SignatureKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L9347-L9350) and [`EtisalatAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/etisalat/transformers.rs#L75-L91).

### Before you start

Have the EPG Password, EPG UserName, and EPG Customer ready. To connect Etisalat to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Etisalat supports.

### Webhooks

Etisalat webhooks are not currently supported. The object lookup, event lookup, and resource lookup methods all return `WebhooksNotImplemented`; use payment sync for payment status and refund sync for refund status. See [`IncomingWebhook for Etisalat`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/etisalat.rs#L591-L614), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/etisalat.rs#L292-L343), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/etisalat.rs#L522-L573).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. See [Etisalat connector source](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/etisalat.rs) and [Etisalat transformers](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/etisalat/transformers.rs).
