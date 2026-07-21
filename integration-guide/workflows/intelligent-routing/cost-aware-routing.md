---
description: Reduce processing cost while protecting authorization performance
icon: scale-balanced
---

# Cost-Aware Routing

Cost-Aware Routing helps merchants reduce payment processing cost without blindly sending traffic to the cheapest processor. It runs as a post-step on Auth-Rate Routing. Hyperswitch first finds the best processor by recent authorization performance, then checks whether another eligible processor has better expected value after cost and margin are considered.

## What It Covers

| Capability | What it does |
| --- | --- |
| Cost-aware processor ranking | Re-ranks auth-rate results using processor cost, authorization rate, and merchant margin. |
| Cost data ingestion | Learns actual processor fees from settlement reports, invoices, and merchant-provided overrides. |
| Debit network routing | Routes supported debit transactions through lower-cost eligible networks where available. See [Least Cost Routing](least-cost-routing.md). |
| Cost savings analytics | Shows cost saved compared with the auth-rate-first route. |

## How Cost-Aware Ranking Works

Hyperswitch ranks processors that have usable cost data by expected value:

```txt
Expected value = authorization rate x settlement value
settlement value = transaction amount - processing cost
```

If a lower-cost processor has strictly better expected value than the auth-rate winner, Hyperswitch can promote it and reorder the fallback list by expected value. If the auth-rate winner is still best, Hyperswitch keeps the auth-rate decision.

Cost-aware ranking does not tune auth-rate scores. It uses the scores that Auth-Rate Routing already produced. Exploration traffic can continue to follow the auth-rate path so the scoring model keeps fresh data.

## What You Need Before Enabling

* At least two eligible processors for the same payment traffic.
* Auth-Rate Routing enabled or available for the same profile.
* Processor cost data from reports, invoices, or fee overrides.
* A configured margin, used as the auth-rate versus cost tradeoff.
* Cost coverage high enough to trust the result for the traffic you want to optimize.

## Cost Data Ingestion

Cost data can reach Hyperswitch through multiple paths:

* Connector settlement report webhooks.
* Scheduled polling from connector reporting APIs.
* Manual settlement report uploads for testing or backfills.
* Invoice uploads for recurring, periodic, or flat fees that are not fully visible in settlement reports.
* Manual fee overrides at connector or segment level.

The cost model is fitted at a granular segment level, such as connector, card network, card variant, funding type, issuer country, currency, and interchange category. The cost coverage view tells you how much settled volume has a trustworthy cost estimate. Traffic without reliable cost data should stay on the auth-rate decision.

<figure><img src="../../../.gitbook/assets/routing-cost-ingestion.png" alt="Cost ingestion page"><figcaption></figcaption></figure>

## Rollout Guidance

Start with cost ingestion and coverage review. Then run an [A/B test](ab-testing.md) between Auth-Rate Routing and Cost-Aware Routing. Move to a larger rollout only after the experiment shows cost savings without an unacceptable authorization-rate drop.

## What To Monitor

* Authorization rate.
* Cost saved.
* Processor share.
* Cost coverage.
* Decisions where cost-aware ranking promoted a lower-cost processor.
* Decisions where the auth-rate winner was retained.
* Segments with thin or unreliable cost coverage.

See [Analytics And Decision Logs](analytics-and-decision-logs.md) for the operational views.
