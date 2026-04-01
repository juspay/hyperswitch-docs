---
icon: chart-diagram
---

# Overcapture

### Overview

In card payments, Over Capture occurs when a merchant captures (settles) an amount greater than the originally authorized amount.

This is particularly useful in scenarios such as:

* Additional charges (e.g., shipping, handling, gratuities).
* Price adjustments made after initial authorization.
* Reducing the risk of under-capturing when final order values differ.

### Enabling Over Capture

#### 1. Profile-level Configuration (via Dashboard)

* Navigate to:\
  Developer → Payment Settings → Always Enable Over Capture
* Toggle Enable/Disable as required.

#### 2. Per-request Configuration (via API)

Use the boolean field `enable_overcapture` in your payment request.

This can be passed in:

[POST /payments ](https://api-reference.hyperswitch.io/v1/payments/payments--create)

[POST /payments/:id/update](https://api-reference.hyperswitch.io/v1/payments/payments--update)

⚠️ Note:

* The request-level `enable_overcapture` will override the profile-level setting.
* Over Capture is only applicable for manual capture payments i.e. `capture_method = manual`.

***

### Example: API Request

```json
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your_publishable_key>' \
--data '{
  "amount": 100,
  "currency": "USD",
  "confirm": true,
  "capture_method": "manual",
  "enable_overcapture": true,
}'

```

### Example: API Response

```json
{
  "payment_id": "pay_GPnTPs4e56yZ8FKAcj0K",
  "status": "requires_capture",
  "amount": 100,
  "amount_capturable": 100,
  "connector": "adyen",
  "enable_overcapture": true,
  "is_overcapture_enabled": true,
  "capture_method": "manual",
  "payment_method": "card",
  "payment_method_type": "debit",
  "network_transaction_id": "112181545921495",
  "created": "2025-09-24T11:29:55.629Z",
  "expires_on": "2025-09-24T11:44:55.629Z"
}

```

#### Field Semantics

`enable_overcapture` Indicates merchant intent.

| Value   | Meaning                    |
| ------- | -------------------------- |
| `true`  | Over-capture requested     |
| `false` | Over-capture not requested |

***

`is_overcapture_enabled` Indicates connector capability acceptance.

| Value   | Meaning                                     |
| ------- | ------------------------------------------- |
| `true`  | Connector supports and enabled over-capture |
| `false` | Connector does not support over-capture     |

***

### Monitoring & Settlement

* After authorization, merchants can view the `amount_capturable` field (under More Payment Details) to see the maximum amount that can be captured.
* Once the payment is captured (or overcaptured), the final amount will be reflected in the `amount_received` field.

### Merchant Action

* Use Dashboard settings for global enablement
* Use API overrides for payment-specific enablement
* Monitor capturable and received amounts to track final settlements
