---
description: >-
  Connect Nuvei to Hyperswitch and review the capabilities declared by the
  connector implementation.
metaLinks:
  alternates:
    - nuvei.md
---

# Nuvei

Nuvei is a payment gateway integration in Hyperswitch.

## Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 4c41905c7d01ddc7ce2b14fc88361d805824a235; host https://sandbox.hyperswitch.io; fetched 2026-09-09; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** disputes, payments

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | EPS | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| bank redirect | Giropay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | EUR |
| bank redirect | Sofort | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 249 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 249 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| network token | Network Token | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| pay later | Afterpay Clearpay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | Klarna | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 59 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 237 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | PayPal | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |

## Configure Nuvei

Supply the merchant ID in the API key field, the merchant site ID in the `key1` field, and the merchant secret in the API secret field. Nuvei requests do not use an Authorization header. The connector includes the authentication values and request checksum in the request body.

Follow the [connector activation guide](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch) to add these credentials in Hyperswitch.

## Webhooks

For payment direct merchant notifications, Hyperswitch verifies the advanced response checksum with SHA-256.

### Payment and refund events

The payment mapper contains 11 branches covering the following status and transaction-type combinations. `DmnStatus` applies an `UPPERCASE` serde rename rule to incoming status values:

| Nuvei status | Transaction type | Hyperswitch effect |
| --- | --- | --- |
| `Success` or `Approved` | `Auth` | `PaymentIntentAuthorizationSuccess` |
| `Success` or `Approved` | `Sale` | `PaymentIntentSuccess` |
| `Success` or `Approved` | `Settle` | `PaymentIntentCaptureSuccess` |
| `Success` or `Approved` | `Void` | `PaymentIntentCancelled` |
| `Success` or `Approved` | `Credit` | `RefundSuccess` |
| `Error` or `Declined` | `Auth` | `PaymentIntentAuthorizationFailure` |
| `Error` or `Declined` | `Sale` | `PaymentIntentFailure` |
| `Error` or `Declined` | `Settle` | `PaymentIntentCaptureFailure` |
| `Error` or `Declined` | `Void` | `PaymentIntentCancelFailure` |
| `Error` or `Declined` | `Credit` | `RefundFailure` |
| `Pending` | `Auth`, `Sale`, or `Settle` | `PaymentIntentProcessing` |

Other payment combinations return `WebhookEventTypeNotFound`.

### Payout events

When the payouts feature is enabled and the client request identifier has the payout prefix, the implementation uses 3 mapping branches:

| Nuvei status | Transaction type | Hyperswitch effect |
| --- | --- | --- |
| `Success` or `Approved` | `Credit` | `PayoutSuccess` |
| `Pending` | Any declared transaction type | `PayoutProcessing` |
| `Declined` or `Error` | Any declared transaction type | `PayoutFailure` |

Other payout combinations return `WebhookEventTypeNotFound`.

### Dispute events

The dispute enum defines 51 exact event codes. The table accounts for all 51:

| Hyperswitch effect | Nuvei event codes |
| --- | --- |
| `DisputeOpened` | `FC`, `CC`, `MCC`, `FC-CLSD-RCL`, `INQ` |
| `DisputeAccepted` | `CC-A-ACPT`, `FC-A-ACPT`, `FC-A-ACPT-MCOLL`, `FC-M-ACPT`, `FC-SPCSE`, `RDR`, `MCC-M-ACPT`, `MCC-A-ACPT`, `INQ-M-RFND`, `IPA-M-ACPT`, `IPA-M-PART`, `IPA-A-ACPT`, `IPAR-M-ACPT`, `IPAR-A-ACPT` |
| `DisputeLost` | `FC-A-EPRD`, `FC-M-PART`, `FC-CLSD-CHF`, `PA-CLSD-CHF`, `MCC-CLSD-CHF` |
| `DisputeChallenged` | `FC-M-RJCT`, `FC-A-RJCT`, `IPA`, `MPA-I-RJCT`, `INQ-M-RSP`, `IPA-M-RJCT` |
| `DisputeExpired` | `FC-A-RJCT-EXP`, `FC-M-PART-EXP`, `FC-M-RJCT-EXP`, `MCC-EXPR`, `INQ-EXPR`, `IPA-M-PART-EXP`, `IPA-M-RJCT-EXP` |
| `DisputeWon` | `MPA-I-ACPT`, `MPA-I-PART`, `FC-CLSD-MF`, `MCC-CLSD-MF`, `PA-CLSD-MF` |
| `DisputeCancelled` | `FC-I-RCL`, `INQ-A-CNLD`, `PA-CLSD-RC`, `CC-I-RCLL` |
| No direct event; category fallback may apply | `MCC-A-RJCT`, `MCC-M-RJCT`, `INQ-A-RJCT`, `INQ-M-P-RFND`, `INQ-UPD` |

The category fallback defines 5 exact category values:

| Chargeback category | Hyperswitch effect |
| --- | --- |
| `cancelled` | `DisputeCancelled` |
| `Duplicate` | `DisputeCancelled` |
| `RDR-Refund` | `DisputeAccepted` |
| `Regular` | No fallback event |
| `Soft_CB` | No fallback event |

## Page gaps

- The capability declaration lists payment and dispute webhook flows, while the event mapper also contains refund and feature-gated payout outcomes. Confirm the intended declaration before relying on the generated webhook-flow list.
- Chargeback source verification reads a checksum header, but the source marks its verification-message format as a placeholder. Confirm that format before enabling chargeback notifications.
- Connector source does not declare the vendor dashboard paths for finding credentials or registering webhook endpoints. Use the current vendor dashboard guidance when completing those steps.
