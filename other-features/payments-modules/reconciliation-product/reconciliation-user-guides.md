# Reconciliation User Guides

This guide shows you how to use Hyperswitch Reconciliation to answer one simple question:

> **"Did every payment I was supposed to receive actually reach my bank account — for the right amount?"**

You don't need to be a payments expert or an engineer to use this guide. Each section walks through one screen of the dashboard, in the order you'll actually use them.

### Before you start — please read this

This guide assumes the following is already true for you. If any of these isn't, stop here and reach out to the Hyperswitch team first.

1. **You've spoken to the Hyperswitch team.** You've shared your setup details with us — which systems you want to reconcile, what your report files look like, and how a payment should be matched across them.
2. **Your account is already configured.** Based on those details, we've set up your accounts, ingestion pipelines, and matching rules. You do **not** need to configure anything yourself — when you log in, everything in this guide is ready to use.
3. **You have your files ready.** Reconciliation works on the reports your systems produce — for example an order export, PSP settlement reports, and a bank statement. Have these downloaded and available to upload.
4. **You're logged into the right place.** Check the top-left of the dashboard: make sure the correct **Merchant Account** and **Profile** are selected. A profile is one reconciliation setup — if your team has more than one, the numbers on screen belong to whichever profile is selected.
5. **Test Mode banner.** If you see a _"You're in Test Mode"_ banner at the top, you're looking at a test environment. That's expected while you're trying things out — your live data lives in live mode.

### The example used throughout this guide

Every screen in this guide is explained using the same simple setup — a **3-way reconciliation**:

```
Your Order System (OMS) ──► PSP 1 ──┐
                                    ├──► Your Bank
                            PSP 2 ──┘
```

In plain words: your order system records a sale, one of two payment providers (PSPs) processes the money, and the money finally lands in your bank account.

Money is verified at **every hop** of that journey:

| Check        | Question it answers                              |
| ------------ | ------------------------------------------------ |
| OMS ↔ PSP 1  | Did PSP 1 process every order we sent it?        |
| OMS ↔ PSP 2  | Did PSP 2 process every order we sent it?        |
| PSP 1 ↔ Bank | Did PSP 1's payouts actually arrive in our bank? |
| PSP 2 ↔ Bank | Did PSP 2's payouts actually arrive in our bank? |

Each of these checks is called a **recon rule**, and each rule appears as its own **tab** across the top of most dashboard screens. Your own setup may have different names and a different number of hops — but the ideas are identical, so you can follow along with your own tabs.

This setup uses **four files**: one OMS export, one report from each PSP, and one bank statement. When the guide says "upload your files," these are the files it means.

### What's in this guide

Follow these in order the first time — it mirrors how you'll actually work:

1. **\[Core concepts in 5 minutes]** — files, entries, transactions, matches, and exceptions, explained by following one payment through the system.
2. **\[Uploading your files (Pipelines)]** — how to get your reports into the system and confirm they were read successfully.
3. **\[Verifying your data (Transformed Entries)]** — how to check every row of your file made it in cleanly.
4. **\[Your daily health check (Overview)]** — match rate, open exceptions, value at risk, and what each number means.
5. **\[Following a payment (Transactions)]** — how to see one payment's full journey and its match status.
6. **\[Fixing problems (Exceptions)]** — what each exception type means, its most common cause, and what to do about it.
7. **\[Your matching rules (Rules Library)]** — a read-only reference for how your matching logic is set up.
8. **\[FAQ & Troubleshooting]** — quick answers to the most common "where's my data?" questions.

### One thing to remember before you go

📅 **Dates work off your file's data, not your upload time.** If you upload yesterday's bank statement today, the entries show under _yesterday's_ date. If a screen looks empty, the #1 fix is: widen the date range at the top right.
