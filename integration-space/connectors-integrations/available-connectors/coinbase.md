---
description: >-
  Accept crypto payments through Coinbase Commerce via Juspay Hyperswitch, with
  multi-asset support and access to millions of retail users.
metaLinks:
  alternates:
    - coinbase.md
---

# Coinbase

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/coinbaseLogo.svg" alt=""></div>

Coinbase Commerce connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — the API Key is sent in a custom `X-CC-API-Key` header (not `Authorization: Bearer`). All requests also include an `X-CC-Version: 2018-03-22` header that pins the Coinbase Commerce API version. All requests use `application/json`. Coinbase Commerce enables crypto payment acceptance (Bitcoin, Ethereum, and other assets) with access to Coinbase's retail user base.

### Connector-Specific Notes

* **Custom X-CC-API-Key header:** Unlike connectors that use `Authorization: Bearer`, Coinbase Commerce expects the API Key in the `X-CC-API-Key` header specifically. Do not set an Authorization header — it will not authenticate the request.
* **API version pinning:** Every request sends `X-CC-Version: 2018-03-22`. This version is hardcoded in the Hyperswitch implementation to ensure stable API behaviour.
* **Credentials location:** The API Key is found in your Coinbase Commerce dashboard.
* **Webhook support:** Coinbase Commerce delivers webhook events to Hyperswitch. Configure the Hyperswitch webhook endpoint in your Coinbase Commerce settings.
* **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
* **SetupMandate:** Not supported for crypto payments.
* Coinbase Commerce provides reduced operational costs, multi-asset support, and access to Coinbase's millions of retail users.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating Coinbase via Hyperswitch

#### Prerequisites

1. You need to be registered with Coinbase Commerce. Sign up at [coinbase.com/commerce](https://www.coinbase.com/commerce).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. The Coinbase Commerce **API Key** is found in your Coinbase Commerce dashboard.

[Steps to activate Coinbase on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, sending the API Key in the `X-CC-API-Key` header and pinning the API version on every request, and unified error mapping. **Coinbase Commerce owns:** crypto charge creation, blockchain settlement confirmation, and webhook delivery.

**Hyperswitch owns:** presenting the correct API Key in the custom header. **Coinbase Commerce owns:** validating it. If the API Key is regenerated in Coinbase Commerce and not updated in Hyperswitch, all requests will fail authentication immediately.

***

### Common Failure Modes

**Authentication failure** Symptom: All requests fail with a Coinbase Commerce authentication error. Fix: Verify the API Key in Hyperswitch matches the one in your Coinbase Commerce dashboard. Ensure the key is entered in the `X-CC-API-Key` credential field — not formatted as a Bearer token.

**Webhook events not processed** Symptom: Coinbase Commerce events arrive at Hyperswitch but payment statuses do not update. Fix: Verify the Hyperswitch webhook endpoint URL is correctly configured in your Coinbase Commerce settings.

**Payment method not available** Symptom: A specific crypto asset fails with an availability error. Fix: Verify the asset is enabled for your Coinbase Commerce account and matches the selection in the Hyperswitch connector configuration.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/coinbase.rs`.
