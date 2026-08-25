# Bulk void exceptions

## Bulk Voiding Transactions

_Time needed: \~5 minutes · Works on the Exceptions screen_

Sometimes you don't want to resolve exceptions one by one — you want to clear a whole batch of them at once, because you already know what happened. That's what **bulk void** is for: filter down to the exceptions you want gone, select them, and void up to **100 in one go**.

**Voiding** a transaction means telling the system: _"Don't try to reconcile this — set it aside."_ Voided transactions are taken out of your open exceptions and out of your match-rate numbers. They're not deleted — they stay visible with a full audit trail of who voided them, when, and why.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_to_Ignore_Data_Mismatch_Transactions_in_Hyperswitch__7sWUPBCyTDSxn4D3k7G3bQ" %}

### When would I use this?

* **A wrong file was uploaded.** Say someone uploaded last week's PSP report by mistake — it created hundreds of exceptions that will never match anything. Void them all in one action instead of clicking through each one.
* **A known, explainable batch.** You've investigated one exception, found the cause, and know every other exception of the same type has the same explanation — e.g. a batch of test transactions, or entries from an account you no longer use. Filter to that type and void the lot.

> ⚠️ Only void exceptions you understand. Voiding makes the exception disappear from your numbers — it doesn't fix the underlying money question. If you're not sure why an exception exists, investigate it first (Guide 4 and Guide 5).

### How to do it

1. **Go to Operate → Exceptions** and pick the rule tab where the exceptions live (e.g. OMS ↔ PSP 1).
2. **Filter down to exactly what you want to void.** Use **Add Filters** (e.g. status = Data Mismatch), the date range, or search — until the list shows only the exceptions you intend to clear. This step is what makes bulk void safe: filter first, select second.
3. **Select the transactions.** Tick individual checkboxes, or tick the header checkbox to select the whole page. A bar appears showing how many you've selected — you can void up to **100 transactions in one action**.
4. **Click Void.** A confirmation opens.
5. **Add a remark** explaining why — e.g. _"Duplicate exceptions from wrong PSP 1 file uploaded Aug 25."_ This remark is saved on every voided transaction and shows up in its audit trail, so three months from now anyone can see why these were set aside.
6.  **Confirm.** The selected transactions are voided and drop out of your open exceptions.

    `[screenshot: void confirmation dialog with remark field]`

> 💡 **Selected everything matching your filter?** If you select the whole page while a filter is applied, you can apply the void to **all transactions matching the filter** — in that case the remark is mandatory, because you're acting on transactions you haven't individually looked at.

### After voiding

* The transactions show status **Void** — you can still find and open them, and their audit trail records the action and your remark.
* Your Open Exceptions count and match metrics update to exclude them.
* Uploaded the wrong file? After voiding its exceptions, upload the correct file as usual

### Quick checklist

* ✅ I filtered the list down to _only_ the exceptions I mean to void.
* ✅ I know why each of these exceptions exists (same known cause).
* ✅ I wrote a remark my teammates will understand later.
