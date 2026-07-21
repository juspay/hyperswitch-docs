---
description: Configure the backup processor order used when no routing rule applies or the selected processor is not eligible
icon: shield-exclamation
metaLinks:
  alternates:
    - default-fallback-routing.md
---

# Default Fallback Routing

Default Fallback Routing is the ordered backup list of processors for a merchant profile. Hyperswitch uses it when there is no active routing strategy, no rule matches, or the selected processor is not eligible for the current payment.

## When It Applies

Default fallback can be used when:

* No routing configuration is active.
* A rule or volume split points to a processor that does not support the payment method.
* A processor is temporarily unavailable.
* A dynamic routing result cannot be used safely.

## Setup

1. Go to `Workflow` > `Routing`.
2. Open `Default Fallback`.
3. Reorder the configured processors by priority.
4. Save the fallback order.

{% hint style="info" %}
Screenshot placeholder: Default fallback processor ordering screen.
{% endhint %}

## Good Practices

Put your most reliable general-purpose processor first, followed by processors that support the broadest set of payment methods and currencies. Review this list whenever you add or remove a connector.
