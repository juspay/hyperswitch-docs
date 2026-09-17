---
description: Accept Blackhawk Network gift card payments.
---

# Blackhawk Network

Blackhawk Network provides a gift card payment route. The route uses automatic capture and does not declare refunds or mandate reuse. Webhook handling is not implemented.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 9e5dd70d1cb4011bbcca3114862406008a0b61f8; host http://localhost:8080; fetched 2026-09-17; matrix canonical-json-v1 sha256 25db1ecc45c5b9c7; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| gift card | BHN Card Network | not supported | not supported | automatic | - | - |

### Authentication

Supply **Client Id**, **Client Secret**, and **Product Line Id**, the labels shown in the Hyperswitch control center. Client Id and Client Secret are sent in a client-credentials token request, while Product Line Id is included in supported gift card requests. See [`BlackhawknetworkAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs#L45-L69), [`get_request_body()` for access tokens](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L113-L126), and [`BlackhawknetworkVerifyAccountRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs#L109-L143).

### Webhooks

Blackhawk Network webhooks are not supported. Use payment sync for status updates. [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L601-L606), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L608-L614), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L616-L622) each return `WebhooksNotImplemented`.

### Source reference

Authentication and webhook behavior on this page follows [Blackhawk Network connector source](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs) and [Blackhawk Network transformers](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs).
