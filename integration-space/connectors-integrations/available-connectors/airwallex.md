---
description: >-
  Accept payments globally through Airwallex via Hyperswitch, with support for
  cross-border payments, foreign exchange, and multiple payment methods.
metaLinks:
  alternates:
    - airwallex.md
---

# Airwallex

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/airwallexLogo.svg" alt=""></div>

Configure an API key and client ID for Airwallex. Hyperswitch exchanges these credentials at the login endpoint and uses the returned bearer token for payment requests. See [`AirwallexAuthType`](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/airwallex/transformers.rs#L46-L64), the [`AccessTokenAuth` login flow](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/airwallex.rs#L296-L355), and the [bearer authorization header](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/airwallex.rs#L89-L109). All requests use `application/json`. Airwallex is primarily used for cross-border payment scenarios where multi-currency support and FX handling are requirements.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch f35edab780c97dd12efdd366246ff3f7fbc0e940; host http://localhost:8080; fetched 2026-09-08; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox  
**Category:** payment gateway  
**Webhook flows:** disputes, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | BLIK | not supported | supported | automatic, sequential automatic | not applicable | - | POL | PLN |
| bank redirect | iDEAL | not supported | supported | automatic, sequential automatic | not applicable | - | NLD | EUR |
| bank redirect | Trustly | not supported | supported | automatic, sequential automatic | not applicable | - | - | DKK, EUR, GBP, NOK, PLN, SEK |
| bank transfer | Indonesian Bank Transfer | not supported | not supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | AUS, HKG, NZL, SGP, USA | 157 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | AUS, HKG, NZL, SGP, USA | 157 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | Atome | not supported | supported | automatic, sequential automatic | not applicable | - | MYS, SGP | MYR, SGD |
| pay later | Klarna | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 9 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 67 ([full list](https://hyperswitch.io/pm-list)) | 56 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | PayPal | not supported | supported | automatic, sequential automatic | not applicable | - | - | 22 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Skrill | not supported | supported | automatic, sequential automatic | not applicable | - | 123 ([full list](https://hyperswitch.io/pm-list)) | EUR, GBP, USD |


### Connector-Specific Notes

* **OAuth-style token exchange:** Unlike connectors with static Bearer tokens, Airwallex requires fetching an access token before each session using the API Key and Client ID. Hyperswitch handles this token exchange internally — the credentials configured in the control center are the API Key and Client ID, not the access token.
* **Credentials location:** API Key and Client ID are found in your Airwallex dashboard under **Developer → API Keys**.
* **Cross-border and FX:** Airwallex's primary differentiator is multi-currency settlement and FX conversion. Payment methods and currencies available depend on your Airwallex account's approved corridors.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Webhooks

Airwallex recognizes 30 named webhook events. The event set comes from [`AirwallexWebhookEventType`](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/airwallex/transformers.rs#L1642-L1706), and the effects come from its [`IncomingWebhookEvent` mapping](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/airwallex/transformers.rs#L1924-L1961).

| Incoming event | Effect |
|---|---|
| `payment_intent.created` | No payment, refund, or dispute state update. |
| `payment_intent.requires_payment_method` | No payment, refund, or dispute state update. |
| `payment_intent.cancelled` | No payment, refund, or dispute state update. |
| `payment_intent.succeeded` | No payment, refund, or dispute state update. |
| `payment_intent.requires_capture` | No payment, refund, or dispute state update. |
| `payment_intent.requires_customer_action` | No payment, refund, or dispute state update. |
| `payment_attempt.authorized` | Payment succeeds. |
| `payment_attempt.authorization_failed` | No payment, refund, or dispute state update. |
| `payment_attempt.capture_requested` | No payment, refund, or dispute state update. |
| `payment_attempt.capture_failed` | No payment, refund, or dispute state update. |
| `payment_attempt.authentication_redirected` | No payment, refund, or dispute state update. |
| `payment_attempt.authentication_failed` | No payment, refund, or dispute state update. |
| `payment_attempt.failed_to_process` | Payment fails. |
| `payment_attempt.cancelled` | No payment, refund, or dispute state update. |
| `payment_attempt.expired` | No payment, refund, or dispute state update. |
| `payment_attempt.risk_declined` | No payment, refund, or dispute state update. |
| `payment_attempt.settled` | No payment, refund, or dispute state update. |
| `payment_attempt.paid` | No payment, refund, or dispute state update. |
| `refund.received` | No payment, refund, or dispute state update. |
| `refund.accepted` | No payment, refund, or dispute state update. |
| `refund.succeeded` | Refund succeeds. |
| `refund.failed` | Refund fails. |
| `dispute.rfi_responded_by_merchant` | No payment, refund, or dispute state update. |
| `dispute.dispute.pre_chargeback_accepted` | Dispute is accepted. |
| `dispute.accepted` | Dispute is accepted. |
| `dispute.dispute_received_by_merchant` | No payment, refund, or dispute state update. |
| `dispute.dispute_responded_by_merchant` | Dispute is challenged. |
| `dispute.won` | Dispute is won. |
| `dispute.lost` | Dispute is lost. |
| `dispute.dispute_reversed` | Dispute is won. |

Hyperswitch verifies each webhook with HMAC-SHA256 over the timestamp followed by the request body. Airwallex supplies the signature and timestamp in the `x-signature` and `x-timestamp` headers. See the [`IncomingWebhook` implementation](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/airwallex.rs#L1077-L1124).

***

### Activating Airwallex via Hyperswitch

#### Prerequisites

1. You need to be registered with Airwallex. Sign up at [airwallex.com](https://www.airwallex.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. The Airwallex API Key and Client ID are found in your Airwallex dashboard under **Developer → API Keys**.
4. Select all payment methods you wish to use Airwallex for. Ensure these match the ones configured in your Airwallex dashboard.

[Steps to activate Airwallex on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, token lifecycle management (fetching and refreshing the Airwallex access token), retry scheduling, and mandate record storage. **Airwallex owns:** payment execution, FX conversion, corridor availability, and settlement. The specific payment methods and currencies available for a given transaction are determined by your Airwallex account's approved corridors — Hyperswitch has no visibility into corridor restrictions at runtime.

**Hyperswitch owns:** initiating the token exchange before payment requests. **Airwallex owns:** issuing and expiring access tokens. If Airwallex's token endpoint is unavailable, payment requests cannot be initiated.

***

### Common Failure Modes

**Token exchange failure** Symptom: Payment requests fail before reaching Airwallex's payment API. Fix: Verify the API Key and Client ID in Hyperswitch are correct and that your Airwallex account is active. An inactive account will cause token exchange to fail.

**Payment method not available for corridor** Symptom: A payment method works in test but fails in production for a specific country or currency. Fix: Confirm with Airwallex that the specific country-currency corridor is approved for your account.

**FX rate unavailable** Symptom: Cross-currency payments fail with a rate or corridor error. Fix: Airwallex's FX rates are real-time — if a rate is temporarily unavailable, retry or use a fallback currency.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/airwallex.rs`.
