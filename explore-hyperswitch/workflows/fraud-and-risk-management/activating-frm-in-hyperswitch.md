---
icon: shield-plus
---

# Activating FRM in Hyperswitch

You can enable the [FRM solution](https://juspay.io/integrations) of your choice with few clicks and very minimal code changes. Below are the two scenarios for activating FRM within Hyperswitch.

#### Prerequisites

Before activation, ensure the following:

1. Payment Method Information: Required for configuration.
2. FRM Solution Signup: Obtain API keys from your selected FRM provider.

#### Pre-Authorization Flow

The Pre-Auth flow is executed before payment authorization and is available for all payment methods. When a customer initiates a payment, transaction details are analyzed by the FRM solution to assess risk using parameters like historical behavior, location, transaction patterns, and device data.

1. Goal: Prevent fraudulent transactions before authorization.
2. Steps:
   1. Transaction details are sent to the FRM solution for analysis.
   2. Based on the FRM risk score or recommendation, below actions are taken:
      * Continue on Accept: Proceed with the transaction.
      * Halt on Decline: Mark the transaction as cancelled.
3. The merchant can influence the outcome of FRM by making changes on their dashboard, so that the FRM risk score or recommendation reflects their Risk appetite.    &#x20;

#### Post-Authorization Flow

The Post-Auth flow occurs after payment authorization by the processor and is only available for Card payment methods. It serves as a second validation layer, analyzing the transaction using updated and historical data to detect potential fraud.

* Goal: Act as a safety net for suspicious transactions.
* Steps:
  1. Post-authorization details are sent to the FRM solution.
  2. Transactions flagged as fraudulent are queued for manual review with a status "Requires Merchant Action" on Hyperswitch.
  3. Merchants review on FRM dashboard and decide next steps on that transaction. Hyperswitch consumes the webhooks from the FRM to:
     * Continue on Accept: Continue with the transaction.
     * Halt on Decline: Mark the transaction as cancelled.
     * Approve/Decline on Review:
       * Hold the transaction in manual review state. Merchants can list and review such transactions.
       * If approved: Capture the payment.
       * If declined: Void the payment.

{% hint style="warning" %}
If the connector doesn’t support manual capture, Post-Authorization manual review should be avoided during configuration setup for the respective connector.
{% endhint %}

#### FRM workflow

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### FRM status and decisions

FRM connectors generally provide a decision based on rules or data models along with a risk score associated with the transaction. Some integrations require providing the model to be used explicitly.&#x20;

Fraud detection can be done via the below methods:

1. Rules: Uses a static set of rules for deciding on the outcome.
2. Scores: Uses a range of numbers for associating risk with the transaction.
3. Decisions/Recommendations: Uses ML data models for predicting and recommending the outcome. This flow is supported by Hyperswitch
4. Chargeback Guarantee: Uses ML data models for responding with a binary outcome (Accept vs Decline). This flow is supported by Hyperswitch
