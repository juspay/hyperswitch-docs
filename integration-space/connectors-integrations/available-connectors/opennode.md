---
description: >-
  Accept bitcoin payments and send bitcoin payouts through OpenNode via Juspay
  Hyperswitch — instant, secure, and low-cost crypto payment processing.
metaLinks:
  alternates:
    - opennode.md
---

# OpenNode

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/opennodeLogo.svg" alt=""></div>

OpenNode connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — the API Key is sent as a raw `Authorization: {api_key}` header (without a "Bearer " prefix). All requests use `application/json`. OpenNode provides Bitcoin payment acceptance and payout capabilities for global businesses.

### Connector-Specific Notes

* **Raw Authorization header (no Bearer prefix):** OpenNode does not use the `Authorization: Bearer {key}` format. The API Key is sent as `Authorization: {api_key}` directly. Entering the key in the control center is sufficient — Hyperswitch handles the header format automatically.
* **Credentials location:** API Key is found in your OpenNode dashboard.
* **Webhook verification:** OpenNode delivers webhook events to Hyperswitch using HMAC-SHA256 verification. Configure the Hyperswitch webhook endpoint in your OpenNode dashboard.
* **Capture methods supported:** Automatic only. Manual capture is not supported for Bitcoin payments.
* OpenNode makes it easy to accept Bitcoin payments and send Bitcoin payouts. They provide every business with access to instant, secure, and low-cost Bitcoin payments.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating OpenNode via Hyperswitch

#### Prerequisites

1. You need to be registered with OpenNode. Sign up at [opennode.com](https://www.opennode.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. The OpenNode **API Key** is found in your OpenNode dashboard.
4. Select all payment methods you wish to use OpenNode for. Ensure these match the ones configured in your OpenNode dashboard.

[Steps to activate OpenNode on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, sending the API Key in the Authorization header on every request, and unified error mapping. **OpenNode owns:** Bitcoin charge creation, Lightning Network routing, blockchain settlement confirmation, and webhook delivery.

**Hyperswitch owns:** presenting the correct API Key. **OpenNode owns:** validating it. If the API Key is regenerated in OpenNode and not updated in Hyperswitch, all requests will fail authentication immediately.

***

### Common Failure Modes

**Authentication failure** Symptom: All requests fail with an OpenNode authentication error. Fix: Verify the API Key in Hyperswitch matches the one in your OpenNode dashboard. Note that OpenNode uses a raw Authorization header (no "Bearer " prefix) — the Hyperswitch implementation handles this format automatically.

**Webhook verification failure** Symptom: OpenNode events arrive at Hyperswitch but payment statuses do not update. Fix: Verify the Hyperswitch webhook endpoint URL is configured correctly in your OpenNode dashboard and that the webhook secret matches.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/opennode.rs`.
