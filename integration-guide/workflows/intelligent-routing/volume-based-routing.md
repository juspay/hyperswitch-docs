---
description: Distribute payment traffic across multiple processors by percentage
icon: chart-simple
metaLinks:
  alternates:
    - volume-based-routing.md
---

# Volume-Based Routing

{% embed url="https://youtu.be/xpU3zmyD4b8" %}

Volume-Based Routing distributes payments across processors using fixed percentages. It is useful when you want predictable traffic allocation without writing conditional rules.

## When To Use It

Use Volume-Based Routing to:

* Gradually move traffic to a new processor.
* Keep multiple processors active.
* Meet a planned traffic allocation.
* Run a simple production rollout before switching to a dynamic strategy.

## Setup

1. Go to `Workflow` > `Routing`.
2. Click `Setup` for Volume-Based Routing.
3. Add a name and description for the routing configuration.
4. Select the processors and configure the required percentage split.
5. Choose whether to only save the configuration or save and activate it for payments.
6. Review the active and previously configured routing algorithms on the [Hyperswitch Dashboard](https://app.hyperswitch.io/routing).

## Notes

The configured percentages apply only to processors that are eligible for the payment. If the selected processor is not eligible, Hyperswitch uses [Default Fallback Routing](default-fallback-routing.md).
