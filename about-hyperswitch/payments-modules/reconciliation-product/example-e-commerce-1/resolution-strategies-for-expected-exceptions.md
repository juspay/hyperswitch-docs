# Resolution Strategies for 'Expected' Exceptions

### Overview

An exception in the `EXPECTED` state indicates a timing or availability issue. The system has a record on one side (typically the internal Source/Ledger) but is still waiting for the corresponding record from the counterparty (Target/Bank)

The goal of resolution here is to either invalidate the source record (if it shouldn't exist) or manually confirm the missing side to close the loop

**Important**: **The Self-Resolving Nature**

Unlike "Mismatched" exceptions (which are actual data breaks), `EXPECTED` exceptions are often temporary. In most cases, these resolve automatically when the counterparty sends their settlement batch (e.g., T+1 or T+2)

***

### Pathway A: Voiding Invalid Data

Action: `Ignore Transaction`

This action is used when the source transaction (the "Expected" item) is invalid or should not be reconciled. Since the counterparty data has not arrived yet, "Ignoring" this record effectively cancels the expectation, preventing the system from waiting indefinitely

* Logic: Marks the transaction status as `VOID` . It removes the item from the "Pending/Aging" queue
* Common Use Cases:
  * Test Transactions: An order created in the production environment for testing purposes that will never settle at the bank
  * Cancelled Prior to Settlement: An authorization that was voided immediately at the gateway but was logged as "Pending" in the ledger

***

### Pathway B: Fixing Valid Data

Action: `Fix Entries`

If the source transaction is valid and represents real money, but the automated match hasn't happened, users can intervene using the three options below.

#### Option 1: Edit Entry

"The Pre-emptive Correction"

Unlike the Mismatched workflow where you are fixing a break, here you are modifying the Source Expectation itself—often _before_ the counterparty data has even arrived. This is used when you realize the internal system generated an incorrect expectation and you want to correct it so that when the bank file _does_ arrive, it matches automatically

* Primary Purpose: To correct the internal source record (Left Side) because the upstream data was wrong, ensuring a clean match when the partner data finally lands
* Target: Modifies the `Expected_Amount` or metadata of the source entry.
* When to use:
  * Incorrect Source Amount: The Order Management System sent an expectation of $100, but you know a $5 discount was applied manually and the bank will only send $95. You edit the expectation to $95 _now_ so it matches later
  * Wrong Currency: The source system erroneously flagged a transaction as `USD` instead of `CAD`. You fix it now to prevent a currency mismatch exception tomorrow
  * Data Enrichment: The source stream missed a critical field (e.g., `Merchant_ID`) that will be required for the match logic to work once the file arrives

#### Option 2: Mark as Received

"The Manual Verification Approach"

This option is unique to `EXPECTED` exceptions. It replaces the "Create Entry" workflow found in mismatches. Since the system is waiting for the right side to arrive, this action allows the user to say, _"Stop waiting. I have verified this funds myself."_

* Primary Purpose: To force-close an open expectation when digital proof (a file/webhook) is missing but physical/offline proof exists
* Process: User clicks "Mark as received" -> System generates a synthetic "Received" entry -> Transaction moves to `MATCHED`&#x20;
* When to use:
  * Cash & Check Deposits: Funds were physically deposited; no electronic file will ever arrive to match the ledger entry
  * Missing Statements: The bank feed failed for a specific day, but the Operations team verified the balance via the online banking portal
  * Lump Sum Settlements: The bank deposited a bulk amount, and you need to manually mark individual expected line items as "Received" against that bulk deposit

#### Option 3: Replace Entry

"The Swap Approach"

This allows you to unlink the current "Expected" entry and replace it with a different transformed entry from the backlog. This is used when the system created an expectation based on the wrong upstream data packet

* Primary Purpose: To swap the active source record with a correct one to restart the matching search
* When to use:
  * Wrong Ledger Account: The expectation was generated for the "USD Ledger" but the transaction actually belongs to the "EUR Ledger." You replace it with the correctly parsed entry
  * Corrupted Source Data: The source event was malformed. You replace it with a clean version of the event so the system can properly search for the counterparty
