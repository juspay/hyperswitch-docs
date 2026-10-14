---
description: Configure GivePayments card payments with Hyperswitch.
metaLinks:
  alternates:
    - givepayments.md
---

# GivePayments

{% hint style="warning" %}
**Alpha connector.** Confirm current availability with the Hyperswitch team before relying on GivePayments in production.
{% endhint %}

GivePayments processes credit and debit card payments through Hyperswitch, with automatic capture, refunds, and card-on-file repeat payments. 3DS is not supported. GivePayments is listed in the Hyperswitch control center.

To connect GivePayments to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what GivePayments supports and how a payment moves.
### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 7a348f02a94edf7b2593e65ca6ffaf8d8f9ee6f8; host http://localhost:8080; fetched 2026-10-07; matrix canonical-json-v1 sha256 531b36912ecfe5250a64589e037de9659c5740997a7c5b984d467fc689c61135; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | supported | supported | automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | - | - |

GivePayments runs through the Unified Connector Service ([`ucs_only_connectors`](https://github.com/juspay/hyperswitch/blob/f237029208a1812aa27281dc9ee5f69fa8c89f84/config/deployments/production.toml#L1099)).

The table reflects the declaration ([`GIVEPAYMENTS_SUPPORTED_PAYMENT_METHODS`](https://github.com/juspay/hyperswitch/blob/f237029208a1812aa27281dc9ee5f69fa8c89f84/crates/hyperswitch_connectors/src/connectors/givepayments.rs#L599-L661)). The service implements authorize, repeat payment, payment sync, refund and refund sync ([flows](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L320-L384)). Capture is not supported and void is not implemented, so every payment is captured automatically and cannot be cancelled through Hyperswitch ([flow status](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L764-L792)).

"Mandates: supported" in the table means card on file. When GivePayments returns a payment-method token with an authorization, the service stores it as the connector mandate id ([`paymethod_token`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs#L594-L606)), and a repeat payment sends that token instead of card data ([`RepeatPayment`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L568-L648), [`connector_mandate_id`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs#L658-L666)). A standalone mandate setup is not implemented ([flow status](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L764-L792)), so establish the mandate on a real payment.

### Authentication

Supply the **API Key**, the label from [`[givepayments.connector_auth.HeaderKey]`](https://github.com/juspay/hyperswitch/blob/f237029208a1812aa27281dc9ee5f69fa8c89f84/crates/connector_configs/toml/sandbox.toml#L9299-L9300). The service sends it as a bearer token in the `Authorization` header ([`get_auth_header`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L405-L425)).

If you take webhooks, also set **Source verification key** ([`[givepayments.connector_webhook_details]`](https://github.com/juspay/hyperswitch/blob/f237029208a1812aa27281dc9ee5f69fa8c89f84/crates/connector_configs/toml/sandbox.toml#L9301-L9302)) to the webhook signing secret from GivePayments. It is the HMAC key callbacks are checked against, not an authentication credential.

### Before you start

Create or sign in to your [GivePayments account](https://www.givepayments.com/resources/high-risk-payment-processing-guide/) and obtain the API Key and, if you take webhooks, the webhook signing secret. GivePayments appears in the control center connector list ([`connectorList`](https://github.com/juspay/hyperswitch-control-center/blob/ecca16a27cb6acb336569ea30714fa05d867c765/src/screens/Connectors/ConnectorUtils.res#L89-L205)). The connector is in alpha, so confirm availability with the Hyperswitch team, then follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).

### Payment flow

Authorize creates the payment at `/payments` and GivePayments captures it ([`Authorize`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L485-L566)). The payment's `processing_state` sets the Hyperswitch status: `created` and `authorized` are pending, `captured` and `settled` are charged, `failed` and `declined` are failures, and `voided` is voided ([`GivepaymentsPaymentProcessingState`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs#L1012-L1028)). A sync reads `/payments/{id}` and applies the same mapping ([`PSync`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L650-L687)). A refund sync maps `created` and `pending` to pending, `approved` and `settled` to success, and `failed`, `declined` and `canceled` to failure ([`RSync`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L721-L762), [`GivepaymentsRefundProcessingState`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs#L1029-L1044)).

### Webhooks

Callbacks are verified with HMAC-SHA256 over the raw request body, keyed on your **Source verification key**. The signature arrives base64-encoded in the `gp-webhook-signature` header ([signature](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L85-L98), [message](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L100-L112), [`verify_webhook_source`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L114-L141)). A callback that arrives when no key is configured fails verification. Verification is not mandatory for this connector ([default](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/types-traits/interfaces/src/connector_types.rs#L859-L861)), so Hyperswitch still accepts an unverified callback, but it sets the content aside and syncs with GivePayments instead, under the unverified-webhook rate limit ([unverified webhook handling](https://github.com/juspay/hyperswitch/blob/f237029208a1812aa27281dc9ee5f69fa8c89f84/crates/router/src/core/webhooks/incoming.rs#L538-L549)). A verified callback is applied directly ([verified callback handling](https://github.com/juspay/hyperswitch/blob/f237029208a1812aa27281dc9ee5f69fa8c89f84/crates/router/src/core/webhooks/incoming.rs#L918-L933)).

The event name selects the event, and the status comes from the payload's `processing_state`, not from the name ([`get_event_type`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L143-L153), [`process_payment_webhook`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L199-L258), [`process_refund_webhook`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L259-L292)). The callback is matched by GivePayments' payment or refund id, with your reference as the merchant-side id ([`get_webhook_event_reference`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs#L170-L197)). A payment callback that carries a payment-method token also records it as the connector mandate id.

| Wire value | Effect |
|---|---|
| `payment.created`, `payment.authorized` | Payment processing |
| `payment.captured`, `payment.settled` | Payment charged |
| `payment.failed`, `payment.declined` | Payment fails |
| `payment.voided` | Payment cancelled |
| `refund.created`, `refund.pending` | Refund processing |
| `refund.approved`, `refund.settled` | Refund succeeds |
| `refund.failed`, `refund.declined`, `refund.canceled` | Refund fails |

The wire values are the serde names on [`GivepaymentsWebhookEventType`](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs#L972-L1003); their effects come from the [event mapping](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs#L1045-L1072). An event name the service does not know maps to an unspecified event and is ignored.

### Source reference

The capability declaration, credential labels and the Hyperswitch-side webhook handling on this page are tied to Hyperswitch `f237029208a1812aa27281dc9ee5f69fa8c89f84`. Flow, authentication and webhook behavior is tied to the Unified Connector Service implementation at hyperswitch-prism `b8993a3a58f586a3ec5b8e350731dae7e632d89b`: see [GivePayments service source](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments.rs) and [GivePayments transformers](https://github.com/juspay/hyperswitch-prism/blob/b8993a3a58f586a3ec5b8e350731dae7e632d89b/crates/integrations/connector-integration/src/connectors/givepayments/transformers.rs).
