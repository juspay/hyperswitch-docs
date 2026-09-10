---
description: >-
  Accept card and bank redirect payments through Shift4 with Hyperswitch.
metaLinks:
  alternates:
    - shift4.md
---

# Shift4

Based in the United States, Shift4 is a payment processing company. Merchants can accept Mastercard and Visa cards alongside EPS, Giropay, iDEAL, and Sofort bank redirects. Every listed method supports refunds and manual capture, while mandates are not supported. Card payments can use optional 3DS, and webhooks cover payment and refund updates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 93becbaee4ee3686e1a4d5750d2e547c56c27047; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | EPS | not supported | supported | automatic, manual, sequential automatic | not applicable | - | AUT | EUR |
| bank redirect | Giropay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | DEU | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, manual, sequential automatic | not applicable | - | NLD | EUR |
| bank redirect | Sofort | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 12 ([full list](https://hyperswitch.io/pm-list)) | CHF, EUR |
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | Mastercard, Visa | 247 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | Mastercard, Visa | 247 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |

### Configure Shift4

Enter the raw Shift4 API key in the API key field. Hyperswitch appends a colon, Base64-encodes the result, and sends it as an HTTP Basic credential ([credential mapping](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/shift4/transformers.rs#L835-L850), [request header](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/shift4.rs#L112-L126)).

Follow the [connector activation guide](../activate-connector-on-hyperswitch/README.md) to add the credential in Hyperswitch. Use Shift4's current dashboard guidance to find the API key and register the webhook endpoint.

### Webhooks

Register the Hyperswitch endpoint in Shift4 using the [standard webhook setup instructions](https://docs.hyperswitch.io/integration-guide/webhooks). The Shift4 connector does not implement a connector-specific source-verification method, so apply verification controls before enabling incoming events ([webhook implementation](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/shift4.rs#L934-L990)).

The source enum contains 6 exact variants. Five variants map the wire values below, and the sixth is a catch-all for any other value. The enum applies `SCREAMING_SNAKE_CASE` to incoming values ([enum](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/shift4/transformers.rs#L883-L899), [mapping](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/shift4/transformers.rs#L1239-L1250)):

| Shift4 event | Hyperswitch effect |
| --- | --- |
| `CHARGE_SUCCEEDED` | Payment processing |
| `CHARGE_UPDATED` | Payment processing |
| `CHARGE_CAPTURED` | Payment succeeded |
| `CHARGE_FAILED` | Payment failed |
| `CHARGE_REFUNDED` | Refund succeeded |
| Any other value | Event not supported |
