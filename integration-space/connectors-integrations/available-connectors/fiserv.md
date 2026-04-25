---
description: >-
  Accept payments through Fiserv via Juspay Hyperswitch — configure API keys,
  prerequisites, and supported payment methods.
metaLinks:
  alternates:
    - fiserv.md
---

# Fiserv

![logo\_fiserv](https://hyperswitch.io/icons/homePageIcons/logos/fiservLogo.svg)

Fiserv connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication with a per-request HMAC-SHA256 signature. Unlike Bearer token connectors, Fiserv requires Hyperswitch to compute a fresh HMAC-SHA256 signature for every request using the API Secret, and transmit it alongside a millisecond-precision timestamp header. All three credentials — API Key, API Secret, and Merchant ID — are required. All requests use `application/json`.

### Connector-Specific Notes

- **Per-request HMAC-SHA256 signature:** Fiserv does not use a static API key in the Authorization header. For every request, Hyperswitch computes an HMAC-SHA256 signature from the request payload and the API Secret, then sends it in the `Authorization` header along with a `Client-Request-Id` and a millisecond-precision `Timestamp` header. The API Key alone is insufficient — the signature and timestamp are always required.
- **Credentials location:** API Key, API Secret, Merchant ID, and Terminal ID are found in your Fiserv dashboard under **Credentials**.
- **Capture methods supported:** Automatic and Manual.
- **SetupMandate:** Supported for applicable payment methods.
- **3DS support:** Fiserv supports 3DS authentication via Hyperswitch's Pre-Authenticate and Post-Authenticate flows.
- Fiserv is a global fintech and payments company with solutions for banking, merchant acquiring, billing and payments, and point-of-sale.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Fiserv via Hyperswitch

#### Prerequisites

1. You need to be registered with Fiserv. Sign up at [fiserv.com](https://www.fiserv.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Fiserv **API Key**, **API Secret**, **Merchant ID**, and **Terminal ID** are found in your Fiserv dashboard under **Credentials**.
4. Select all payment methods you wish to use Fiserv for. Ensure these match the ones configured in your Fiserv dashboard.

[Steps to activate Fiserv on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, computing the HMAC-SHA256 Authorization signature and Timestamp header on every request, and unified error mapping. **Fiserv owns:** payment execution, fraud decisioning, and validating the HMAC-SHA256 signature and timestamp on each request. Fiserv enforces timestamp recency — requests with stale timestamps are rejected.

**Hyperswitch owns:** generating a valid signature for each request. **Fiserv owns:** validating it. If the API Secret changes in Fiserv and is not updated in Hyperswitch, all requests will fail signature validation immediately. Timestamp drift between Hyperswitch's clock and Fiserv's server time can also cause authentication failures.

---

### Common Failure Modes

**HMAC signature validation failure**
Symptom: All requests fail with a Fiserv authentication or signature error. Fix: Verify all three credentials (API Key, API Secret, Merchant ID) in Hyperswitch exactly match those in your Fiserv dashboard. Any mismatch in the API Secret causes the computed signature to fail validation.

**Timestamp rejected**
Symptom: Requests fail with a timestamp or replay-protection error from Fiserv. Fix: Fiserv validates that the `Timestamp` header is within an acceptable recency window. Ensure the Hyperswitch server clock is synchronized (NTP). A large clock skew will cause every request to be rejected.

**Terminal ID mismatch**
Symptom: Payments fail with a terminal or merchant configuration error. Fix: Verify the Terminal ID in Hyperswitch matches the one configured for your Fiserv merchant account.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Fiserv merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/fiserv.rs`.
