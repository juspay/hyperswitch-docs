---
description: Reduce processing cost while protecting authorization performance
icon: scale-balanced
---

# Cost-Aware Routing

Cost-Aware Routing helps merchants reduce payment processing cost without blindly sending traffic to the cheapest processor. It compares processor cost with authorization performance so the selected route protects both conversion and margin.

## What It Covers

| Capability | What it does |
| --- | --- |
| Multi-objective routing | Re-ranks eligible processors using authorization rate and estimated processing cost. |
| Cost ingestion | Learns processor costs from settlement reports, invoices, or merchant-provided overrides. |
| Debit network routing | Routes supported debit transactions through lower-cost eligible networks where available. |
| Cost savings analytics | Shows cost saved compared with the auth-rate-first route. |

## How Multi-Objective Routing Works

Auth-Rate Routing first identifies the best processor by recent authorization performance. Cost-aware routing then checks whether another eligible processor has better expected value after accounting for processing cost.

In simple terms:

```text
Expected value = authorization rate x net settlement value
net settlement value = transaction amount - processing cost
```

If a lower-cost processor has better expected value, Hyperswitch can promote it. If the auth-rate winner is still better, Hyperswitch keeps the auth-rate choice.

## What You Need Before Enabling

* At least two eligible processors for the same payment traffic.
* Auth-Rate Routing enabled or available for the same profile.
* Processor cost data from settlement reports, invoices, or manual fee overrides.
* A configured business margin where required for expected-value calculations.
* Cost coverage high enough to trust the result for the traffic you want to optimize.

{% hint style="info" %}
Screenshot placeholder: Cost-aware routing setup showing cost coverage, margin, and enablement control.
{% endhint %}

## Cost Data Ingestion

Cost data can come from:

* Settlement report uploads.
* Connector settlement webhooks or scheduled report polling.
* Invoice ingestion for fees not fully represented in settlement reports.
* Manual connector-level or segment-level fee overrides.

Use cost coverage before rollout. If a processor or segment does not have reliable cost data, cost-aware routing should fall back to the auth-rate decision for that case.

{% hint style="info" %}
Screenshot placeholder: Cost ingestion page showing report upload, column mapping, ingestion status, and cost coverage.
{% endhint %}

## Rollout Guidance

Start with analytics-only review, then run an [A/B test](ab-testing.md) between Auth-Rate Routing and Cost-Aware Routing. Move to a larger rollout only after the experiment shows cost savings without an unacceptable authorization-rate drop.

## What To Monitor

* Authorization rate.
* Cost saved.
* Processor share.
* Cost coverage.
* Cases where the auth-rate winner was kept.
* Cases where the cost-aware route was selected.

See [Analytics And Decision Logs](analytics-and-decision-logs.md) for the operational views.
