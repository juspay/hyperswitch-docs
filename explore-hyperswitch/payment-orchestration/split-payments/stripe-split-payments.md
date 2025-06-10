---
description: Get started with Stripe Split Payments via Hyperswitch
icon: stripe
---

# Stripe Split Payments

Stripe's Split Payments functionality create a charge and split payments between your platform and your sellers or service providers. This feature is supported through their Charge solutions and implemented via Hyperswitch. Hyperswitch facilitates splitting payments during authorization and refund processing, ensuring smooth fund distribution at all transaction stages.

## Split Stripe payments  via Hyperswitch

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

* **transfer\_account\_id**: Identifier of a Connected Account created using the API or through the Dashboard. \{{CONNECTED\_ACCOUNT\_ID\}}
* **charge\_type:** It is of two types: \
  \
  **1.** [**Direct**](https://docs.stripe.com/connect/direct-charges) : This can be used when customers directly transact with your connected account, often unaware of your platform’s existence. You’d like to choose if Stripe fees are debited from your connected accounts or your platform.\
  \
  **2.** [**Destination**](https://docs.stripe.com/connect/destination-charges): This can be used when customers transact with your platform for products or services provided by your connected account. Stripe fees are debited from your platform account.\

* **application\_fees**: This attribute specifies the amount your platform deducts from the transaction as an application fee. After the payment is processed on the connected account, the `application_fee_amount` is transferred to the platform.\


Payments Response

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

In the case of charge typeIn the refund create request, include the following according to your split rule

1. **If "charge\_type": "direct"**

```
"split_refunds": {
    "stripe_split_refund": {
        "revert_platform_fee": true
    }
}
```

Parameter:

**revert\_platform\_fee**: `Boolean`

* Toggle for reverting the application fee that was collected for the payment. If set to false, the funds are pulled from the destination account.



2. **If "charge\_type": "Destination"**

```
"split_refunds": {
    "stripe_split_refund": {
        "revert_platform_fee": true,
        "revert_transfer": true
    }
}
```

Parameter:

**revert\_platform\_fee**: `Boolean`&#x20;

* Indicates whether the application fee should be refunded when refunding this charge.&#x20;
* If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded.&#x20;
* An application fee can be refunded only by the application that created the charge.

**revert\_transfer**: `Boolean`&#x20;

* Indicates whether the transfer should be reversed when refunding this charge.&#x20;
* The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).
* A transfer can be reversed only by the application that created the charge

### Split recurring payments using Hyperswitch via Stripe



1. In CIT call, passing customer\_id is mandatory. Along with that, the Stripe Split Payments object.

```
    "split_payments": {
        "stripe_split_payment": {
            "charge_type": "direct",
            "application_fees": 10,
            "transfer_account_id": "STRIPE_CONNECT_ACCOUNT_ID"
        }
    },
```

#### For charge type=direct

The charge is created on the `connect_account` 's end and not on the platform. We should pass `connect_account_id` in `transfer_account_id` field. If `platform_id` is passed in `transfer_account_id` field then no `application_fees` should not be passed.

#### For charge\_type = destination

The `transfer_account_id` cannot be `platform_account_id`. This is because charge cannot be created on your own account itself. Stripe will throw an error.

\
2\. In CIT call, The merchant would also need to pass the `customer_acceptance` object

```
"customer_acceptance": {
        "acceptance_type": "offline",
        "accepted_at": "1963-05-03T04:07:52.723Z",
        "online": {
            "ip_address": "125.0.0.1",
            "user_agent": "amet irure esse"
        }
    },
```

3\. In the response of the CIT call, the `payment_method_id` and `customer_id` received will be used in future MIT calls. Along with that the merchant would need to pass this object as well in the MIT call

```
"split_payments": {
        "stripe_split_payment": {
            "charge_type": "direct",
            "application_fees": 10,
            "transfer_account_id": "STRIPE_CONNECT_ACCOUNT_ID"
        }
    }

```

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
    },
    "browser_info": {
        "user_agent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/70.0.3538.110 Safari\/537.36",
        "accept_header": "text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,image\/apng,*\/*;q=0.8",
        "language": "nl-NL",
        "color_depth": 24,
        "screen_height": 723,
        "screen_width": 1536,
        "time_zone": 0,
        "java_enabled": true,
        "java_script_enabled": true,
        "ip_address": "128.0.0.1"
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
