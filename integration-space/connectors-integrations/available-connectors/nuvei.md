---
description: >-
  Connect Nuvei to Juspay Hyperswitch to accept payments globally across
  e-commerce and high-growth industries using Nuvei's payment processing and
  acquiring services.
metaLinks:
  alternates:
    - nuvei.md
---

# Nuvei

![logo\_nuvei](https://hyperswitch.io/icons/homePageIcons/logos/nuveiLogo.svg)

Nuvei connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication — API key, site ID, and secret key are combined with a SHA-256 request signature. Unlike Bearer token connectors, Nuvei validates each request using a signature computed from the request parameters and the secret key, included in the request body. All requests use `application/json`. Nuvei also supports payouts through Hyperswitch's unified payouts interface.

### Connector-Specific Notes

- **Request-level signature:** Nuvei does not use a static Bearer token for auth. Each request includes a SHA-256 signature computed from the concatenation of specific request fields and the secret key. The API key and site ID are also required. All three credentials are needed to construct valid requests.
- **Credentials location:** The Nuvei API key is found in your Nuvei dashboard under **Settings → My Account → Account Details**.
- **Payouts:** Nuvei supports payout fulfillment through Hyperswitch's unified payouts interface.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- Payment methods must be enabled in both Hyperswitch and your Nuvei dashboard — a mismatch is the most common source of payment failures.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Nuvei via Hyperswitch

#### Prerequisites

1. You need to be registered with Nuvei. Sign up at [nuvei.com](https://nuvei.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. The Nuvei API key is found in your Nuvei dashboard under **Settings → My Account → Account Details**.
4. Select all payment methods you wish to use Nuvei for. Ensure these match the ones configured in your Nuvei dashboard.

[Steps to activate Nuvei on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, request signature computation, and unified error mapping. **Nuvei owns:** payment execution, fraud scoring, payout disbursement, and the signature validation logic that authenticates each request.

**Hyperswitch owns:** computing the correct SHA-256 signature for every request. **Nuvei owns:** validating it. If the secret key changes in Nuvei and is not updated in Hyperswitch, all requests will fail Nuvei's signature validation.

---

### Common Failure Modes

**Signature validation failure**
Symptom: All requests return a Nuvei authentication or signature error. Fix: Verify that all three credentials (API key, site ID, secret key) in Hyperswitch exactly match those in your Nuvei account. Any mismatch causes the computed signature to fail validation.

**Payment method not enabled**
Symptom: A payment method selected in Hyperswitch fails with a method availability error from Nuvei. Fix: Verify the method is enabled in your Nuvei account configuration and matches the selection in Hyperswitch.

**Payout failure**
Symptom: Payout fulfillment fails at Nuvei. Fix: Ensure all required recipient and payout details are populated before initiating the payout through Hyperswitch.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/nuvei.rs`.
