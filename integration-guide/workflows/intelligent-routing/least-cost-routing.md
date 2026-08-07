---
description: Optimize debit payment cost by routing through the lowest-cost eligible network
icon: hand-holding-dollar
metaLinks:
  alternates:
    - least-cost-routing.md
---

# Least Cost Routing

Least Cost Routing helps merchants reduce debit payment cost by selecting the most cost-efficient eligible debit network for a transaction. It is focused on debit network choice, while [Multi-Objective Routing](multi-objective-routing.md) focuses on processor-level cost and auth-rate tradeoffs.

## Prerequisites

To use Least Cost Routing in Hyperswitch, confirm:

* Connectors that support local debit network routing are configured.
* Debit card support is enabled.
* One or more local debit networks are enabled in both connector and Hyperswitch dashboards.
* The payment has the debit card and network data required to identify eligible local networks.

## Setup

1. Go to `Workflow` > `Routing` > `Least Cost Routing`.
2. Confirm the connector setup, debit card enablement, and local network configuration prerequisites.
3. Click `Enable` to activate Least Cost Routing.
4. Review the active routing configuration in the Hyperswitch Dashboard.

<figure><img src="../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

## Supported Configuration

| Item | Supported values |
| --- | --- |
| Geography | US |
| Payment method | Cards |
| Networks | Star, Pulse, NYCE, Accel |

## How It Works

For supported debit card payments, Hyperswitch checks the available card networks and eligible connector capabilities. It compares eligible global and local debit networks and selects the network with the lowest estimated cost.

Least Cost Routing can run as a standalone debit network routing strategy or alongside auth-rate routing in a hybrid setup, where Hyperswitch keeps processor performance in view while also selecting the debit network.

## Cost Computation

Hyperswitch estimates transaction cost using payment attributes such as amount, issuer, network, acquirer country, and merchant category.

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

The cost computation considers:

* MCC supplied by the merchant.
* Transaction amount.
* Card issuer bank.
* Co-badged card network data, when available.
* Global network and local network eligibility.
* Default cost values available in Hyperswitch when merchant-specific cost data is not available.
* Merchant-provided PSP-network contracts where those inputs are available.

When supported by the processor, Hyperswitch passes the selected debit network in the payment request.
