---
description: Self-deploy the routing service used by Hyperswitch Intelligent Routing
icon: screwdriver-wrench
metaLinks:
  alternates:
    - self-deployment-guide.md
---

# Self-Deployment Guide

Self-hosted Hyperswitch deployments can run the routing service in their own infrastructure. Hyperswitch remains the payment orchestrator; the routing service is used by Hyperswitch to evaluate dynamic routing decisions.

{% hint style="info" %}
Hosted Hyperswitch merchants usually do not need this setup. Use this guide only when you are running Hyperswitch yourself.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

## Run The Routing Service

Clone the routing service repository:

```bash
git clone https://github.com/juspay/decision-engine.git
cd decision-engine
```

## Install Docker

Make sure Docker is installed on your system.

* Mac: [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
* Windows: [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
* Linux: [Docker Engine for Linux](https://docs.docker.com/desktop/setup/install/linux/)

Start the API with Docker Compose:

```bash
docker compose --profile postgres-ghcr up -d
```

For the API, dashboard, and local docs together:

```bash
docker compose --profile dashboard-postgres-ghcr up -d
```

## Repository Make Targets

You can also use the repository Make targets:

```bash
make init-pg-ghcr
make run-pg-ghcr
```

Legacy aliases are also available:

```bash
make init
make run
```

The init targets start the backing services, apply database setup, and load routing configuration from the repository config files. The run targets start only the routing API container for an already initialized setup.

Verify the service:

```bash
curl http://localhost:8080/health
```

Plan for approximately 2 GB of disk space. After the service starts, refer to the [Hyperswitch API reference](https://api-reference.hyperswitch.io/) for the payment APIs that use routing.

## Connect With Hyperswitch

Configure the routing service URL in Hyperswitch:

```toml
[open_router]
dynamic_routing_enabled = true
static_routing_enabled = true
url = "http://localhost:8080"
```

When you are ready for Hyperswitch to use the external routing service, set the routing result source to `decision_engine`. Keep it as `hyperswitch_routing` while validating or migrating.

## How Hyperswitch Uses It

Hyperswitch calls the routing service during the payment flow, receives the selected processor, performs eligibility and fallback checks, and then continues the payment with the chosen connector. After the payment outcome is known, Hyperswitch sends feedback so auth-rate routing and analytics stay accurate.

## Production Checklist

Before sending live traffic, confirm:

* Redis and database persistence are configured.
* Health and readiness checks are monitored.
* Default Fallback Routing is configured in Hyperswitch.
* Payment outcomes are being reported for successful and failed attempts.
* Routing decisions are visible in Hyperswitch analytics or logs.
