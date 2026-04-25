---
description: >-
  Accept payments globally through Worldline via Juspay Hyperswitch — enabling
  in-store, online, and omnichannel payment solutions with increased conversion
  and approval rates.
metaLinks:
  alternates:
    - worldline.md
---

# Worldline

![logo\_worldline](https://hyperswitch.io/icons/homePageIcons/logos/worldlineLogo.svg)

Worldline connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication with a custom HMAC-SHA256 scheme. The `Authorization` header uses the format `GCS v1HMAC:{api_key_id}:{signed_data}` where `signed_data` is an HMAC-SHA256 signature of the canonical request. All three credentials — API Key ID, Secret API Key, and Merchant ID — are required. Worldline also verifies inbound webhooks using HMAC-SHA256.

### Connector-Specific Notes

- **Custom HMAC signature scheme:** Worldline uses a `GCS v1HMAC` authorization scheme, not a standard Bearer token. Hyperswitch computes the canonical request string (HTTP method + content-type + date + request path) and signs it with HMAC-SHA256 using the Secret API Key. The API Key ID is included in the header to identify which key was used for signing.
- **Credentials location:** API Key ID, Secret API Key, and Merchant ID are found in your Worldline dashboard under **API Keys**.
- **Webhook verification:** Worldline uses HMAC-SHA256 to sign webhook events. Hyperswitch verifies inbound Worldline webhooks using the Secret API Key.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- Worldline supports online, in-store, and omnichannel payment scenarios with a strong presence in Europe.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Worldline via Hyperswitch

#### Prerequisites

1. You need to be registered with Worldline. Sign up at [worldline.com](https://worldline.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Worldline **API Key ID**, **Secret API Key**, and **Merchant ID** are found in your Worldline dashboard under **API Keys**.
4. Select all payment methods you wish to use Worldline for. Ensure these match the ones configured in your Worldline dashboard.

[Steps to activate Worldline on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, HMAC signature construction on every request, and unified error mapping. **Worldline owns:** payment execution, fraud decisioning, and webhook delivery to Hyperswitch's endpoint. Worldline's fraud layer runs before authorization — a fraud-declined payment is not an authorization failure and cannot be retried automatically.

**Hyperswitch owns:** computing the `GCS v1HMAC` signature on every request. **Worldline owns:** validating it. If the Secret API Key changes in Worldline and is not updated in Hyperswitch, all requests will fail signature validation immediately.

---

### Common Failure Modes

**HMAC signature validation failure**
Symptom: All requests fail with a Worldline authentication error. Fix: Verify all three credentials (API Key ID, Secret API Key, Merchant ID) in Hyperswitch match exactly what is configured in your Worldline dashboard. Any mismatch causes the computed signature to fail validation.

**Webhook verification failure**
Symptom: Worldline webhooks arrive at Hyperswitch but are rejected — payment statuses do not update. Fix: Ensure the Secret API Key stored in Hyperswitch is the same key Worldline uses to sign webhook events.

**Payment method not available**
Symptom: A payment method fails with an availability error from Worldline. Fix: Verify the method is enabled for your Worldline merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/worldline.rs`.
