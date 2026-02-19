---
description: Get started with Stripe Split Settlements via Hyperswitch
icon: stripe
---

# Stripe Split Settlement

Stripe's Split Settlements functionality allows you to create charges and distribute payments between your platform and connected accounts (sellers or service providers). This feature is implemented in Hyperswitch through the `SplitPaymentsRequest` and supports both payment authorization and refund processing.

## Stripe Split settlements via Hyperswitch

In the payment create request, include the Stripe split rule as provided below.

```
     "split_payments": {
    	"stripe_split_payment": {
        	"charge_type": "direct",
        	"application_fees": 100,
        	"transfer_account_id": "{{CONNECTED_ACCOUNT_ID}}"
    	}
      }

```

Parameters

* **transfer\_account\_id**: Identifier of a Connected Account created using Stripe's API or Dashboard. \{{CONNECTED\_ACCOUNT\_ID\}}
* **charge\_type:** It is of two types:\
  \
  **1.** [**Direct**](https://docs.stripe.com/connect/direct-charges) : Customers transact directly with your connected account. The charge is created on the connected account, and you can choose whether Stripe fees are debited from the connected account or your platform.\
  \
  **2.** [**Destination**](https://docs.stripe.com/connect/destination-charges): Customers transact with your platform for products/services provided by your connected account. Stripe fees are debited from your platform account. The funds are then transferred to the destination account.\\
* **application\_fees**: Platform fee amount deducted from the transaction (in minor currency units. The `application_fee_amount` is transferred to the platform.\\

### Payment Response

The response includes charge details for split settlements:

```
    "split_payments": {
        "stripe_split_payment": {
            "charge_id": "ch_3QSzoAIhl7EEkW0O12IPHRiC",
            "charge_type": "direct",
            "application_fees": 100,
            "transfer_account_id": "acct_1PDftAIhl7EEkW0O"
        }
    }
```

## Split Stripe refunds via Hyperswitch

For refunds, include the appropriate split refund configuration based on the original charge type.

1. **For "charge\_type": "direct"**

```
"split_refunds": {
    "stripe_split_refund": {
        "revert_platform_fee": true
    }
}
```

2. **For "charge\_type": "Destination"**

```
"split_refunds": {
    "stripe_split_refund": {
        "revert_platform_fee": true,
        "revert_transfer": true
    }
}
```

**Refund Parameters:**

**revert\_platform\_fee**: `Boolean`

* Indicates whether the application fee should be refunded when refunding this charge.
* If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded.
* An application fee can be refunded only by the application that created the charge.

**revert\_transfer**: `Boolean`

* Indicates whether the transfer should be reversed when refunding this charge.
* The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).
* A transfer can be reversed only by the application that created the charge

### Recurring Payments (CIT/MIT) with Split Settlements

**Customer-Initiated Transaction (CIT)**

1. In CIT call, passing `customer_id` is mandatory. Along with that, the Stripe Split settlements object.

```
{  
    "customer_id": "StripeCustomer123",  
    "split_payments": {  
        "stripe_split_payment": {  
            "charge_type": "direct",  
            "application_fees": 100,  
            "transfer_account_id": "acct_123456789"  
        }  
    },  
    "customer_acceptance": {  
        "acceptance_type": "offline",  
        "accepted_at": "1963-05-03T04:07:52.723Z",  
        "online": {  
            "ip_address": "125.0.0.1",  
            "user_agent": "amet"  
        }  
    }  
}
```

The split settlement metadata is stored in the mandate for future MIT calls.

#### Important Implementation Notes

* For **direct** charges, the `transfer_account_id` must be the connected account ID, not your platform account ID.
* For **destination** charges, the `transfer_account_id` cannot be your platform account ID as Stripe doesn't allow charges to your own account.
* The system validates that MIT calls match the split settlement configuration from the original CIT call.

<details>

<summary>Example of CIT call</summary>

```bash
{
    "amount": 200,
    "currency": "USD",
    "confirm": true,
    "capture_method": "automatic",
    "amount_to_capture": 200,
    "customer_id": "cus_idxxxxxxx",
    "setup_future_usage": "off_session",
    "customer_acceptance": {
        "acceptance_type": "offline",
        "accepted_at": "1963-05-03T04:07:52.723Z",
        "online": {
            "ip_address": "125.0.0.1",
            "user_agent": "amet irure esse"
        }
    },
    "authentication_type": "no_three_ds",
    "return_url": "",
    "name": "John Doe",
    "phone": "999999999",
    "phone_country_code": "+65",
    "description": "Its my first payment request",
    "payment_method": "card",
    "payment_method_type": "debit",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "09",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "card_cvc": "123"
        }
    },
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "joseph",
            "last_name": "Doe"
        },
        "phone": {
            "number": "8056XXX427",
            "country_code": "+91"
        }
    },
    "split_payments": {
        "stripe_split_payment": {
            "charge_type": "direct",
            "application_fees": 10,
            "transfer_account_id": "STRIPE_CONNECT_ACCOUNT_ID"
        }
    }
}
```

</details>

<details>

<summary>Example of MIT call</summary>

```bash
{
    "amount": 200,
    "currency": "USD",
    "customer_id": "cus_vnkxxxxxxxxjk",    // customer_id field received in CIT response
    "description": "Subsequent Mandate Test Payment (MIT from New CIT Demo)",
    "confirm": true,
    "off_session": true,
    "recurring_details": {
        "type": "payment_method_id",
        "data": "pm_hxxxxxxxxoqw7"    // payment_method_id field received in CIT response    
    },
    "split_payments": {
        "stripe_split_payment": {
            "charge_type": "direct",
            "application_fees": 10,
            "transfer_account_id": "STRIPE_CONNECT_ACCOUNT_ID"
        }
    }
}

```

</details>
