# Payments Report

## Payments Report — Column Reference

The Payments Report is a CSV export generated from the Control Center that gives you a row-by-row breakdown of every payment attempt in the selected time range. Each row represents a single **payment attempt** (a payment can have more than one attempt if it was retried), so `payment_id` may repeat across rows while `attempt_id` is always unique.

Below is what each column in the report means.

| Column                         | What it means                                                                                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `payment_id`                   | The unique identifier for the payment. Stays the same across retries of the same payment.                                                                    |
| `attempt_id`                   | The unique identifier for this specific attempt to process the payment.                                                                                      |
| `status`                       | The outcome of this attempt — e.g. `charged` (successful), `failed`, `pending`, `cancelled`, `requires_capture`.                                             |
| `amount`                       | The amount that was attempted, in the payment's currency's standard unit (e.g. `100.0` for $100).                                                            |
| `currency`                     | The 3-letter currency code for the payment (e.g. `USD`, `EUR`).                                                                                              |
| `connector`                    | The payment processor/gateway used to process this attempt (e.g. `stripe`, `adyen`).                                                                         |
| `connector_transaction_id`     | The transaction reference ID returned by the connector/processor — useful when reconciling with the processor's own dashboard or statements.                 |
| `amount_to_capture`            | For payments using manual capture, the amount that was (or is to be) captured. Empty if not applicable or if the full amount was captured.                   |
| `customer_id`                  | Your identifier for the customer who made the payment.                                                                                                       |
| `created_at`                   | Timestamp when the attempt was created.                                                                                                                      |
| `order_details`                | Line-item/order details passed at payment creation, if provided.                                                                                             |
| `error_message`                | Human-readable reason the attempt failed, if it did.                                                                                                         |
| `capture_method`               | How the payment is captured — `automatic` (captured immediately on success) or `manual` (captured separately later).                                         |
| `authentication_type`          | Whether 3D Secure authentication was used — `three_ds` or `no_three_ds`.                                                                                     |
| `mandate_id`                   | The mandate reference, if this payment was made using a saved mandate (e.g. for recurring/subscription payments).                                            |
| `payment_method`               | The high-level payment method used — e.g. `card`, `wallet`, `bank_transfer`.                                                                                 |
| `payment_method_type`          | The specific type within the payment method — e.g. `credit`, `debit`, `google_pay`.                                                                          |
| `metadata`                     | Any custom key-value metadata you attached to the payment.                                                                                                   |
| `setup_future_usage`           | Indicates whether the payment method was saved for future use, and how — `on_session` or `off_session`.                                                      |
| `statement_descriptor_name`    | The text that appears on the customer's card/bank statement for this charge, if customized.                                                                  |
| `description`                  | A free-text description of the payment, if provided.                                                                                                         |
| `off_session`                  | Whether the payment was made without the customer being actively present (e.g. a subscription charge).                                                       |
| `business_country`             | The business unit/country this payment was processed under, if your account uses business profiles by country.                                               |
| `business_label`               | The business unit label this payment was processed under, if configured.                                                                                     |
| `business_sub_label`           | A further sub-classification of the business unit, if configured.                                                                                            |
| `allowed_payment_method_types` | The list of payment method types that were allowed to be shown/used for this payment, if restricted.                                                         |
| `payment_method_data`          | Details captured about the payment method used (e.g. card last 4 digits, card ISIN, expiry) — sensitive fields are masked.                                   |
| `card_network`                 | The card scheme/network used, if the payment was made by card — e.g. `Visa`, `Mastercard`.                                                                   |
| `fingerprint_id`               | An identifier that stays consistent for the same underlying payment instrument (e.g. same card) across payments, useful for spotting repeat customers/cards. |
| `modified_at`                  | Timestamp when the attempt was last updated (e.g. moved from pending to charged).                                                                            |
| `error_code`                   | The error code returned when the attempt failed, if it did.                                                                                                  |
| `payment_method_id`            | The identifier of the saved payment method used, if the customer paid with a previously saved payment method.                                                |
| `card_holder_name`             | The cardholder's name as provided at checkout, if applicable.                                                                                                |
| `merchant_order_reference_id`  | Your own order/reference ID for this payment, if you passed one when creating it — useful for matching against your internal order system.                   |
| `profile_id`                   | The business profile this payment belongs to (relevant if you operate multiple profiles under one merchant account).                                         |

### Notes

* Many fields are blank when they don't apply to a given payment (e.g. `mandate_id` is empty for one-off payments, `business_country`/`business_label` are empty unless business profiles by country/label are configured).
* One `payment_id` can appear on multiple rows if the payment was retried — each row is a distinct `attempt_id`.
