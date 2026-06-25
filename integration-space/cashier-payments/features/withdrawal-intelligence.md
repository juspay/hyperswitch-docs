# Withdrawal Intelligence

Withdrawal experience is one of the most under-pitched levers in iGaming payments - and one of the most consequential. Slow or failed withdrawals are consistently among the top reasons players churn and the top sources of public complaints on review platforms. At the same time, withdrawals carry real per-transaction cost (instant push-to-card rails like Visa Direct and Mastercard Send charge meaningfully more than ACH or bank transfer), and the operator faces a permanent tradeoff between speed, cost, and success rate.

Juspay’s Smart Router for Payouts and Smart Retries for Payouts are built specifically for this tradeoff - and the routing operates within the closed-loop constraints set by AML. The router cannot choose to send a Visa-funded deposit out via ACH to a different bank account; it can only optimize among the rails that are valid for the originating funding source.

### What the router optimizes for

For each eligible payout leg, the router scores candidate rails on:

* **Success rate** - historical SR per rail, per BIN range, per issuer, per region. Juspay’s MAB-based auth-rate routing continuously updates these scores from live traffic.
* **Cost** - explicit per-transaction fees for each rail, plus scheme fees and FX costs.
* **Speed** - target settlement time (real-time, same-day, T+1, T+2). Operators can express speed preferences per player tier (e.g., VIPs get fastest rail; others get cheapest rail meeting a 24-hour SLA).
* **Connector health** - real-time availability and decline-rate elimination of underperforming connectors.

### Routing strategies for payouts

Juspay supports the same routing strategies for payouts as it does for deposits:

* **Rule-based routing** - explicit if-this-then-that logic keyed off amount, currency, country, player tier, BIN, payout method, recency
* **Volume-based routing** - split traffic across connectors by percentage; useful for honoring volume commitments to multiple payout providers
* **Default fallback routing** - pecking order applied when no rule fires
* **Elimination routing** - connectors with elevated failure rates are dynamically deprioritized
* **Auth-rate-based routing** - Multi-Armed Bandit (MAB) model continuously evaluates and adjusts based on real-time payout performance

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
