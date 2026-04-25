---
description: >-
  Accept online, in-store, and mobile payments through Worldpay via Juspay
  Hyperswitch with built-in fraud protection.
metaLinks:
  alternates:
    - worldpay.md
---

# Worldpay

![logo\_worldpay](https://hyperswitch.io/icons/homePageIcons/logos/worldpayLogo.svg)

Worldpay (FIS Worldpay) connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication — Username and API Key are combined as `{username}:{api_key}`, Base64-encoded, and sent as an `Authorization: Basic {encoded}` header. All requests use `application/json`. Worldpay supports mandate flows via a CIT→MIT model (SetupMandate → RepeatPayment), multiple captures via a dedicated `/partialSettlements` endpoint, and full 3DS authentication.

### Connector-Specific Notes

- **HTTP Basic auth with combined credentials:** Worldpay's `SignatureKey` auth concatenates the Username (key1) and API Key as `{username}:{api_key}`, Base64-encodes the result, and sends it as `Authorization: Basic {encoded}`. Both credentials are required — neither alone is sufficient.
- **Credentials location:** Worldpay **Username** and **Password (API Key)** are found in your Worldpay dashboard.
- **Multiple capture support:** Worldpay supports partial captures via the `/partialSettlements` endpoint. When multiple captures are requested, Hyperswitch routes to `/partialSettlements` instead of `/settlements`. Each partial capture reduces the authorized amount.
- **Mandate flow — CIT to MIT:** SetupMandate (CIT) stores the payment instrument reference. RepeatPayment (MIT) uses the stored reference to initiate subsequent payments without requiring customer interaction.
- **3DS authentication:** Worldpay supports full 3DS via Hyperswitch's Pre-Authenticate and Post-Authenticate flows. Session tokens are also supported for the checkout session flow.
- **Capture methods supported:** Automatic, Manual, and ManualMultiple.
- **SetupMandate:** Supported for applicable payment methods.
- **Dispute support:** Accept dispute, submit evidence, and dispute defence are all supported.
- Worldpay offers online, in-store, and mobile payment solutions with built-in fraud protection, widely used in Europe and North America.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Worldpay via Hyperswitch

#### Prerequisites

1. You need to be registered with Worldpay. Sign up at [worldpay.com](https://online.worldpay.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Worldpay **Username** and **Password** are found in your Worldpay dashboard.
4. Select all payment methods you wish to use Worldpay for. Ensure these match the ones configured in your Worldpay dashboard.

[Steps to activate Worldpay on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate reference storage (ConnectorMandateId from SetupMandate used in RepeatPayment), constructing the Base64-encoded Authorization header on every request, routing captures to `/settlements` or `/partialSettlements` based on capture type, and unified error mapping. **Worldpay owns:** payment execution, fraud scoring, settlement routing, and token issuance for mandate flows.

**Hyperswitch owns:** sending the correct payment instrument reference in RepeatPayment requests. **Worldpay owns:** validating that the reference is active and matches the original SetupMandate. If a mandate reference expires or is revoked in Worldpay and is not updated in Hyperswitch, RepeatPayment requests will fail.

---

### Common Failure Modes

**Authentication failure**
Symptom: All requests fail with a Worldpay 401 or authentication error. Fix: Verify both the Username and Password (API Key) in Hyperswitch exactly match those in your Worldpay dashboard. Hyperswitch Base64-encodes them automatically — do not manually encode before entering in the control center.

**Partial capture fails**
Symptom: A multiple capture request fails after the first capture. Fix: Ensure the original payment was authorized with `capture_method: manual` and that the sum of partial captures does not exceed the authorized amount.

**RepeatPayment fails — invalid mandate reference**
Symptom: MIT payment fails with a Worldpay token or reference error. Fix: Verify the mandate reference from the original SetupMandate is stored correctly in Hyperswitch and has not been revoked in Worldpay.

**Payment method not configured**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Worldpay merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/worldpay.rs`.
