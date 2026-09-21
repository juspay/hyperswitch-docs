---
description: >-
  Configure volume-based, rule-based, or fallback routing strategies to
  distribute payout traffic across multiple processors using the Hyperswitch
  Smart Router.
icon: swap
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/connectors/payouts/route-your-payout-transactions-using-smart-router
---

<!-- truth manifest; hyperswitch 6fd72e5e6653326acaaf19b5f6aa76a524ff202e; spec api-reference/v1/openapi_spec_v1.json@6fd72e5e6653326acaaf19b5f6aa76a524ff202e
     symbols: make_dsl_input_for_payouts = crates/router/src/core/payments/routing.rs:165-230
     symbols: PaymentMethodInput.payment_method = crates/router/src/core/payments/routing.rs:199-204
     symbols: PaymentMethodInput.payment_method_type = crates/router/src/core/payments/routing.rs:204-221
     symbols: payout routing algorithm = crates/router/src/core/routing.rs:1739-1741
     checked: 2026-09-21 -->

# Smart Router for Payouts

The Juspay Hyperswitch Smart Router allows you to define logic for distributing payout traffic across multiple processors. This ensures redundancy, optimizes for cost, and manages transaction volumes programmatically.

> **Note:** Routing configurations for payout operations are isolated from payment operations. Modifying payout routing rules will not impact your payment routing logic and vice-versa.

For a conceptual deep dive into the routing engine, refer to the [Smart Router Overview](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/route-your-payout-transactions-using-smart-router).

### Prerequisites

Before creating a routing rule, confirm payouts are enabled for your account and integrate at least two active payout processors. Follow [Payout features](README.md) to configure them.

### Configuration Options

You can manage your routing logic via the [Hyperswitch Dashboard](https://app.hyperswitch.io) or the [Routing APIs](https://api-reference.hyperswitch.io/v1/routing/routing--list). The dashboard provides a visual interface for constructing and activating these rules.

### Setting Up Payout Routing

#### Access Routing Settings

Navigate to Workflow -> Payout Routing in your [Dashboard](https://app.hyperswitch.io).

<figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption><p>Head to Payout Routing</p></figcaption></figure>

#### Select a Routing Strategy

Hyperswitch supports three distinct formats for payout orchestration:

* [Volume-Based Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/volume-based-routing): Distribute a percentage of total payout traffic across multiple connectors.
* [Rule-Based Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing): Create conditional logic to route payouts by supported attributes. Payout rules use the same normalized routing field names as payment rules: `payment_method` and `payment_method_type`. For payouts, `payment_method` is derived from the request's `payout_type`, and `payment_method_type` is derived from `payout_method_data`. See [`make_dsl_input_for_payouts`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/router/src/core/payments/routing.rs#L165-L230).
* [Default Fallback Routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/default-fallback-routing): Establish a static priority list. If a primary processor is unavailable, the system attempts the payout with the next processor in the sequence.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td></td><td>Volume Based Routing</td><td></td><td><a href="../../../.gitbook/assets/image (71).png">image (71).png</a></td></tr><tr><td></td><td>Rule Based Routing</td><td></td><td><a href="../../../.gitbook/assets/image (72).png">image (72).png</a></td></tr><tr><td></td><td>Default fallback Routing</td><td></td><td><a href="../../../.gitbook/assets/image (73).png">image (73).png</a></td></tr></tbody></table>

<figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption><p>View configured rules</p></figcaption></figure>

#### Manage and Activate Configurations

Once your rules are defined, you can manage them from the Payout Routing summary page.

* Activation: Only one routing configuration (Volume, Rule, or Fallback) can be active at any given time.
* Switching Rules: To change the active logic, select a saved configuration and click `Activate Configuration`.

<figure><img src="../../../.gitbook/assets/image (75).png" alt=""><figcaption><p>Activate routing rule</p></figcaption></figure>

Fallback Behavior: If no custom routing rule is activated, Hyperswitch will automatically process transactions based on the order defined in your Default Fallback Priority list.

<figure><img src="../../../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>
