---
description: >-
  Accept payments globally through BlueSnap via Juspay Hyperswitch, supporting
  e-commerce, subscription billing, and mobile payments.
metaLinks:
  alternates:
    - bluesnap.md
---

# Bluesnap

![BlueSnap Logo](https://hyperswitch.io/icons/homePageIcons/logos/bluesnapLogo.svg)

BlueSnap connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication — the API Username and Password are combined as `{username}:{password}`, Base64-encoded, and sent as `Authorization: Basic {encoded}` on every request. All requests use `application/json`. BlueSnap is a global payment platform supporting e-commerce, subscription billing, and mobile payments.

### Connector-Specific Notes

- **HTTP Basic auth with username and password:** BlueSnap's `BodyKey` auth concatenates the API Username (key1) and API Password (api_key) in Basic auth format: `Authorization: Basic base64(username:password)`. Both credentials are required — the username alone or password alone will cause authentication failure.
- **Credentials location:** API Username and API Password are found in your BlueSnap dashboard under **API Settings**.
- **Webhook support:** BlueSnap delivers webhook events to Hyperswitch. Configure the Hyperswitch webhook endpoint in your BlueSnap dashboard.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- BlueSnap provides end-to-end payment processing with built-in conversion optimization, fraud prevention, and global payment method coverage.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating BlueSnap via Hyperswitch

#### Prerequisites

1. You need to be registered with BlueSnap. Sign up at [home.bluesnap.com](https://home.bluesnap.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. BlueSnap **API Username** and **API Password** are found in your BlueSnap dashboard under **API Settings**.
4. Select all payment methods you wish to use BlueSnap for. Ensure these match the ones configured in your BlueSnap dashboard under **Checkout Page → Payment Methods**.

[Steps to activate BlueSnap on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate reference storage, constructing the Base64-encoded Basic authorization header on every request, and unified error mapping. **BlueSnap owns:** payment execution, fraud decisioning, and webhook delivery to Hyperswitch's endpoint.

**Hyperswitch owns:** embedding credentials correctly in every request header. **BlueSnap owns:** validating the username and password combination. If either credential changes in BlueSnap and is not updated in Hyperswitch, all requests will fail authentication immediately.

---

### Common Failure Modes

**Authentication failure**
Symptom: All requests fail with a BlueSnap 401 or authentication error. Fix: Verify both the API Username and API Password in Hyperswitch match exactly what is configured in your BlueSnap dashboard under **API Settings**. Do not manually Base64-encode them before entering in the control center.

**Webhook events not processed**
Symptom: BlueSnap events arrive at Hyperswitch but payment statuses do not update. Fix: Verify the Hyperswitch webhook endpoint is correctly configured in your BlueSnap dashboard.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your BlueSnap merchant account and matches the selection in the Hyperswitch connector configuration under **Checkout Page → Payment Methods**.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/bluesnap.rs`.
