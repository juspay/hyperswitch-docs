---
icon: swap
---

# Smart Router for Payouts

The Hyperswitch Smart Router allows you to define logic for distributing payout traffic across multiple processors. This ensures redundancy, optimizes for cost, and manages transaction volumes programmatically.

> Note: Routing configurations for payout operations are isolated from payment operations. Modifying payout routing rules will not impact your payment routing logic and vice-versa.

For a conceptual deep dive into the routing engine, refer to the [Smart Router Overview](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/route-your-payout-transactions-using-smart-router).

#### Configuration Options

You can manage your routing logic via the [Hyperswitch Dashboard](https://app.hyperswitch.io) or the [Routing APIs](https://api-reference.hyperswitch.io/v1/routing/routing--list). The dashboard provides a visual interface for constructing and activating these rules.

#### Prerequisites

To utilize Smart Routing, you must have at least two payout processors integrated and active on your account. Follow the [Getting Started with Payouts](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/get-started-with-payouts) guide to add connectors.

### Setting Up Payout Routing

Access Routing Settings

Navigate to Workflow -> Payout Routing in your [Dashboard](https://app.hyperswitch.io).

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption><p>Head to Payout Routing</p></figcaption></figure>

Select a Routing Strategy

Hyperswitch supports three distinct formats for payout orchestration:

* [Volume-Based Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/volume-based-routing): Distribute a percentage of total payout traffic across multiple connectors.&#x20;
* [Rule-Based Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing): Create conditional logic (if/then) to route payouts based on specific attributes like currency, region, or method.&#x20;
* [Default Fallback Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/default-fallback-routing): Establish a static priority list. If a primary processor is unavailable, the system attempts the payout with the next processor in the sequence.&#x20;

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td></td><td>Volume Based Routing</td><td></td><td><a href="../../../.gitbook/assets/image (12).png">image (12).png</a></td></tr><tr><td></td><td>Rule Based Routing</td><td></td><td><a href="../../../.gitbook/assets/image (13).png">image (13).png</a></td></tr><tr><td></td><td>Default fallback Routing</td><td></td><td><a href="../../../.gitbook/assets/image (14).png">image (14).png</a></td></tr></tbody></table>

<figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption><p>View configured rules</p></figcaption></figure>

Manage and Activate Configurations

Once your rules are defined, you can manage them from the Payout Routing summary page.

* Activation: Only one routing configuration (Volume, Rule, or Fallback) can be active at any given time.
* Switching Rules: To change the active logic, select a saved configuration and click `Activate Configuration`.

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Activate routing rule</p></figcaption></figure>

Fallback Behavior: If no custom routing rule is activated, Hyperswitch will automatically process transactions based on the order defined in your Default Fallback Priority list.

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
