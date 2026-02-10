---
hidden: true
---

# Extended Authorization

#### **Overview**

Extended Authorization allows merchants to extend the authorization hold period beyond the standard window — giving more flexibility before a transaction is captured or settled.

This is particularly useful for industries where the final transaction amount or service completion time isn’t known upfront — such as:

* Hospitality (room service or stay extensions)
* Car rentals (extra mileage, damages)
* Fuel & utilities (variable usage-based billing)

Example: A hotel may authorize a card for $500 during check-in but extend the authorization period if the guest extends their stay.

### How to Enable Extended Authorization

You can enable Extended Authorization at two levels — Profile Level or Per Payment Request.

#### 1. Profile-level configuration (via Dashboard)

To enable globally across all transactions:

1. Navigate to Developer → Payment Settings → Always Enable Extended Authorization
2. Toggle Enable/Disable as required

#### 2. Per-request configuration (via API)

To enable it for specific transactions, include the boolean field request\_extended\_authorization in your payment request.

This flag can be used in the following API calls:

* /payments/create with `confirm = false`
  * /payments/update
* /payments/create call with `confirm = true`

> **⚠️ Note:**
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
  "extended_authorization_last_applied_at": "2025-09-24T11:29:55.729Z"
  "extended_authorization_applied": true,
  "request_extended_authorization": true,
  "capture_by": "2025-09-24T11:44:55.629Z"
}

```

#### 3. Post-Authorization: Extended Authorization via API

Some connectors require extended authorization to be triggered manually. This API allows you to request an extended authorization when automatic handling is not supported.

Currently, manual extended authorization is supported for:

* Adyen
* PayPal

Calling this endpoint will initiate an extended authorization request. The actual behavior, including how much the capture or honor period is extended, depends on the specific connector and the issuing bank.&#x20;

{% hint style="info" %}
Be aware: With some connectors like Adyen, a failed extended authorization attempt may also cause the initial authorization to fail.
{% endhint %}



> **⚠️ Note:**
>
> * To use this API, extended authorization must be enabled for the authorization you are attempting to extend.
> * Adyen handles extended authorization asynchronously. In such cases, you’ll need to perform a psync to retrieve the updated response.

### Example Request

```
curl --location --request POST '{{basue_url}}/payments/{{payment_id}}/extend_authorization' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: ******************'
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
  "extended_authorization_last_applied_at": "2025-09-24T12:29:55.729Z"
  "extended_authorization_applied": true,
  "request_extended_authorization": true,
  "capture_by": "2025-09-24T11:44:55.629Z"
}

```

### Response Field Reference

| `request_extended_authorization`         | Indicates if extended authorization was requested for this payment               |
| ---------------------------------------- | -------------------------------------------------------------------------------- |
| `extended_authorization_applied`         | Shows whether extended authorization has been applied                            |
| `capture_by`                             | The deadline for capturing the payment (if available from the connector)         |
| `extended_authorization_last_applied_at` | The date when the connector last successfully applied an extended authorization. |

If the connector doesn’t provide the capture deadline, the `capture_by` field will appear as null.

### Monitoring

After authorization, you can view the capture deadline under `capture_by` in the More Payment Details section of the dashboard. This helps you ensure capture occurs before the authorization hold expires. If `capture_by` is not available use the `extended_authorization_last_applied_at` parameter to compute the capture window&#x20;

