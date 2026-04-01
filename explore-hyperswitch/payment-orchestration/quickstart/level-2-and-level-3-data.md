---
description: Learn how to include Level 2 and Level 3 enhanced data in payment requests to optimize interchange costs on commercial card transactions
---

# Level 2 and Level 3 data

### Overview

Juspay Hyperswitch allows merchants to include **Level 2 and Level 3** enhanced data in payment requests to optimize interchange costs on eligible commercial card transactions. This is done using a set of unified fields in the `payment_create` API, which are internally routed and transformed per connector.

- Level 2: Adds tax, invoice, and reference-level data
- Level 3: Adds full line-item details (e.g., item quantity, commodity code, shipping, duty)

Visa and Mastercard support Level 2 and Level 3 processing. American Express supports Level 2 only.

### Availability

- Regions: Most connectors currently support U.S. domestic processing only for Level 2 and Level 3 data
- Support for level 2/level 3 varies by connector and is not guaranteed

### Unified L2/L3 Fields

Hyperswitch exposes a set of generic fields in the `payment_create` API that can be directly used to pass Level 2 and Level 3 data. These fields cover the most common requirements across card networks and connectors, so merchants can send enhanced transaction data without worrying about connector-specific differences.

The fields are organized into two groups:

#### 1. Top-Level Fields (apply to the entire order/payment)

These fields represent order-wide attributes that are required by most connectors:

- `order_date` — when the order was placed
- `customer_reference` — unique reference, PO number, or invoice number
- `order_tax_amount` — total sales tax for the order
- `shipping_cost` — freight/shipping charges
- `duty_amount` — duty or customs charges
- `discount_amount` — any discount applied at the order level
- `tax_status` — whether the order is taxable or exempt

#### 2. Nested Fields (grouped by domain for clarity)

Some data is structured to align with domain-specific groupings, making it easier to map downstream:

- Shipping
  - `shipping.*` (general attributes)
  - `shipping.address.*` (e.g., line1, postal_code, country)
  - `shipping.phone.*`
  - `shipping.email`
- Customer
  - `customer.*` (general attributes)
  - `customer.address.*`
  - `customer.phone.*`
  - `customer.email`
- Order Details (Line Items)

  Each item can include:
  - `order_details[].product_name`
  - `order_details[].commodity_code`
  - `order_details[].quantity`
  - `order_details[].unit_of_measure`
  - `order_details[].unit_price`
  - `order_details[].item_tax_amount`
  - `order_details[].item_discount_amount`

### Supported Connectors

Our unified (generic) L2/L3 fields in `payment_create` cover the majority of requirements across connectors.

If your connector requires fields that aren't in our unified list, we'll evaluate and add the minimal set needed.
