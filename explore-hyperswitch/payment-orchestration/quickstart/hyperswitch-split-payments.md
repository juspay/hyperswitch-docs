---
description: Get started with Split Payments via Hyperswitch
icon: split
---

# Split Payments

Hyperswitch enables split payments, allowing a single transaction to be completed using more than one payment method. This is commonly used for gift card + card scenarios, where a customer pays partially with a gift card and covers the remaining balance with another method.

This capability helps merchants:

* Increase conversion when gift card balances are insufficient
* Improve customer flexibility at checkout
* Support common retail and digital wallet experiences

Hyperswitch manages the orchestration, balance checks, and sequential processing behind the scenes.

### Supported Configurations

Currently, Hyperswitch supports:

* Atmost one gift cards combined with **at most one credit/debit card** (Non-3DS card)
* Gift Cards via Givex (through Adyen)

These configurations are designed to cover the most common real-world split payment use cases while maintaining predictable authorization behavior

### Steps to Enable Split Payments

To activate split Transactions:

1. Enable **Split Transaction** flag from Hyperswitch Control Center under Payment Settings.
2. Configure at least one connector that supports gift cards (e.g., Adyen).

No custom orchestration logic is required on the merchant side beyond standard SDK integration.

<figure><img src="../../../.gitbook/assets/Screen Recording 2026-02-04 at 9 (1).gif" alt=""><figcaption></figcaption></figure>



### Hyperswitch Split Payments Flow

<figure><img src="../../../.gitbook/assets/Untitled (12).svg" alt=""><figcaption></figcaption></figure>



#### 1. Payment Initialization

After the [payment intent](https://api-reference.hyperswitch.io/v1/payments/payments--create) is created, the checkout SDK is initialized. The SDK retrieves and displays all supported payment methods configured for the merchant, including gift cards if they are enabled.

#### 2. Gift Card Application and Validation

When a customer applies a gift card during checkout, the SDK collects the gift card details and sends them for validation.

The backend service then communicates with the configured gift card provider to:

* Validate the gift card credentials
* Retrieve the available balance
* Determine whether an additional payment method is required

The SDK receives the balance and eligibility response and updates the checkout interface accordingly.

If the gift card balance fully covers the transaction amount, the customer can proceed directly to payment confirmation.

If the balance is insufficient, the customer is prompted to add another payment method. The remaining payable amount is automatically calculated and displayed.

#### 3. Payment Confirmation

When the customer confirms the payment, the SDK submits all selected payment method details to Hyperswitch.

At this stage, the system:

* Uses the previously validated gift card balance
* Calculates the amount to be charged to each payment method
* Initiates sequential authorization of the payment methods

#### 4. Sequential Payment Processing

Split payments are processed in a fixed order to maintain transaction consistency and avoid partial payment risks.

**Primary Payment Processing**

If a secondary payment method such as a card is present, the remaining transaction amount is first authorized using that method.

If authorization succeeds, processing continues with the gift card charge.

If authorization fails, the transaction is stopped and the gift card is not charged. The customer can retry using another payment method.

**Gift Card Processing**

After successful authorization of the primary payment method, the gift card is authorized for its applicable amount.

If the gift card authorization succeeds, the transaction proceeds toward completion.

If the gift card authorization fails after the card payment has already been processed, refund handling is automatically triggered for the card payment to maintain transaction consistency.

#### 5. Payment Completion

Once all payment methods are processed, the final transaction status is returned to the SDK.



#### API Details :&#x20;



**Apply a gift card**

```
curl --request POST \
  --url https://sandbox.hyperswitch.io/v2/payments/{id}/eligibility/check-balance-and-apply-pm-data \
  --header 'Content-Type: application/json' \
  --header 'X-Profile-Id: <x-profile-id>' \
  --header 'api-key: <api-key>' \
  --data '
{
  "payment_methods": [
    {
      "gift_card": {
        "givex": {
          "number": "<string>",
          "cvc": "<string>"
        }
      }
    }
  ]
}
'

```



**Payment Confirm with Split PM details**

```
curl --request POST \
  --url https://sandbox.hyperswitch.io/v2/payments/confirm-intent \
  --header 'Content-Type: application/json' \
  --header 'X-Profile-Id: <x-profile-id>' \
  --header 'api-key: <api-key>' \
  --data '
{
    "payment_method_data": {
        "card": {
            "card_cvc": "123",
            "card_exp_month": "10",
            "card_exp_year": "26",
            "card_number": "4000000000001091",
            "card_holder_name": "joseph Doe"
        }
    },
    "payment_method_type": "card",
    "payment_method_subtype": "card",
    "split_payment_method_data": [
        {
            "payment_method_data": {
                "gift_card": {
                    "givex": {
                        "cvc": "123",
                        "number": "6036280000000000000"
                    }
                }
            },
            "payment_method_type": "gift_card",
            "payment_method_subtype": "givex"
        }
    ]  
}
'

```
