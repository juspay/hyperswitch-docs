---
description: Self-deploy Decision Engine and connect it to Hyperswitch or an existing payment orchestrator
icon: screwdriver-wrench
metaLinks:
  alternates:
    - self-deployment-guide.md
---

# Self-Deployment Guide

Self-deploy Decision Engine when you want to run intelligent routing in your own infrastructure, either with self-hosted Hyperswitch or with an existing payment orchestrator.

{% hint style="info" %}
Hosted Hyperswitch merchants usually do not need to self-deploy Decision Engine. Use this guide for self-hosted or custom-orchestrator setups.
{% endhint %}

## Run Decision Engine

Clone the repository:

```bash
git clone https://github.com/juspay/decision-engine.git
cd decision-engine
```

Start the API with Docker Compose:

```bash
docker compose --profile postgres-ghcr up -d
```

Verify the service:

```bash
curl http://localhost:8080/health
```

For the API, dashboard, and docs together:

```bash
docker compose --profile dashboard-postgres-ghcr up -d
```

Default local URLs:

| Service | URL |
| --- | --- |
| Decision Engine API | `http://localhost:8080` |
| Decision Engine dashboard | `http://localhost:8081/dashboard/` |
| Decision Engine docs | `http://localhost:8081/introduction` |

## Connect With Hyperswitch

For self-hosted Hyperswitch, configure the Decision Engine URL in Hyperswitch:

```toml
[open_router]
dynamic_routing_enabled = true
static_routing_enabled = true
url = "http://localhost:8080"
```

When you are ready to use Decision Engine results for routing, set the routing result source to `decision_engine`. Keep it as `hyperswitch_routing` while validating or migrating.

{% hint style="info" %}
Screenshot placeholder: Self-hosted architecture diagram showing Hyperswitch, Decision Engine, Redis, database, and processors.
{% endhint %}

## Connect With An Existing Orchestrator

If you are not using Hyperswitch as the payment orchestrator:

1. Call Decision Engine before making the processor authorization call.
2. Pass the eligible processor list and payment attributes.
3. Use the returned processor for the payment attempt.
4. Send the final authorization outcome back to Decision Engine so future scoring remains accurate.

The core API loop is:

| Step | Endpoint |
| --- | --- |
| Get routing decision | `POST /decide-gateway` |
| Send payment outcome | `POST /update-gateway-score` |

## Production Checklist

Before sending live traffic, confirm:

* Redis and database persistence are configured.
* Health and readiness checks are monitored.
* Your fallback route is defined in the orchestrator.
* Score feedback is sent for successful and failed attempts.
* Routing decisions are visible in logs or analytics.
