---
description: >-
  Accept UPI Collect payments in India through Razorpay on Hyperswitch.
metaLinks:
  alternates:
    - razorpay.md
---

# Razorpay

Razorpay brings UPI Collect payments to Hyperswitch for merchants in India, with INR settlement and refunds. The integration is in sandbox; mandates are not supported. Razorpay is listed in the Hyperswitch control center.

To connect Razorpay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Razorpay supports and how a payment moves.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| upi | UPI Collect | not supported | supported | automatic | IND | INR |

Razorpay runs through the Unified Connector Service ([`ucs_only_connectors`](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/config/deployments/production.toml#L1099)).

The table reflects the declaration ([`RAZORPAY_SUPPORTED_PAYMENT_METHODS`](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/hyperswitch_connectors/src/connectors/razorpay.rs#L798-L826)). The service implements authorize, payment sync, capture, refund and refund sync. Mandate setup, repeat payments and the dispute flows are not implemented, and void is not supported ([flow status](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L1363-L1389)). The declaration lists automatic capture only, so that is what the table shows, even though the service carries a capture flow.

### Authentication

Supply **Razorpay Id** and **Razorpay Secret**, the labels from [`[razorpay.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/connector_configs/toml/sandbox.toml#L3176-L3178). They are your Razorpay key id and key secret. The service joins them as `id:secret`, base64-encodes the pair and sends it as HTTP Basic authentication in the `Authorization` header ([`generate_authorization_header`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L233-L250)).

There is no webhook verification key to set. The connector has no `connector_webhook_details` entry, so the form shows no **Source verification key** field, and the service does not check callback signatures (see Webhooks).

### Before you start

Razorpay is available in the control center connector list. Have the key id and key secret from the Authentication section ready, and enable UPI Collect on the connector; it is the only payment method declared. Read the next two sections before going live, because on the pinned code a payment's status does not move after the customer approves the collect request.

### Payment flow

Every payment starts with a Razorpay order. The service creates the order first ([`should_do_order_create`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L90-L92), [`CreateOrder`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L597-L724)), then creates the UPI collect request against it at `v1/payments/create/upi` ([`get_url`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L289-L305)). Razorpay asks the customer to approve the request in their UPI app, so authorize returns the payment as `requires_customer_action` with wait-screen instructions rather than a redirect ([UPI response handling](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L2069-L2157), [`get_wait_screen_metadata`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L2159-L2168)).

{% hint style="warning" %}
On the pinned code, nothing moves the payment past that point. A status sync never reaches Razorpay, and a webhook is answered with that same sync (both explained below), so the payment keeps the status authorize returned. Refunds are not affected: a refund sync does reach Razorpay.
{% endhint %}

#### Status sync

A sync asks Razorpay for the payment at `v1/orders/{order_id}/payments` when the order id is known, otherwise at `v1/payments/{payment_id}` ([`get_url`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L505-L530)), and maps `created` to pending, `authorized` and `captured` to charged (capture is automatic), `refunded` to auto-refunded and `failed` to failure ([`get_psync_razorpay_payment_status`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L808-L825)).

That request is never sent for a UPI Collect payment. Before building it, the service checks that the sync carries redirect data (`encoded_data`) and refuses when it does not ([`validate_psync_reference_id`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L76-L89)). Hyperswitch only fills that field for a sync made from a redirect return ([`param`](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/api_models/src/payments.rs#L8729-L8731), [`payment_attempt.encoded_data`](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/router/src/core/payments/operations/payment_get.rs#L197-L200)), and UPI Collect never redirects. The refused sync comes back with no status ([sync pre-flight](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/grpc-server/grpc-server/src/server/payments.rs#L1106-L1139)), and Hyperswitch keeps the status it already had ([status mapping](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/hyperswitch_interfaces/src/unified_connector_service/transformers.rs#L668-L712)).

### Webhooks

The service parses Razorpay callbacks. It does not read the `event` name; it looks at the payload: a `refund` object means a refund event, anything else is a payment event ([`get_event_type`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L942-L953)). The payment is matched by the Razorpay order id, and the status comes from the entity's `status` ([`process_payment_webhook`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L955-L990), [`process_refund_webhook`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L992-L1019)):

| Payload | `status` | Effect |
|---|---|---|
| `payment` | `authorized` | Payment authorized |
| `payment` | `captured` | Payment charged |
| `payment` | `failed` | Authorization failed |
| `refund` | `created`, `pending` | Refund pending |
| `refund` | `processed` | Refund succeeds |
| `refund` | `failed` | Refund fails |

The wire values are the serde names on [`RazorpayPaymentStatus`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L1398-L1403) and [`RazorpayRefundStatus`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L1406-L1412); the effects are in [`get_razorpay_payment_webhook_status`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L1440-L1452) and [`get_razorpay_refund_webhook_status`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs#L1454-L1468).

That status is not what Hyperswitch records, though. The service has no signature check for Razorpay, so it reports every callback as unverified ([default `verify_webhook_source`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/types-traits/interfaces/src/connector_types.rs#L616-L623), [webhook verification](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/grpc-server/grpc-server/src/server/events.rs#L241-L270)). Verification is not mandatory ([`is_webhook_source_verification_mandatory`](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs#L1243-L1245)), so Hyperswitch accepts the callback, but as with any unverified webhook it sets the content aside and syncs with the connector instead, under the unverified-webhook rate limit ([unverified webhook handling](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/router/src/core/webhooks/incoming.rs#L538-L548), [sync instead of the webhook content](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/router/src/core/webhooks/incoming.rs#L918-L932)). For a payment, that sync is the refused one above, so a payment webhook changes nothing. For a refund, the fallback is a refund sync, which does reach Razorpay ([refund webhook flow](https://github.com/juspay/hyperswitch/blob/906a4021a2c5fd8e611f3993a8eb9b6b183d3256/crates/router/src/core/webhooks/incoming.rs#L1642-L1679)), so refund webhooks do move the refund status, one sync later.

### Source reference

The capability declaration, credential labels and the Hyperswitch-side webhook and sync handling on this page are tied to Hyperswitch `906a4021a2c5fd8e611f3993a8eb9b6b183d3256`. Flow, authentication and webhook parsing is tied to the Unified Connector Service implementation at hyperswitch-prism `07b381b8f4c100857ba16cae46d251c8b6c2a4ca`: see [Razorpay service source](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay.rs) and [Razorpay transformers](https://github.com/juspay/hyperswitch-prism/blob/07b381b8f4c100857ba16cae46d251c8b6c2a4ca/crates/integrations/connector-integration/src/connectors/razorpay/transformers.rs).
