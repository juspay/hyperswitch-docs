---
description: Route every payment to the best processor based on business rules, live performance, cost, and fallback preferences
icon: route
metaLinks:
  alternates:
    - ./
---

# Intelligent Routing

Hyperswitch Intelligent Routing helps merchants control where each payment is processed. You can use it to improve authorization rates, reduce processing cost, shift volume across processors, and keep payments moving when a processor is unavailable.

## What You Can Do

| Goal | Use this |
| --- | --- |
| Route specific traffic to specific processors | [Rule-Based Routing](rule-based-routing.md) |
| Split traffic by percentage | [Volume-Based Routing](volume-based-routing.md) |
| Send more traffic to better-performing processors | [Auth-Rate Routing](auth-rate-based-routing.md) |
| Balance authorization rate with processing cost | [Cost-Aware Routing](cost-aware-routing.md) |
| Define the backup processor order | [Default Fallback Routing](default-fallback-routing.md) |
| Compare two routing setups before rollout | [A/B Testing](ab-testing.md) |
| Let Hyperswitch tune auth-rate routing automatically | [Autopilot](autopilot.md) |
| See why a processor was selected | [Analytics And Decision Logs](analytics-and-decision-logs.md) |

## How A Payment Is Routed

1. Hyperswitch checks which processors are eligible for the payment method, currency, country, and connector configuration.
2. The active routing strategy ranks or filters those processors.
3. Optional optimization layers, such as downtime elimination or cost-aware routing, refine the choice.
4. If the selected processor is not eligible or available, Hyperswitch uses Default Fallback Routing.
5. The decision is logged so your team can review the selected processor, routing approach, and outcome.

{% hint style="info" %}
Screenshot placeholder: Routing overview page showing the active routing strategy, default fallback list, and recent routing performance.
{% endhint %}

## Recommended Rollout

Start with Default Fallback Routing, then add Rule-Based or Volume-Based Routing for business controls. Use Auth-Rate Routing once you have multiple processors handling meaningful traffic. Add Cost-Aware Routing after cost data is available, and use A/B Testing before moving a new strategy to all traffic.

For self-hosted deployments or merchants integrating routing into an existing orchestrator, see the [Self-Deployment Guide](self-deployment-guide.md).
