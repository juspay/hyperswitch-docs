---
description: Improve successful payments by routing traffic to processors with stronger recent authorization performance
icon: badge-check
metaLinks:
  alternates:
    - auth-rate-based-routing.md
---

# Auth-Rate Routing

Auth-Rate Routing uses recent payment outcomes to choose the processor most likely to authorize the next payment. It is useful when you have multiple processors for the same payment method and want routing to adapt as performance changes.

## How It Works

Hyperswitch tracks processor performance across payment attributes such as payment method, payment method type, currency, country, card network, authentication type, and amount band. The routing engine then ranks eligible processors by recent success rate.

The model balances two behaviors:

* **Exploitation:** Send most traffic to the processor with the best recent performance.
* **Exploration:** Send a smaller share of traffic to other eligible processors so the model keeps fresh performance data.

Downtime or repeated technical failures can deprioritize a processor before the final decision is made.

## Merchant Controls

| Control | Why it matters |
| --- | --- |
| Traffic split | Roll out auth-rate routing gradually before using it for all payments. |
| Bucket size | Controls how much recent traffic is used to calculate processor performance. |
| Hedging percentage | Controls how much traffic is used for exploration. |
| Elimination threshold | Controls when a poorly performing processor is temporarily deprioritized. |

{% hint style="info" %}
Screenshot placeholder: Auth-rate routing setup screen showing traffic split, bucket size, and hedging percentage.
{% endhint %}

## Setup

1. Configure at least two processors that support the same payment method.
2. Go to `Workflow` > `Routing`.
3. Choose `Auth-Rate Routing`.
4. Configure rollout percentage and scoring settings.
5. Save and activate the configuration.
6. Monitor processor share, auth rate, and decision logs.

For automatic tuning of bucket size and exploration settings, see [Autopilot](autopilot.md).
