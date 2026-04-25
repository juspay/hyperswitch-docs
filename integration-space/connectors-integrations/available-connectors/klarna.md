---
description: >-
  Integrate Klarna with Juspay Hyperswitch to offer buy-now-pay-later,
  installment plans, and direct payment options in a seamless checkout
  experience.
metaLinks:
  alternates:
    - klarna.md
---

# Klarna

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/klarnaLogo.svg" alt=""></div>

Klarna connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication — the API Username and Password are combined as `{username}:{password}`, Base64-encoded, and sent as `Authorization: Basic {encoded}` on every request. All requests use `application/json`. Klarna enables buy-now-pay-later, installment plans, and pay-later options with Klarna's native checkout experience.

### Connector-Specific Notes

* **HTTP Basic auth with username and password:** Klarna's `BodyKey` auth maps key1 to the API username and api\_key to the API password. The authorization header is `Authorization: Basic base64(username:password)`. Both credentials are required — neither alone is sufficient.
* **Credentials location:** Klarna API Username and Password are found in your Klarna merchant portal under **Settings → API credentials**.
* **Webhook support:** Webhooks are not implemented for Klarna in Hyperswitch — status updates rely on sync polling.
* **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
* **SetupMandate:** Supported for applicable payment methods.
* Klarna provides direct payments, pay later options, and installment plans in a one-click purchase experience. It is widely used in Europe and North America.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating Klarna via Hyperswitch

#### Prerequisites

1. You need to be registered with Klarna. Sign up at [klarna.com/us/business](https://www.klarna.com/us/business/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Klarna **API Username** and **API Password** are found in your Klarna merchant portal under **Settings → API credentials**.
4. Select all payment methods you wish to use Klarna for. Ensure these match the ones configured in your Klarna merchant portal.

[Steps to activate Klarna on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate reference storage, constructing the Base64-encoded Basic authorization header on every request, and unified error mapping. **Klarna owns:** payment execution, credit risk decisioning for BNPL offers, and settlement. Klarna's credit decision is made before authorization — a Klarna rejection is a pre-authorization outcome, not a card decline.

**Hyperswitch owns:** sending the correct credentials on every request. **Klarna owns:** validating the API username and password. If either credential changes in Klarna and is not updated in Hyperswitch, all requests will fail authentication immediately.

***

### Common Failure Modes

**Authentication failure** Symptom: All requests fail with a Klarna authentication error. Fix: Verify both the API Username and API Password in Hyperswitch match exactly what is configured in your Klarna merchant portal under **Settings → API credentials**. Do not manually Base64-encode them before entering in the control center.

**Klarna credit decision rejection** Symptom: Payment fails with a Klarna-specific rejection code before authorization. Fix: Klarna makes its own credit decision for BNPL payments based on the customer's profile. A rejection here is not a card or gateway failure — it cannot be retried with the same payment method.

**Payment method not available** Symptom: A specific Klarna option (Pay Later, Installments) is not offered for a country or currency. Fix: Verify Klarna's availability for the specific country-currency combination is enabled for your merchant account. Klarna's product availability varies by market.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/klarna.rs`.
