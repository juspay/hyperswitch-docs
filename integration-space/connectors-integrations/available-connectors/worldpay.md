---
description: >-
  Accept online, in-store, and mobile payments through Worldpay via Juspay
  Hyperswitch with built-in fraud protection.
metaLinks:
  alternates:
    - worldpay.md
---

# Worldpay

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/worldpayLogo.svg" alt=""></div>

Worldpay connects to Hyperswitch as a payment gateway. Its current `SignatureKey` mapping combines the username and API key for HTTP Basic authentication and reads the entity ID from the third connector-account field ([auth mapping](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay/transformers.rs#L720-L745), [request header](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L149-L159)).

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e679350d9c54a0d3b22f4489be8b12c0f0cec1; host http://localhost:8080; fetched 2026-09-09T01:54:47Z; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live
**Category:** payment gateway
**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, JCB, Maestro, Mastercard, Visa | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, JCB, Maestro, Mastercard, Visa | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 90 ([full list](https://hyperswitch.io/pm-list)) | 58 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 75 ([full list](https://hyperswitch.io/pm-list)) | 57 ([full list](https://hyperswitch.io/pm-list)) |

### Connector-specific notes

* **Connector account fields:** Configure the API key, username, and entity ID used by the `SignatureKey` mapping.
* **Mandate setup:** The connector implements `MandateSetup` ([flow implementation](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L212-L221)).
* **Payout fulfillment:** The connector implements payout fulfillment ([flow implementation](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L1145-L1160)).
* For the full payment-method list behind the generated table, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

### Webhooks

The source enum contains 12 named event variants plus an `Unknown` fallback. Hyperswitch maps 7 variants to an effect and 5 to `EventNotSupported` ([event enum](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay/response.rs#L233-L253), [effect mapping](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L1350-L1374)).

* `PaymentIntentAuthorizationSuccess`: `Authorized`
* `PaymentIntentSuccess`: `Settled`
* `PaymentIntentProcessing`: `SentForSettlement`, `SentForAuthorization`
* `PaymentIntentFailure`: `Error`, `Expired`, `SettlementFailed`
* `EventNotSupported`: `Cancelled`, `Refused`, `Refunded`, `SentForRefund`, `RefundFailed`

Webhook source verification is implemented. Hyperswitch reads the final signature value from `Event-Signature`, verifies the request body with HMAC-SHA256, and compares the computed and received hex values ([verification implementation](https://github.com/juspay/hyperswitch/blob/d4e679350d9c54a0d3b22f4489be8b12c0f0cec1/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L1264-L1335)).

***

### Activating Worldpay via Hyperswitch

#### Prerequisites

1. You need to be registered with Worldpay. Sign up at [worldpay.com](https://online.worldpay.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Worldpay **Username** and **Password** are found in your Worldpay dashboard.
4. Select all payment methods you wish to use Worldpay for. Ensure these match the ones configured in your Worldpay dashboard.

[Steps to activate Worldpay on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate reference storage (ConnectorMandateId from SetupMandate used in RepeatPayment), constructing the Base64-encoded Authorization header on every request, routing captures to `/settlements` or `/partialSettlements` based on capture type, and unified error mapping. **Worldpay owns:** payment execution, fraud scoring, settlement routing, and token issuance for mandate flows.

**Hyperswitch owns:** sending the correct payment instrument reference in RepeatPayment requests. **Worldpay owns:** validating that the reference is active and matches the original SetupMandate. If a mandate reference expires or is revoked in Worldpay and is not updated in Hyperswitch, RepeatPayment requests will fail.

***

### Common Failure Modes

**Authentication failure** Symptom: All requests fail with a Worldpay 401 or authentication error. Fix: Verify both the Username and Password (API Key) in Hyperswitch exactly match those in your Worldpay dashboard. Hyperswitch Base64-encodes them automatically — do not manually encode before entering in the control center.

**Partial capture fails** Symptom: A multiple capture request fails after the first capture. Fix: Ensure the original payment was authorized with `capture_method: manual` and that the sum of partial captures does not exceed the authorized amount.

**RepeatPayment fails — invalid mandate reference** Symptom: MIT payment fails with a Worldpay token or reference error. Fix: Verify the mandate reference from the original SetupMandate is stored correctly in Hyperswitch and has not been revoked in Worldpay.

**Payment method not configured** Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Worldpay merchant account and matches the selection in the Hyperswitch connector configuration.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/worldpay.rs`.
