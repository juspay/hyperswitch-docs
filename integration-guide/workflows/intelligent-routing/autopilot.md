---
description: Automatically tune auth-rate routing based on observed traffic
icon: gauge
---

# Autopilot

Autopilot automatically tunes Auth-Rate Routing settings using observed payment traffic. It is useful when processor performance changes over time and manual tuning becomes hard to maintain.

## What Autopilot Tunes

Autopilot can tune:

* Bucket size, which controls how much recent traffic is used for scoring.
* Hedging percentage, which controls exploration traffic.

Autopilot does not change your connector credentials, payment method setup, explicit rule-based routing conditions, or default fallback order.

## When To Use It

Use Autopilot when:

* You have enough transaction volume for reliable scoring.
* You use Auth-Rate Routing across multiple processors.
* You want routing to adapt without frequent manual retuning.
* You can monitor the changes through analytics and decision logs.

{% hint style="info" %}
Screenshot placeholder: Autopilot settings screen showing enablement and recent calibration actions.
{% endhint %}

## Recommended Rollout

1. Enable Auth-Rate Routing first.
2. Confirm payment outcomes are being reported correctly.
3. Run Autopilot on a limited scope or compare it with manual settings using [A/B Testing](ab-testing.md).
4. Monitor auth rate, processor share, and routing events.
5. Expand rollout after the results are stable.

## What To Monitor

* Auth-rate trend after calibration.
* Changes in processor share.
* Calibration events.
* Any increase in fallback usage.
* Experiment results if Autopilot is being tested against manual settings.
