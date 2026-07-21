---
description: Monitor routing performance and inspect why a processor was selected
icon: chart-line
---

# Analytics And Decision Logs

Analytics and decision logs help merchants verify that routing is working as expected. Use them to understand processor performance, investigate individual payments, and measure the impact of routing changes.

## Key Views

| View | Use it for |
| --- | --- |
| Gateway scores | See recent processor authorization performance. |
| Decisions | Track which processors were selected and which routing approach was used. |
| Cost savings | Measure savings from Cost-Aware Routing. |
| A/B test results | Compare control and variant performance. |
| Payment audit | Inspect the routing decision for a specific payment. |
| Routing events | Review changes such as leader changes, downtime behavior, or Autopilot calibration. |

{% hint style="info" %}
Screenshot placeholder: Routing analytics dashboard with gateway scores, processor share, auth rate, and cost savings.
{% endhint %}

## Investigate A Payment

Use Payment Audit when a payment went through an unexpected processor.

Check:

* The eligible processor list for the payment.
* The active routing configuration.
* The routing approach used.
* Whether the selected processor failed eligibility.
* Whether fallback was applied.
* The final payment outcome sent back for scoring.

{% hint style="info" %}
Screenshot placeholder: Payment audit timeline showing routing decision, selected processor, fallback, and score update.
{% endhint %}

## Metrics To Review Before Rollout

Before increasing traffic for a routing strategy, review:

* First-attempt authorization rate.
* Overall authorization rate.
* Processor share.
* Fallback rate.
* Cost saved.
* Failed or missing score updates.
* A/B test guardrails and verdicts.
