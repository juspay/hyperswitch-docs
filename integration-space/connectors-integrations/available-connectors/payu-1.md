---
description: >-
  Accept payments through PayU via Juspay Hyperswitch — OAuth-based token
  exchange with Merchant POS ID across multiple payment methods.
metaLinks:
  alternates:
    - payu-1.md
---

# PayU

![logo\_payu](https://hyperswitch.io/icons/homePageIcons/logos/payuLogo.svg)

PayU connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey`-based OAuth token exchange. The API Key (client_secret) and Merchant POS ID are used to obtain a Bearer access token from PayU's token endpoint. The resulting token is used on all payment requests as `Authorization: Bearer {token}`. All requests use `application/json`. PayU is a payment service provider with broad payment method coverage across Central and Eastern Europe, LATAM, and APAC.

### Connector-Specific Notes

- **OAuth token exchange:** PayU does not accept a static API key on payment requests. The API Key (client_secret) and Merchant POS ID are exchanged for a short-lived Bearer access token. Hyperswitch manages token acquisition internally — configure the API Key and Merchant POS ID in the control center, not the token itself.
- **Credentials location:** API Key and Merchant POS ID are found in your PayU dashboard under **My Shops**.
- **Webhook support:** Webhooks are not implemented for PayU in Hyperswitch — payment status relies on sync polling.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- PayU is a payment service provider offering a broad range of payment methods across Central and Eastern Europe, LATAM, and APAC markets.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating PayU via Hyperswitch

#### Prerequisites

1. You need to be registered with PayU. Sign up at [corporate.payu.com](https://corporate.payu.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. PayU **API Key** and **Merchant POS ID** are found in your PayU dashboard under **My Shops**.
4. Select all payment methods you wish to use PayU for. Ensure these match the ones configured in your PayU dashboard.

[Steps to activate PayU on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, token lifecycle management (OAuth exchange using API Key and Merchant POS ID), retry scheduling, mandate reference storage, and unified error mapping. **PayU owns:** token issuance, payment execution, and payment method routing across markets.

**Hyperswitch owns:** performing the token exchange before each payment session. **PayU owns:** validating the API Key and Merchant POS ID, and issuing a valid token. If either credential changes in PayU and is not updated in Hyperswitch, the token exchange will fail and no payments can proceed.

---

### Common Failure Modes

**Token exchange failure**
Symptom: Payment requests fail before reaching the payment API. Fix: Verify the API Key and Merchant POS ID in Hyperswitch match exactly what is configured in your PayU dashboard under **My Shops**. An incorrect API Key causes the token exchange to fail.

**Payment status not updating**
Symptom: Payments remain pending in Hyperswitch. Fix: Since PayU webhooks are not implemented, status is updated via sync polling. Ensure Hyperswitch's sync polling is running and the PayU endpoint is reachable.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your PayU merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/payu.rs`.
