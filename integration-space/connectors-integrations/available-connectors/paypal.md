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

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 42bbdc2c61a2fe968791a4bb9ea2d586064aeaea; host http://127.0.0.1:8080; fetched 2026-09-03; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live  
**Category:** payment gateway  
**Webhook flows:** disputes, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | EPS | not supported | supported | automatic, sequential automatic | not applicable | - | 195 ([full list](https://hyperswitch.io/pm-list)) | 24 ([full list](https://hyperswitch.io/pm-list)) |
| bank redirect | Giropay | not supported | supported | automatic, sequential automatic | not applicable | - | - | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, sequential automatic | not applicable | - | - | EUR |
| bank redirect | Sofort | not supported | supported | automatic, sequential automatic | not applicable | - | 195 ([full list](https://hyperswitch.io/pm-list)) | 24 ([full list](https://hyperswitch.io/pm-list)) |
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 195 ([full list](https://hyperswitch.io/pm-list)) | 24 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 195 ([full list](https://hyperswitch.io/pm-list)) | 24 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | PayPal | supported | supported | automatic, manual, sequential automatic | not applicable | - | 195 ([full list](https://hyperswitch.io/pm-list)) | 24 ([full list](https://hyperswitch.io/pm-list)) |

### Connector-Specific Notes

* **OAuth2 token exchange:** PayPal uses Client ID and Client Secret to obtain a Bearer access token. Hyperswitch handles the token exchange and refresh internally — configure the Client ID and Client Secret in the control center, not the token itself. The token endpoint uses form-encoded requests; payment API requests use JSON.
* **Credentials location:** PayPal Client Secret and Client ID are found in your PayPal Developer dashboard.
* **Webhook events:** PayPal declares payment, refund, and dispute webhook flows in the generated block. At the block SHA, `get_webhook_event_type()` handles 25 exact-string verified PayPal event serde names: `CUSTOMER.DISPUTE.RESOLVED`, `CUSTOMER.DISPUTE.CREATED`, `RISK.DISPUTE.CREATED`, `CUSTOMER.DISPUTE.UPDATED`, `PAYMENT.AUTHORIZATION.CREATED`, `PAYMENT.AUTHORIZATION.VOIDED`, `PAYMENT.CAPTURE.DECLINED`, `PAYMENT.CAPTURE.COMPLETED`, `PAYMENT.CAPTURE.PENDING`, `PAYMENT.CAPTURE.REFUNDED`, `CHECKOUT.ORDER.APPROVED`, `CHECKOUT.ORDER.COMPLETED`, `CHECKOUT.ORDER.PROCESSED`, `PAYMENT.PAYOUTSBATCH.DENIED`, `PAYMENT.PAYOUTSBATCH.PROCESSING`, `PAYMENT.PAYOUTSBATCH.SUCCESS`, `PAYMENT.PAYOUTS-ITEM.BLOCKED`, `PAYMENT.PAYOUTS-ITEM.CANCELED`, `PAYMENT.PAYOUTS-ITEM.DENIED`, `PAYMENT.PAYOUTS-ITEM.FAILED`, `PAYMENT.PAYOUTS-ITEM.HELD`, `PAYMENT.PAYOUTS-ITEM.REFUNDED`, `PAYMENT.PAYOUTS-ITEM.RETURNED`, `PAYMENT.PAYOUTS-ITEM.SUCCEEDED`, `PAYMENT.PAYOUTS-ITEM.UNCLAIMED`. The handler maps those variants to Hyperswitch incoming webhook events in `get_payapl_webhooks_event()`; payout event variants in this list are gated by the `payouts` feature. See the event handler (https://github.com/juspay/hyperswitch/blob/42bbdc2c61a2fe968791a4bb9ea2d586064aeaea/crates/hyperswitch_connectors/src/connectors/paypal.rs#L2403-L2455), serde names (https://github.com/juspay/hyperswitch/blob/42bbdc2c61a2fe968791a4bb9ea2d586064aeaea/crates/hyperswitch_connectors/src/connectors/paypal/transformers.rs#L3754-L3819), and event mapping (https://github.com/juspay/hyperswitch/blob/42bbdc2c61a2fe968791a4bb9ea2d586064aeaea/crates/hyperswitch_connectors/src/connectors/paypal/transformers.rs#L3963-L4011). An empty webhook body returns `EndpointVerification` before payload parsing (https://github.com/juspay/hyperswitch/blob/42bbdc2c61a2fe968791a4bb9ea2d586064aeaea/crates/hyperswitch_connectors/src/connectors/paypal.rs#L2408-L2410). Webhook source verification is implemented by posting a `PaypalSourceVerificationRequest` to PayPal's `v1/notifications/verify-webhook-signature` endpoint and parsing `PaypalSourceVerificationResponse`, not by accepting the webhook without verification (https://github.com/juspay/hyperswitch/blob/42bbdc2c61a2fe968791a4bb9ea2d586064aeaea/crates/hyperswitch_connectors/src/connectors/paypal.rs#L2234-L2325).
* **Incremental authorization:** PayPal supports incrementally increasing an authorized amount before capture. Available via Hyperswitch's `IncrementalAuthorization` flow — requires `capture_method: manual` on the original payment.
* **Payouts:** PayPal supports payout creation, fulfillment, and sync through Hyperswitch's unified payouts interface.

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
