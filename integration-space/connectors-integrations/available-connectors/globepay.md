---
description: Configure GlobePay Alipay and WeChat Pay wallet payments with Hyperswitch.
metaLinks:
  alternates:
    - globepay.md
---

# GlobePay

GlobePay brings Alipay and WeChat Pay wallet payments to Hyperswitch. Both routes support refunds and automatic capture, including sequential automatic capture. Mandate setup is not supported.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| wallet | Alipay | not supported | supported | automatic, sequential automatic | GBR | CNY, GBP |
| wallet | WeChat Pay | not supported | supported | automatic, sequential automatic | GBR | CNY, GBP |


### Authentication

Provide the **Partner Code** and **Credential Code** from [`globepay.connector_auth.BodyKey`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L3051-L3053); [`GlobepayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay/transformers.rs#L139-L150) maps them. **Source verification key** is currently unused because webhooks are not implemented ([`globepay.connector_webhook_details`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L3054-L3055)).

### Before you start

Create or sign in to your [GlobePay account](https://www.globepay.co/services/) and obtain the **Partner Code** and **Credential Code**. GlobePay appears in the control center list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). Then follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).

### Payment flow

GlobePay is a QR flow. Send the QR wallet variants, `ali_pay_qr` or `we_chat_pay_qr`; the redirect variants of Alipay and WeChat Pay return a not-implemented error ([wallet handling](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay/transformers.rs#L56-L95)). Authorize returns the QR image URL in `connector_metadata` as `image_data_url`, and the payment stays `requires_customer_action` until the customer scans it ([QR metadata](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay/transformers.rs#L207-L231)). Only a payment sync moves it on: `PAYING` keeps it pending, `PAY_SUCCESS` marks it charged, and `CLOSED` or a failure marks it failed ([`GlobepayPaymentPsyncStatus`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay/transformers.rs#L266-L281)). A refund sync maps `FINISHED` to success, `WAITING` and `SUCCESS` to pending, and `CHANGE` to failure ([`GlobepayRefundStatus`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay/transformers.rs#L366-L382)).

### Webhooks

GlobePay webhooks are not supported; use payment sync and refund sync for status. See [`IncomingWebhook for Globepay`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay.rs#L548-L572), [`ConnectorIntegration<PSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay.rs#L294-L365), and [`ConnectorIntegration<RSync>`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay.rs#L474-L546).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [GlobePay connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay.rs) and [GlobePay transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/globepay/transformers.rs).
