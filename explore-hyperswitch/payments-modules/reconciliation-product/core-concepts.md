# Core Concepts

### How We Model Money

At its core, our system treats money as **accounting data**. This approach, known as double-entry bookkeeping, provides powerful guarantees for financial integrity. It ensures that money is never created or lost, gives you a full audit trail, and provides clear, point-in-time balances for your finance and operations teams

Double-entry bookkeeping is the most reliable way to track money. It ensures every financial event is recorded accurately, with a clear source and destination for funds

### Core Concepts: Accounts, Entries, and Transactions

#### **Accounts**

An account is a named ledger location that represents a segregated pool of value, like a digital wallet or a specific category of money. Think of them as the containers for your funds.

* **Purpose**: Each account has a clear purpose, such as holding Bank Money, tracking Revenue, or categorizing Processing Fees
* **Currency**: Each account is for one currency only to prevent confusing conversions and ensure healthy balances
* **Type**: Accounts are of two types: DEBIT or CREDIT. This distinction is key to how entries affect an account's balance

#### **Debit Normal vs. Credit Normal Accounts**

As we've mentioned, every account has a type. The two types we will focus on are debit normal and credit normal. This distinction is critical for how our system processes entries and ensures your ledger remains balanced

**Debit Normal Accounts** represent the uses of money. They are where your funds are allocated or reside. Think of them as your assets and expenses. A debit entry increases their balance, while a credit entry decreases it

* Examples of `uses` of funds:
  * Processor Account: The funds you are owed by a payment processor
  * Bank Account: The funds you hold in your bank
  * Operating Expenses: Fees paid to a third-party service

**Credit Normal Accounts** represent the sources of money. They are where your funds originate from. Think of them as your liabilities and revenue. A credit entry increases their balance, while a debit entry decreases it

* Examples of `sources` of funds:
  * Order Sales: The revenue from a customer order
  * Loans: Money you've received from a financing partner

#### **Entries**

An entry is the smallest recorded unit in our system. It's a single posting to an account, recording the `amount`, `direction` (DEBIT/CREDIT), `account`, and `currency`

Entries never exist alone; they are always part of a larger transaction. You can think of an entry as a single action, like "$50 moved into Bank:USD-1234." Because entries also record a status (PENDING, EXPECTED, POSTED), you get transparent visibility into your cash flow, knowing what money is on its way versus what has been fully settled

#### What are Debits and Credits for Entries?

While the terms debit and credit can be confusing, it's essential to understand them when building financial systems. In our system, they act as flags that determine how an entry affects an account's balance based on its type. They are not simply "plus" or "minus" signs

Here is the simplest way to think about them:

* **Debit Entry**: This adds to the balance of a debit normal account (like your Bank or Processor Account) or subtracts from the balance of a credit normal account (like your Revenue or Loans Account)
* **Credit Entry**: This adds to the balance of a credit normal account or subtracts from the balance of a debit normal account

#### **Transactions**

A transaction is a group of entries that represents a single, logical movement of funds. It's the atomic event that affects account balances

Transactions are the foundation of our system's integrity. They enforce the double-entry bookkeeping rule: **the sum of all debits must equal the sum of all credits**. This mathematical guarantee ensures that money cannot be created or destroyed

Consider moving money between two wallets: a single transaction removes money from the first wallet and adds it to the second. If one part of this action fails, the entire transaction is canceled, preventing a "half-transfer" where money is removed but never properly placed

This design provides:

* Mathematical Safety: If total debits don't equal total credits, something is wrong. This immediate invariant helps detect bugs or data corruption
* Clear Provenance: You can always answer, "Why did this balance change?" because every sale, refund, or fee is an explicit entry within a transaction
* Auditable History: Transactions are the only mechanism that creates or changes entries, simplifying reasoning, auditing, and reconciliation
* Atomic Consistency: Either all entries in a transaction are written, or none are. This prevents inconsistent states and is crucial for handling system failures gracefull
