# Verifying Your Data (Transformed Entries)

_Time needed: \~10 minutes · Do this after uploading your files (Guide 2)_

Every file you upload gets broken down into individual rows, and each row becomes a **transformed entry** — one money movement (a payment, a refund, a payout) converted into a standard format the system can work with: amount, currency, credit or debit, order ID, and date.

**This page is where all your data lands.** Whatever the file looked like — an OMS export, a PSP report, a bank statement — after upload, every single row from every account shows up here. Before looking at match rates or exceptions, come here to answer one question:

> **"Did every row of my files make it in cleanly?"**

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/Filtering_Transformed_Reconciliation_Entries_in_Hyperswitch__ibdnoy7aRp2RNPMyFFrPyQ" %}

***

### Step 1: Read the four cards at the top

| Card                    | What it means                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Total Records**       | Every row the system read from your files, across all accounts. In the demo: all rows from the OMS export, both PSP reports, and the bank statement combined. |
| **Processed**           | Rows that were read cleanly and are ready for matching.                                                                                                       |
| **Needs Manual Review** | Rows the system read but couldn't fully process — something about them needs a human look (see Step 4).                                                       |
| **% Valid**             | Processed ÷ Total. Your data-quality score for the period.                                                                                                    |

> 💡 **The cards are clickable.** Click **Processed** or **Needs Manual Review** and the table below filters to just those entries. Click **Total Records** to go back to everything.

**Rule of thumb:** if **% Valid** is low, fix the data first — a low match rate downstream is usually just a symptom of rows that never made it in cleanly.

### Step 2: Read the table

Each row in the table is one entry from one of your files:

* **Date** — when the money movement happened, according to your file (not when you uploaded it).
* **Order ID** — the identifier that ties this entry to a payment.
* **Entry Type** — **Credit** (money in) or **Debit** (money out).
* **Amount** and **Currency** — as read from your file.
* **Transformed Entry ID** — the system's own ID for this row (useful when talking to support).
* **Status** — where this row stands (see Step 4).

### Step 3: Filter and search

With four accounts uploading files, this table gets big. Narrow it down with:

* **Account** — see entries from just one system, e.g. only Bank entries. This is the filter you'll use most.
* **Transformation** — see entries that came through one specific transformation config (e.g. only PSP 1 refunds, if refunds have their own config).
* **Entry Type** — only Credits, or only Debits.
* **Status** — e.g. only entries needing review.
* **Search by ID** — look up a specific entry by **Order ID**, **Transformed (Staging) Entry ID**, or **Transformation History ID**. Order ID is the practical one: paste an order number from your OMS and see every entry related to it.
* **Date range** (top right) — remember, this works off the entry's date _from your file_, not your upload time.

### Step 4: Understand the statuses

| Status                  | What it means                                            | What to do                            |
| ----------------------- | -------------------------------------------------------- | ------------------------------------- |
| **Processed**           | Row read cleanly, ready for matching.                    | Nothing.                              |
| **Pending**             | Still being worked on.                                   | Wait a moment and refresh.            |
| **Needs Manual Review** | Row was read but has a problem.                          | Open it and check the reason (below). |
| **Void / Archived**     | Row was cancelled or retired — excluded from the counts. | Nothing.                              |

When an entry **needs manual review**, the system tells you why. The common reasons, in plain English:

* **Duplicate entry** — this row already exists (e.g. the same file uploaded twice, or the same transaction appearing in two reports).
* **Currency mismatch** — the currency doesn't match what was expected for this account.
* **Missing field** — the row is missing something the matching rules need, like an order ID or amount.
* **No matching rule found** — the system couldn't figure out which rule this entry belongs to.

Most of these trace back to the file itself — a duplicate upload, an export with missing columns, or an unexpected format change from your PSP or bank. If the reason isn't obvious, share the Transformed Entry ID with the Hyperswitch team.

### Step 5: Trace an entry back to its file

Click any entry to see its full lineage — the paper trail of where it came from:

**Source** (which file, which ingestion) → **Transformation** (which config read it) → **Transformed Entry** (the result).

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-08-25 at 11.34.32 PM.png" alt=""><figcaption></figcaption></figure>

This answers "where did this number come from?" definitively: you can trace any entry back to the exact file — and re-download that file from Pipelines (Guide 2).

### Before you move on — quick checklist

* ✅ **Total Records** roughly matches the number of rows across my files.
* ✅ **% Valid** is high (near 100%).
* ✅ I filtered by each account and confirmed all four systems have entries.
* ✅ Any **Needs Manual Review** entries — I've checked the reason, or noted them to resolve later.
