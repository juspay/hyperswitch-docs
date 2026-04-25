---
description: >-
  Connect TrustPay with Juspay Hyperswitch to accept secure e-commerce payments
  across the EEA with support for multiple payment methods and cross-border
  reach.
metaLinks:
  alternates:
    - trustpay.md
---

# TrustPay

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/trustpayLogo.svg" alt=""></div>

TrustPay connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication with three credentials: API Key, Project ID, and Secret Key. Authentication is dual-mode depending on payment method. Card payments use `X-API-Key: {api_key}` with `application/x-www-form-urlencoded` content. Bank redirect and bank transfer payments use an OAuth Bearer access token (`Authorization: Bearer {token}`) with `application/json` content. TrustPay is a European payment institution offering secure e-commerce payments and cross-border payment solutions across the EEA.

### Connector-Specific Notes

* **Dual authentication mode:** The auth header sent depends on the payment method. For card payments, Hyperswitch sends `X-API-Key: {api_key}` and form-encoded content. For bank redirect and bank transfer payments, Hyperswitch exchanges credentials for a Bearer access token and sends `Authorization: Bearer {token}` with JSON content.
* **Project ID and Secret Key:** These are used in bank redirect flows for a HMAC-based signature on the payment body (Project ID and Secret Key are combined to produce the `notification_signature`). They are not sent directly in headers.
* **Credentials location:** API Key, Project ID, and Secret Key are found in your TrustPay dashboard.
* **Webhook verification:** TrustPay delivers webhook events to Hyperswitch using HMAC-SHA256 verification. Configure the Hyperswitch webhook endpoint in your TrustPay dashboard.
* **Capture methods supported:** Automatic and SequentialAutomatic. Manual capture is not supported.
* TrustPay belongs to the first financial institutions in the EEA region to provide secure e-commerce payments. They offer innovative payment services with cross-border reach and a variety of payment methods.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating TrustPay via Hyperswitch

#### Prerequisites

1. You need to be registered with TrustPay. Sign up at [trustpay.eu](https://www.trustpay.eu/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. TrustPay **API Key**, **Project ID**, and **Secret Key** are found in your TrustPay dashboard.
4. Select all payment methods you wish to use TrustPay for. Ensure these match the ones configured in your TrustPay dashboard.

[Steps to activate TrustPay on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, selecting the correct auth mode per payment method (X-API-Key for cards, Bearer token for bank redirects/transfers), retry scheduling, webhook HMAC verification, and unified error mapping. **TrustPay owns:** token issuance, payment execution, fraud decisioning, and settlement.

**Hyperswitch owns:** presenting the correct credentials for each payment type. **TrustPay owns:** validating the API Key on card flows and the Bearer token on bank redirect/transfer flows. If any credential changes in TrustPay and is not updated in Hyperswitch, the corresponding payment methods will fail authentication.

***

### Common Failure Modes

**Card authentication failure** Symptom: Card payment requests fail with a TrustPay authentication error. Fix: Verify the API Key in Hyperswitch matches the one in your TrustPay dashboard. Card payments use `X-API-Key` header — ensure the key is entered in the API Key field (not Project ID or Secret Key).

**Bank redirect/transfer token failure** Symptom: Bank redirect or bank transfer payments fail before reaching the payment API. Fix: Verify the Project ID and Secret Key in Hyperswitch match what is configured in your TrustPay dashboard. An incorrect credential causes the token exchange or signature to fail.

**Webhook verification failure** Symptom: TrustPay events arrive at Hyperswitch but payment statuses do not update. Fix: Verify the Hyperswitch webhook endpoint URL is configured correctly in your TrustPay dashboard and that the webhook HMAC secret matches.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/trustpay.rs`.
