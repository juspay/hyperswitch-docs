# Resolving Amount Mismatch Exceptions

_Time needed: \~10 minutes · Works on the Exceptions screen_

An **amount mismatch** means both systems saw the payment — but they disagree on the money. One side says 100.00, the other says 98.20. The payment isn't lost; the numbers just don't line up, and the system won't call it matched until a human decides what to do.

This is the most common exception type, and usually the easiest to explain.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_to_Resolve_a_Reconciliation_Amount_Mismatch_in_Hyperswitch__SAA6wIR1QgG7bMvvIW8JUQ" %}

### Why amount mismatches happen

* **Fees deducted along the way.** The most common cause. The PSP received 100.00 from the customer but paid out 98.20 to the bank — the 1.80 is their fee. Both sides are "right"; they're just measuring at different points.
* **Partial refunds or adjustments** applied on one side but not yet visible on the other.
* **Currency conversion** — the amount changed because the money changed currency between systems.
* **A genuine error** — a wrong amount in a file, a double charge, or money that truly went missing. Rare, but this is exactly what reconciliation exists to catch.

### Step 1: Open the exception

Go to **Operate → Exceptions**, pick the rule tab (e.g. PSP 1 ↔ Bank), and filter or look for status **Data Mismatch**. Click the transaction to open it.

The detail view shows you exactly what disagrees: the **expected value vs. the actual value**, side by side, for each mismatched field — along with both sides' entries so you can compare everything that came from the files (Guide 4 covers this view).

### Step 2: Figure out which story you're in

Ask: **does the difference make sense?**

* Is the difference roughly your PSP's fee percentage? → It's a fee.
* Does the difference match a refund or adjustment you can find? → It's an adjustment.
* Is it a currency pair with a plausible exchange rate? → It's conversion.
* None of the above? → Treat it as a genuine discrepancy: check the original file (trace the entry's lineage, Guide 3), and if the file is right, take it up with your PSP or bank.

### Step 3: Resolve it

Click **Resolve Exception** on the transaction. You'll get options — the two you'll use most for amount mismatches:

| Option                 | What it does                                                                        | Use when                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Force Match**        | Marks the transaction as matched despite the difference, with your remark attached. | The difference is explained and acceptable — a fee, a known adjustment. You're telling the system: _"this is fine, I've verified it."_ |
| **Edit Entry**         | Corrects the data on one side (e.g. a wrongly-read amount), then re-runs the match. | The file had bad data and you know the correct value.                                                                                  |
| **Ignore Transaction** | Voids the transaction — sets it aside, out of your numbers.                         | The transaction shouldn't be reconciled at all (test data, wrong file). See the Bulk voiding guide for clearing many at once.          |

Whichever you choose, **add a clear remark** — e.g. _"1.80 diff = PSP 1 processing fee, verified against fee schedule."_ The remark is saved on the transaction and shows in its audit trail, so anyone reviewing later sees exactly why it was resolved and by whom.

After resolving, the transaction's status updates (e.g. **Matched (Manual)** after a force match) and it drops out of your open exceptions.

### A note on recurring fee mismatches

If the _same_ fee mismatch shows up on every payout, you shouldn't have to force-match it forever. Matching rules can be configured with a **tolerance** (e.g. "amounts within X count as matched") or with fees modeled explicitly. If you're force-matching the same pattern daily, tell the Hyperswitch team — the rule can likely be adjusted so these match automatically.

### Quick checklist

* ✅ I compared the expected vs. actual amounts and identified the cause.
* ✅ I picked the right resolution: Force Match (explained), Edit Entry (bad data), or Ignore (shouldn't exist).
* ✅ I left a remark that explains the difference, not just "resolved."
* ✅ Recurring pattern? I flagged it to the Hyperswitch team for a rule adjustment.
