---
description: >-
  Configure and use Adyen Split Settlements via Hyperswitch to distribute
  payments and refunds across multiple accounts.
icon: space-awesome
metaLinks:
  alternates:
    - adyen-split-payments.md
---

<!-- truth manifest; hyperswitch 59c3249bf29bc3800ce391de49fab00590c0cf9e
     symbols: SplitPaymentsRequest.adyen_split_payment externally tagged shape = crates/common_types/src/payments.rs:35-66
     symbols: AdyenSplitData.store, split_items; AdyenSplitItem.amount, split_type, account, reference, description = crates/common_types/src/domain.rs:14-75
     symbols: Adyen split amount and field validation = crates/router/src/core/payments/helpers.rs:9628-9710
     symbols: ConnectorChargeResponseData.adyen_split_payment snake_case response key = crates/common_types/src/payments.rs:436-468
     checked: 2026-10-05 -->

# Adyen Split Settlement

### Before you start

Enable split settlement for the Business Profile and configure an Adyen merchant connector account for that profile. The sum of provided split amounts must equal the payment amount, and each split type must include the fields required by the validation rules below.

### Overview

Juspay Hyperswitch supports Adyen's Split Settlements functionality, allowing businesses to divide a single transaction into multiple payouts, ensuring funds are accurately distributed across various accounts. This feature is supported through their Platform solutions and implemented via Hyperswitch.

Hyperswitch facilitates splitting payments during both authorization and refund processing, ensuring smooth fund distribution at all transaction stages.

### Split Adyen Payments via Juspay Hyperswitch

In the [payment create](https://api-reference.hyperswitch.io/v1/payments/payments--create) request, include the Adyen split rule as provided below.

```json
{
  "split_payments": {
    "adyen_split_payment": {
      "store": "4935y84385736",
      "split_items": [
        {
          "split_type": "BalanceAccount",
          "amount": 900,
          "account": "*********",
          "reference": "7823648726",
          "description": "adyen split test"
        },
        {
          "split_type": "Commission",
          "amount": 100,
          "account": "************",
          "reference": "7823648726",
          "description": "adyen split test"
        }
      ]
    }
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

```json
{
  "split_payments": {
    "adyen_split_payment": {
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
}
```

### Split Adyen Refunds via Juspay Hyperswitch

In the [refund create request](https://api-reference.hyperswitch.io/v1/refunds/refunds--create#refunds-create), include the following according to your split rule.

```json
{
  "split_refund": {
    "adyen_split_refund": {
      "store": "4935y84385736",
      "split_items": [
        {
          "split_type": "BalanceAccount",
          "amount": 900,
          "account": "*********",
          "reference": "7823648726",
          "description": "adyen split test"
        },
        {
          "split_type": "Commission",
          "amount": 100,
          "account": "************",
          "reference": "7823648726",
          "description": "adyen split test"
        }
      ]
    }
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

```json
{
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
}
```
