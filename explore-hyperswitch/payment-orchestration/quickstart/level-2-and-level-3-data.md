# Level 2 and Level 3 data

### Overview

Hyperswitch allows merchants to include **Level 2 and Level 3** enhanced data in payment requests to optimize interchange costs on eligible commercial card transactions. This is done using a set of unified fields in the payment\_create API, which are internally routed and transformed per connector.

* Level 2: Adds tax, invoice, and reference-level data
* Level 3: Adds full line-item details (e.g., item quantity, commodity code, shipping, duty)

Visa and Mastercard support Level 2 and 3 processing. American Express supports Level 2 only

### Availability

* Regions: Most connectors currently support U.S. domestic processing only for Level 2 and Level 3 data
* Support for level 2/level 3 varies by connector and is not guaranteed

### Unified L2/L3 Fields

Hyperswitch exposes a set of generic fields in the payment\_create API that can be directly used to pass Level 2 and Level 3 data. These fields cover the most common requirements across card networks and connectors, so merchants can send enhanced transaction data without worrying about connector-specific differences.

The fields are organized into two groups:

#### 1. Top-Level Fields (apply to the entire order/payment)

These fields represent order-wide attributes that are required by most connectors:

* order\_date — when the order was placed
* customer\_reference — unique reference, PO number, or invoice number
* order\_tax\_amount — total sales tax for the order
* shipping\_cost — freight/shipping charges
* duty\_amount — duty or customs charges
* discount\_amount — any discount applied at the order level
* tax\_status — whether the order is taxable or exempt

#### 2. Nested Fields (grouped by domain for clarity)

Some data is structured to align with domain-specific groupings, making it easier to map downstream:

* Shipping
  * shipping.\* (general attributes)
  * shipping.address.\* (e.g., line1, postal\_code, country)
  * shipping.phone.\*
  * shipping.email<br>
* Customer
  * customer.\* (general attributes)
  * customer.address.\*
  * customer.phone.\*
  * customer.email<br>
* Order Details (Line Items)\
  Each item can include:
  * order\_details\[].product\_name
  * order\_details\[].commodity\_code
  * order\_details\[].quantity
  * order\_details\[].unit\_of\_measure
  * order\_details\[].unit\_price
  * order\_details\[].item\_tax\_amount
  * order\_details\[].item\_discount\_amount

### Supported Connectors

Our unified (generic) L2/L3 fields in payment\_create cover the majority of requirements across connectors

If your connector requires fields that aren’t in our unified list, we’ll evaluate and add the minimal set needed

<br>
