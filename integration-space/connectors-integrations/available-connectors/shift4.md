---
description: >-
  Connect Shift4 to Hyperswitch and review the capabilities declared by the
  connector implementation.
metaLinks:
  alternates:
    - shift4.md
---

# Shift4

Shift4 is a payment gateway integration in Hyperswitch.

## Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 4c41905c7d01ddc7ce2b14fc88361d805824a235; host https://sandbox.hyperswitch.io; fetched 2026-09-09; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
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

## Configure Shift4

Supply the Shift4 API key in the API key field. Hyperswitch appends a colon to the API key, Base64-encodes the result, and sends it in the Authorization header. Enter the raw API key in Hyperswitch rather than an already encoded value.

Follow the [connector activation guide](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch) to add the credential in Hyperswitch.

## Webhooks

The webhook enum contains 6 exact variants. Five variants represent mapped events, and `Unknown` is the catch-all:

| Shift4 event variant | Hyperswitch event |
| --- | --- |
| `ChargeSucceeded` | `PaymentIntentProcessing` |
| `ChargeUpdated` | `PaymentIntentProcessing` |
| `ChargeCaptured` | `PaymentIntentSuccess` |
| `ChargeFailed` | `PaymentIntentFailure` |
| `ChargeRefunded` | `RefundSuccess` |
| `Unknown` | `EventNotSupported` |

The enum applies the `SCREAMING_SNAKE_CASE` serde rename rule to incoming values.

## Page gaps

- The connector does not define a connector-specific webhook source-verification method. Confirm the required verification controls before enabling incoming events.
- Connector source does not declare the vendor dashboard paths for finding the API key or registering the webhook endpoint. Use the current vendor dashboard guidance when completing those steps.
