---
description: >-
  Place a hold on your customers' funds and capture them later, fully or
  partially, in one capture or several
icon: transmission
metaLinks:
  alternates:
    - ./
---

<!-- truth manifest; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; spec api-reference/v1/openapi_spec_v1.json@184ffd4c015fd3fea2f3868549f1a86ffa5f40da
     symbols: capture_method wire values automatic, manual, manual_multiple, scheduled, sequential_automatic = crates/common_enums/src/enums.rs:814-830, serde rename_all = "snake_case" at enums.rs:814
     symbols: capture_method default automatic = crates/common_enums/src/enums.rs:819-821
     symbols: capture_method scheduled returns 501 Not Implemented on payment create and update = crates/router/src/routes/payments.rs:86-88, 205, 910, 1216
     symbols: POST /payments/{payment_id}/capture request fields = crates/api_models/src/payments.rs:6731-6760 PaymentsCaptureRequest; api-reference/v1/openapi_spec_v1.json:33991-34030
     symbols: amount_to_capture omitted captures the whole amount_capturable = crates/api_models/src/payments.rs:6740-6743
     symbols: amount_to_capture must be positive and not above amount_capturable = crates/router/src/core/payments/helpers.rs:4054-4072
     symbols: amount_to_capture required for manual_multiple = crates/router/src/core/payments/operations/payment_capture.rs:116-119
     symbols: capture ceiling skipped when overcapture is on = crates/router/src/core/payments/operations/payment_capture.rs:101-111
     symbols: capture_method automatic rejected by the capture endpoint = crates/router/src/core/payments/helpers.rs:4005-4019
     symbols: statuses the capture endpoint accepts = crates/router/src/core/payments/helpers.rs:4022-4051
     symbols: requires_capture, partially_captured, partially_captured_and_capturable, partially_authorized_and_requires_capture, partially_captured_and_processing, cancelled, cancelled_post_capture, expired, succeeded = crates/common_enums/src/enums.rs:2124-2170
     symbols: partially_captured is terminal, partially_captured_and_capturable is not = crates/common_enums/src/enums.rs:2181-2199
     symbols: PartialCharged maps to partially_captured, PartialChargedAndChargeable maps to partially_captured_and_capturable = crates/common_enums/src/transformers.rs:2128-2129
     symbols: amount_capturable set to zero on partially_captured, left alone on partially_captured_and_capturable = crates/router/src/types.rs:429-469
     symbols: multiple-capture attempt status rule = crates/router/src/core/payments/types.rs:133-146
     symbols: refund eligibility succeeded or partially_captured = crates/router/src/core/refunds.rs:391-403
     symbols: refundable ceiling is amount_captured = crates/router/src/core/refunds.rs:1665-1674
     symbols: refund_uncaptured_amount = crates/api_models/src/payments.rs:6747-6749; api-reference/v1/openapi_spec_v1.json:34006-34009
     absent: refund_uncaptured_amount reader = checked crates/router, crates/hyperswitch_domain_models, crates/hyperswitch_connectors, crates/common_enums; the only other occurrence in the repo is crates/router/src/core/fraud_check/operation/fraud_check_post.rs:315 which writes None; no code path reads the field
     absent: producer of expired = checked crates/router/src/core, crates/hyperswitch_domain_models/src, crates/hyperswitch_connectors/src, crates/scheduler for any arm or assignment yielding AttemptStatus::Expired or IntentStatus::Expired; every occurrence at this SHA is a match arm on the left, none produces the value
     derived: partially_captured_and_processing is produced only when enable_partial_authorization is true and cumulative amount_captured is above zero and the attempt status is Pending, sources crates/hyperswitch_domain_models/src/router_data.rs:1255-1267,1298-1310 (inside the cfg(feature = "v2") impl opened at 1012) and crates/router/src/core/payments/operations/payment_attempt_record.rs:269-276; no capture_method value appears in any of those conditions
     checked: 2026-09-16 -->

# Manual Capture

{% embed url="https://youtu.be/XtOMZVhvLwQ" %}

In most online payments the merchant captures funds in one step, right after the issuer authorizes. Hyperswitch calls that the automatic capture flow.

Manual capture splits it in two. The authorization places a hold on the customer's funds, and you capture later, once you have shipped the goods or delivered the service. The industry calls this auth and capture, or the two-step flow.

### Why use it

1. You capture only after you have delivered, so you control when the customer is charged.
2. You can capture the full authorized amount or part of it.
3. The customer sees a charge that matches what they received.

### Choose a capture method before you authorize

`capture_method` is set at payment creation and decides everything that follows, including whether an uncaptured remainder survives. The wire values are:

| `capture_method`       | What it does                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------- |
| `automatic`            | Default. Authorization and capture happen together. The capture endpoint rejects it. |
| `manual`               | One capture only. Capture the whole hold or part of it, once.                        |
| `manual_multiple`      | Several captures against one authorization, up to the authorized amount.             |
| `scheduled`            | Not implemented. Accepted as a wire value, but payment create and update reject it with `501 Not Implemented`. |
| `sequential_automatic` | Separate authorization and capture run back to back, like `automatic`.                |

Do not build against `scheduled`: it is declared in the enum and published in the spec, but every payment create or update carrying it returns `501 Not Implemented` before the payment is touched. To capture at a later time, use `manual` or `manual_multiple` and call the capture endpoint when you are ready.

Pick `manual_multiple` at creation if you might capture in more than one go. You cannot change your mind after authorizing: a `manual` payment releases whatever you do not capture in the single capture call.

### How to do manual capture

#### Step 1. Create the payment with deferred capture

Set `"capture_method": "manual"` when you create the payment from your server. Omitting `capture_method` gives you `automatic`.

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <api key>' \
--data '{
    "amount": 6540,
    "currency": "USD",
    "confirm": false,
    "capture_method": "manual",
    "authentication_type": "no_three_ds",
    "return_url": "https://duck.com",
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "John"
        }
    }
}'
```

#### Step 2. Confirm, which authorizes

[Confirm](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) the payment after you collect the payment method details, and tell the customer their funds will be held and charged later. Unified checkout does this for you. On successful authorization the payment moves to `requires_capture`.

You can also set `"confirm": true` in step 1 and go straight to capture.

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<original_payment_id>/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <api key>' \
--data '{
    "payment_method": "card",
    "client_secret": "<client_secret_of_the_original_payment>",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "card_cvc": "123"
        }
    }
}'
```

#### Step 3. Capture

Call [`POST /payments/{payment_id}/capture`](https://api-reference.hyperswitch.io/v1/payments/payments--capture). Omit `amount_to_capture` and the whole of `amount_capturable` is captured. Pass it to capture less.

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<payment_id>/capture' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <api key>' \
--data '{
    "amount_to_capture": 6540,
    "statement_descriptor_name": "Joseph",
    "statement_descriptor_suffix": "JS"
}'
```

The endpoint rejects `capture_method: automatic` outright. It accepts the payment only in `requires_capture`, `partially_captured_and_capturable`, `partially_authorized_and_requires_capture`, or `processing`, and `processing` only when the capture method is `manual_multiple`.

`amount_to_capture` must be greater than zero and no greater than the current `amount_capturable`. The only exception is a payment with overcapture enabled, where the ceiling check is skipped; see [Overcapture](overcapture.md). For `manual_multiple`, `amount_to_capture` is required on every capture call.

### What happens to the amount you did not capture

This is the part that decides whether you lose the remainder, and `capture_method` decides it.

**`manual`.** One capture, and the payment lands in a terminal state. Capture the full amount and the payment is `succeeded`. Capture less and the payment is `partially_captured`, `amount_capturable` is set to `0`, and the rest of the hold is not capturable through Hyperswitch again. There is no second capture call. The issuer releases the untouched part of the hold on its own schedule; Hyperswitch does not send a void for it and does not report when the issuer lets go.

**`manual_multiple`.** Each capture creates a capture record. After a capture that does not exhaust the hold, the payment is `partially_captured_and_capturable` and `amount_capturable` becomes the authorized amount minus everything already blocked by earlier captures. That remainder stays capturable, so you can call the capture endpoint again. When the captures add up to the authorized amount, the payment becomes `succeeded`.

`amount_captured` tracks what you actually took, and it is the ceiling for refunds. A payment is refundable only in `succeeded` or `partially_captured`. A `manual_multiple` payment sitting in `partially_captured_and_capturable` is not refundable yet. See [Refunds](../../refunds.md).

### Statuses you will see

| Status                              | What it means for capture                                                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `requires_capture`                  | Authorized. The full authorized amount is capturable.                                                             |
| `succeeded`                         | Everything capturable has been captured. Terminal.                                                                |
| `partially_captured`                | Part captured, nothing left to capture. Terminal. Refundable up to `amount_captured`.                             |
| `partially_captured_and_capturable` | Part captured, remainder still capturable. Not terminal. Not refundable until it becomes terminal.                |
| `partially_authorized_and_requires_capture` | The processor authorized less than you asked for. Capture against the smaller authorized amount.           |
| `cancelled`                         | Voided before any capture.                                                                                        |
| `cancelled_post_capture`            | Voided after a capture. A payment in this state cannot be refunded.                                               |

`partially_captured_and_processing` also exists as a wire value, and it is not a capture status. It is produced only on the partial authorization path, when `enable_partial_authorization` is on, some amount has already been captured, and the attempt is still pending at the processor. No value of `capture_method` produces it. If you are seeing it, look at partial authorization, not at your capture calls.

### About `refund_uncaptured_amount`

The capture request accepts a boolean `refund_uncaptured_amount`. It does nothing today. No code path in the payments backend reads it, so sending `true`, sending `false`, and omitting it all behave the same way, and there is no default to speak of. The field's own description in the API reference says it is not fully supported.

We are working on it. Until it does something, do not plan around it. What governs the remainder is `capture_method`, described above: choose `manual_multiple` at creation if you need the uncaptured part to stay capturable, and accept that with `manual` a partial capture ends the payment.

### Questions this page does not answer

* Capturing more than you authorized, the `enable_overcapture` and `is_overcapture_enabled` fields, and which connectors accept it: [Overcapture](overcapture.md).
* Refund eligibility, the refundable ceiling, and how many refunds one payment allows: [Refunds](../../refunds.md).
* Raising the authorized amount before capture: [Incremental Authorization](../authorizations/incremental-authorization.md).
* Holding an authorization open for longer: [Extended Authorization](../authorizations/extended-authorization.md).
* Whether a given connector supports single or multiple captures: the connector's page under Connectors and Integrations.

Whether an authorization can lapse before you capture it, and what Hyperswitch shows when it does, is not answered here. The backend declares an `expired` status and a `payment_expired` webhook event, but at the commit this page was checked against, no code path sets either for an uncaptured authorization. Until that is resolved, treat authorization lifetime as a connector question and confirm the window with your connector.
