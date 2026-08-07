---
description: >-
  Accept payments through PayPal via Juspay Hyperswitch — configure credentials,
  supported payment methods, and activation steps.
metaLinks:
  alternates:
    - paypal.md
---

# Paypal

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/paypalLogo.svg" alt=""></div>

PayPal connects to Hyperswitch as a `PaymentGateway` connector using OAuth2 authentication — Client ID and Client Secret are exchanged for a Bearer access token via PayPal's token endpoint (using `application/x-www-form-urlencoded`), and this token is used on all subsequent payment requests (`application/json`). PayPal supports incremental authorization and payouts — two capabilities available on only a small set of connectors in Hyperswitch.

### Connector-Specific Notes

* **OAuth2 token exchange:** PayPal uses Client ID and Client Secret to obtain a Bearer access token. Hyperswitch handles the token exchange and refresh internally — configure the Client ID and Client Secret in the control center, not the token itself. The token endpoint uses form-encoded requests; payment API requests use JSON.
* **Credentials location:** PayPal Client Secret and Client ID are found in your PayPal Developer dashboard.
* **Incremental authorization:** PayPal supports incrementally increasing an authorized amount before capture. Available via Hyperswitch's `IncrementalAuthorization` flow — requires `capture_method: manual` on the original payment.
* **Payouts:** PayPal supports payout creation, fulfillment, and sync through Hyperswitch's unified payouts interface.
* **Capture methods supported:** Automatic and SequentialAutomatic for most payment methods; Automatic, Manual, and SequentialAutomatic for cards.
* **SetupMandate:** Supported for applicable payment methods.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating PayPal via Hyperswitch

#### Prerequisites

1. You need to be registered with PayPal. Access the developer dashboard at [developer.paypal.com](https://developer.paypal.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. PayPal's **Client Secret** and **Client ID** are found in your PayPal developer dashboard.
4. Select all payment methods you wish to use PayPal for. Ensure these match the ones configured in your PayPal dashboard.

[Steps to activate PayPal on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, OAuth2 token lifecycle management (exchange and refresh), retry scheduling, mandate record storage, and unified error mapping. **PayPal owns:** payment execution, buyer protection and dispute management, payout disbursement, and access token issuance. PayPal's buyer protection policies apply to transactions processed through Hyperswitch — these are managed entirely by PayPal, not Hyperswitch.

**Hyperswitch owns:** initiating the token exchange before each session. **PayPal owns:** issuing and expiring tokens. If PayPal's token endpoint is unavailable, payment requests cannot be initiated. PayPal token expiry is handled by Hyperswitch automatically — manual token management is not required.

***

### Common Failure Modes

**OAuth2 token exchange failure** Symptom: Payment requests fail before reaching PayPal's payment API. Fix: Verify the Client ID and Client Secret in Hyperswitch are correct and match the credentials in your PayPal developer dashboard. Ensure you are using live credentials for production and sandbox credentials for testing.

**Incremental authorization with automatic capture** Symptom: Incremental authorization call fails. Fix: Incremental authorization requires `capture_method: manual` on the original payment. PayPal does not support incremental authorization on automatically-captured payments.

**Payout failure — missing recipient details** Symptom: Payout fails with a PayPal validation error. Fix: Ensure all required recipient fields (PayPal email, or recipient wallet details) are populated before initiating the payout via Hyperswitch.

**Payment method mismatch** Symptom: A payment method enabled in Hyperswitch fails with an availability error from PayPal. Fix: Verify the method is active in your PayPal account and matches the configuration in Hyperswitch.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/paypal.rs`.
