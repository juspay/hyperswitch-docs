---
description: >-
  Connect AbsaSanlam for EFT debit orders through Hyperswitch.
metaLinks:
  alternates:
    - absa_sanlam.md
---

# AbsaSanlam

AbsaSanlam takes EFT debit orders through Hyperswitch, with automatic capture, and reports each order's outcome by webhook. It does not offer refunds, mandates, or a status sync, and it is not listed in the Hyperswitch control center, so you set it up through the API.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank debit | EFT Debit Order | not supported | not supported | automatic | - | - |

AbsaSanlam runs through the Unified Connector Service.

The table matches what is implemented. Authorize is the one payment flow; it submits the debit order and the capture is automatic ([`Authorize`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs#L235-L299)). Payment sync, refund sync, capture, refunds, mandate setup and repeat payments are not implemented ([flow status](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs#L339-L371)). Because there is no sync, the outcome of a debit order reaches Hyperswitch only through webhooks, so configure them before you depend on the result.

### Authentication

Supply an **API Key** and a **Merchant Id**, the labels from [`[absa_sanlam.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/d483971dcc77e5dfae5a7a034062f65bcdd7523d/crates/connector_configs/toml/sandbox.toml#L9062-L9064). The API Key is sent unchanged in the `Authorization` header and the Merchant Id in the `Merchant-Id` header ([`get_auth_header`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs#L324-L335)); the mapping is [`AbsaSanlamAuthType`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/sanlam_common/transformers.rs#L25-L28).

If you take webhooks, also set **Source verification key** ([`[absa_sanlam.connector_webhook_details]`](https://github.com/juspay/hyperswitch/blob/d483971dcc77e5dfae5a7a034062f65bcdd7523d/crates/connector_configs/toml/sandbox.toml#L9067-L9068)). It is the HMAC key callbacks are checked against, not an authentication credential.

### Before you start

AbsaSanlam is not offered in the Hyperswitch control center, so there is no activation form. Create the connector account through the connector-account API with the three values above, then return here for what AbsaSanlam supports.

### Webhooks

AbsaSanlam webhooks report the outcome of each debit order, and they are the only way Hyperswitch learns it, since there is no sync.

Callbacks are verified with HMAC-SHA256 over the raw request body, keyed on your **Source verification key**. The signature arrives hex-encoded in the `x-signature` header ([signature and message](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs#L78-L101)). A callback that arrives when no key is configured is rejected, not accepted ([`verify_webhook_source`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs#L103-L125)).

| Wire value | Effect |
|---|---|
| `payment.succeeded` | Payment succeeds |
| `payment.failed` | Payment fails |
| `dispute.opened` | Recorded as a dispute-opened event; no dispute details are extracted, so there is nothing further to act on |

The wire values are the serde names on [`AbsaSanlamWebhookEventType`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/sanlam_common/transformers.rs#L503-L509); their effects come from [`get_event_type`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs#L127-L149).

### Source reference

The capability declaration and credential labels on this page are tied to Hyperswitch `d483971dcc77e5dfae5a7a034062f65bcdd7523d`. Flow, authentication and webhook behavior is tied to the Unified Connector Service implementation at hyperswitch-prism `882997b7447232b53a28d09676ff9f8d2797c3b0`: see [AbsaSanlam service source](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/absa_sanlam.rs) and [shared Sanlam types](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/sanlam_common/transformers.rs).
