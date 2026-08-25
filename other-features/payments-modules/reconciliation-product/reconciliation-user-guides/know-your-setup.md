# Know your setup

## Guide 1: Know Your Setup

_Time needed: \~5 minutes · Nothing to upload yet_

Your account starts empty — no files, no numbers, no matches. That's fine. Before you upload anything, it's worth spending five minutes understanding what's already been built for you.

When the Hyperswitch team configured your account, they set up two things:

* **Your accounts** — one for each system in your money flow. In our demo that's four: the Order System (OMS), PSP 1, PSP 2, and the Bank.
* **Your recon rules** — the checks that compare two accounts against each other. One rule per hop of the money's journey.

In this guide you'll look at both, in two places:

1. **The Overview diagram** — a visual map of how your accounts connect. Even with no data in it, it shows the shape of your reconciliation: where money starts, where it flows through, and where it should end up.
2. **The Rules Library** — the list of rules behind that diagram. You won't edit anything here; you're just confirming the setup matches how your business actually moves money.

By the end, you'll be able to answer: _"Which systems is my account reconciling, and what checks run between them?"_ — and you'll be ready to upload your first files in Guide 2.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_To_Navigate_The_Hyperswitch_Recon_Engine_Dashboard__rBR06cgRSL6-HW-9rNXqMQ" %}

***

### Step 1: See the shape of your money flow (Overview)

Go to **Operate → Overview** in the left sidebar.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-08-25 at 10.51.52 PM.png" alt=""><figcaption></figcaption></figure>



With no data uploaded yet, the numbers will all be zero — ignore them for now. What you're here for:

* **The tabs across the top.** Next to the "Overview" tab you'll see one tab per recon rule — in our demo, one for each hop: OMS ↔ PSP 1, OMS ↔ PSP 2, PSP 1 ↔ Bank, PSP 2 ↔ Bank. These same tabs appear on most screens in the product, so it's worth recognizing them now: **one tab = one check between two systems.**
* **The flow diagram.** This is your setup drawn as a picture: your systems as boxes, with arrows showing how money moves between them. Trace it once and confirm it matches reality — money starts at your order system, passes through a PSP, and lands at your bank.

> 💡 If a system you use is missing from the diagram, or the flow looks different from how your money actually moves, stop and contact the Hyperswitch team before going further.

### Step 2: Meet your rules (Rules Library)

Go to **Configure → Rules Library** in the left sidebar.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-08-25 at 10.52.09 PM.png" alt=""><figcaption></figcaption></figure>



This is the list of checks behind those tabs. Each row is one rule, and you can read it in plain English:

| Column          | What it tells you                                                                                                                                                                                                                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Priority**    | The order rules are evaluated in. Lower number = checked first.                                                                                                                                                                                                                                                        |
| **Rule Name**   | The two accounts being compared — e.g. _OMS ↔ PSP 1_. Matches the tab names you saw on the Overview.                                                                                                                                                                                                                   |
| **Rule Type**   | _How_ rows are matched. **Single–Single**: one row on this side matches exactly one row on the other. **Single–Many**: one row here matches several rows there (e.g. one payout covering many payments). **Many–Single**: several rows grouped together match one row (e.g. a day's payments against one bank credit). |
| **Description** | A short note about what the rule checks.                                                                                                                                                                                                                                                                               |
| **Status**      | **Active** means the rule will run as soon as data arrives.                                                                                                                                                                                                                                                            |

You don't need to memorize the rule types — just know that the matching logic was built from the setup details you shared with us, and this page is where you can always look it up.

> 🔒 This page is read-only for you by design. If a rule needs changing, that goes through the Hyperswitch team.

### Before you move on — quick checklist

* ✅ I can see all my systems on the Overview diagram.
* ✅ There's a tab (and a rule) for each hop money takes in my business.
* ✅ Every rule in the Rules Library shows **Active**.
* ✅ Nothing on either screen surprised me.

If anything looks wrong or missing, contact the Hyperswitch team before uploading files.
