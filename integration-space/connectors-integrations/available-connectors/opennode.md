---
description: >-
  Accept cryptocurrency payments through OpenNode with signed payment status callbacks.
metaLinks:
  alternates:
    - opennode.md
---

# OpenNode

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/opennodeLogo.svg" alt=""></div>

OpenNode provides a bitcoin checkout path with asynchronous payment states. Underpaid and expired orders require merchant attention, while paid orders complete the payment. The declared checkout path does not include refunds or mandate reuse.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** beta

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | not supported | automatic | 31 ([full list](https://hyperswitch.io/pm-list)) | 12 ([full list](https://hyperswitch.io/pm-list)) |


### Authentication

OpenNode requires an **API Key**. Hyperswitch sends it unchanged in the `Authorization` header for each implemented request path. See [`OpennodeAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode/transformers.rs#L65-L75) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode.rs#L124-L134).

### Webhooks

Hyperswitch verifies the hexadecimal `hashed_order` value with HMAC-SHA256 over the raw request body. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode.rs#L396-L406) and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode.rs#L408-L417).

Handled status wire values: **6**.

| Wire value | Effect |
|---|---|
| `paid` | Payment succeeds |
| `underpaid` | Payment requires action |
| `expired` | Payment requires action |
| `processing` | Payment is processing |
| `unpaid` | No payment update is applied |
| `refunded` | No payment update is applied |

The lowercase wire values come from [`OpennodePaymentStatus`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode/transformers.rs#L78-L90); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode.rs#L430-L451).

### Activate OpenNode with Hyperswitch

#### Before you start

1. Register with OpenNode at [opennode.com](https://www.opennode.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key** from the OpenNode dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for OpenNode-specific behavior.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [OpenNode connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode.rs) and [OpenNode transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/opennode/transformers.rs).
