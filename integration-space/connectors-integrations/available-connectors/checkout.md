---
description: Accept card, wallet, and bank payments through Checkout.com on Hyperswitch.
metaLinks:
  alternates:
    - checkout.md
---

# Checkout

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/checkoutLogo.svg" alt=""></div>

Checkout.com supports cards, network tokens, Apple Pay, and Google Pay through Hyperswitch, including manual multiple capture and refunds across every listed method.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; fetched 2026-09-09; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** disputes, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic, manual multiple | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | 49 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic, manual multiple | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | 49 ([full list](https://hyperswitch.io/pm-list)) | 154 ([full list](https://hyperswitch.io/pm-list)) |
| network token | Network Token | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | - | - |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 85 ([full list](https://hyperswitch.io/pm-list)) | 55 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 72 ([full list](https://hyperswitch.io/pm-list)) | 53 ([full list](https://hyperswitch.io/pm-list)) |

### Connector-specific notes

* **Authentication:** The `SignatureKey` mapping reads the API key, secret key, and processing channel ID. Payment requests send the mapped secret as a bearer token in the `Authorization` header ([`SignatureKey` mapping](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout/transformers.rs#L637-L654), [`get_auth_header`](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout.rs#L123-L132)).
* **Raw card data:** Checkout.com requires enablement of raw card data handling. Contact Checkout.com support at support@checkout.com before processing raw card data.
* **Dispute evidence:** The connector implements accept, defend, file upload, retrieval, and evidence submission flows ([connector flow implementations](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout.rs#L259-L263), [file upload](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout.rs#L1032-L1044), [evidence submission](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout.rs#L1142-L1160)).
* For the full payment-method list behind the generated table, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

### Webhooks

The source enum contains 25 named event variants plus an `Unknown` fallback. Hyperswitch maps 21 variants to an effect and 4 to `EventNotSupported` ([event enum](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout/transformers.rs#L2399-L2428), [effect mapping](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout/transformers.rs#L2502-L2535)).

* `PaymentIntentAuthorizationFailure`: `AuthenticationExpired`, `AuthenticationFailed`, `PaymentAuthenticationFailed`
* `PaymentIntentSuccess`: `PaymentCaptured`
* `PaymentIntentFailure`: `PaymentDeclined`
* `RefundSuccess`: `PaymentRefunded`
* `RefundFailure`: `PaymentRefundDeclined`
* `PaymentIntentCancelFailure`: `PaymentCanceled`
* `PaymentIntentCaptureFailure`: `PaymentCaptureDeclined`
* `PaymentIntentCancelled`: `PaymentVoided`
* `DisputeOpened`: `DisputeReceived`, `DisputeEvidenceRequired`
* `DisputeExpired`: `DisputeExpired`
* `DisputeAccepted`: `DisputeAccepted`
* `DisputeCancelled`: `DisputeCanceled`
* `DisputeChallenged`: `DisputeEvidenceSubmitted`, `DisputeEvidenceAcknowledgedByScheme`
* `DisputeWon`: `DisputeWon`, `DisputeArbitrationWon`
* `DisputeLost`: `DisputeLost`, `DisputeArbitrationLost`
* `EventNotSupported`: `AuthenticationStarted`, `AuthenticationApproved`, `AuthenticationAttempted`, `PaymentApproved`

Webhook source verification is implemented. Hyperswitch reads the hex-encoded signature from `cko-signature` and verifies the request body with HMAC-SHA256 ([verification implementation](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/checkout.rs#L1289-L1312)).

***

### Activating Checkout.com via Hyperswitch

#### Prerequisites

1. You need to be registered with Checkout.com. Sign up at [checkout.com/get-test-account](https://www.checkout.com/get-test-account).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. Request the Checkout.com support team to enable raw card data handling via email (support@checkout.com).
4. Your Checkout.com API key, Processing Channel ID, and Secret Key are available in your Checkout.com dashboard under the [Developers section](https://dashboard.sandbox.checkout.com/developers/get-started).
5. To configure a webhook endpoint, navigate to the webhooks section of your Checkout.com dashboard and create a new webhook.

[Steps to activate Checkout.com on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and webhook fan-out to your endpoint. **Checkout.com owns:** payment execution, fraud evaluation, and webhook delivery to Hyperswitch's endpoint. The Processing Channel ID determines which Checkout.com business unit processes the payment — Hyperswitch passes this on every request but has no visibility into how Checkout.com routes internally based on it.

**Hyperswitch owns:** dispute case tracking and evidence submission orchestration. **Checkout.com owns:** dispute resolution, chargeback adjudication, and final outcome. File evidence submitted via Hyperswitch is forwarded to Checkout.com's dispute API — the final chargeback decision is made entirely by Checkout.com.

***

### Common Failure Modes

**Raw card data not enabled** Symptom: Card payments fail before authorization. Fix: Contact Checkout.com support (support@checkout.com) to enable raw card data handling for your account.

**Wrong Processing Channel ID** Symptom: Payments fail with a channel or merchant configuration error. Fix: Verify the Processing Channel ID in Hyperswitch matches the channel in your Checkout.com dashboard. Each business unit has a distinct channel ID.

**Secret Key mismatch for webhooks** Symptom: Checkout.com webhooks are received but rejected — payment statuses do not update. Fix: Ensure the Secret Key stored in Hyperswitch matches the webhook signing key in your Checkout.com dashboard.

**ManualMultiple capture exceeds authorized amount** Symptom: A partial capture call fails with an amount error. Fix: The sum of all partial captures cannot exceed the originally authorized amount — Checkout.com enforces this at the API level.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/checkout.rs`.
