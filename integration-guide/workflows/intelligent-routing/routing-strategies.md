---
description: Choose the right routing strategy for your payment traffic
icon: route
---

# Routing Strategies

Choose the routing strategy based on the problem you are solving.

| Strategy | Best for | Start here |
| --- | --- | --- |
| Rule-Based Routing | Deterministic routing by business condition | [Rule-Based Routing](rule-based-routing.md) |
| Volume-Based Routing | Fixed traffic allocation and gradual rollout | [Volume-Based Routing](volume-based-routing.md) |
| Auth-Rate Routing | Improving authorization rate dynamically | [Auth-Rate Routing](auth-rate-based-routing.md) |
| Cost-Aware Routing | Reducing cost while protecting auth rate | [Cost-Aware Routing](cost-aware-routing.md) |
| Default Fallback Routing | Backup processor order | [Default Fallback Routing](default-fallback-routing.md) |

## Recommended Starting Point

1. Configure [Default Fallback Routing](default-fallback-routing.md).
2. Use [Rule-Based Routing](rule-based-routing.md) for known business constraints.
3. Use [Volume-Based Routing](volume-based-routing.md) to ramp new processors.
4. Use [Auth-Rate Routing](auth-rate-based-routing.md) when multiple processors can handle the same traffic.
5. Add [Cost-Aware Routing](cost-aware-routing.md) once processor cost data is available.

{% hint style="info" %}
Screenshot placeholder: Routing strategy selection page with available strategy cards.
{% endhint %}
