---
description: >-
  Accept payments through Bambora (a Worldline solution) via Juspay Hyperswitch
  — configure Merchant ID and Passcode credentials.
metaLinks:
  alternates:
    - bambora.md
---

# Bambora

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/bamboraLogo.svg" alt=""></div>

Bambora connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication with a custom `Passcode` scheme. The Merchant ID and Passcode are combined as `{merchant_id}:{passcode}`, Base64-encoded, and sent as `Authorization: Passcode {encoded}` on every request. All requests use `application/json`. Bambora is a Worldline solution.

### Connector-Specific Notes

* **Passcode auth scheme:** Bambora uses a custom `Passcode` header value (not HTTP Basic or Bearer). The authorization header format is `Authorization: Passcode {base64(merchant_id:passcode)}`. Both the Merchant ID and Passcode are required — neither alone is sufficient. Do not manually encode them before entering in the control center; Hyperswitch performs the encoding automatically.
* **Credentials location:** Merchant ID and Passcode are found in your Bambora dashboard.
* **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
* **SetupMandate:** Not supported.
* **Webhook support:** Webhooks are not implemented for Bambora — payment status is not pushed via webhook.
* Bambora is a Worldline solution that provides digital payment and transactional solutions.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating Bambora via Hyperswitch

#### Prerequisites

1. You need to be registered with Bambora. Sign up at [bambora.com](https://www.bambora.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Bambora **Merchant ID** and **Passcode** are found in your Bambora dashboard.
4. Select all payment methods you wish to use Bambora for. Ensure these match the ones configured in your Bambora dashboard.

[Steps to activate Bambora on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, constructing the Base64-encoded `Passcode` authorization header on every request, and unified error mapping. **Bambora owns:** payment execution, card authorization, and refund processing. Bambora validates the Merchant ID and Passcode on every request — a mismatch fails immediately.

**Hyperswitch owns:** polling for payment status (no webhook delivery). **Bambora owns:** making payment status available via the sync endpoint. Since webhooks are not supported, all status updates depend on Hyperswitch's sync polling — a delayed sync may result in stale payment status in Hyperswitch.

***

### Common Failure Modes

**Authentication failure** Symptom: All requests fail with a Bambora authentication error. Fix: Verify both the Merchant ID and Passcode in Hyperswitch match exactly what is configured in your Bambora dashboard. Hyperswitch Base64-encodes them automatically — do not manually encode before entering in the control center.

**Payment status not updating** Symptom: Payments remain in a pending state in Hyperswitch. Fix: Since Bambora does not push webhooks, status is updated via sync polling. Ensure Hyperswitch's sync polling is running and the Bambora endpoint is reachable.

**Payment method not configured** Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Bambora merchant account and matches the selection in the Hyperswitch connector configuration.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/bambora.rs`.
