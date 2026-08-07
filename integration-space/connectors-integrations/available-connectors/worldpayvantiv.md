---
description: >-
  Accept card payments in North America through Worldpay Vantiv (formerly
  Vantiv/Litle) via Juspay Hyperswitch — XML-based CNP Online protocol with
  multi-credential authentication.
metaLinks:
  alternates:
    - worldpayvantiv.md
---

# Worldpay Vantiv

Worldpay Vantiv connects to Hyperswitch as a `PaymentGateway` connector using `MultiAuthKey` authentication — Username, Password, and Merchant ID are all required and embedded in every XML request body. Unlike connectors that use HTTP header auth, Worldpay Vantiv uses the CNP Online XML protocol (version 12.23) with the `http://www.vantivcnp.com/schema` namespace. All requests and responses use `text/xml`. Worldpay Vantiv does not support inbound webhooks — payment status is retrieved via sync polling.

### Connector-Specific Notes

- **XML-based protocol:** Worldpay Vantiv uses the CNP (Card Not Present) Online XML schema, not a JSON REST API. Hyperswitch serializes every request into the `CnpOnlineRequest` XML structure and deserializes responses from `CnpOnlineResponse`. The protocol version is fixed at 12.23.
- **Credentials embedded in XML body:** Username, Password, and Merchant ID are placed inside the `<authentication>` element of each XML request. There is no separate Authorization HTTP header for auth.
- **Credentials location:** Username, Password, and Merchant ID are found in your Worldpay Vantiv dashboard.
- **No webhook support:** Worldpay Vantiv does not deliver inbound webhooks. Payment status updates are retrieved by Hyperswitch via sync polling against Worldpay Vantiv's reporting endpoint.
- **Secondary base URL for report sync:** Worldpay Vantiv uses a separate reporting endpoint for payment status sync — distinct from the primary transaction processing URL.
- **Capture methods supported:** Automatic and Manual.
- **SetupMandate:** Supported for applicable payment methods.
- **Dispute support:** Submit evidence is supported through Hyperswitch's unified dispute interface.
- Worldpay Vantiv specializes in card-not-present (CNP) payments and is widely used for North American e-commerce and enterprise acquiring.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Worldpay Vantiv via Hyperswitch

#### Prerequisites

1. You need to be registered with Worldpay Vantiv. Sign up at [worldpayvantiv.com](https://www.worldpayvantiv.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Worldpay Vantiv **Username**, **Password**, and **Merchant ID** are found in your Worldpay Vantiv dashboard.
4. Select all payment methods you wish to use Worldpay Vantiv for. Ensure these match the ones configured in your Worldpay Vantiv dashboard.

[Steps to activate Worldpay Vantiv on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, serializing every request into the CNP Online XML schema with credentials embedded, and unified error mapping. **Worldpay Vantiv owns:** payment execution, card authorization, and the XML protocol validation — including schema version enforcement. A malformed XML request or schema version mismatch is rejected immediately by Worldpay Vantiv.

**Hyperswitch owns:** polling Worldpay Vantiv's reporting endpoint for payment status (no webhooks available). **Worldpay Vantiv owns:** making the transaction status available via the reporting API. If the reporting endpoint is unavailable, payment status cannot be updated until polling resumes.

---

### Common Failure Modes

**Authentication failure in XML body**
Symptom: All requests fail with a Worldpay Vantiv authentication error. Fix: Verify all three credentials (Username, Password, Merchant ID) in Hyperswitch match exactly what is configured in your Worldpay Vantiv dashboard. Credentials are embedded in the XML body, not HTTP headers — any mismatch causes immediate rejection.

**Payment status not updating**
Symptom: Payments are processed but status remains pending in Hyperswitch. Fix: Since Worldpay Vantiv does not push webhooks, status is updated via polling. Ensure Hyperswitch's sync polling is running and the secondary reporting endpoint is reachable.

**XML schema validation error**
Symptom: Requests fail with a schema or protocol version error from Worldpay Vantiv. Fix: This is typically caused by a Worldpay Vantiv API change. Check for protocol version updates and contact Worldpay Vantiv support to verify whether your account requires a specific version.

**Payment method not available**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Worldpay Vantiv merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs`.
