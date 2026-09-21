---
description: >-
  Accept card-redirect payments through Prophetpay using profile-scoped credentials.
metaLinks:
  alternates:
    - prophetpay.md
---

# Prophetpay

{% hint style="warning" %}
**Alpha connector, no production configuration.** Prophetpay has no entry in Hyperswitch's production connector configuration, which is compiled into production builds. It is available in Test mode on the hosted control center. Whether it is offered to you in Live mode depends on how your Hyperswitch deployment was built, so confirm with the Hyperswitch team before planning a live rollout.

It is also at alpha integration status. Reach out on the [Slack Community](https://inviter.co/hyperswitch-slack) to check where it stands before you build on it.
{% endhint %}

Prophetpay uses a hosted card-entry path for one-time payments. Refunds are supported for that path, while mandate reuse is not declared. The connector supports immediate and follow-up automatic capture behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| card redirect | Card Redirect | not supported | supported | automatic, sequential automatic | USA | USD |

### Authentication

Prophetpay requires **Username**, **Password**, and **Profile ID**. Hyperswitch combines Username and Password into a Basic authorization header, and includes Profile ID in tokenization requests. Details: the connector's [`build_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L75-L93) override sets `Content-Type` and appends [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L112-L127). That method constructs `<Username>:<Password>`, Base64-encodes it, and sends `Authorization: Basic <encoded value>`; [`ProphetpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay/transformers.rs#L52-L68) maps the three credentials, and [`TryFrom<&ProphetpayRouterData<&types::PaymentsAuthorizeRouterData>> for ProphetpayTokenRequest`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay/transformers.rs#L129-L153) places Profile ID in tokenization requests.

### Before you start

1. Register for Prophetpay at [clubprophet.com](https://www.clubprophet.com/products/prophetpay).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain **Username** and **Password** during onboarding and obtain **Profile ID** from the Prophetpay dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Prophetpay-specific behavior.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L710-L715), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L717-L723), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L725-L730) each return `WebhooksNotImplemented`.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0`. See [Prophetpay connector source](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay.rs) and [Prophetpay transformers](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/prophetpay/transformers.rs).
