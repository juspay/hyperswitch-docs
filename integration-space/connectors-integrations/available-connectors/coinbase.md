---
description: >-
  Accept cryptocurrency payments through Coinbase Commerce with signed payment webhooks.
metaLinks:
  alternates:
    - coinbase.md
---

# Coinbase

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/coinbaseLogo.svg" alt=""></div>

Coinbase Commerce gives this connector a cryptocurrency checkout path. Coinbase sends webhooks when a charge changes status, and Hyperswitch checks each webhook's signature before applying the update.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** beta

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | not supported | automatic, manual, sequential automatic | 15 ([full list](https://hyperswitch.io/pm-list)) | - |

The connector declares refund webhooks in code, but they cannot be processed: only `charge:*` events are recognized, and there is no refund event. Webhooks work for payments only.

The connector also declares manual and sequential automatic capture, but capture is not implemented: capture requests return `FlowNotSupported`. Only automatic capture works.

### Authentication

Coinbase requires an **API Key**. Hyperswitch sends it unchanged in the `X-CC-API-KEY` header for each implemented request path. Every request also pins the Coinbase Commerce API version with an `X-CC-Version: 2018-03-22` header. See [`CoinbaseAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase/transformers.rs#L75-L86), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase.rs#L120-L131), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase.rs#L85-L103) (version header).

### Before you start

1. Register with Coinbase Commerce at [coinbase.com/commerce](https://www.coinbase.com/commerce).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key** from the Coinbase Commerce dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Coinbase-specific behavior.

### Webhooks

Hyperswitch verifies the hexadecimal `X-CC-Webhook-Signature` value with HMAC-SHA256 over the raw request body. Configure the Coinbase webhook signing secret in Hyperswitch's connector `merchant_secret` (the **Source Verification Key**); Hyperswitch uses it as the HMAC key when checking the signature. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase.rs#L392-L401) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase.rs#L403-L412).

Handled event wire values: **5**.

| Wire value | Effect |
|---|---|
| `charge:confirmed` | Payment succeeds |
| `charge:resolved` | Payment succeeds |
| `charge:failed` | Payment requires action |
| `charge:pending` | Payment is processing |
| `charge:created` | No payment update is applied |

The wire names come from [`WebhookEventType`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase/transformers.rs#L340-L354); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase.rs#L427-L450).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Coinbase connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase.rs) and [Coinbase transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/coinbase/transformers.rs).
