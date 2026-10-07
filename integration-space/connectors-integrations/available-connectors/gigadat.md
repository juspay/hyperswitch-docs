---
description: Configure Gigadat Interac payments with Hyperswitch.
metaLinks:
  alternates:
    - gigadat.md
---

# Gigadat

Gigadat brings Interac bank redirect payments to Hyperswitch. The route supports refunds and both automatic and manual capture. Payment and payout callbacks are processed, but their source is not verified by the connector.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, payouts

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank redirect | Interac | not supported | supported | automatic, manual | - | CAD |


### Authentication

Provide the **Access Token**, **Security Token**, and **Campaign ID**. Also provide the required **Site where transaction is initiated** metadata. These fields come from [`gigadat connector configuration`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L8436-L8449), and [`GigadatAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/gigadat/transformers.rs#L154-L171) maps the credentials.

### Before you start

Gigadat appears in the control center payment-processor list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). Have the three credentials and Site value ready. Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).

### Webhooks

Gigadat handles payment and payout callbacks, but source verification returns `false`. Treat callbacks as unverified and confirm status through the API. See [`IncomingWebhook for Gigadat`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/gigadat.rs#L983-L1052).

The code handles nine flow codes and eight exact status values ([`GigadatFlow::get_flow()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/gigadat/transformers.rs#L214-L232), [`get_gigadat_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/gigadat/transformers.rs#L234-L282)).

| Flow | Wire values |
|---|---|
| Payment | `ETI`, `RFM`, `CPI`, `ACK` |
| Payout | `ETO`, `RTO`, `RTX`, `ANR`, `ANX` |

| Status wire value | Payment effect | Payout effect |
|---|---|---|
| `STATUS_SUCCESS` | Payment succeeds | Payout succeeds |
| `STATUS_FAILED` | Payment fails | Payout fails |
| `STATUS_REJECTED` | Payment fails | Payout fails |
| `STATUS_REJECTED1` | Payment fails | Payout fails |
| `STATUS_EXPIRED` | Payment fails | Payout fails |
| `STATUS_ABORTED1` | Payment fails | Payout fails |
| `STATUS_INITED` | Payment remains in processing | Payout remains in processing |
| `STATUS_PENDING` | Payment remains in processing | Payout remains in processing |

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [Gigadat connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/gigadat.rs) and [Gigadat transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/gigadat/transformers.rs).
