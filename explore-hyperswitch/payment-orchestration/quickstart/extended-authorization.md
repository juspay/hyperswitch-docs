---
icon: clock
---

# Extended Authorization

### Overview

Extended Authorization allows merchants to extend the authorization hold period beyond the standard window — giving more flexibility before a transaction is captured or settled.

This is particularly useful for industries where the final transaction amount or service completion time isn’t known upfront — such as:

* Hospitality (room service or stay extensions)
* Car rentals (extra mileage, damages)
* Fuel & utilities (variable usage-based billing)

Example: A hotel may authorize a card for $500 during check-in but extend the authorization period if the guest extends their stay.

### Current PSP Support

Hyperswitch currently supports Extended Authorization for the following PSPs:

* Stripe

If you require Extended Authorization for other PSPs, please reach out to the Hyperswitch Support Team.

### How to Enable Extended Authorization

You can enable Extended Authorization at two levels — Profile Level or Per Payment Request.

#### 1. Profile-level configuration (via Dashboard)

To enable globally across all transactions:

1. Navigate to Developer → Payment Settings → Always Enable Extended Authorization
2. Toggle Enable/Disable as required

#### 2. Per-request configuration (via API)

To enable it for specific transactions, include the boolean field request\_extended\_authorization in your payment request.

This flag can be used in the following API calls:

* /payments/create with `confirm = false`&#x20;
  * /payments/update
* /payments/create call with `confirm = true`

> **⚠️ Note:**&#x20;
>
> * The value of request\_extended\_authorization in the request will override the profile-level setting.
> * Extended Authorization is applicable only for manual capture payments (`capture_method = manual`)

### Example Request

```json
{
  "amount": 100,
  "currency": "USD",
  "confirm": true,
  "capture_method": "manual",
  "request_extended_authorization": true,
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

### Example Response

```json
{
  "payment_id": "pay_GPnTPs4e56yZ8FKAcj0K",
  "status": "requires_capture",
  "amount": 100,
  "amount_capturable": 100,
  "connector": "stripe",
  "enable_overcapture": true,
  "is_overcapture_enabled": true,
  "capture_method": "manual",
  "payment_method": "card",
  "payment_method_type": "debit",
  "network_transaction_id": "112181545921495",
  "created": "2025-09-24T11:29:55.629Z",
  "extended_authorization_applied": true,
  "request_extended_authorization": true,
  "capture_by": "2025-09-24T11:44:55.629Z"
}

```

### Response Field Reference

| `enable_overcapture`             | Indicates if overcapture was requested for this payment                  |
| -------------------------------- | ------------------------------------------------------------------------ |
| `extended_authorization_applied` | Shows whether extended authorization has been applied                    |
| `capture_by`                     | The deadline for capturing the payment (if available from the connector) |

If the connector doesn’t provide the capture deadline, the `capture_by` field will appear as null.

### Monitoring

After authorization, you can view the capture deadline under `capture_by` in the More Payment Details section of the dashboard. This helps you ensure capture occurs before the authorization hold expires.

\
