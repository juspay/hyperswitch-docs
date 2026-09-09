---
description: >-
  Connect Braintree to Hyperswitch and review the capabilities declared by the
  connector implementation.
metaLinks:
  alternates:
    - braintree.md
---

# Braintree

Braintree is a payment gateway integration in Hyperswitch.

## Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 4c41905c7d01ddc7ce2b14fc88361d805824a235; host https://sandbox.hyperswitch.io; fetched 2026-09-09; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, JCB, Mastercard, UnionPay, Visa | 45 ([full list](https://hyperswitch.io/pm-list)) | 134 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, JCB, Mastercard, UnionPay, Visa | 45 ([full list](https://hyperswitch.io/pm-list)) | 134 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | PayPal | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |

## Configure Braintree

Supply the Braintree public key in the API key field and the private key in the API secret field. Hyperswitch combines those values as HTTP Basic credentials for connector requests. The third `SignatureKey` field is accepted by the shared credential shape but is not used by Braintree's authentication conversion.

The connector sends payment operations through GraphQL. Follow the [connector activation guide](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch) to add these credentials in Hyperswitch.

## Webhooks

Hyperswitch verifies Braintree webhook payloads with HMAC-SHA1. The handler reads the signature and encoded payload from the incoming form body.

The implementation recognizes 7 event names:

| Braintree event | Hyperswitch effect |
| --- | --- |
| `dispute_opened` | `DisputeOpened` |
| `dispute_lost` | `DisputeLost` |
| `dispute_won` | `DisputeWon` |
| `dispute_accepted` | `DisputeAccepted` |
| `dispute_auto_accepted` | `DisputeAccepted` |
| `dispute_expired` | `DisputeExpired` |
| `dispute_disputed` | `DisputeChallenged` |

Other event names map to `EventNotSupported`.

## Page gaps

- The capability declaration lists payment and refund webhook flows, while the implemented event mapper recognizes dispute events. Confirm the intended declaration before relying on the generated webhook-flow list.
- Connector source does not declare the vendor dashboard paths for finding credentials or registering the webhook endpoint. Use the current vendor dashboard guidance when completing those steps.
