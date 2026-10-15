---
description: Configure HyperPG card payments with Hyperswitch.
metaLinks:
  alternates:
    - hyperpg.md
---

# HyperPG

HyperPG processes credit and debit card payments through Hyperswitch, with automatic capture, refunds and optional 3DS. Mandates are not supported. HyperPG is not offered in the Hyperswitch control center, so you set it up through the API.

To connect HyperPG to your Hyperswitch account, create the connector account as described under Before you start, then return here for what HyperPG supports and how a payment moves.
### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, INR, USD |
| card | Debit Card | supported | supported | automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, INR, USD |

HyperPG runs through the Unified Connector Service ([`ucs_only_connectors`](https://github.com/juspay/hyperswitch/blob/01365da86035c7bb6ebe99126443248d811cbcaf/config/deployments/production.toml#L1099)).

The table reflects the declaration ([`HYPERPG_SUPPORTED_PAYMENT_METHODS`](https://github.com/juspay/hyperswitch/blob/01365da86035c7bb6ebe99126443248d811cbcaf/crates/hyperswitch_connectors/src/connectors/hyperpg.rs#L588-L655)). The service implements authorize, payment sync, refund and refund sync ([flows](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L106-L175)). Capture, void, mandate setup and repeat payments are not implemented ([flow status](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L466-L495)), so every payment is captured automatically and cannot be cancelled through Hyperswitch.

The table marks mandates as supported, but the service cannot set one up, run a repeat payment, or return a mandate reference ([flow status](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L466-L495), [`mandate_reference`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg/transformers.rs#L408)). Treat mandates and recurring payments as not supported through HyperPG.

### Authentication

HyperPG needs three values: a username, a password and a merchant id. The connector form only defines **Username** and **Password** ([`[hyperpg.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/01365da86035c7bb6ebe99126443248d811cbcaf/crates/connector_configs/toml/sandbox.toml#L8171-L8173)), and the service rejects an account that carries no merchant id ([auth mapping](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/types-traits/domain_types/src/router_data.rs#L3577-L3589)). Create the account through the API with `auth_type` set to `SignatureKey`: `api_key` is the username, `key1` the password and `api_secret` the merchant id ([`HyperpgAuthType`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg/transformers.rs#L25-L49)).

The service sends the username as HTTP Basic authentication with an empty password, and the merchant id in the `X-Merchant-Id` header as well as in the request body ([`build_headers`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L137-L158)). The password is stored but not used by any request.

### Before you start

Create or sign in to your [HyperPG account](https://hyperpg.in/) and obtain the username, password and merchant id. HyperPG is not in the control center connector list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)), so there is no activation form: create the connector account through the connector-account API with the three values above.

### Payment flow

Authorize posts the card to `/txns` ([`Authorize`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L254-L283)). When HyperPG returns an authentication link, Hyperswitch redirects the customer to it and the payment is `requires_customer_action` until they return; otherwise the response status applies directly ([redirect](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg/transformers.rs#L390-L400)). HyperPG's charged status maps to charged; new, authorizing, pending and pending-VBV to pending; failed, authorization-failed and authentication-failed to the matching failures; and cancelled to voided ([`HyperpgPaymentStatus`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg/transformers.rs#L83-L108)).

A sync reads `/orders/{order_id}` using the order id the authorize response returned ([`PSync`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L285-L314)). A refund posts to `/orders/{order_id}/refunds` ([`Refund`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L316-L362)), and refund sync maps HyperPG's pending, success and failed to the same Hyperswitch states ([`RSync`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L364-L393), [`HyperpgRefundStatus`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg/transformers.rs#L113-L126)).

### Webhooks

HyperPG webhooks are not supported. The service's webhook handler is empty ([`IncomingWebhook for Hyperpg`](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs#L80-L83)), so a callback is answered with the trait default, `WebhooksNotImplemented` ([default](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/types-traits/interfaces/src/connector_types.rs#L647-L653)). Use payment sync and refund sync for status.

### Source reference

The capability declaration and credential labels on this page are tied to Hyperswitch `01365da86035c7bb6ebe99126443248d811cbcaf`. Flow, authentication and webhook behavior is tied to the Unified Connector Service implementation at hyperswitch-prism `6a4b09bf2551defe9f8b315f206d12dcea0abe24`: see [HyperPG service source](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg.rs) and [HyperPG transformers](https://github.com/juspay/hyperswitch-prism/blob/6a4b09bf2551defe9f8b315f206d12dcea0abe24/crates/integrations/connector-integration/src/connectors/hyperpg/transformers.rs).
