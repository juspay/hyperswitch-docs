---
description: Configure the backup processor order used when no routing rule applies or the selected processor is not eligible
icon: shield-exclamation
metaLinks:
  alternates:
    - default-fallback-routing.md
---

# Default Fallback Routing

{% embed url="https://youtu.be/5ymPEkOf-BQ" %}

Default Fallback Routing is the priority order of configured processors for a merchant profile. Hyperswitch can use this order on its own, or as the backup path when another routing strategy does not return a usable processor.

## When It Applies

Default fallback can be used when:

* No routing configuration is active.
* A rule or volume split points to a processor that does not support the payment method.
* A processor is temporarily unavailable.
* A dynamic routing result cannot be used safely.

## Setup

1. Go to `Workflow` > `Routing`.
2. Click `Manage` for Default Fallback.
3. Review the list of configured processors.
4. Reorder processors based on the priority you want Hyperswitch to use when no routing algorithm is active or the selected processor is not eligible.
5. Save the fallback order.

## Good Practices

Put your most reliable general-purpose processor first, followed by processors that support the broadest set of payment methods and currencies. Review this list whenever you add or remove a connector.
