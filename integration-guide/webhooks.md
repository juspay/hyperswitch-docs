---
description: Configure outgoing webhooks from Hyperswitch
icon: anchor
metaLinks:
  alternates:
    - webhooks.md
---

<!-- truth manifest; hyperswitch e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0; spec api-reference/v1/openapi_spec_v1.json@e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0
     symbols: POST = crates/router/src/core/webhooks/outgoing.rs:912-913
     symbols: /account/{account_id}/webhooks/{merchant_connector_id} = api-reference/v1/openapi_spec_v1.json:3110-3181
     symbols: merchant_id, event_id, event_type, content, timestamp, processor_merchant_id = api-reference/v1/openapi_spec_v1.json:30162-30195
     symbols: payment_details, refund_details, dispute_details, mandate_details, payout_details, subscription_details = api-reference/v1/openapi_spec_v1.json:30197-30310
     symbols: payment_succeeded, payment_failed, payment_processing, payment_cancelled, payment_cancelled_post_capture, payment_authorized, payment_partially_authorized, payment_captured, payment_expired, action_required, refund_succeeded, refund_failed, refund_review, dispute_opened, dispute_expired, dispute_accepted, dispute_cancelled, dispute_challenged, dispute_won, dispute_lost, mandate_active, mandate_revoked, payout_success, payout_failed, payout_initiated, payout_processing, payout_cancelled, payout_expired, payout_reversed, payout_not_permitted, invoice_paid, surcharge_payment_succeeded, surcharge_refund_succeeded = api-reference/v1/openapi_spec_v1.json:23229-23265
     symbols: X-Webhook-Signature-512 = crates/router/src/lib.rs:153
     symbols: HMAC-SHA512 = crates/router/src/core/webhooks/types.rs:44-75
     symbols: payment_response_hash_key = api-reference/v1/openapi_spec_v1.json:26948-26954
     symbols: 2xx = crates/router/src/core/webhooks/outgoing.rs:1580-1581
     symbols: retry schedule = config/superposition_seed.toml:2596-2613
     symbols: content.object.updated = api-reference/v1/openapi_spec_v1.json:30197-30215,35622-35626
     checked: 2026-09-14 -->

# Webhooks

Webhooks let Hyperswitch send event updates to your server without polling. Each delivery is an HTTP `POST` with a JSON body.

### Configuring webhooks

#### Create an endpoint on your server

Create a public HTTPS endpoint that accepts `POST` requests. Return a `2xx` status only after your application has accepted the event for processing.

#### Configure your webhook endpoint on Hyperswitch Dashboard

1. Select the business profile and mode that the endpoint belongs to.
2. Go to **Developers → Payment Settings → Payment Behaviour**.
3. Add the endpoint URL.
4. In live mode, ask the Hyperswitch team to allowlist the URL.
5. Save the setting. After your payment flow can produce an event, send a test payment and confirm that your endpoint responds.

These steps follow the [Control Center developers guide](control-center/developers.md#setting-up-a-webhook).

#### Update Hyperswitch's webhook endpoints on your connector dashboard

This step applies after the connector account exists. Register the connector webhook with:

```http
POST /account/{account_id}/webhooks/{merchant_connector_id}
```

The path parameters are the merchant account ID and merchant connector ID. The request configures the webhook at the connector for that existing account.

### Handling webhooks

The v1 API schema defines 33 event wire values:

1. `payment_succeeded`
2. `payment_failed`
3. `payment_processing`
4. `payment_cancelled`
5. `payment_cancelled_post_capture`
6. `payment_authorized`
7. `payment_partially_authorized`
8. `payment_captured`
9. `payment_expired`
10. `action_required`
11. `refund_succeeded`
12. `refund_failed`
13. `refund_review`
14. `dispute_opened`
15. `dispute_expired`
16. `dispute_accepted`
17. `dispute_cancelled`
18. `dispute_challenged`
19. `dispute_won`
20. `dispute_lost`
21. `mandate_active`
22. `mandate_revoked`
23. `payout_success`
24. `payout_failed`
25. `payout_initiated`
26. `payout_processing`
27. `payout_cancelled`
28. `payout_expired`
29. `payout_reversed`
30. `payout_not_permitted`
31. `invoice_paid`
32. `surcharge_payment_succeeded`
33. `surcharge_refund_succeeded`

The outgoing webhook object has six fields. `merchant_id`, `event_id`, `event_type`, `content`, and `timestamp` are required; `processor_merchant_id` is optional.

The `content` object has six wire shapes. Its `type` is one of `payment_details`, `refund_details`, `dispute_details`, `mandate_details`, `payout_details`, or `subscription_details`. The matching resource is in `content.object`.

See the [outgoing webhook schema](https://api-reference.hyperswitch.io/v1/schemas/outgoing--webhook) for each resource shape.

### Webhook signature verification

Set `payment_response_hash_key` on the business profile and store it securely. Hyperswitch signs the serialized webhook body with HMAC-SHA512 and sends the hex-encoded digest in `X-Webhook-Signature-512`.

#### Webhook signature generation

Hyperswitch generates the signature from the exact serialized JSON body and `payment_response_hash_key`. Any byte-level change to the body changes the digest.

#### Webhook validation

1. Read the raw request body before parsing it.
2. Read `X-Webhook-Signature-512`.
3. Generate an HMAC-SHA512 digest from the raw body with `payment_response_hash_key`.
4. Hex-encode the digest.
5. Compare the generated and received values in constant time.
6. Reject the delivery if they do not match.

#### Troubleshooting signature verification failures

* **Signature does not match:** use the raw request bytes, not JSON that your application parsed and serialized again.
* **Header is missing:** check `X-Webhook-Signature-512` and confirm that the business profile has `payment_response_hash_key` configured.
* **Digest format differs:** compare the hex-encoded HMAC-SHA512 digest.

### Webhook delivery behavior

A delivery succeeds when your endpoint returns a `2xx` response. The default retry schedule has 16 retries after the original attempt:

| Retry attempt | Delay from the preceding attempt |
| --- | --- |
| 1st | 1 minute |
| 2nd and 3rd | 5 minutes |
| 4th through 8th | 10 minutes |
| 9th through 13th | 1 hour |
| 14th through 16th | 6 hours |

#### Handling duplicates

Retries can deliver the same event more than once. Store the required `event_id` and make event processing idempotent. If an `event_id` has already completed, acknowledge the duplicate without applying the change again.

#### Handling out-of-order deliveries

Do not assume that delivery order matches event order. For payment webhooks, compare `content.object.updated` with the value already stored and apply only the newer payment state. The v1 schema does not define `updated` on every other webhook resource shape, so handle their ordering with fields from the matching resource schema.
