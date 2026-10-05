---
description: Configure Fiserv Commerce Hub card payments with Hyperswitch.
metaLinks:
  alternates:
    - fiservcommercehub.md
---

# Fiserv Commerce Hub

Fiserv Commerce Hub processes credit and debit card payments through Hyperswitch. Both routes support mandates, refunds, and manual capture alongside automatic capture. Cardholders can complete payments with or without 3DS across the declared card networks.

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
| card | Credit Card | supported | supported | automatic, manual | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | supported | supported | automatic, manual | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | - |

### Authentication

Provide the **API Key**, **Merchant ID**, **API Secret**, and **Terminal ID** shown in the connector form. The labels and accepted multi-auth fields are defined by the [`fiservcommercehub.connector_auth.MultiAuthKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L2716-L2720) and [`FiservcommercehubAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiservcommercehub/transformers.rs#L75-L93).

### Before you start

Have the API Key, Merchant ID, API Secret, and Terminal ID ready. To connect Fiserv Commerce Hub to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Fiserv Commerce Hub supports.

### Webhooks

Fiserv Commerce Hub webhooks are not supported. Use Hyperswitch payment sync and refund sync to check status. Both routes go through Connector Service. See [`IncomingWebhook for Fiservcommercehub`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiservcommercehub.rs#L583-L606) and [Connector Service routing](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/config/development.toml#L1684).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. See [Fiserv Commerce Hub connector source](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiservcommercehub.rs) and [Fiserv Commerce Hub transformers](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiservcommercehub/transformers.rs).
