---
description: >-
  Use Hyperswitch's unified Disputes module to track and manage disputes across
  multiple processors
---

# 🚩 Disputes/Chargebacks Management

A dispute occurs when a customer contacts their payment method issuer (card issuer/bank/wallet) to question or challenge a particular transaction so that the payment can be reversed.&#x20;

{% hint style="info" %}
When a card payment is reversed, and the processor debits the merchant's account, it's termed a 'chargeback.' Hyperswitch uses the term 'Disputes' interchangeably to refer to 'Chargebacks' in the context of card payments.
{% endhint %}

The merchants receive notifications from their payment processor when a dispute is raised by their customers against a payment made at their site.

After receiving a dispute notification, merchants are given an opportunity to provide evidence or documentation to support their side of the transaction. The resolution can involve a chargeback, where the funds are reversed from the merchant's account and returned to the cardholder, or a decision in favor of the merchant if the dispute is deemed invalid.

Each processor has their own standards or processes around how they notify about disputes and how merchants can challenge/accept them and thus it becomes cumbersome for a merchant using multiple processors to manage disputes across different processors on their own.

Hyperswitch unifies all the dispute notifications from all your different processors and makes it easier for you to track, accept and as well as challenge them by uploading evidences across different processors from one place.



## Disputes Lifecycle on Hyperswitch

Hyperswitch's unified disputes module uses the following stages and statuses to track your disputes:

<div data-full-width="true">

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

</div>

### Pre-Dispute stage

Some payment method issuers start an investigation before creating a dispute on a transaction challenged by a customer. Such transactions are grouped under the 'Pre-Dispute' stage and these transactions could go through the following states:

<table><thead><tr><th width="192">dispute_state</th><th>description</th></tr></thead><tbody><tr><td>Opened</td><td>Occurs when an investigation is opened and a dispute is created on Hyperswitch</td></tr><tr><td>Challenged</td><td>Occurs when a merchant uploads evidence to support the original transaction</td></tr><tr><td>Expired</td><td>Occurs when a merchant doesn't respond in time or if the investigation is closed</td></tr></tbody></table>

Visa or Mastercard do not open an investigation before creating a dispute and so most of your transactions would skip the Pre-Dispute stage

### Dispute stage

In most cases, the processors directly debit your account while reversing the payment made by a customer after a transaction has been challenged.&#x20;

For transactions that go through 'Pre-Dispute' stage, they will end up moving to 'Dispute' stage if the merchant's evidence was deemed not satisfactory.

<table><thead><tr><th width="155">dispute_state</th><th>description</th></tr></thead><tbody><tr><td>Opened</td><td>Occurs when a dispute is opened and your processor has debited your account</td></tr><tr><td>Challenged</td><td>Occurs when a merchant uploads an evidence to support their case</td></tr><tr><td>Expired</td><td>Occurs when a merchant doesn't respond in time interval before which an issuer expects a response after the dispute was opened</td></tr><tr><td>Cancelled</td><td>Occurs when a customer withdraws their challenge </td></tr><tr><td>Accepted</td><td>Occurs when a merchant accepts a dispute as valid</td></tr><tr><td>Won</td><td>Occurs when the merchant's challenge was accepted successfully. Known as 'chargeback reversal' in cases of card payments</td></tr><tr><td>Lost</td><td>Occurs when a merchant's challenge was deemed not satisfctory</td></tr></tbody></table>

### Pre-Arbitration stage

Even after a successful dispute challenge, a payment method issuer might deem the evidence 'not satisfactory' and raise another review appeal. Such payments transition to 'Pre-Arbitration' stage.



<table><thead><tr><th width="167">dispute_state</th><th>description</th></tr></thead><tbody><tr><td>Opened</td><td>Occurs when the issuer opens a review appeal after deeming the evidence unsatisfactory</td></tr><tr><td>Won</td><td>Occurs when the merchant is successful in the pre-arbitration appeal prcoess</td></tr><tr><td>Lost</td><td> Occurs when the merchant loses during the pre-arbitration appeal. Also, known as 'second_chargeback'</td></tr></tbody></table>



## #Managing Disputes on Hyperswitch

Hyperswitch communicates to your server whenever a dispute is raised or whenever there is a change in the existing disputes' statuses by sending you a Dispute webhook that has one of the following event\_type:

`dispute_opened`,`dispute_expired`,`dispute_accepted`,`dispute_cancelled`,`dispute_challenged`,`dispute_won`,`dispute_lost`

