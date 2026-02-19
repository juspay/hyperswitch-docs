---
description: Get started with Adyen Split Settlements via Hyperswitch
icon: space-awesome
---

# Adyen Split Settlement

Adyen's Split Settlements functionality allows businesses to divide a single transaction into multiple payouts, ensuring funds are accurately distributed across various accounts. This feature is supported through their Platform solutions and implemented via Hyperswitch. Hyperswitch facilitates splitting payments during authorization and refund processing, ensuring smooth fund distribution at all transaction stages

***

## Split Adyen payments via Hyperswitch

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

#### Field Specifications

**`store`** (Optional): Required only for Adyen Platform implementations, not needed for Adyen Marketplace.

**`split_items`**: Array of split rules where the sum of all `amount` values must equal the total payment amount.

**Split Item Fields**

**`split_type`**: Defines the payment portion allocation. Supported values:

* `BalanceAccount`: Direct allocation to specified account (requires `account` field)
* `Commission`: Platform commission (requires `amount` field)
* `Vat`: Value-added tax allocation
* `TopUp`: Balance account funding (requires `account`, not available with Platform)
* Fee types (`AcquiringFees`, `PaymentFee`, `AdyenFees`, etc.): Calculated automatically

**`amount`**: Split amount in minor units. Required for `Commission`, `Vat`, and `TopUp` types; optional for fee types as they're calculated by Adyen.

**`account`**: Target account identifier. Required for `BalanceAccount` and `TopUp` types.

**`reference`**: Unique identifier for tracking.

**`description`**: Optional description for reporting.

#### Validation Rules

Hyperswitch enforces several validation rules:

* Split amounts must sum to total payment amount
* `BalanceAccount` and `TopUp` types require `account` field
* `Commission`, `Vat`, and `TopUp` types require `amount` field
* `TopUp` splits are incompatible with Platform store configuration

#### Payments Response

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

## Split Adyen refunds via Hyperswitch

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

The request structure includes fields:

* `store`: Optional store identifier for Adyen Platform
* `split_items`: Array of split items with the same structure as payment splits
* `split_type`: The type of split (BalanceAccount, Commission, etc.)
* `amount`: Split amount in minor units
* `account`: Target account identifier
* `reference`: Unique identifier for tracking
* `description`: Optional description

#### Refund Response

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
