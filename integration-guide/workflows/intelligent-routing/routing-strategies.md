---
description: Choose the right routing strategy for your payment traffic
icon: route
---

# Routing Strategies

Choose the routing strategy based on the problem you are solving. Static strategies give you deterministic control. Dynamic strategies use observed performance or cost data and should be rolled out after you have enough traffic and monitoring.

| Strategy | Use it when | Requires |
| --- | --- | --- |
| [Rule-Based Routing](rule-based-routing.md) | A business condition must force a processor, split, or fallback list. | Processor setup and rule conditions. |
| [Volume-Based Routing](volume-based-routing.md) | You want a fixed traffic allocation or a controlled ramp to a new processor. | Processor setup and percentage allocation. |
| [Auth-Rate Routing](auth-rate-based-routing.md) | Multiple processors can handle the same traffic and you want routing to adapt to recent authorization performance. | Outcome feedback and enough volume for scoring. |
| [Cost-Aware Routing](cost-aware-routing.md) | You want to reduce processing cost without ignoring authorization performance. | Auth-Rate Routing, margin, and cost coverage. |
| [Least Cost Routing](least-cost-routing.md) | You process supported debit card traffic where local debit networks can reduce cost. | Debit support and enabled local networks. |
| [Default Fallback Routing](default-fallback-routing.md) | You need the backup processor order for unmatched or ineligible routing results. | At least one configured processor. |

## Recommended Starting Point

1. Configure [Default Fallback Routing](default-fallback-routing.md).
2. Use [Rule-Based Routing](rule-based-routing.md) for known business constraints.
3. Use [Volume-Based Routing](volume-based-routing.md) to ramp new processors.
4. Use [Auth-Rate Routing](auth-rate-based-routing.md) when multiple processors can handle the same traffic.
5. Add [Cost-Aware Routing](cost-aware-routing.md) once processor cost data is available.
6. Use [Least Cost Routing](least-cost-routing.md) for supported debit network optimization.

{% hint style="info" %}
Screenshot placeholder: Routing strategy selection page with available strategy cards.
{% endhint %}
