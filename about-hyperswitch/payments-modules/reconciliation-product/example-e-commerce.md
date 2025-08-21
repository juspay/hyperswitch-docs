# Example: E Commerce

## Ecomm Three way reconciliation

Three-way reconciliation verifies the flow of money across three systems to ensure financial accuracy. For e-commerce this commonly means:

* **Order Management System (OMS)** — customer orders and fulfillment
* **Payment Service Provider (PSP)** — payment processing & settlements
* **Bank** — actual cash deposits

How we will solve it:

* We run **two recon processes: Order → PSP and PSP → Bank**
* Steps: define accounts, define rules, ingest data, create expectations, match & post
* Outcome: every order creates an expectation to PSP; matched PSP creates an expectation to Bank; matched Bank closes the three-way flow



**Step 1: Account Setup**

**Account Structure:**

* **Orders Account (Credit type)**
  * Tracks customer order values
* **PSP Settlement Account (Debit type)**
  * Tracks payment processor settlements
* **Bank Account (Credit type)**
  * Tracks actual cash received

**Configuration:**

* Orders Account: account\_type: Credit, currency: USD
* PSP Settlement Account: account\_type: Debit, currency: USD
* Bank Account: account\_type: Credit, currency: USD\


**Step 2: Reconciliation Rules Configuration**

**Rule 1: Order-to-PSP Matching**

Purpose: Match customer orders with PSP payments. Rule Settings:

* Name: "Order to PSP Reconciliation"
* Priority: 1
* When to Apply(Filter): Transaction type equals "customer\_order"
* How to Find Match: Use order\_id to find PSP transaction with same original\_reference
* What to Verify:
* Order amount = PSP gross amount
* Order currency = PSP currency
* Order ID = PSP original reference

**Rule 2: PSP-to-Bank Matching**

Purpose: Match PSP settlements with bank deposits. Rule Settings:

* Name: "PSP to Bank Settlement"
* Priority: 1
* When to Apply: Transaction type equals "psp\_settlement"
* How to Find Match: Use settlement\_batch\_id to find bank transaction with same batch\_reference
* What to Verify:
* PSP net amount = Bank deposit amount
* PSP currency = Bank currency
* Settlement date = Bank value date

#### Sample transaction journey (state transitions, concise)

1. **Order ingested (OMS)** — `order_id=12345`, amount `$100` → **Staged (PENDING)**.
2. **Rule 1 applies** → create **Expectation (Order→PSP, EXPECTED)** for `$100`.
3. **PSP webhook** — `{ gross_amount: 100, net_amount: 95, fee: 5, original_reference: 12345 }` → engine finds expectation → **Expectation POSTED**; create **Expectation (PSP→Bank, EXPECTED)** for `$95`.
4. **Bank file** — `{ amount: 95, batch_reference: "BATCH-456", value_date: 2024-01-15 }` → Rule 2 matches expectation → **Expectation POSTED** → Three-way **RECONCILED / CLOSED**.
