---
icon: hexagon-xmark
---

# Xendit Split Payments

If your platform charges a fee or commission when facilitating payments for your partners, or if you need to split payments between multiple parties, this feature enables you to do so automatically. Xendit via Hyperswitch offers multiple ways to route your payments based on your specific use cases.

* Partner to Platform
* Partner to Partner
* Platform to Partner
* Accepting Payments for Sub-Accounts

For more information on these types, refer [here](https://docs.xendit.co/xenplatform/split-payments)

***

## Split Xendit payments  via Hyperswitch

Split payments between multiple sub-merchants, partners, or platforms by including the Xendit split rules in the [payment creation API request](https://api-reference.hyperswitch.io/api-reference/payments/payments--create).

```
 "split_payments": {
        "xendit_split_payment": {
          "multiple_splits" : {
            "name": "20210908 Test",
            "for_user_id":"***************", 
            "description": "Platform fee and Delivery Fee for Marketplace",
            "routes": [
                {
                    "flat_amount": 3000,
                    "currency": "IDR",
                    "destination_account_id": "***************",
                    "reference_id": "1234"
                },
                {
                    "percent_amount": 5,
                    "currency": "IDR",
                    "destination_account_id": "***************",
                    "reference_id": "1235"
                }
            ]
          }
        }
    }
```

Parameters

1. **name**\
   Name to identify split rule. Not required to be unique. Typically based on transaction and/or sub-merchant types
2. **description**\
   Description to identify fee rule
3. **for\_user\_id** \[Optional]\
   The sub-account user-id&#x20;
4. **routes:**\
   Array of objects that define how the platform wants to route the fees and to which accounts. Each Route object is equivalent to a single payment split from the end user to a destination account|\
   \
   a) **flat\_amount** \[Optional]\
   Amount of payments to be split, using flat rate as a unit. This will be null if not applicable. This        will be required if percent\_amount is null. \
   \
   b) **percent\_amount**\
   Number Amount of payments to be split, using a percent rate as unit. This will be null if not applicable. This will be required if flat\_amount is null. Percent amounts are rounded off to the nearest monetary unit.\
   \
   c) **destination\_account\_id**\
   string ID of the destination account where the amount will be routed to. This could be the ID of your platform or sub account.\
   \
   d) **reference\_id**\
   Reference ID which acts as an identifier of the route itself. This is used to distinguish in case one split rule has multiple routes of the same destinations. Its value must be unique and case sensitive for every route object under the same Split Rule.\


**Response of Payment Create will Include**

```
 "split_payments": {
        "xendit_split_payment": {
          "multiple_splits" : {
            "name": "20210908 Test",
            "for_user_id":"***************", //Include in case of partner to platform or platform to partner 
            "description": "Platform fee and Delivery Fee for Marketplace",
            "routes": [
                {
                    "flat_amount": 3000,
                    "currency": "IDR",
                    "destination_account_id": "***************",
                    "reference_id": "1234"
                },
                {
                    "percent_amount": 5,
                    "currency": "IDR",
                    "destination_account_id": "***************",
                    "reference_id": "1235"
                }
            ]
          }
        }
    }
```

### Accept Payments for Sub-Accounts

Include this following request in the payments create

```
 "split_payments": {
        "xendit_split_payment": {
         "single_split" : {
            "for_user_id":"***************",
        }
      }
    }
```

## Refunds for Xendit Split Payments

If you have made a split payment using `for_user_id`, whether for multiple split payments or a single split payment, you will need to include the associated `for_user_id` in the refund request.

```
   "split_refunds": {
        "xendit_split_refund": {
            "for_user_id": "*****************"
        }
    }
```

