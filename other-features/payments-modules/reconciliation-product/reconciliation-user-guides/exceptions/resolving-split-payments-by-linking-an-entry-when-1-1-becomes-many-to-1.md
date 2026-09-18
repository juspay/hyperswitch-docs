# Resolving Split Payments by Linking an Entry (When 1:1 Becomes Many-to-1)

_Time needed: \~15 minutes · Works on the Exceptions screen_

A 1:1 rule expects one entry on each side: one order in the OMS, one payment at the PSP. But real life sometimes produces **two entries on the left for one entry on the right** — most commonly a **split payment**: the customer pays one order in two parts (two cards, gift card + card, two installments), so your OMS records two rows, while the PSP settles it as a single payment.

The rule can't match this on its own — it was told to expect one-to-one. The fix is a one-time manual action: **link the extra entry to the existing transaction**, turning that one transaction into a many-to-1 match.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_to_Resolve_Transaction_Payment_Exceptions_for_Split_Payments__Nm3et72VThqOBAfkOKg5ag" %}

### The example

For Aug 25, our OMS file has **two rows for order ORD-10540007** — the customer paid 75.00 and then 45.00. PSP 1's report has **one row** for the same order: a single payment of 120.00.

| System | Order        | Rows | Amounts       |
| ------ | ------------ | ---- | ------------- |
| OMS    | ORD-10540007 | 2    | 75.00 + 45.00 |
| PSP 1  | ORD-10540007 | 1    | 120.00        |

The money is all there — 75 + 45 = 120. The system just needs to be told these three entries belong together.

### What you'll see after uploading

Upload both files as usual (Guide 2). The other nine orders in the file match cleanly — **Matched (Auto)**. Order ORD-10540007 splits into two problems:

1. **A transaction that doesn't add up.** One OMS entry was paired with the PSP entry, but the amounts disagree (75.00 vs 120.00) — so on the **OMS ↔ PSP 1** tab it shows as an exception instead of a match.
2. **A leftover entry.** The second OMS row (45.00) couldn't join — the rule had already used its one expected entry for this order. It lands in **Exceptions** as an entry **needing manual review**.

Neither is an error in your data. It's the 1:1 rule correctly saying: _"I found more entries than I was told to expect — a human should confirm they belong together."_

### How to resolve it: link the entry

1. **Go to Operate → Exceptions** and open the **OMS ↔ PSP 1** tab.
2. **Find the transaction** — search for the order ID (ORD-10540007). Open it. You'll see the OMS side (75.00) vs the PSP side (120.00), short by exactly the amount of the leftover entry.
3. **Click Resolve Exception** and choose **Link a transformed entry**.
4. **Pick the waiting entry.** You'll see linkable entries — the OMS entries for this order that aren't part of any transaction yet. Our 45.00 entry is right there. Select it.
5. **Confirm, with a remark** — e.g. _"Split payment: customer paid 75 + 45 for one order."_

The transaction now has **two OMS entries against one PSP entry** — 75 + 45 = 120 — the amounts agree, and it resolves to matched. The leftover-entry exception disappears too, because that entry now belongs to a transaction.

### Check your work

Open the transaction again (or find it on the Transactions screen, Guide 4):

* Both OMS entries and the PSP entry appear together, grouped by account.
* The status shows it was resolved manually.
* The **audit trail** records the link — who did it, when, and your remark — so the "why" survives long after you've forgotten this order existed.

### When to link vs. when _not_ to

**Link when the money genuinely adds up** — the extra entries are parts of the same real payment (splits, installments) and their sum equals the other side.

**Don't link to force numbers together.** If the second entry exists because of a duplicate row in the file or a system error, linking would hide a real problem. Check the entry's lineage first (Guide 3) — if it traces to a duplicated or wrong file, void it instead.

> 💡 **Happens on every order?** If split payments are routine for your business (installments, BNPL), don't hand-link them daily — tell the Hyperswitch team. The rule can be changed from one-to-one to many-to-one so these match automatically, like your PSP ↔ Bank rule already does.

### Quick checklist

* ✅ I found both halves of the problem: the mismatched transaction and the leftover entry.
* ✅ I confirmed the amounts add up before linking (75 + 45 = 120).
* ✅ I linked the entry with a remark explaining the split.
* ✅ The transaction now shows all three entries and a matched status.
