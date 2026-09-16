---
description: Create, limit, and track API refunds against captured payment amounts
---

<!-- truth manifest; hyperswitch 02ba5ea0b4cc0ad8debea4cefd28a7de5916d9db; spec api-reference/v1/openapi_spec_v1.json@02ba5ea0b4cc0ad8debea4cefd28a7de5916d9db
     symbols: POST /refunds = api-reference/v1/openapi_spec_v1.json:2283-2351; crates/router/src/routes/app.rs:1564-1602
     symbols: GET /refunds/{refund_id} = api-reference/v1/openapi_spec_v1.json:2353-2380; crates/router/src/routes/app.rs:1564-1602
     symbols: RefundRequest has 10 fields; payment_id, refund_id, amount, reason, metadata are the 5 covered here = api-reference/v1/openapi_spec_v1.json:43403-43482
     symbols: RefundResponse has 21 fields; refund_id, payment_id, amount, currency, status, reason, metadata are the 7 covered here = api-reference/v1/openapi_spec_v1.json:43484-43603
     symbols: succeeded, failed, pending, review = api-reference/v1/openapi_spec_v1.json:43604-43612; crates/api_models/src/refunds.rs:571-604
     symbols: refund.max_age = crates/router/src/configs/settings.rs:1173-1178; crates/router/src/configs/defaults.rs:90-95
     symbols: refund.max_attempts = crates/router/src/configs/settings.rs:1173-1178; crates/router/src/core/refunds.rs:1676-1680
     symbols: refundable payment statuses succeeded, partially_captured = crates/router/src/core/refunds.rs:391-403
     symbols: initial refund status pending = crates/router/src/core/refunds.rs:1715-1721
     symbols: refund.max_attempts default 10, rejects when existing refund count exceeds it, counts all refunds including failed = crates/router/src/configs/defaults.rs:90-95; crates/router/src/core/utils/refunds_validator.rs:93-100
     symbols: GET /feature_matrix = crates/router/src/routes/app.rs:3386-3388, route registration only, absent from api-reference/v1/openapi_spec_v1.json
     symbols: refund.max_age compared with payment created_at in whole days = crates/router/src/core/refunds.rs:1656-1663; crates/router/src/core/utils/refunds_validator.rs:80-90
     symbols: post-capture void blocks refund = crates/router/src/core/refunds.rs:412; crates/hyperswitch_domain_models/src/payments.rs:442-461
     symbols: connector refund support check = crates/router/src/core/refunds.rs:1697; crates/router/src/core/utils/refunds_validator.rs:119-147
     symbols: reason stored on refund = crates/router/src/core/refunds.rs:1715-1725; Stripe connector does not send reason = crates/hyperswitch_connectors/src/connectors/stripe/transformers.rs:4309-4331
     absent: customer statement timing = checked api-reference/v1/openapi_spec_v1.json:2283-2380,43403-43612; crates/router/src/routes/app.rs:1564-1605; crates/api_models/src/refunds.rs:19-76, no duration contract found
     external: customer statement timing = payment processor and issuer owned; no fixed duration asserted, consistent with the in-repo refund status contract at api-reference/v1/openapi_spec_v1.json:43484-43612
     derived: remaining refundable amount = amount_captured - sum of refund_amount for refunds not in failure or transaction_failure, sources crates/router/src/core/utils/refunds_validator.rs:51-77
     derived: omitted request amount = req.amount.or(payment_intent.amount_captured), then validated against the remaining refundable amount, sources crates/router/src/core/refunds.rs:414-419,1665-1674; crates/router/src/core/utils/refunds_validator.rs:51-77
     checked: 2026-09-15 -->

# Refunds

A refund can return only money that has already been captured. If a payment is still authorized and waiting for capture, capture it before requesting a refund. For a partially captured payment, the captured amount is the upper bound.

Use `POST /refunds` to create a refund. Use `GET /refunds/{refund_id}` to retrieve it and track its API status.

## Create a refund

The request schema has 10 fields. These 5 cover the common full and partial refund flow:

| Field | Required | What to send |
| --- | --- | --- |
| `payment_id` | Yes | The payment to refund. |
| `amount` | No | The amount in the currency's lowest denomination. Send it for a partial refund. |
| `refund_id` | No | Your unique identifier for this refund operation. Hyperswitch generates one when it is omitted. |
| `reason` | No | A reason string. Hyperswitch stores it on the refund; whether it is passed to the processor depends on the connector. |
| `metadata` | No | Additional structured information for your own reference. |

For a partial refund:

```json
{
  "payment_id": "<payment_id>",
  "refund_id": "<refund_id>",
  "amount": 500,
  "reason": "Customer returned the item",
  "metadata": {
    "order_reference": "test_order"
  }
}
```

The response schema has 21 fields. The 7 used in this flow are `refund_id`, `payment_id`, `amount`, `currency`, `status`, `reason`, and `metadata`.

## Full and partial refund amounts

Omit `amount` only when you intend to refund the complete captured amount and no earlier non-failed refund has consumed part of it. Hyperswitch initially substitutes `amount_captured` when `amount` is omitted, then applies the remaining-amount check.

For each refund, Hyperswitch calculates:

`remaining refundable amount = amount_captured - previous non-failed refund amounts`

The new `amount` must not exceed that remainder. Failed refund operations do not consume it. This allows multiple partial refunds, subject to the remaining captured amount and the deployment's `refund.max_attempts` limit. Hyperswitch rejects a new refund when the payment attempt already has more than `refund.max_attempts` refunds, so the default of 10 allows up to 11 refunds on one payment attempt. Every refund counts toward that limit, including failed ones, even though failed refunds do not consume the refundable amount. Deployments can configure a different value. Use a distinct `refund_id` for each operation.

## Refunds and captures

A payment is eligible for this refund flow when its payment status is `succeeded` or `partially_captured`. A payment waiting for capture is not eligible.

The limit is based on `amount_captured`, not the originally requested payment amount. If you captured only part of an authorization, you can refund only that captured portion.

A payment that had a void issued after capture cannot be refunded; the request fails with a precondition error.

The connector must also support refunds for the payment's method type. If the connector does not declare refund support for that payment method type, Hyperswitch rejects the request before creating a refund, with the message `Refunds are currently not supported for <payment method type> transactions via <connector>`. Call `GET /feature_matrix` to see which payment method types each connector declares refund support for.

## Refund status lifecycle

The API returns four wire values:

| Wire value | Meaning |
| --- | --- |
| `pending` | The refund was created and does not yet have a final processor outcome. |
| `succeeded` | The refund completed. |
| `failed` | The refund did not complete. |
| `review` | The refund requires review. |

A newly created refund starts as `pending`. Retrieve it with `GET /refunds/{refund_id}` when you need the current API value. For event-driven updates, use the refund events listed in [Webhooks](../webhooks.md).

The Control Center uses display labels for operators. See [Operations](../control-center/operations.md) for the dashboard workflow. Those labels and the API wire values serve different interfaces.

## Refund windows

Hyperswitch checks the time since the payment was created (not since it was captured) against the deployment's `refund.max_age` setting, in days, before creating the refund. The repository default is 365 days, but deployments can configure a different value.

This server-side eligibility window is separate from the time it takes a refund to appear on a customer statement. Statement timing is owned by the payment processor and issuer, and the Hyperswitch API does not define a fixed duration.

See the [Create a Refund](https://api-reference.hyperswitch.io/v1/refunds/refunds--create) and [Retrieve a Refund](https://api-reference.hyperswitch.io/v1/refunds/refunds--retrieve) API references for the complete schemas.
