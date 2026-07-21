---
description: Route every payment to the best processor based on business rules, live performance, cost, and fallback preferences
icon: route
metaLinks:
  alternates:
    - ./
---

# Intelligent Routing

Hyperswitch Intelligent Routing helps merchants decide where each payment should be processed. You can use it to improve authorization rates, reduce processing cost, shift traffic across processors, and keep payments moving when a processor is unavailable.

## What You Can Do

| Goal | Use this |
| --- | --- |
| Route specific traffic to specific processors | [Rule-Based Routing](rule-based-routing.md) |
| Split traffic by percentage | [Volume-Based Routing](volume-based-routing.md) |
| Send more traffic to better-performing processors | [Auth-Rate Routing](auth-rate-based-routing.md) |
| Balance authorization rate with processing cost | [Cost-Aware Routing](cost-aware-routing.md) |
| Route supported debit payments through lower-cost networks | [Least Cost Routing](least-cost-routing.md) |
| Define the backup processor order | [Default Fallback Routing](default-fallback-routing.md) |
| Compare two routing setups before rollout | [A/B Testing](ab-testing.md) |
| Let Hyperswitch tune auth-rate routing automatically | [Autopilot](autopilot.md) |
| See why a processor was selected | [Analytics And Decision Logs](analytics-and-decision-logs.md) |

## Strategy Types

Hyperswitch supports both merchant-defined routing and performance-based routing:

* **Rule-Based Routing:** Route payments using explicit business conditions such as payment method, amount, currency, country, card type, or customer context.
* **Volume-Based Routing:** Split traffic across processors by percentage for planned distribution or gradual rollout.
* **Auth-Rate Routing:** Use recent authorization performance to route most traffic to the best-performing processor while keeping a small exploration share.
* **Cost-Aware Routing:** Re-rank auth-rate results using processor cost and merchant margin, so a lower-cost processor can win only when expected value is better.
* **Least Cost Routing:** Route supported debit payments through the lowest-cost eligible debit network.
* **Default Fallback Routing:** Define the backup processor order when no routing rule applies or the selected processor is not eligible.

## How A Payment Is Routed

1. Hyperswitch checks which processors are eligible for the payment method, currency, country, and connector configuration.
2. The active routing strategy ranks or filters those processors.
3. Optional optimization layers, such as downtime elimination, cost-aware ranking, or debit network routing, refine the choice.
4. If the selected processor is not eligible or available, Hyperswitch uses Default Fallback Routing.
5. The decision is logged so your team can review the selected processor, routing approach, and outcome.

## Architecture Diagram

<figure><img src="../../../.gitbook/assets/image (141).png" alt=""><figcaption></figcaption></figure>

## Recommended Rollout

Start with Default Fallback Routing, then add Rule-Based or Volume-Based Routing for business controls. Use Auth-Rate Routing once multiple processors handle meaningful traffic for the same payment segment. Add Cost-Aware Routing only after cost coverage is available, and use A/B Testing before moving a new strategy to all traffic.

For self-hosted Hyperswitch deployments, see the [Self-Deployment Guide](self-deployment-guide.md).

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Self Deploy the Routing Engine</td><td><a href="../../../.gitbook/assets/image (35).png">image (35).png</a></td><td><a href="self-deployment-guide.md">self-deployment-guide.md</a></td></tr><tr><td>Using Auth Rate based Routing for Hyperswitch</td><td><a href="../../../.gitbook/assets/tryHyperswitch.jpg">tryHyperswitch.jpg</a></td><td><a href="auth-rate-based-routing.md">auth-rate-based-routing.md</a></td></tr></tbody></table>
