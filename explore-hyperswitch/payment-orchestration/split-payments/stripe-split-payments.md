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
