---
description: Accept Blackhawk Network gift card payments.
metaLinks:
  alternates:
    - blackhawknetwork.md
---

# Blackhawk Network

{% hint style="warning" %}
**Alpha connector.** Blackhawk Network is at alpha integration status and supports one flow only: a single, automatically captured gift card payment. There are no refunds, no separate capture, no webhooks, and no payment or refund sync, so once Hyperswitch submits a payment it has no way to re-check what happened to it.

If you want to use this connector, reach out on the [Slack Community](https://inviter.co/hyperswitch-slack) first so someone on the Hyperswitch team can tell you where it stands. Please post in the #dev-support channel. 
{% endhint %}

Blackhawk Network accepts gift card payments on the BHN Card Network as a single automatically captured redemption. Redemption takes two steps: a preprocessing call to `verifyAccount` returns an account ID, and the authorize request redeems against that ID. Hyperswitch does not drive this sequence for you. The connector leaves [`is_balance_check_flow_required()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_interfaces/src/api.rs#L455-L457) at its default `false`, so the router never runs the balance-check flow automatically, and [`BlackhawknetworkPaymentsRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs#L255-L283) fails with `MissingConnectorRelatedTransactionID` if no preprocessing step has supplied the ID. Mandates and refunds are not supported, so a card cannot be stored for reuse and a completed payment cannot be reversed through Hyperswitch.

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

**Webhook flows:** There's nothing declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| gift card | BHN Card Network | not supported | not supported | automatic | - | - |

### Authentication

Supply **Client Id**, **Client Secret**, and **Product Line Id**, the labels shown in the Hyperswitch control center. Client Id and Client Secret are sent in a client-credentials token request, while Product Line Id is included in supported gift card requests. See [`BlackhawknetworkAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs#L45-L69), [`get_request_body()` for access tokens](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L113-L126), and [`BlackhawknetworkVerifyAccountRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs#L109-L143).

### Before you start

1. Register with Blackhawk Network at [blackhawknetwork.com](https://www.blackhawknetwork.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain **Client Id**, **Client Secret**, and **Product Line Id** from Blackhawk Network, then enter them during connector activation.
4. If the activation flow asks you to select payment methods, choose only the gift card methods enabled on your Blackhawk Network account.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Blackhawk Network-specific behavior.

### Webhooks

Blackhawk Network webhooks are unsupported, and neither is payment sync. There is no way to re-check a payment after Hyperswitch submits it, so treat the authorize response as the only status you will receive, and record it on your side.

The three webhook handlers ([`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L601-L606), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L608-L614), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L616-L622)) each return `WebhooksNotImplemented`. Four further flows reject the request outright with `FlowNotSupported`: [payment sync](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L541-L553), [capture](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L555-L567), [refund execute](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L571-L583), and [refund sync](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs#L585-L597).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `9e5dd70d1cb4011bbcca3114862406008a0b61f8`. See [Blackhawk Network connector source](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork.rs) and [Blackhawk Network transformers](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/blackhawknetwork/transformers.rs).
