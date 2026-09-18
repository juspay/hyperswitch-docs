# Following a Payment (Transactions)

_Time needed: \~15 minutes · Do this after your files are uploaded and verified (Guides 2–3)_

In Guide 3 you saw individual **entries** — single rows from single files. This screen is where those entries meet: the system takes entries from two different systems that describe the _same_ payment and groups them into one **transaction**, then tells you whether they agree.

One transaction = one payment, seen from both sides of one hop.

***

### Before you read the table: two things to know

**Inflow vs Outflow.** Each transaction carries a direction tag:

* **INFLOW** — money coming _into_ this hop's receiving side (e.g. a customer payment flowing from OMS to PSP 1, or a PSP payout arriving at the bank).
* **OUTFLOW** — money going _out_ (e.g. a refund or a payout leaving the account).

**The date filter works on your file's dates.** The date range (top right) filters by each transaction's **effective date** — the date recorded _inside your file_, not when you uploaded it. During setup we also configure the timezone your files are written in, so the dates you see here line up with the dates your own systems show. Practical upshot: to find yesterday's payments, filter for yesterday — regardless of when the file was uploaded.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_to_Navigate_and_Filter_Recon_Engine_Transactions__Ild1sqfGTyWuzZ2MmlijDg" %}

### Step 1: Pick a hop (tab) and read the table

Select a rule tab at the top — start with a simple 1:1 hop, e.g. **OMS ↔ PSP 1**. In this rule, one order on our side should match exactly one payment on the PSP's side.

Each table row is one transaction:

* **Date** — the payment's effective date.
* **Transaction ID** — the system's ID for this grouped payment.
* **Status** — the verdict (below).
* **Entry ID / Order ID** — the individual entries that were grouped together, one line per side. For a 1:1 rule you'll typically see two entries: one from OMS, one from PSP 1.

### Step 2: Understand the statuses

| Status                | What it means                                                                                                        | Worry?                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Matched (Auto)**    | Both sides agree — matched automatically by the rule.                                                                | No — this is the goal.                |
| **Matched (Manual)**  | Both sides agree, confirmed by a person.                                                                             | No.                                   |
| **Expected**          | We've seen one side and are waiting for the other (e.g. OMS says the order exists; the PSP file hasn't arrived yet). | Usually just a timing gap.            |
| **Partially Matched** | Some of this payment's hops are confirmed, others aren't yet.                                                        | Check what's pending.                 |
| **Data Mismatch**     | Both sides arrived but disagree — usually on amount.                                                                 | Yes — this is an exception (Guide 5). |
| **Missing**           | One side never showed up.                                                                                            | Yes — an exception (Guide 5).         |

### Step 3: Open a transaction — the full story of one payment

Click any transaction to open its detail view. This is the most useful screen in the product when someone asks _"what happened to this payment?"_ You'll see:

* **The entries, grouped by account.** Each side's entry with its amount, currency, credit/debit direction, and status — so you can see exactly what OMS said vs. what PSP 1 said, side by side. Expand an entry to see the raw details that came from the file.
* **The rule that was used.** The detail shows which recon rule grouped and compared these entries — so you always know _why_ the system paired them, and which logic (from your Rules Library, Guide 1) made the call.
* **Linked transactions.** A payment's journey doesn't stop at one hop. Under **"Linked with"** you'll see this payment's transaction on the _adjacent_ hop — e.g. from the OMS ↔ PSP 1 transaction you can jump straight to the PSP 1 ↔ Bank transaction for the same money. Click it to follow the payment down the chain without searching again.
* **Audit trail.** A step-by-step history of everything that happened to this transaction: when each side's entry arrived, when it was matched (or flagged), and any manual actions — who did what, and when. Nothing is ever silently changed; it's all recorded here.
* **Resolution remark.** If someone resolved this transaction manually, their note appears at the top.

### Step 4: Now look at a many-to-one hop (PSP ↔ Bank)

Switch to the **PSP 1 ↔ Bank** tab. This hop behaves differently, on purpose.

PSPs don't transfer money order by order — they batch it. Many payments on the PSP side become **one payout** on the bank statement. The rule for this hop (a _many-to-one_ rule, as you saw in the Rules Library) knows this: it groups the PSP entries and matches the group's **total** against the single bank credit.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-08-25 at 11.51.42 PM.png" alt=""><figcaption></figcaption></figure>



So on this tab, expanding a transaction shows **many entries on the PSP side and one on the bank side** — that's not an error, that's the batching. The match question changes from "do these two rows agree?" to "do these 50 rows _add up to_ this one bank credit?"

> 💡 This is also why a mismatch on this hop usually means a **fee or deduction**: the PSP batched 50 payments totalling 5,000 but the bank received 4,985 — the 15 difference is typically the PSP's fee.

### Step 5: Finding a specific payment

* **Search by ID** — paste a Transaction ID, Entry ID, or (most usefully) an **Order ID** from your own system.
* **Add Filters** — narrow by status, e.g. show only Data Mismatch.
* **Generate Report** — export the current view to share with your team, PSP, or bank.

### Before you move on — quick checklist

* ✅ I opened a 1:1 transaction (OMS ↔ PSP) and saw both sides' entries agree.
* ✅ I found the rule used and the audit trail in the detail view.
* ✅ I jumped to a linked transaction and followed one payment across two hops.
* ✅ I looked at a PSP ↔ Bank transaction and understood why many entries match one bank credit.
