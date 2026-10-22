---
description: Get your settlement reports and invoices into Intelligent Routing so cost-aware routing knows your true processor fees
icon: file-import
---

# Cost Ingestion

Cost ingestion is how your real fee data reaches Intelligent Routing. It takes the **settlement reports** your processor already produces - the files that list, transaction by transaction, exactly what you were charged - parses them, and builds a per-cluster cost model. That model is what [Multi-Objective Routing](multi-objective-routing.md) uses to price each decision, and what you see in [Cost Estimation](cost-estimation.md).

{% hint style="info" %}
This page is about getting cost data **in**. What Intelligent Routing does with it afterwards - how it becomes the cost model routing relies on - is covered in [Cost Estimation](cost-estimation.md).
{% endhint %}

## Open Cost Ingestion

1. Select your merchant account and **Profile** in the dashboard.
2. Go to **Decision Engine Routing** > **Multi Objective**.
3. Open **Cost Estimation** > **Data ingestion**.
4. Select **Automatic**, **Manual**, or **Invoice** for the data you want to provide.

## Ways To Provide Cost Data

There are two ways settlement reports can reach Intelligent Routing, plus a sample runner for testing and an invoice path for the fees a settlement report cannot carry. All of them feed the **same** ingestion pipeline and appear in the **same** ingestion history.

| Method | How it works |
| --- | --- |
| **Manual upload** | Upload a report file directly in the dashboard. Processed in the background. |
| **Automatic (webhook)** | Your processor notifies Intelligent Routing when a report is ready, and Intelligent Routing verifies, downloads, and fits it - hands-free. |
| **Sample file** | Runs a curated demo report through the real pipeline so you can see the full flow without your own file. |
| **Invoice** | Upload the monthly invoice to recover flat and periodic fees that never appear per transaction. |

{% hint style="info" %}
Manual and automatic are just different front doors to the same room. Once a report is queued, it is downloaded (if needed), parsed, and fitted identically, and shows up in the same history labelled by its source.
{% endhint %}

## Method 1 - Manual Upload

Use manual upload when automatic delivery is not set up yet, to backfill historical months, or for testing. Reports can be several gigabytes, so the file uploads and processes in the background - you get a job you can watch rather than a frozen screen.

1. **Open the upload screen.** Under **Data ingestion**, select **Manual** and choose **Upload a file**.
2. **Choose the processor and account.** Select the processor in **Connector** and enter the processor-side account in **Account**.
3. **Choose the report file.** Select the processor's settlement report (CSV) in **Report file**. Intelligent Routing reads the header row and checks that every required column is present before the full upload begins.
4. **Map columns if prompted.** If your file's column names do not match the expected ones, a column-mapping panel appears. Map each of your columns to the expected field, preview the result to confirm the amounts and fees look right, then save. The mapping is remembered for every future report on this processor and account, so it is a one-time step.
5. **Upload and fit.** Click **Upload & fit**. When processing finishes, you will see how many rows were ingested, the period covered, and how many clusters were graded trustworthy.

{% hint style="warning" %}
A file that is missing required columns is blocked before the large upload starts, so you are not left waiting on a multi-GB upload only for it to fail parsing.
{% endhint %}

<figure><img src="../../../.gitbook/assets/routing-cost-manual-upload.png" alt="Manual settlement report upload screen"><figcaption></figcaption></figure>

## Method 2 - Automatic (Webhook)

With automatic ingestion, your processor notifies Intelligent Routing every time a settlement report is ready. Intelligent Routing verifies the notification's signature, downloads the report, and fits it - no manual step, ever. This is the recommended setup wherever your processor supports automatic report delivery.

Automatic ingestion needs three things:

1. Your processor produces settlement reports on a schedule (for example, a daily report).
2. Your processor calls the Intelligent Routing settlement webhook when each report is ready, signing the call so Intelligent Routing can trust it.
3. You register the processor's credentials in Intelligent Routing - the signing secret (to verify the webhook) and the download credential (to fetch the report).

Intelligent Routing verifies each notification's signature against the secret you stored, so only genuine, unmodified notifications are accepted. Any that fail the check are ignored, and a valid one is acknowledged instantly and processed in the background.

<figure><img src="../../../.gitbook/assets/routing-cost-ingestion.png" alt="Cost ingestion page"><figcaption></figcaption></figure>

### Register Credentials In Intelligent Routing

Under **Data ingestion**, select **Automatic**, then choose Adyen or Checkout in **Connector**.

Use the copy button beside **Webhook URL** to copy the settlement notification URL. This URL includes the selected profile and connector. Paste the copied URL into the matching processor's webhook settings. Copy it again if you change the profile or connector.

Complete the remaining fields using the provider setup below.

| Field | What to enter |
| --- | --- |
| **Account** | The processor-side account the report relates to. Use Adyen's merchant account code or Checkout's entity ID. |
| **Webhook secret** | The HMAC key or signature key used to verify report notifications. Use the key for the environment you are configuring. |
| **Report download auth** | The credential used to download the report after a notification arrives. |

Click **Save credentials** when all fields are complete. Use **Update credentials** when changing a saved source. Stored secrets are encrypted and displayed only as masked hints.

{% hint style="info" %}
The steps below reference the Adyen and Checkout dashboards. Exact menu labels can change over time - the linked provider docs are the source of truth.
{% endhint %}

### Adyen Setup

Intelligent Routing consumes Adyen's **Payment Accounting Report**, notified by a **Report** webhook (`REPORT_AVAILABLE`).

1. **Schedule the Payment Accounting Report.** In the Adyen Customer Area, go to **Reports → Report overview**, select **Payment accounting report → Manage report**, choose **Automatic (generate on a schedule)**, set the format to **CSV**, and add a schedule (Daily is typical). This requires the **Merchant Report** user role.
2. **Create report-download credentials.** Under **Developers → API credentials**, create a **Report user** with the **Merchant Report Download** role. You can authenticate downloads with Basic authentication using the report user's username and password, or with a Report Service API key.
3. **Add the report webhook and generate an HMAC key.** In Hyperswitch, select Adyen in **Connector** on the **Automatic** ingestion form and copy **Webhook URL** for the selected profile. In the Adyen Customer Area, go to **Developers → Webhooks → Create new webhook**, add a **Report** webhook, and paste the copied URL as its endpoint.

   Subscribe it to the **`REPORT_AVAILABLE`** event so each generated report is delivered, then under **Security** generate a new HMAC key and copy it. Use the HMAC key from your **live** Customer Area for production.
4. **Save the credentials in Hyperswitch.** Enter the merchant account code in **Account**, the HMAC key in **Webhook secret**, and the report-user credential in **Report download auth**. Click **Save credentials**.

**Provider documentation**

[Adyen - Automatically get reports](https://docs.adyen.com/reporting/automatically-get-reports/) · [Configure and manage webhooks](https://docs.adyen.com/development-resources/webhooks/configure-and-manage)

### Checkout Setup

Intelligent Routing consumes Checkout's **Financial Actions** report, notified by a **`report_generated`** event.

1. **Schedule the Financial Actions report.** In the Checkout Dashboard, open **Reporting** and create a schedule for the **Financial Actions** report. Pick a frequency (Daily, Weekly, or Monthly) and enable delivery by webhook so a `report_generated` event fires when each report is ready.
2. **Create a secret key for downloads.** Under **Developers → Keys**, use or create a **secret key** (`sk_…`). Intelligent Routing uses it to fetch the report through the Reports API.
3. **Create the webhook and generate a signature key.** In Hyperswitch, select Checkout in **Connector** on the **Automatic** ingestion form and copy **Webhook URL** for the selected profile. In the Checkout Dashboard, go to **Developers → Webhooks → New webhook** and paste the copied URL as the endpoint.

   Subscribe it to the **`report_generated`** event, and generate a signature key.
4. **Save the credentials in Hyperswitch.** Enter the Checkout entity ID in **Account**, the signature key in **Webhook secret**, and the secret key in **Report download auth**. Click **Save credentials**.

**Provider documentation**

[Financial Actions reports](https://www.checkout.com/docs/business-operations/retrieve-reports/reconciliation-reports/financial-actions-reports) · [Manage webhooks in the Dashboard](https://www.checkout.com/docs/developer-resources/event-notifications/receive-webhooks/manage-webhooks-in-the-dashboard)

## Try It With A Sample File

If you do not have a report file handy, run a curated sample to see how ingestion produces a cost model.

1. Under **Data ingestion**, select **Manual** and choose **Use a sample file**.
2. Select the processor in **Connector**.
3. Click **Run sample**.

The sample is filed under a demo account and appears in your ingestion history. You can watch it process and inspect the resulting coverage and clusters.

<figure><img src="../../../.gitbook/assets/routing-cost-sample-file.png" alt="Run a sample report through the ingestion pipeline"><figcaption></figcaption></figure>

## Recovering Invoice-Only Fees

A settlement report carries a transaction's **core** fees (interchange, scheme, markup, commission). But your processor also charges flat per-transaction fees (such as a processing fee or a risk fee) and periodic fees that appear **only on the monthly invoice**. These are invisible to the settlement report and account for roughly the last **~10%** of your true cost.

Uploading the invoice recovers them. Under **Data ingestion**, select **Invoice**.

1. Select the processor in **Connector** and enter the account it covers in **Account**.
2. Optionally, enter **Invoice number** for your records.
3. Select the invoice PDF (as downloaded) or CSV export in **Invoice file**.
4. Click **Upload & identify fees**.
5. Review the result. It includes a per-transaction add-on, split into a flat part and a percentage part, with a line-by-line breakdown of the identified fees.

<figure><img src="../../../.gitbook/assets/routing-cost-invoice.png" alt="Connector invoice upload screen showing connector, account, invoice number, and invoice file fields"><figcaption></figcaption></figure>

Intelligent Routing classifies each invoice line to avoid mispricing or double-counting fees:

| Category | Treatment |
| --- | --- |
| **Flat per transaction** (processing, risk) | Added to every cluster's flat fee - the bulk of the gap. |
| **Periodic / non-transactional** (scheme, chargeback, management) | Spread across volume as a small percentage add-on. |
| **Credits** (rebates, corrections, refunds) | Subtracted - reduces net cost. |
| **Already in the report** (interchange, scheme, markup, commission) | Ignored - already modelled by the fit, so never counted twice. |

The add-on is layered on top of the learned model for that processor in every routing decision. You can review active add-ons, remove one (which reverts to the report-only model), and check invoice reconciliation to see how much of the invoice the model now explains.

## After Ingestion

Every ingestion - however it arrived - lands in the same three places.

Open **Ingested data** under **Cost Estimation** to review report history and coverage.

* **Ingestion history.** Every report is listed newest first, with live progress for in-flight jobs. Each row shows when it was ingested, its source, processor and account, the period covered, status, rows staged, and how many clusters graded trustworthy. Delete a row to **undo** that ingestion - its transactions are removed, the processor is refitted from what remains, and coverage reverts accordingly.
* **Cost model coverage.** How much of your volume now has a trustworthy cost model, and the fit accuracy. This is explained in [Cost Estimation → Coverage](cost-estimation.md#coverage).
* **Price changes.** Because the model refits on every ingestion, a processor quietly changing its pricing shows up as a step in a cluster's fee between its two most recent fits - so a silent reprice does not go unnoticed.

## Related

* [Cost Estimation](cost-estimation.md) - what happens to your data once ingested.
* [Multi-Objective Routing](multi-objective-routing.md) - how cost drives routing.
