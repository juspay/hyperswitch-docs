---
description: >-
  Use Hyperswitch's unified Disputes module to track and manage disputes across
  multiple processors
---

# 🚩 Disputes/Chargebacks Management

A dispute/chargeback occurs when a customer contacts their payment method issuer (card issuer/bank/wallet) to question or challenge a particular transaction so that the payment can be reversed.&#x20;

The merchants receive notifications from their payment processor when a dispute is raised by their customers against a payment made at their site.

After receiving a dispute notification, merchants are given an opportunity to provide evidence or documentation to support their side of the transaction. The resolution can involve a chargeback, where the funds are reversed from the merchant's account and returned to the cardholder, or a decision in favor of the merchant if the dispute is deemed invalid.

Each processor has their own standards or processes around how they notify about disputes and how merchants can challenge/accept them and thus it becomes cumbersome for a merchant using multiple processors to manage disputes across different processors on their own.

Hyperswitch unifies all the dispute notifications from all your different processors and makes it easier for you to track, accept and as well as challenge them by uploading evidences across different processors from one place.



**Disputes lifecycle on Hyperswitch:**

Hyperswitch's unified disputes module uses the following stages and statuses to track your disputes:







dispute\_stage

<table><thead><tr><th width="184">dispute_stage</th><th>description</th></tr></thead><tbody><tr><td>pre_dispute</td><td></td></tr><tr><td>dispute</td><td></td></tr><tr><td>pre-arbitration</td><td></td></tr></tbody></table>

Pre-dispute



Dispute



Pre-Arbitration

`dispute_opened`,`dispute_expired`,`dispute_accepted`,`dispute_cancelled`,`dispute_challenged`,`dispute_won`,`dispute_lost`

