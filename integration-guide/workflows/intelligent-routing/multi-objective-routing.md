---
description: Balancing Auth Rate and Cost Savings
icon: hexagon-nodes
---

# Multi-objective Routing

In Multi-Objective Routing, the transactions are routed across PSPs based on the Economic Value.&#x20;

**Economic value:** the expected value of routing a transaction to a given PSP, calculated as **auth rate × settlement value, where settlement value = transaction amount − cost of processing**. Cost of processing is the sum of issuer, network, and acquirer fees for that PSP on that transaction, read from settlement data rather than estimated.

<figure><img src="../../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Configurations

#### Autopilot: auto-tuning the routing parameters per cluster

The routing module derives its routing parameters from each cluster's own data and refreshes them continuously. Every hour, it auto-updates bucket size and hedging percentage based on the previous hour's transactions, keeping routing decisions statistically reliable while still reacting quickly to PSP performance changes.

Bucket size balances confidence against agility. It has to be large enough to trust the auth-rate comparison, but lean enough to react quickly when a PSP's performance shifts. Bucket size scales with transaction volume: to detect a 2% net-auth-rate difference, a cluster needs roughly 150 transactions per hour of history at 500 transactions/hour, rising to around 900 at 4,000 transactions/hour. More traffic affords a wider, more accurate window that's still fresh.

Hedging percentage balances learning against exploitation. It has to be large enough to keep PSP comparisons fresh, so the engine notices when a lagging provider recovers but controlled enough not to give back net-auth-rate gains from the top performer by over-sampling weaker ones.

The high-level goal a merchant sets is deliberately small: a single business preference on whether the system should optimize for cost at all. Everything underneath - bucket size, hedging, and the economic-value comparison itself - is derived automatically from the merchant's own historical data and updates as success-rate estimates and settlement costs change.

<figure><img src="../../../.gitbook/assets/routing-autopilot-settings.png" alt="Autopilot settings screen"><figcaption></figcaption></figure>

### Cost Data Inputs

There are two ways in which you can provide the cost data:

1. **Automatic:** Connect to your PSP account by entering the credentials and Hyperswitch will receive the Cost Fee Reports at the set cadence

<figure><img src="../../../.gitbook/assets/routing-cost-ingestion.png" alt="Cost ingestion page"><figcaption></figcaption></figure>

2. **Manual:** Upload the fee report as a .csv file as per the expected template (which can be downloaded from the dashboard). In case of data field mismatch resolve by manually mapping the columns in the data with the expected fields.
   1. In sandbox there are also sample files available to try it out.&#x20;

<figure><img src="../../../.gitbook/assets/routing-cost-manual-upload.png" alt="Manual settlement report upload screen"><figcaption></figcaption></figure>

Follow this video guide to learn more:

{% embed url="https://drive.google.com/file/d/1Fv3ZCCAwXO6BT5svDaIqOu3Y-soiiCun/view?usp=drive_link" %}

### Demo Playground

You can use the Decision Simulator to run various scenarios to see the behaviour of the routing module under the set configurations&#x20;

<figure><img src="../../../.gitbook/assets/image (162).png" alt=""><figcaption></figcaption></figure>

Follow this video guide to learn more:

{% embed url="https://drive.google.com/file/d/1sT45F1RMC8al1yQwm71pWVvZkE87Wlan/view?usp=drive_link" %}

### FAQs

#### What's next on multi-objective payment routing?

Economic value is the first non-auth objective folded into routing; the roadmap adds three more, each a new lever on business impact.&#x20;

Volume-discount constraints steer enough GMV to a PSP within a period to qualify for invoice-level discounts that never appear in per-transaction pricing.&#x20;

Multi-currency support normalizes costs to one preferred currency and folds forex into the economic-value calculation, so cross-border routing decisions account for conversion cost.&#x20;

Fraud-dilution constraints track a merchant's standing in the Visa Acquirer Monitoring Program (VAMP) and Mastercard's Excessive Chargeback Merchant (ECM) program, read dispute webhooks, and cut volume to a PSP before a monitoring breach.

#### Will multi-objective routing reduce my authorization rate or lose revenue?

Net Auth Rate is designed to hold, and First Attempt Auth Rate typically eases only \~20 bps on cost-optimized clusters. Cost is an additional constraint, not the engine's objective — the primary goal is still improving the First Attempt Auth Rate — and smart retry provides a fallback on retry-eligible failures whether a transaction was routed to the highest-auth PSP or a cheaper one.

#### How much configuration does multi-objective routing need?

Configuration is fully self-managed in autopilot mode. Bucket size and hedging percentage are derived automatically from each cluster's own historical data and refreshed hourly. The only mandatory high-level input is a single business preference: whether the system should optimize for cost at all. There are no per-transaction tolerances for a merchant to set.

#### What cost data does Hyperswitch need to run economic-value routing?

A single report with the cost breakdown at the transaction level — the Payment Accounting Report for Adyen, or the equivalent for other PSPs. Setup is one-time with zero ongoing effort; cost data refreshes automatically each time new settlement reports are ingested. Hyperswitch's cost observability layer derives the true per-transaction processing fee from these reports rather than estimating it.

#### How does the system decide whether a cost saving is worth the auth-rate impact?

Through the economic-value comparison itself. Because a PSP's score is auth rate × (amount − cost), a lower-cost PSP only wins when its cost advantage outweighs its authorization disadvantage. On a $60 sale, for example, a $0.40 fee gap is offset at an auth-rate lead of about 0.61 percentage points — below that lead the cheaper PSP wins, above it the higher-auth PSP does.&#x20;

<br>
