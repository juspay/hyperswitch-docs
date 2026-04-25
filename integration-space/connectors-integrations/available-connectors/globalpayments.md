---
description: >-
  Connect Global Payments with Juspay Hyperswitch to accept over 140 payment
  types across multiple channels with subscription and recurring payment support.
metaLinks:
  alternates:
    - globalpayments.md
---

# GlobalPayments

![logo\_globalPayment](https://hyperswitch.io/icons/homePageIcons/logos/GlobalPaymentsLogo.svg)

Global Payments connects to Hyperswitch as a `PaymentGateway` connector using a `BodyKey`-based OAuth token exchange. The App ID and App Key are used to obtain a short-lived Bearer access token: Hyperswitch generates a random 12-character nonce, computes a SHA-512 digest of `{nonce}{app_key}` (hex-encoded), and submits `{app_id, nonce, secret, grant_type: "client_credentials"}` to the token endpoint. The resulting Bearer token is then used on all payment requests as `Authorization: Bearer {token}` alongside an `X-GP-Version: 2021-03-22` header. All requests use `application/json`.

### Connector-Specific Notes

- **OAuth token exchange with SHA-512 nonce:** Global Payments does not accept a static API key on payment requests. Instead, Hyperswitch exchanges App ID and App Key for a short-lived Bearer token using a nonce-based SHA-512 challenge: `secret = hex(SHA-512({nonce}{app_key}))`. The token is then used on all subsequent payment API calls. If the token endpoint is unavailable, no payment requests can proceed.
- **API version header:** Every request sends `X-GP-Version: 2021-03-22`. This pins the Global Payments API version for consistent behaviour.
- **Credentials location:** App Key, App ID, and Account Name are found in your Global Payments dashboard under **My Account → My Apps & Keys**.
- **Webhook support:** Webhook delivery from Global Payments is supported. Configure the Hyperswitch webhook endpoint in your Global Payments dashboard.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- Global Payments accepts over 140 payment types across multiple channels with industry-specific solutions and subscription support.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Global Payments via Hyperswitch

#### Prerequisites

1. You need to be registered with Global Payments. Sign up at [globalpayments.com](https://www.globalpayments.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Global Payments **App Key**, **App ID**, and **Account Name** are found in your dashboard under **My Account → My Apps & Keys**.
4. Select all payment methods you wish to use Global Payments for. Ensure these match the ones configured in your Global Payments dashboard.

[Steps to activate Global Payments on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, token lifecycle management (SHA-512 nonce exchange to obtain and refresh the Bearer token), retry scheduling, mandate reference storage, and unified error mapping. **Global Payments owns:** token issuance and expiry, payment execution, and webhook delivery.

**Hyperswitch owns:** performing the token exchange before each payment session. **Global Payments owns:** validating the App ID, nonce, and SHA-512 secret, and issuing a valid token. If the App Key changes in Global Payments and is not updated in Hyperswitch, the token exchange will fail and no payments can proceed.

---

### Common Failure Modes

**Token exchange failure**
Symptom: Payment requests fail before reaching the payment API. Fix: Verify the App ID and App Key in Hyperswitch match exactly what is configured in your Global Payments dashboard under **My Account → My Apps & Keys**. An incorrect App Key causes the SHA-512 secret computation to fail validation.

**API version mismatch**
Symptom: Requests fail with a Global Payments version or compatibility error. Fix: The Hyperswitch implementation pins `X-GP-Version: 2021-03-22`. If Global Payments updates its API in a breaking way, contact Hyperswitch support to update the pinned version.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Global Payments merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/globalpay.rs`.
