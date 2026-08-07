---
description: >-
  Accept payments through Bank of America via Juspay Hyperswitch — CyberSource-
  family HTTP Signature authentication with three credentials.
metaLinks:
  alternates:
    - boa.md
---

# Bank of America

Bank of America connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication with the same HTTP Signature scheme as CyberSource. Hyperswitch computes an HMAC-SHA256 signature over canonical request headers and body, sends it as a standalone `Signature: keyid="{api_key}",algorithm="HmacSHA256",headers="{headers}",signature="{value}"` header, and sends the Merchant ID separately in a `v-c-merchant-id` header. All three credentials — API Key, Merchant ID, and Shared Secret — are required. All requests use `application/json;charset=utf-8`.

### Connector-Specific Notes

- **HTTP Signature authentication (CyberSource-family):** Bank of America uses the same `GCS`-style HTTP Signature scheme as CyberSource. The API Key appears in the `Signature` header as the `keyid` value (lowercase). The Shared Secret (api_secret) is Base64-decoded and used as the HMAC-SHA256 signing key. The Merchant ID is sent as the `v-c-merchant-id` header, not in the Authorization or Signature header.
- **Credentials location:** API Key and Shared Secret are generated under **Payment Configuration → Key Management** in the Bank of America developer dashboard. Merchant ID appears at the top of the dashboard once logged in.
- **SetupMandate:** Supported for applicable payment methods.
- **Webhook support:** Webhooks are not implemented for Bank of America. Payment status is not pushed via webhook — rely on sync polling.
- **Capture methods supported:** Automatic and Manual.
- Bank of America's payment gateway is based on the CyberSource platform. Credentials are managed through the developer.cybersource.com portal.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Bank of America via Hyperswitch

#### Prerequisites

1. You need to be registered with Bank of America. Access the developer portal at [developer.cybersource.com](https://developer.cybersource.com/hello-world/sandbox.html).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. **Merchant ID** — found at the top of the dashboard once logged in.
4. **API Key** and **Shared Secret** — generated under **Payment Configuration → Key Management**.
5. Select all payment methods you wish to use Bank of America for. Ensure these match the ones configured in your Bank of America dashboard.

[Steps to activate Bank of America on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate reference storage, computing the HMAC-SHA256 Signature header on every request, and unified error mapping. **Bank of America owns:** payment execution, fraud decisioning, and signature validation. If any credential changes in the Bank of America dashboard and is not updated in Hyperswitch, all requests will fail signature validation immediately.

**Hyperswitch owns:** polling for payment status (no webhook delivery). **Bank of America owns:** making payment status available via the sync endpoint. All status updates rely on Hyperswitch's sync polling.

---

### Common Failure Modes

**HTTP Signature validation failure**
Symptom: All requests return a Bank of America authentication error. Fix: Verify all three credentials (API Key, Merchant ID, Shared Secret) in Hyperswitch match exactly what is configured in the developer dashboard. Any mismatch causes the computed signature to fail validation.

**Merchant ID mismatch**
Symptom: Requests fail with a merchant configuration error. Fix: The Merchant ID is sent as the `v-c-merchant-id` header on every request. Verify it matches the Merchant ID shown at the top of your Bank of America developer dashboard.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Bank of America merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/bankofamerica.rs`.
