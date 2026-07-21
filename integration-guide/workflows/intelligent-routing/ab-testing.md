---
description: Compare routing strategies on live traffic before rolling them out
icon: flask
---

# A/B Testing

A/B Testing lets you compare two routing strategies on a controlled percentage of traffic before making a full rollout decision.

## Common Tests

| Test | Why run it |
| --- | --- |
| Auth-Rate Routing vs Cost-Aware Routing | Check whether cost savings are worth any auth-rate movement. |
| Manual auth-rate settings vs Autopilot | Validate automatic tuning before full rollout. |
| Existing rule setup vs new rule setup | Measure impact before replacing a production rule. |
| Current processor mix vs new processor mix | Ramp a new connector with lower risk. |

## How It Works

1. Choose the control routing strategy.
2. Choose the variant routing strategy.
3. Set the percentage of traffic sent to the variant.
4. Define minimum sample size and guardrails.
5. Activate the experiment.
6. Review results before promoting the variant.

Traffic assignment is stable per payment, so retries for the same payment stay in the same experiment arm.

{% hint style="info" %}
Screenshot placeholder: A/B test setup screen showing control strategy, variant strategy, split percentage, minimum sample size, and guardrail.
{% endhint %}

## What To Monitor

* Control auth rate.
* Variant auth rate.
* Cost saved, if one arm uses Cost-Aware Routing.
* Sample size per arm.
* Guardrail status.
* Final verdict.

{% hint style="info" %}
Screenshot placeholder: A/B test results screen showing control vs variant metrics and verdict.
{% endhint %}

## Rollout Guidance

Keep the variant below full traffic until it has enough sample size and passes guardrails. If the variant wins, promote it to the active routing configuration. If it loses or breaches a guardrail, deactivate the experiment and keep the control strategy.
