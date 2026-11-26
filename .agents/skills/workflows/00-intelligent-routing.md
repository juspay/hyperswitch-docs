---
name: hyperswitch-docs-intelligent-routing
description: Use this skill when the user asks about "intelligent routing in Hyperswitch", "auth rate based routing", "least cost routing", "volume based routing", "rule based routing", "smart routing setup", "Multi-Armed Bandit routing", "how does Hyperswitch choose a connector", "routing engine", "self-deploy routing", "routing configuration in dashboard", or needs to understand or configure Hyperswitch's routing strategies.
version: 1.0.0
tags: [hyperswitch, docs, routing, intelligent-routing, cost-optimization, auth-rate]
---

# Intelligent Routing

## Overview

The Hyperswitch Intelligent Routing module dynamically selects the optimal payment processor for every transaction to maximise authorisation rates and minimise processing cost. It sits between your payment request and the connector layer, applying configurable strategies in real-time.

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/README.md`

---

## Routing Strategies

### 1. Auth Rate Based Routing

Tracks real-time authorisation success rates per connector at a granular level (payment method, card network, amount range, currency, authentication type) and uses a **Multi-Armed Bandit** model to optimise routing.

- **Exploration**: Small % of traffic tests all connectors continuously
- **Exploitation**: Majority of traffic routes to best-performing connector

Configuration: Dashboard → Workflows → Intelligent Routing → Auth Rate Based

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing.md`

### 2. Least Cost Routing

Routes each transaction to the cheapest available network, using back-of-card network data and processor compatibility.

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/least-cost-routing.md`

### 3. Volume Based Routing

Distributes payments across connectors by percentage to meet contractual volume commitments or A/B test processors.

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/volume-based-routing.md`

### 4. Rule Based Routing

Configures explicit routing rules based on payment attributes (amount, currency, card BIN, country, payment method).

Example rules:
- `amount > 50000 AND currency = EUR` → Adyen
- `card.country = IN` → Razorpay
- `payment_method = bank_redirect` → Mollie

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/rule-based-routing.md`

### 5. Default Fallback Routing

Defines a priority-ordered fallback list used when other routing strategies don't match.

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/default-fallback-routing.md`

---

## Routing Configuration in Dashboard

1. Navigate to **Dashboard → Workflows → Intelligent Routing**
2. Select **Create New Algorithm**
3. Choose strategy: Auth Rate, Least Cost, Volume, Rule-Based, or Fallback
4. Configure connectors and rules
5. Click **Activate** — becomes the live routing algorithm immediately

Only one algorithm is active at a time. Previous configurations are archived and can be reactivated.

---

## Self-Deploy the Routing Engine

For merchants who need the routing engine in their own infrastructure:

**Doc reference:** `explore-hyperswitch/workflows/intelligent-routing/self-deployment-guide.md`

The routing engine is open-source and deployable as a standalone service:

```bash
git clone https://github.com/juspay/euclid
cd euclid
docker-compose up
```

Configure the endpoint in Hyperswitch settings to point to your self-hosted instance.

---

## Smart Retries

When a payment fails, Smart Retries automatically retries with the next available connector without requiring the customer to re-enter details.

- **Doc reference:** `explore-hyperswitch/workflows/smart-retries/README.md`
- Processor error code mapping: `explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping.md`
- 3DS step-up retries (retry without 3DS after a 3DS failure): `explore-hyperswitch/workflows/smart-retries/3ds-step-up-retries.md`
- Manual/user-triggered retries: `explore-hyperswitch/workflows/smart-retries/manual-user-triggered-retries.md`

---

## Production Tips

- Start with **Default Fallback Routing** to establish a baseline. Switch to Auth Rate Based once you have sufficient transaction volume (~500+ transactions across connectors).
- Auth Rate routing tracks success rates at the granularity of payment method + card network + currency. For low-volume merchants, coarser granularity may be more reliable.
- **Least Cost Routing** requires connectors to provide interchange data. Verify this is available with your connectors before enabling.
- Rule-Based Routing takes precedence over dynamic strategies — use it for hard requirements (compliance, currency-specific processors) and let dynamic routing handle the rest.
- Monitor routing decisions in Dashboard → Analytics → Routing Breakdown.
