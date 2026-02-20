---
icon: magnifying-glass-arrows-rotate
---

# Smart Retries in Payout

Smart Retries enable the automatic recovery of failed payout attempts by re-initiating transactions based on specific error types and connector availability. This mechanism optimizes the success rate of disbursements by evaluating whether a retry is likely to resolve the initial failure.

### How Smart Retries Work

Smart Retries are triggered based on connector-specific error configurations. A retry is only attempted if the error is categorized as recoverable and the configuration suggests a high probability of success upon re-attempt.

#### Retry Strategies

Hyperswitch employs two primary strategies for payout recovery:

* Single Connector Retry: If only one connector is configured for a specific payout method, eligible errors are retried through that same connector.
* Multi-Connector Retry: If multiple connectors are available for a payout method, Hyperswitch attempts the retry using the next available connector in your priority list.

#### Supported Payout Methods by Connector

Smart Retries are available for the following connector and method combinations:

<table><thead><tr><th width="243">Connector</th><th>Payout Methods</th></tr></thead><tbody><tr><td>Adyen</td><td>Cards, Banks and Wallets</td></tr><tr><td>Cybersource</td><td>Cards</td></tr><tr><td>Ebanx</td><td>Banks</td></tr><tr><td>Paypal</td><td>Wallets</td></tr><tr><td>Stripe</td><td>Cards and Banks</td></tr><tr><td>Wise</td><td>Banks</td></tr></tbody></table>

### Conditions and Constraints

The execution of a Smart Retry is governed by the following logic:

* Method Consistency: The payout method remains unchanged during a retry. For example, a failed bank transfer will not be retried as a card payout.
* Error Configuration: Retries are only initiated for error codes that have been loaded into the Hyperswitch engine. Merchants can submit custom error configurations to the Hyperswitch team.
* Retry Limits: \* The system continues retrying until the payout is successful, the retry count is exhausted, or all eligible connectors are exhausted.
  * The default Retry Count is 5 per connector, which can be customized based on merchant requirements.
* Multi-Connector Eligibility: Multi-connector retries require at least two active [payout connectors](https://www.google.com/search?q=/docs/payouts/connectors) to be configured for the same payout method.
