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

This flag can be set in the following API calls:

* /payments/create with `confirm = false`
  * /payments/update
* /payments/create call with `confirm = true`

⚠️ Note:

* The request-level `enable_overcapture` will override the profile-level setting.
* Over Capture is only applicable for manual capture payments i.e. `capture_method = manual`.

### Example: API Request

```
{
  "amount": 100,
  "currency": "USD",
  "confirm": true,
  "capture_method": "manual",
  "enable_overcapture": true,
  "payment_method": "card",
  "payment_method_type": "credit",
  "payment_method_data": {
    "card": {
      "card_number": "4111111111111111",
      "card_exp_month": "03",
      "card_exp_year": "30",
      "card_cvc": "7373"
    }
  }
}

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

* `enable_overcapture`
  * `true` → Overcapture was requested for this payment.
  * `false` → Overcapture was not requested.
* `is_overcapture_enabled`
  * `true` → Connector enabled Overcapture for this payment.
  * `false` → Overcapture is not applicable for this PSP/payment.

### Monitoring & Settlement

* After authorization, merchants can view the `amount_capturable` field (under More Payment Details) to see the maximum amount that can be captured.
* Once the payment is captured (or overcaptured), the final amount will be reflected in the `amount_received` field.

### Merchant Action

* Use Dashboard settings for global enablement
* Use API overrides for payment-specific enablement
* Monitor capturable and received amounts to track final settlements
