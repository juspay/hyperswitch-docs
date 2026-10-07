---
description: Configure IATA Pay bank redirect, real-time payment, and UPI payments with Hyperswitch.
metaLinks:
  alternates:
    - iatapay.md
---

# IATA Pay

IATA Pay connects bank redirect, real-time payment, and UPI routes to Hyperswitch. Every declared route supports refunds with automatic capture. Payment and refund callbacks are verified before status updates are applied.

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

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank redirect | iDEAL | not supported | supported | automatic | NLD | EUR |
| bank redirect | Local Bank Redirect | not supported | supported | automatic | 28 | 15 |
| real time payment | DuitNow | not supported | supported | automatic | MYS | MYR |
| real time payment | FPS | not supported | supported | automatic | GBR | GBP |
| real time payment | PromptPay | not supported | supported | automatic | THA | THB |
| real time payment | VietQR | not supported | supported | automatic | VNM | VND |
| upi | UPI Collect | not supported | supported | automatic | IND | INR |
| upi | UPI Intent | not supported | supported | automatic | IND | INR |


### Authentication

Provide **Client ID**, **Airline ID**, **Client Secret**, and **Source verification key** from [`iatapay connector configuration`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/connector_configs/toml/sandbox.toml#L3072-L3077); [`IatapayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/iatapay/transformers.rs#L259-L275) maps the API credentials.

### Before you start

IATA Pay appears in the control center list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). Have all four values ready and follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).

### Webhooks

IATA Pay verifies callbacks with HMAC-SHA256 over the raw body. The Base64 signature follows the `IATAPAY-HMAC-SHA256 ` prefix in the `Authorization` header ([`IATA Pay webhook verification`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/iatapay.rs#L670-L699)).

The payment enum defines nine known wire values and the refund enum seven ([`IATA Pay webhook event mapping`](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/iatapay/transformers.rs#L659-L718)).

| Payload | Wire value | Effect |
|---|---|---|
| Payment | `AUTHORIZED` | Payment succeeds |
| Payment | `SETTLED` | Payment succeeds |
| Payment | `INITIATED` | Payment remains in processing |
| Payment | `FAILED` | Payment fails |
| Payment | `CREATED` | No payment update |
| Payment | `CLEARED` | No payment update |
| Payment | `TOBEINVESTIGATED` | No payment update |
| Payment | `BLOCKED` | No payment update |
| Payment | `UNEXPECTED SETTLED` | No payment update |
| Refund | `CLEARED` | Refund succeeds |
| Refund | `AUTHORIZED` | Refund succeeds |
| Refund | `SETTLED` | Refund succeeds |
| Refund | `FAILED` | Refund fails |
| Refund | `CREATED` | No refund update |
| Refund | `LOCKED` | No refund update |
| Refund | `INITIATED` | No refund update |

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8`. See [IATA Pay connector source](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/iatapay.rs) and [IATA Pay transformers](https://github.com/juspay/hyperswitch/blob/7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8/crates/hyperswitch_connectors/src/connectors/iatapay/transformers.rs).
