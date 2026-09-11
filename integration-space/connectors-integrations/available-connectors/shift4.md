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

### Authentication

Supply the raw Shift4 API key in the connector configuration. Hyperswitch appends a colon, Base64-encodes `api_key:`, and sends the result with the HTTP Basic scheme. See [`Shift4AuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/740e642eabb5b54094f589d4ebc08aa9e796fab1/crates/hyperswitch_connectors/src/connectors/shift4/transformers.rs#L837-L850) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/740e642eabb5b54094f589d4ebc08aa9e796fab1/crates/hyperswitch_connectors/src/connectors/shift4.rs#L112-L126).

### Before you start

1. Register with Shift4.
2. Create or sign in to your account in the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Find the API key on the Home page of your Shift4 dashboard.
4. Enable the same payment methods in Shift4 that you plan to select in Hyperswitch.
5. Have the credential listed in [Authentication](#authentication) ready.

To connect Shift4 to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Shift4 supports.

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
