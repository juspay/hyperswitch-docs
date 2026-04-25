---
description: >-
  Learn how to activate Rapyd as a payment connector on Juspay Hyperswitch to
  accept and send global payments across multiple payment methods.
metaLinks:
  alternates:
    - rapyd.md
---

# Rapyd

![logo\_rapyd](https://hyperswitch.io/icons/homePageIcons/logos/rapydLogo.svg)

Rapyd connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication — an Access Key and Secret Key are used to generate a per-request HMAC-SHA256 signature. The signature is computed as `HMAC-SHA256(secret_key, "{method}{url_path}{salt}{timestamp}{access_key}{secret_key}{body}")`, hex-encoded, then URL-safe Base64-encoded. Per-request `access_key`, `salt`, `timestamp`, and `signature` values are sent as individual HTTP headers on every request (no static Authorization header). All requests use `application/json`. Rapyd is a global payment network enabling businesses to accept and send payments across 100+ countries and 900+ payment methods.

### Connector-Specific Notes

- **Per-request HMAC signature:** Rapyd does not use a static Authorization header. Each request requires a freshly computed signature. Hyperswitch generates the `salt` (random 12-character alphanumeric), captures the `timestamp` (Unix epoch), computes the HMAC-SHA256 signature, and sends all four values — `access_key`, `salt`, `timestamp`, `signature` — as individual headers on every request.
- **Signature construction:** `to_sign = "{http_method}{url_path}{salt}{timestamp}{access_key}{secret_key}{body}"`. The HMAC is keyed with `secret_key` using SHA-256, hex-encoded, then URL-safe Base64-encoded before sending.
- **Credentials location:** Access Key and Secret Key are found in your Rapyd dashboard under **Developers > Access & Secret Keys**.
- **Webhook verification:** Rapyd delivers webhook events to Hyperswitch using HMAC-SHA256 verification. Configure the Hyperswitch webhook endpoint in your Rapyd dashboard.
- **Capture methods supported:** Automatic, Manual, and SequentialAutomatic.
- Rapyd allows businesses to accept and send payments to any business or consumer entity anywhere in a faster, cheaper, and easier manner.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Rapyd via Hyperswitch

#### Prerequisites

1. You need to be registered with Rapyd. Sign up at [rapyd.net](https://www.rapyd.net/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Rapyd **Access Key** and **Secret Key** are found in your Rapyd dashboard under **Developers > Access & Secret Keys**.
4. Select all payment methods you wish to use Rapyd for. Ensure these match the ones configured in your Rapyd dashboard.

[Steps to activate Rapyd on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, per-request salt and timestamp generation, HMAC-SHA256 signature computation on every request, retry scheduling, and unified error mapping. **Rapyd owns:** payment execution, payment method routing, and cross-border settlement.

**Hyperswitch owns:** sending correctly signed requests using the Access Key and Secret Key. **Rapyd owns:** validating the signature on every request. If either credential changes in Rapyd and is not updated in Hyperswitch, all requests will fail signature validation immediately.

---

### Common Failure Modes

**Signature validation failure**
Symptom: All requests fail with a Rapyd authentication or signature error. Fix: Verify the Access Key and Secret Key in Hyperswitch match exactly what is shown in your Rapyd dashboard under **Developers > Access & Secret Keys**. The signature is recomputed fresh on every request — any credential mismatch causes immediate failure.

**Webhook verification failure**
Symptom: Rapyd events arrive at Hyperswitch but payment statuses do not update. Fix: Verify the Hyperswitch webhook endpoint URL is configured correctly in your Rapyd dashboard and that the webhook secret matches.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Rapyd account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/rapyd.rs`.
