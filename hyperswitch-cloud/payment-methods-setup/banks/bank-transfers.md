---
description: Bank Transfer payment methods
---

# Bank Transfers

{% hint style="info" %}
Bank transfers allow customers to push funds from their bank account to the merchant's.&#x20;
{% endhint %}

Bank Transfers are a popular way of transmitting money between different bank accounts and they are popular in US, EU and few Asian and LATAM countries. They are primarily used by businesses for accepting large payments from other businesses. Bank transfers are also used by consumers in certain countries as a preferred method for transferring money to others and while transacting online.

**Payment flow in Bank Transfers:**

1. Customers select a Bank Transfer method on your checkout page
2. You request Hyperswitch to initiate a Bank Transfer payment
3. Hyperswitch connects to one of your preferred payment processors for Bank transfers to initiate Bank transfer. Then, Hyperswitch shares the processor’s response which contains Virtual bank account details and instructions for the customers to transfer money and complete the payment
4. Customers instruct their bank through in-person visit/phone/website/app to transfer money to the account number mentioned in the instructions in the above step. It takes up to 5 days for the transaction to be settled
5. After the customer’s bank transfers the money, the processor notifies Hyperswitch of the transaction’s status, following which Hyperswitch notifies your server through Webhooks.

Hyperswitch supports the following Bank Transfers:

* ACH Bank Transfer in US
* SEPA Bank Transfer in EU
* BACS Bank Transfer in UK
* Multibanco in EU (Portugal)
* All Indonesian bank transfers
