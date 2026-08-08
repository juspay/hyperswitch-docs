# Operations

## Operations

**Operations** is your day-to-day command center. It's where support and ops teams spend most of their time: looking up transactions, issuing refunds, fighting disputes, and managing customers and payouts.

Everything here respects your current **mode (Test/Live)** and **selected profile** — see Getting Started if that's new to you.

The Operations section contains:

* Payments
* Refunds
* Disputes
* Customers
* Payouts

***

### Payments

The **Payments** screen lists every payment attempt for the selected profile and mode.

#### Finding a payment

* **Search** by payment ID, connector reference, customer email, or amount.
* **Filter** by status, connector, payment method, currency, or a date range.
* **Saved views** let you save a filter combination (e.g. "Failed card payments today") and reuse it with one click.
* **Customize columns** to show the fields your team cares about, then export the list if you need it in a spreadsheet.

#### Payment statuses at a glance

| Status                       | Meaning                                |
| ---------------------------- | -------------------------------------- |
| **Succeeded**                | Payment completed and captured         |
| **Requires capture**         | Authorized, waiting for you to capture |
| **Processing**               | In flight at the processor             |
| **Requires customer action** | Awaiting 3DS / redirect / next action  |
| **Failed**                   | Declined or errored                    |
| **Cancelled**                | Voided before capture                  |

#### Payment details

Click any row to open the full payment view.

Here you can see:

* **Summary** — amount, currency, status, customer, connector used.
* **Timeline** — an event-by-event history (created → authorized → captured → refunded), useful for debugging.
* **Attempts** — if routing retried across connectors, each attempt is listed.
* **Connector response** — raw processor codes and messages for troubleshooting declines.
* **Actions** — depending on status: **Capture**, **Refund**, or **Cancel/Void**.

> 💡 A declined payment's **connector response code** is the fastest way to understand _why_ it failed. Pair it with the timeline to see exactly where it stopped.

***

### Refunds

The **Refunds** screen lists all refunds and their status. You can also start a refund directly from a payment.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/Operations_On_Hyperswitch_Refunding_the_test_payment__3mmCY4kiRT2z48-G_nc07w" %}

#### Issuing a refund

1. Open the payment (Operations → Payments → click the row), or go to **Refunds → Create**.
2. Choose **full** or **partial** refund and enter the amount.
3. Add an optional reason/note for your records.
4. Confirm. The refund is sent to the processor and appears with a **Pending** status until the processor confirms.

#### Refund statuses

| Status        | Meaning                                      |
| ------------- | -------------------------------------------- |
| **Pending**   | Sent to the processor, awaiting confirmation |
| **Succeeded** | Funds returned to the customer               |
| **Failed**    | Processor rejected the refund                |

> Refund capabilities depend on the connector — some support partial refunds, some don't. If the refund action is disabled, check the connector's capabilities.

***

### Disputes

When a customer challenges a charge with their bank, it becomes a **dispute** (chargeback). The Disputes screen helps you track and respond to them.

#### The dispute lifecycle

| Stage                       | What it means          | Your move                                      |
| --------------------------- | ---------------------- | ---------------------------------------------- |
| **Opened / Needs response** | Bank raised a dispute  | Gather and submit evidence before the deadline |
| **Under review**            | Evidence submitted     | Wait for the bank's decision                   |
| **Won**                     | Resolved in your favor | Nothing to do                                  |
| **Lost**                    | Resolved against you   | Funds are debited                              |

#### Responding to a dispute

1. Open the dispute to see the reason code, amount, and **respond-by deadline**.
2. Review the linked payment for context.
3. Submit **evidence** (receipts, shipping proof, customer comms) if the connector supports it through Hyperswitch.
4. Track status until it resolves.

> ⏰ Disputes are deadline-driven. Sort by respond-by date and handle the soonest first.

***

### Customers

The **Customers** screen lists the customers created against your account and their saved details.

From here you can:

* **Search** customers by name, email, or ID.
* Open a customer to see their **profile**, **saved payment methods / tokens**, and their **payment history**.
* Understand a customer's full relationship with you in one place before taking a support action.

> Saved payment methods and tokens tie into the **Vault** — see the Vault section for how tokenization works.

***

### Payouts

If payouts are enabled for your account, the **Payouts** screen manages money going _out_ to recipients (sellers, contractors, users).

Here you can:

* View **payout transactions** and their status.
* Create a payout to a recipient using a configured **payout processor**.
* Track lifecycle from initiated → in-transit → succeeded/failed.

> Payouts require a **payout processor** connected under Connectors, and can use **Payout Routing** to pick the best rail. See the Connectors and Workflow sections.

***

### Where to go next

* **Connectors** → connect the processors that power these payments.
* **Workflow** → set up routing, 3DS, and fraud rules that shape payment outcomes.
* **Analytics** → aggregate views and trends across all this operational data.
