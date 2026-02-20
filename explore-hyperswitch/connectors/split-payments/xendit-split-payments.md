---
icon: hexagon-xmark
---

# Xendit Split Settlement

### Overview

If your platform charges a fee or commission when facilitating payments for your partners, or if you need to split settlement between multiple parties, this feature enables you to do so automatically. Xendit via Hyperswitch offers multiple routing methods to support diverse use cases:

* Partner to Platform
* Partner to Partner
* Platform to Partner
* Accepting Payments for Sub-Accounts

For more information on these types, refer [here](https://docs.xendit.co/xenplatform/split-payments)

## Split Xendit payments via Hyperswitch

Split settlements between multiple sub-merchants, partners, or platforms by including the Xendit split rules in the [payment creation API request](https://api-reference.hyperswitch.io/api-reference/payments/payments--create).

#### Example: Flat amount Split

```json
{  
  "amount": 10000,  
  "currency": "IDR",  
  "confirm": true,  
  "split_payments": {  
    "xendit_split_payment": {  
      "multiple_splits": {  
        "name": "Marketplace Split",  
        "description": "Platform fee and merchant payment",  
        "routes": [  
          {  
            "flat_amount": 1000,  
            "currency": "IDR",  
            "destination_account_id": "platform_account_123",  
            "reference_id": "platform_fee"  
          },  
          {  
            "flat_amount": 9000,  
            "currency": "IDR",   
            "destination_account_id": "merchant_account_456",  
            "reference_id": "merchant_payment"  
          }  
        ]  
      }  
    }  
  }  
}
```

#### Example: Percentage-Based Split

```json
{  
  "amount": 10000,  
  "currency": "IDR",  
  "confirm": true,  
  "split_payments": {  
    "xendit_split_payment": {  
      "multiple_splits": {  
        "name": "Percentage Split",  
        "description": "Commission-based split",  
        "routes": [  
          {  
            "percent_amount": 10,  
            "currency": "IDR",  
            "destination_account_id": "platform_account_123",  
            "reference_id": "commission"  
          },  
          {  
            "percent_amount": 90,  
            "currency": "IDR",  
            "destination_account_id": "merchant_account_456",   
            "reference_id": "merchant_share"  
          }  
        ]  
      }  
    }  
  }  
}
```

#### Constraints & Validation Logic

Constrains are that:

* Each route must specify either `flat_amount` OR `percent_amount`, never both
* For zero-amount payments, all split amounts must be zero
* Sum of split amounts cannot exceed total payment amount

The validation ensures that:

1. **Missing both fields**: Returns error `Expected either split_payments.xendit_split_payment.routes.flat_amount or split_payments.xendit_split_payment.routes.percent_amount to be provided`
2. **Having both fields**: Returns error `Expected either split_payments.xendit_split_payment.routes.flat_amount or split_payments.xendit_split_payment.routes.percent_amount, but not both`

#### **XenditSplitRequest Structure**

The main `XenditSplitRequest` enum supports two types:

1. **MultipleSplits** - For splitting across multiple accounts
2. **SingleSplit** - For routing to a single sub-merchant

#### **MultipleSplits Parameters**

For the `XenditMultipleSplitRequest` structure payments.rs:352-361 :

**`name`** (string, **required**)

* Name to identify the split rule
* Not required to be unique
* Typically based on transaction and/or sub-merchant types

**`description`** (string, **required**)

* Description to identify the fee rule
* Used for internal tracking and identification

**`for_user_id`** (string, optional)

* The sub-account user-id that you want to make this transaction for
* Used when making payments on behalf of a sub-merchant

**`routes`** (array, **required)**

* Array of `XenditSplitRoute` objects that define how the platform wants to route the fees and to which accounts
* Each route object represents a single payment split from the end user to a destination account

#### **XenditSplitRoute Parameters**

Each route in the `routes` array has these parameters payments.rs:331-343 :

**`flat_amount`** (MinorUnit, optional)

* Amount of payments to be split using a flat rate
* Specified in minor units (e.g., 3000 for $30.00 or 30.00 IDR)
* **Validation**: Must specify either `flat_amount` OR `percent_amount`, never both helpers.rs:466-473

**`percent_amount`** (i64, optional)

* Amount of payments to be split using a percentage rate
* Integer percentage value (e.g., 5 = 5%)
* Percent amounts are calculated and rounded to the nearest monetary unit helpers.rs:478

**`currency`** (Currency enum, **required**)

* Currency code for the split amount
* Must match supported currency values

**`destination_account_id`** (string, **required**)

* ID of the destination account where the amount will be routed
* Can be the ID of your platform account or sub-merchant account

**`reference_id`** (string, **required**)

* Reference ID that acts as an identifier for the route itself
* Used to distinguish routes when one split rule has multiple routes to the same destination
* Must be unique and case-sensitive for every route object under the same split rule

#### SingleSplit Parameters

For single split settlements, the structure is simpler domain.rs:55-58 :

**`for_user_id`** (string, **required**)

* The sub-account user-id that you want to make this transaction for
* Required field for single split scenarios

#### Split Settlement Response Types

**Multiple Splits Response**

For multiple splits, the `charges` field contains detailed split rule information:

<pre><code>{"charges": {
    "xendit_split_payment":{
<strong>        "multiple_splits": {
</strong>            "split_rule_id": "sr_12345", 
            "for_user_id": "user_123", 
            "name": "Split Rule Name",
            "description": "Split description",
            "routes": [...]        
            }      
        }
    }  
}
</code></pre>

Key fields to document:

* `split_rule_id`: Generated during preprocessing step transformers.rs:549-555
* `for_user_id`: Optional sub-merchant identifier
* `routes`: Array of split route details with amounts and destinations

**Single Split Response**

For single splits, the structure is simpler transformers.rs:370-382 :

```
{"charges": { 
    "xendit_split_payment": {
        "single_split": {
            "for_user_id": "user_123"       
         }      
     }    
   }  
}
```

#### Response Processing Flow

Document the transformation process:

1. **Raw Xendit Response**: Received from Xendit's API
2. **Response Transformation**: Converted using the transformer logic transformers.rs:496-576
3. **Charge Data Storage**: Split information preserved for subsequent operations

#### Important Documentation Points

**Field Usage Distinction**: `split_payments` is used in requests while `charges` is used in responses. This is a common source of confusion.

**Preprocessing Context**: For multiple splits, the response includes data from the preprocessing step where split rules are created.

**Refund Integration**: The response data is used for refunds, particularly the `for_user_id` field requirement.

## Refunds for Xendit Split Payments

If you have made a split payment using `for_user_id`, whether for multiple split payments or a single split payment, you will need to include the associated `for_user_id` in the refund request.

```
   "split_refunds": {
        "xendit_split_refund": {
            "for_user_id": "*****************"
        }
    }
```
