---
description: Configure Etisalat card payments with Hyperswitch.
metaLinks:
  alternates:
    - etisalat.md
---

# Etisalat

Etisalat processes credit and debit card payments through Hyperswitch. Both card routes support refunds and manual capture alongside automatic capture. Mandate setup and 3DS are not available for these routes, and there is no status sync: the response to each call is the status you get.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d03f8547d6367fab56690e4f5043590be4935dcd; host http://127.0.0.1:8080; fetched 2026-10-02; matrix canonical-json-v1 sha256 8b92b42f08eb323a31ea974c99ac67dc4972774ab49bda767a79da9d2992fd5b; 147 connectors.
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
| card | Credit Card | not supported | supported | automatic, manual | not supported | Mastercard, Visa | 7 | 9 |
| card | Debit Card | not supported | supported | automatic, manual | not supported | Mastercard, Visa | 7 | 9 |

Etisalat runs through the Unified Connector Service.

3DS is not supported. Neither the pre-authentication nor the post-authentication flow is implemented for Etisalat ([flow status](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs#L395-L426)).

Mandate setup is not implemented, which is why the table says mandates are not supported. A merchant-initiated repeat payment is implemented, but only against a recurrence reference obtained from Etisalat outside Hyperswitch: Etisalat's master TransactionID from its own registration and finalization, passed as `connector_mandate_id`. Without it the request fails with a missing-field error ([`RepeatPayment`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs#L339-L365), [transformer](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat/transformers.rs#L595-L613)).

### Authentication

Provide the **EPG Password**, **EPG UserName**, and **EPG Customer** shown in the connector form. The labels and accepted signature-key fields are defined by the [`etisalat.connector_auth.SignatureKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L9347-L9350) and the three are carried as `user_name`, `password` and `customer` ([`EtisalatAuthType`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat/transformers.rs#L111-L115)). They are sent in the JSON body of each request, not in HTTP headers ([`body_only_headers`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs#L224-L226)).

### Before you start

Have the EPG Password, EPG UserName, and EPG Customer ready. To connect Etisalat to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Etisalat supports.

### Webhooks

Etisalat webhooks are not supported. The incoming-webhook handler for this connector is empty ([`IncomingWebhook for Etisalat`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs#L105-L108)), and Etisalat's own webhooks cover only Central Bank offline payments, which are out of scope ([flow status](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs#L395-L397)).

There is no sync fallback either. Etisalat has no per-transaction sync endpoint, so payment sync and refund sync are not implemented ([`not_implemented`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs#L398-L426)). The status returned by the authorize, capture, void and refund calls is final for that call; design your integration to act on those responses rather than polling. The routing itself is set by [`ucs_only_connectors`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/config/development.toml#L1684).

### Source reference

The capability declaration and credential labels on this page are tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. Flow, authentication and webhook behavior is tied to the Unified Connector Service implementation at hyperswitch-prism `882997b7447232b53a28d09676ff9f8d2797c3b0`: see [Etisalat service source](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat.rs) and [Etisalat service transformers](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/etisalat/transformers.rs).
