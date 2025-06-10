---
icon: swap
---

# Smart Router for Payouts

_Before continuing further, refer to_ [_this_](https://docs.hyperswitch.io/features/merchant-controls/smart-router) _comprehensive guide on Smart Router._

**Note: routing rules are distinct for payment and payout operations. Configuring one does not affect the other and vice-versa.**

## How to get started?

Routing rules can be configured using Hyperswitch's dashboard _(beta feature)_ or via APIs. We will be using Hyperswitch's dashboard as it provides a simple, intuitive UI for configuring these rules.

Dashboard - [https://app.hyperswitch.io](https://app.hyperswitch.io)

#### Pre-requisites

Make sure there are at least two or more payout processors integrated with your account. You can follow [this](https://docs.hyperswitch.io/features/payment-flows-and-management/payouts/get-started-with-payouts#how-to-get-started) guide for integrating a payout connector of your choice.

#### Steps for configuring routing rules for payouts

**Step 1 -** Head to _**Workflow -> Payout Routing**_

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption><p>Head to Payout Routing</p></figcaption></figure>

**Step 2 -** From here, you can select one of the three routing rule formats for creating a routing rule and follow one of the below guides for configuring your routing rule

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td></td><td>Volume Based Routing</td><td></td><td><a href="../../../.gitbook/assets/image (12).png">image (12).png</a></td></tr><tr><td></td><td>Rule Based Routing</td><td></td><td><a href="../../../.gitbook/assets/image (13).png">image (13).png</a></td></tr><tr><td></td><td>Default fallback Routing</td><td></td><td><a href="../../../.gitbook/assets/image (14).png">image (14).png</a></td></tr></tbody></table>

**Step 3 -** You can view the created routing rules at the main page

<figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption><p>View configured rules</p></figcaption></figure>

**Step 4 -** Only a single routing rule can be activated at a given time. For selecting a different rule, click on the rule and click `Activate Configuration`

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Activate routing rule</p></figcaption></figure>

**Step 5 -** If none of the rules are activated, the transaction is routed in the order listed in Default Fallback Priority

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
