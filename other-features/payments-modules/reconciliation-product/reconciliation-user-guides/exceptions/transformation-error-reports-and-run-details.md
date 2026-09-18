# Transformation Error Reports & Run Details

_Time needed: \~10 minutes · Works from the Pipelines screen_

When a file is uploaded, the system doesn't just swallow it — it runs a **transformation**: reading the file row by row and converting each row into a standard entry . This page shows you how to check exactly what happened during that run: how many rows made it, how many were skipped on purpose, how many errored — and how to download a row-level report of it all.

Use this when a file shows errors, when **Needs Manual Review** is above zero, or when the numbers on the Transformed Entries page don't add up to what you expected from your file.

***

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_to_Process_OMS_Manual_Uploads_and_Filter_Transformations__K1E3QaIfR-m-y-FeHwbfGg" %}

### Step 1: Open the file's transformation runs

Go to **Monitor → Pipelines** and click the file you want to inspect. You'll see a card for each transformation run on that file, summarizing it in one line:

* **Status** — Processed (green), Failed (red), Processing / Pending (in progress).
* **X / Y transformed** — how many of the file's rows became entries.
* **Run duration.**
* **N ignored** (orange) — rows skipped _on purpose_ by a skip rule (see Step 3). Ignored is not an error.
* **N errors** (red) — rows that could not be transformed. These are the ones to look at.

### Step 2: Download the transformation summary (the error report)

Every completed run has a **"Transformation summary"** button on its card. Click it to download a **CSV report** of the run — a row-by-row account of what happened to your file: which rows transformed cleanly, which were ignored and why, and which errored with the reason.

This is the file to open when someone asks _"why did 30 rows not make it in?"_ — and the file to send back to whoever produces the source report (your PSP, bank, or internal team) so they can see exactly which rows had problems.

### Step 3: Open the right pane — what the run actually did

Click the run card itself and a **details pane opens on the right**. This is the full explanation of how your file was read, top to bottom:

<figure><img src="../../../../../.gitbook/assets/Screenshot 2026-08-26 at 12.14.40 AM.png" alt=""><figcaption></figcaption></figure>



**The header** — the transformation's name, its status, and which account it **writes into** (e.g. _writes into → PSP 1_). Confirms your file fed the account you intended.

**The funnel** — four numbers that must add up: **Total** rows found in the file, **Transformed** (became entries), **Ignored** (skipped intentionally), **Errors** (failed). If Total = Transformed + Ignored + Errors, every row is accounted for — nothing silently disappeared.

**Run info** — Started, Finished, Duration, and the **Run ID** (share this with the Hyperswitch team if you need help with a specific run).

**Parsing** — how the file was read: the **format** (CSV, Excel…), which **header row** was used, which **sheet** (for Excel files), and the **unique key** — the field(s) used to detect duplicate rows. If a re-uploaded file's rows land as duplicates, this is the logic that caught them.

**Skip rules — what is being skipped and why.** This section lists every rule that intentionally drops rows before they become entries, each described in plain language — for example, skipping rows whose status column says `PENDING`, or summary/footer rows that aren't real transactions. Each skipped row counts toward **Ignored** in the funnel. If the section says _"No rows skipped — every parsed row is mapped,"_ then every row in your file is expected to become an entry.

> 💡 If your Ignored count looks high, read the skip rules first — the answer is usually right there ("oh, it skips all `PENDING` rows"). If a rule seems wrong for your files, that's a conversation with the Hyperswitch team — skip rules are part of your setup.

**Fields & rules — the transformation rule itself.** The bottom section lists every field the transformation produces (amount, currency, order ID, date…) and the rule used to build it from your file's columns — which source column it reads, and any conversion applied. This is the answer to _"where does this number come from?"_ at the column level: the exact mapping from your file's format to the standard entry format, as configured during your setup.

### Putting it together: a quick triage recipe

1. **Errors > 0?** Download the transformation summary, find the errored rows and their reasons. Usually it's a malformed value in the source file — fix at the source and re-upload, or contact the team.
2. **Ignored higher than expected?** Read the skip rules in the right pane — almost always intentional.
3. **A field looks wrong on Transformed Entries?** Check Fields & rules to see which source column feeds it — then check that column in your file.
4. **Still stuck?** Send the Hyperswitch team the **Run ID** and the downloaded summary.

### Quick checklist

* ✅ I can find the transformation run cards for any uploaded file.
* ✅ I downloaded a transformation summary and understood its row-level detail.
* ✅ I know the funnel: Total = Transformed + Ignored + Errors.
* ✅ I know where to see what's being skipped (skip rules) and how each field is built (fields & rules).
