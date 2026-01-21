# Resolution Strategies for Mismatched Exceptions

### Overview

When a transaction falls into the `MISMATCHED` state, it indicates that while records exist on both sides, their key attributes (Amount, Currency, Status) do not align, or the data quality is insufficient for an automated match.

The system provides two primary pathways for resolution: Voiding (removing invalid data) or Fixing (correcting valid data)

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-12-17 at 2.46.45 PM.png" alt=""><figcaption></figcaption></figure>

### Pathway A: Voiding Invalid Data

Action: `Ignore Transaction`

This action effectively "soft deletes" the exception. It is used when the transaction record itself is invalid and should not have been ingested into the reconciliation layer in the first place. Ignoring a transaction removes it from the active queue and excludes it from financial reports.

* Logic: Marks the transaction status as `VOID` . It does not delete the audit trail but prevents further processing
* Common Use Cases:
  * Test Data: Developers generated $0.01 test transactions in the Production environment
  * Cancelled/Voided Orders: Transactions that were cancelled at the source but were erroneously synced to the reconciliation layer

***

### Pathway B: Fixing Valid Data

Action: `Fix Entries`

If the transaction is valid but simply incorrect or incomplete, users must select one of the three "Fix" strategies below to align the data

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-12-17 at 2.47.26 PM.png" alt=""><figcaption></figcaption></figure>

#### Option 1: Edit Entry

"The Data Correction Approach"

This option allows you to modify specific attributes of the existing Staging Entry without breaking the link to the original source file. It is best used for minor metadata errors where the transaction _identity_ is correct, but the _details_ are wrong.

* Primary Purpose: Fix incorrect or incomplete data fields while maintaining the entry's history.
* When to use:
  * Metadata Gaps: A rule failed because a required field (e.g., `Merchant_ID`) was null. You can manually input the missing ID
  * Processing Mode Errors: The transaction was flagged as "Test" instead of "Live" due to a configuration error
  * Typos: Correcting a reference number that was keyed in incorrectly (e.g., `INV-01` vs `INV-O1`)

#### Option 2: Create Entry

"The Manual Injection Approach"

This option enables you to manually generate a missing side of the transaction. Use this when the external system failed to send the data entirely, but you have offline proof that the event occurred

* Primary Purpose: To fill a gap where data is completely missing (not just incorrect)
* Process: User manually inputs payload -> System creates Staging Entry -> System re-runs matching logic
* When to use:
  * Lost Webhooks: The payment gateway experienced an outage and never sent the `payment_success` webhook, but the money is in the bank
  * Legacy Data: Reconciling historical transactions where the source logs are no longer accessible via API
  * Manual Adjustments: Creating a "Fee" or "Tax" entry to explain a variance&#x20;

#### Option 3: Replace Entry

"The Swap Approach"

This option allows you to discard the current active entry and link the transaction to a different, pre-existing "Transformed Entry." This is useful when the system incorrectly linked the wrong record during the ingestion/transformation phase

* Primary Purpose: To correct a structural linkage error by selecting a better candidate from the available pool of transformed data
* When to use:
  * Incorrect Mapping: The system auto-matched Transaction A to Ledger Entry X, but it should have matched to Ledger Entry Y
  * Corrupted Transformation: The current entry was parsed incorrectly (garbage data). You can swap it for a clean, re-parsed version of the entry that exists in the backlog

#### Summary: Which Button Should I Click?

| If the issue is...                             | Click this Action  |
| ---------------------------------------------- | ------------------ |
| "This record is garbage/fake."                 | Ignore Transaction |
| "This is the right record, but it has a typo." | Edit Entry         |
| "The record is missing entirely."              | Create Entry       |
| "The system picked the wrong record."          | Replace Entry      |

