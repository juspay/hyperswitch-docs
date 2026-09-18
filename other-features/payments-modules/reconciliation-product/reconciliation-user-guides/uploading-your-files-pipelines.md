# Uploading Your Files (Pipelines)

_Time needed: \~10 minutes · You'll need your report files downloaded and ready_

Reconciliation runs on the reports your systems produce. This guide shows you how to get them into Hyperswitch: you'll upload each file, tell the system which account it belongs to, and confirm it was processed successfully.

In our demo setup that means **four files**:

| File                    | Belongs to account |
| ----------------------- | ------------------ |
| Order export            | OMS                |
| PSP 1 settlement report | PSP 1              |
| PSP 2 settlement report | PSP 2              |
| Bank statement          | Bank               |

Your own files may have different names — what matters is that each file gets uploaded against the **right account**.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/Manually_Uploading_Reconciliation_Files_in_Hyperswitch__18itv8Y7TWCu92MA_VC96g" %}

***

### Step 1: Open Pipelines

Go to **Monitor → Pipelines** in the left sidebar.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-08-25 at 11.03.01 PM.png" alt=""><figcaption></figcaption></figure>



This page is the home for everything file-related: every upload you (or an automated connection) ever make shows up here as one row, with its processing status.

### Step 2: Upload a file

Click the **Upload** button at the top right.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-08-25 at 11.03.18 PM.png" alt=""><figcaption></figcaption></figure>



The upload asks you for three things, in order:

1.  **Select the account.** Which system does this file come from? For your bank statement, pick **Bank**; for your PSP 1 report, pick **PSP 1**; and so on.

    > ⚠️ This is the most common mistake on this page. If you upload a file against the wrong account, the system will try to read it with the wrong format and match it against the wrong rules. Double-check before you continue.
2. **Select the transformation config.** This tells the system _how to read_ the file — which columns mean what. The configs were created for you during setup, based on the sample files you shared. Usually there's one obvious choice per account; if an account has more than one (for example, separate configs for payments and refunds), pick the one that matches the file you're uploading.
3. **Choose the file and upload.** Select the file from your computer and confirm.

That's it. Repeat for each of your files — in the demo, all four.

### Step 3: Watch it process

Back on the Pipelines page, your file appears as a new row at the top of the list. Each row shows:

* **Account** — which system you uploaded it against.
* **File Name** — the file you selected.
* **Ingestion Name** — which pipeline handled it.
* **Status** — starts as processing, and should turn **Processed** within a few moments.
* **Received At** — when the upload happened.
* **Download icon** — re-download exactly what you uploaded, anytime.



### Step 4: Read the tiles at the top

The four tiles above the list summarize all your uploads for the selected date range:

| Tile                    | What it means                                                                                            | What to do                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ingestion Runs**      | Total number of files uploaded (and how many are processing right now).                                  | Nothing — just a count.                                                                                                                           |
| **Failed**              | Files the system couldn't read at all.                                                                   | Check you picked the right account and config, re-download the file from your system, and try again. Still failing? Contact the Hyperswitch team. |
| **Processed**           | Files read successfully, end to end.                                                                     | You want every upload to land here.                                                                                                               |
| **Needs Manual Review** | Files were read, but some _rows inside them_ had problems (e.g. a missing amount or an unreadable date). | The file went through — but check those rows in the next guide (Transformed Entries).                                                             |

### Step 5: Finding a file later

When the list grows, two tools help you find things:

* **Search & filters.** Use the search box to find a file by name or connector, or **Add Filters** to narrow the list down to one account — e.g. show only Bank uploads.
* **Date range.** Use the date picker at the top right to look at a specific period.

> 💡 One row per upload, forever. This page doubles as your audit trail: if anyone ever asks "which bank statement did we upload on the 27th?", the answer is here, including the file itself via the download icon.

### Before you move on — quick checklist

* ✅ I uploaded one file for each account (all four in the demo).
* ✅ Every file shows **Processed** — the Failed tile reads 0.
* ✅ I noted whether **Needs Manual Review** is above 0 (we'll look at those rows next).

