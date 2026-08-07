---
description: >-
  Connect Checkout.com as a payment connector on Hyperswitch to accept global
  payments via its end-to-end gateway, acquirer, and processor solution.
metaLinks:
  alternates:
    - checkout.md
---

# Checkout

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/checkoutLogo.svg" alt=""></div>

Checkout.com connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication — three credentials are required: API Key, Processing Channel ID, and Secret Key. The API Key is passed as `Authorization: Bearer {api_key}` on payment requests; the Processing Channel ID identifies which Checkout.com channel the payment is routed to. All requests use `application/json`. Checkout.com is one of two connectors in Hyperswitch (alongside Adyen) that supports `ManualMultiple` capture — authorizing once and capturing in multiple partial steps.

### Connector-Specific Notes

* **Three-credential auth:** API Key (Bearer token for requests), Processing Channel ID (identifies the processing channel), and Secret Key (used for webhook signature verification). All three are found in your Checkout.com dashboard under [Developers](https://dashboard.sandbox.checkout.com/developers/get-started).
* **ManualMultiple capture:** Checkout.com supports capturing a single authorization in multiple partial steps, controlled via `capture_method: manual_multiple` in Hyperswitch. Capture methods supported: Automatic, Manual, SequentialAutomatic, ManualMultiple.
* **Raw card data:** Checkout.com requires explicit enablement of raw card data handling. Contact Checkout.com support at support@checkout.com to enable this before processing card payments through Hyperswitch.
* **Dispute evidence upload:** Checkout.com supports the full dispute evidence flow — file upload followed by evidence submission against the dispute ID. Both steps are handled through Hyperswitch's unified disputes interface.
* **Webhook verification:** Checkout.com signs webhook events using the Secret Key. Hyperswitch verifies incoming webhooks using this key — store it separately from the API Key in the Hyperswitch connector configuration.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating Checkout.com via Hyperswitch

#### Prerequisites

1. You need to be registered with Checkout.com. Sign up at [checkout.com/get-test-account](https://www.checkout.com/get-test-account).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. Request the Checkout.com support team to enable raw card data handling via email (support@checkout.com).
4. Your Checkout.com API key, Processing Channel ID, and Secret Key are available in your Checkout.com dashboard under the [Developers section](https://dashboard.sandbox.checkout.com/developers/get-started).
5. To configure a webhook endpoint, navigate to the webhooks section of your Checkout.com dashboard and create a new webhook.

[Steps to activate Checkout.com on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and webhook fan-out to your endpoint. **Checkout.com owns:** payment execution, fraud evaluation, and webhook delivery to Hyperswitch's endpoint. The Processing Channel ID determines which Checkout.com business unit processes the payment — Hyperswitch passes this on every request but has no visibility into how Checkout.com routes internally based on it.

**Hyperswitch owns:** dispute case tracking and evidence submission orchestration. **Checkout.com owns:** dispute resolution, chargeback adjudication, and final outcome. File evidence submitted via Hyperswitch is forwarded to Checkout.com's dispute API — the final chargeback decision is made entirely by Checkout.com.

***

### Common Failure Modes

**Raw card data not enabled** Symptom: Card payments fail before authorization. Fix: Contact Checkout.com support (support@checkout.com) to enable raw card data handling for your account.

**Wrong Processing Channel ID** Symptom: Payments fail with a channel or merchant configuration error. Fix: Verify the Processing Channel ID in Hyperswitch matches the channel in your Checkout.com dashboard. Each business unit has a distinct channel ID.

**Secret Key mismatch for webhooks** Symptom: Checkout.com webhooks are received but rejected — payment statuses do not update. Fix: Ensure the Secret Key stored in Hyperswitch matches the webhook signing key in your Checkout.com dashboard.

**ManualMultiple capture exceeds authorized amount** Symptom: A partial capture call fails with an amount error. Fix: The sum of all partial captures cannot exceed the originally authorized amount — Checkout.com enforces this at the API level.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/checkout.rs`.
