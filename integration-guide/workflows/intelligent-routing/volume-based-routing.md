---
description: Distribute payment traffic across multiple processors by percentage
icon: chart-simple
metaLinks:
  alternates:
    - volume-based-routing.md
---

# Volume-Based Routing

Volume-Based Routing lets you split traffic across processors using fixed percentages. Use it when you want predictable distribution without writing conditional rules.

## When To Use It

Use Volume-Based Routing to:

* Gradually move traffic to a new processor.
* Keep multiple processors active.
* Meet a planned traffic allocation.
* Run a simple production rollout before switching to a dynamic strategy.

## Setup

1. Go to `Workflow` > `Routing`.
2. Choose `Volume-Based Routing`.
3. Select the processors.
4. Set the percentage split for each processor.
5. Save and activate the routing configuration.

{% hint style="info" %}
Screenshot placeholder: Volume split configuration showing processors and percentage allocation.
{% endhint %}

## Notes

The configured percentages apply only to processors that are eligible for the payment. If the selected processor is not eligible, Hyperswitch uses [Default Fallback Routing](default-fallback-routing.md).
