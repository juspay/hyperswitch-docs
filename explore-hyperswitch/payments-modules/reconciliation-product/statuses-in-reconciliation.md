# Statuses in Reconciliation

In reconciliation, **status** is the fastest way to understand what’s happening to your data — from file upload to posted ledger transactions.\
This guide explains statuses at four layers of the workflow: **Ingestion**, **Transformation**, **Staging Entries**, and **Transactions (Ledger)**

***

### 1. Ingestion Statuses (File Level)

Ingestion tracks the very first stage: getting your raw files (CSV etc.) into the system

| Status     | What it means for you                                                                                                                                                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending    | The file has been uploaded and is sitting in the queue                                                                                                                                                                                          |
| Processing | Our engine is currently reading and parsing the file                                                                                                                                                                                            |
| Processed  | Success! The file was read, and the data is moving to the next stage                                                                                                                                                                            |
| Failed     | There was a technical error (e.g., a broken file format or missing columns)                                                                                                                                                                     |
| Discarded  | Note: This represents an "Audit Version." To keep a perfect history, when a file moves from _Pending_ to _Processing_, the system "discards" the old _Pending_ record and creates a new one. This ensures we have a trail of every state change |

### Phase 2: Transformation (Cleaning & Mapping)

Before data can be reconciled, it must be "cleaned." The Transformation layer maps your raw data to our system fields and strips out any "noise" (like extra spaces, invalid characters, or incorrect date formats)

* **Pending**: Data is queued for cleaning
* **Processing**: The system is currently mapping fields and scrubbing the data
* **Processed**: The data is now clean and structured
* **Failed**: The mapping rules failed (e.g., a required column was empty)

### Phase 3: Staging Entries (The "Waiting Room")

Once data is cleaned, it becomes a Staging Entry. This is the holding area where records live before the Reconciliation Engine processes them

| Status              | Action Required                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Pending             | No action. The record is waiting for the next "run" of the recon engine                                                         |
| Needs Manual Review | Action Required. The engine couldn't process this automatically (e.g., it looks like a duplicate or no matching rule was found) |
| Processed           | Success. The entry has been matched to a transaction                                                                            |
| Void / Archived     | The record was cancelled or replaced during a manual correction                                                                 |

### Phase 4: Transaction Status (The Final Goal)

A Transaction represents the end-to-end journey of money. Its status reflects whether the two sides of the ledger (e.g., Order vs. Bank) have been successfully balanced

#### Reconciled States (The "Done" List)

**Posted:** The transaction is fully reconciled. The sum of all debits equals the sum of all credits, and all metadata rules have passed. A transaction can reach this state in three ways:

* **Auto**: The Reconciliation Engine automatically matched and validated all data
* **Manual**: An operator manually linked entries to close the transaction
* **Force**: An operator bypassed a minor data discrepancy (e.g., a mismatched Reference ID) to close the transaction

#### Mismatch States (The "To-Do" List)

* **Expected:** The transaction has been created based on a source entry (e.g., a Sale in your Order Management System) and is waiting for a matching entry from the counterparty (e.g., the Bank)\
  &#xNAN;_**Note on "Missing"**_: If a transaction remains in the Expected state longer than your configured SLA (e.g., T+3 days), the UI flags it as Missing. This is not a separate database status, but a time-based alert indicating that the counterparty data is overdue
*   **Over Amount**: The confirmed amount (Right Side) is higher than the expected amount (Left Side)

    This status can be **transient** or **final**, depending on whether more counterpart entries are still expected:

    * If more entries are pending, the mismatch may resolve when all entries arrive
    * If all expected entries are confirmed and the mismatch persists, it requires manual resolution
* **Under Amount**: The confirmed amount (Right Side) is lower than the expected amount (Left Side)\
  Behavior mirrors Over Amount:
  * It may resolve if additional expected entries arrive later
  * If the transaction is fully confirmed and still under, it requires manual resolution
* **Data Mismatch**: The amounts balance perfectly, but a secondary validation rule failed
  * _Example:_ The Bank deposited $100 for Order `#123`, but the Bank Reference said `REF-999` instead of `REF-123`
* **Currency Mismatch**: The counterparty entry arrived in a currency different from the source expectation (e.g., Expected `USD`, Received `EUR`)
* **Split Mismatch**: For complex split payments (e.g., Marketplace payouts), the total amount is correct, but the distribution logic between sub-accounts does not match the rule definition

#### Operational States

* **Partially Reconciled**: The transaction has been partially resolved (through exception handling), but it does not yet meet the conditions to be posted
  * _**Key Characteristic**:_ This status is never assigned by the automated engine. It only appears when an operator saves "work in progress" during exception handling without fully resolving the discrepancy

#### Historical States

* **Archived:** The transaction is a historical record that has been superseded. This occurs when a transaction is updated, re-processed, or split, creating a new "Active" version while preserving this version for the audit trail
* **Void:** The transaction was cancelled by an operator or system rule. Voiding effectively "soft deletes" the transaction from the active ledger while keeping the data visible for auditing

