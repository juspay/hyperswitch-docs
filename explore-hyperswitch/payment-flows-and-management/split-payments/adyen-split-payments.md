---
description: Get started with Adyen Split Payments via Hyperswitch
icon: space-awesome
---

# Adyen Split Payments

Adyen's Split Payments functionality allows businesses to divide a single transaction into multiple payouts, ensuring funds are accurately distributed across various accounts. This feature is supported through their Platform solutions and implemented via Hyperswitch. Hyperswitch facilitates splitting payments during authorization and refund processing, ensuring smooth fund distribution at all transaction stages

***

## Split Adyen payments  via Hyperswitch

In the payment create request, include the Adyen split rule as provided below.

```
     "split_payments": {
        "adyen_split_payment": {
            "store": "4935y84385736",
            "split_items":  [{
            "split_type": "BalanceAccount",
            "amount": 900,
            "account": "*********",
            "reference":"7823648726",
            "description": "adyen split test"
        },
        {
            "split_type": "Commission",
            "amount": 100,
            "account": "************",
            "reference":"7823648726",
            "description": "adyen split test"
        }]
        }
    }
```

Parameters

1.  **store**  \[Optional - not required for Adyen Marketplace ]

    Your unique ID for the Adyen platform store.
2.  **split\_items**\
    Split Rules Array

    The array contains a set of split rules where the sum of the `amount` parameter of each item must equal the total payment amount. \
    \
    Each split item includes the following fields \


    * **split\_type**: \
      Defines the part of the payment you want to book to the specified account.  Possible values \
      \
      &#xNAN;_**BalanceAccount**_**:** Books split amount to the specified account\
      &#xNAN;_**AcquiringFees**_**:** The aggregated amount of the interchange and scheme fees\
      &#xNAN;_**PaymentFee**_**:** The aggregated amount of all transaction fees\
      &#xNAN;_**AdyenFees**_**:** The aggregated amount of Adyen's commission and markup fees\
      &#xNAN;_**AdyenCommission**_**:** The transaction fees due to Adyen under blended rates\
      &#xNAN;_**AdyenMarkup**_**:** The transaction fees due to Adyen under Interchange ++ pricing\
      &#xNAN;_**Interchange**_**:** The fees paid to the issuer for each payment made with the card network\
      &#xNAN;_**SchemeFee**_**:** The fees paid to the card scheme for using their network\
      &#xNAN;_**Commission**_**:** Your platform's commission on the payment (specified in amount), booked to your liable balance account\
      &#xNAN;_**TopUp**_**:** Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods\
      &#xNAN;_**Vat**_**:** The value-added tax charged on the payment, booked to your platforms liable balance account



    * **amount** \[Optional-depending on the [split\_type](https://docs.adyen.com/platforms/online-payments/split-transactions/#split-types)]\
      The value of the part of the payment you want to the specified account.  You do not need to specify this field for transaction fees, because they are not known at the time of payment.\

    * **account**\[Optional-depending on the [split\_type](https://docs.adyen.com/platforms/online-payments/split-transactions/#split-types)]\
      The account that will receive (or be charged) the split amount \

    * **reference**\
      Your unique identifier for the part of the payment you want to book to the specified account\

    * **description**\[Optional]\
      &#x20;Your description for the part of the payment you want to booking to the specified account, returned in Adyen reports.

Payments Response

```
    "split_payments": {
        "AdyenSplitPayment": {
            "store": "4935y84385736",
            "split_items": [
                {
                    "amount": 900,
                    "split_type": "BalanceAccount",
                    "account": "*****************",
                    "reference": "7823648726",
                    "description": "adyen split test"
                },
                {
                    "amount": 100,
                    "split_type": "Commission",
                    "account": "**************",
                    "reference": "7823648726",
                    "description": "adyen split test"
                }
            ]
        }
    },
```

***

## Split Adyen refunds  via Hyperswitch

In the refund create request, include the following according to your split rule

```

     "split_refund": {
        "adyen_split_refund": {
            "store": "4935y84385736",
            "split_items":  [{
            "split_type": "BalanceAccount",
            "amount": 900,
            "account": "*********",
            "reference":"7823648726",
            "description": "adyen split test"
        },
        {
            "split_type": "Commission",
            "amount": 100,
            "account": "************",
            "reference":"7823648726",
            "description": "adyen split test"
        }]
        }
    }
```

Refund Response&#x20;

```
   "split_refund": {
        "adyen_split_refund": {
            "store": "4935y84385736",
            "split_items": [
                {
                    "amount": 900,
                    "split_type": "BalanceAccount",
                    "account": "*****************",
                    "reference": "7823648726",
                    "description": "adyen split test"
                },
                {
                    "amount": 100,
                    "split_type": "Commission",
                    "account": "**************",
                    "reference": "7823648726",
                    "description": "adyen split test"
                }
            ]
        }
    }
```
