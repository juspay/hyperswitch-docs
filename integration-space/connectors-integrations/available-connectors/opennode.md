---
description: >-
  Accept cryptocurrency payments through OpenNode. Payment status updates rely on payment sync.
metaLinks:
  alternates:
    - opennode.md
---

# OpenNode

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/opennodeLogo.svg" alt=""></div>

OpenNode provides a bitcoin checkout path with asynchronous payment states. Underpaid and expired orders require merchant attention, while paid orders complete the payment. The declared checkout path does not include refunds or mandate reuse.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** beta

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | not supported | automatic | 31 ([full list](https://hyperswitch.io/pm-list)) | 12 ([full list](https://hyperswitch.io/pm-list)) |

The payments webhook flow above is what the connector declares in code. OpenNode webhooks do not currently work: callbacks fail to parse or fail signature verification, so use payment sync for status updates. See [Webhooks](#webhooks) below and the tracking issue [juspay/hyperswitch#14205](https://github.com/juspay/hyperswitch/issues/14205).

### Authentication

OpenNode requires an **API Key**. The connector's [`build_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L82-L105) override sets `Content-Type` and `Accept`, then appends the result of [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L124-L134). That method sends the value mapped by [`OpennodeAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode/transformers.rs#L65-L75) unchanged in the `Authorization` header.

### Before you start

1. Register with OpenNode at [opennode.com](https://www.opennode.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key** from the OpenNode dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for OpenNode-specific behavior.

### Webhooks

OpenNode's webhooks do not currently work with Hyperswitch. OpenNode's documented payloads are missing fields that Hyperswitch requires (`payment_method`, `net_fiat_value`, `fiat_value`), so they fail to parse and the webhook is rejected outright. Payloads that do parse then fail signature verification: Hyperswitch computes the HMAC-SHA256 for the `hashed_order` value over the raw request body keyed by the connector's `merchant_secret`, while [OpenNode's webhook documentation](https://developers.opennode.com/docs/charges-webhooks) specifies the charge `id` as the message and the API key as the key. Until this is fixed, do not rely on webhooks for OpenNode payment status; use payment sync instead. We are working on it; see [the tracking issue](https://github.com/juspay/hyperswitch/issues/14205). See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L396-L406) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L408-L417).

Object lookup uses the callback `id` as the connector transaction ID; see [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L419-L428). Resource extraction returns the parsed payment status; see [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L453-L462). Event dispatch reads the status and produces the outcomes below; see [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs#L430-L451).

Handled status wire values: **6**.

| Wire value | Effect |
|---|---|
| `paid` | Payment succeeds |
| `underpaid` | Payment requires action |
| `expired` | Payment requires action |
| `processing` | Payment is processing |
| `unpaid` | No payment update is applied |
| `refunded` | No payment update is applied |

The lowercase wire values and unknown-value fallback come from [`OpennodePaymentStatus`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode/transformers.rs#L78-L90). OpenNode also documents a `failed` status (a dropped mempool transaction); the enum has no variant for it, so it deserializes to the unknown fallback and no payment update is applied.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0`. See [OpenNode connector source](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode.rs) and [OpenNode transformers](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/opennode/transformers.rs).
