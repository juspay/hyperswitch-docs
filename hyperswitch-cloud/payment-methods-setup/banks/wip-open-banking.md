---
description: >-
  Account Verification and Payment Initiation Services using open banking
  providers
---

# \[WIP] Open Banking

### Overview

Open banking enables the sharing of financial data between banks and third-party providers via APIs.  It serves as a framework for services like bank-to-bank transfers and account verification, allowing customers to transfer funds to merchants directly from their bank accounts.

### Open Banking Use-Cases

#### Account Information Service



#### Payment Initiation Service



### **Steps to configure Account Verification for bank debits**

1. On the Hyperswitch dashboard, head to Connectors Tab
2. Head on to the PM Authentication Tab and select your Open Banking AIS connector
3. Add your credentials and you should be good to go.
4. Head on to Payment Processor and configure a Payment Processor, on select payment methods like Bank debits, you'll be asked to select a PM authentication connector to link with the payment Processor
5. Select a PM auth connector and and configure the rest of the steps.

### **Steps to configure Payment Initiation (via Plaid)**

1.

### **Payment flow for AIS based Bank debits:**

1. Customers select a Bank debit method on your checkout page
2. They are prompted to save the payment method with hyperswitch and your configured PM auth (open banking AIS) processor.
3. Customer is then asked to select their bank account in Processor SDK for saving it with the PM auth processor.
4. Hyperswitch connects with the PM auth processor to get the necessary information about their bank accounts and saves it.
5. The customer can now select their saved bank account at hyperswitch to make payment.

{% embed url="https://www.youtube.com/watch?v=T-UIaQWUQFY" %}

### **Payment flow for PIS based Open banking payments:**

1. Customers select a Open banking PIS method on hyperswitch
2. They are prompted to save the payment method with hyperswitch and your configured PM auth (open banking AIS) processor.
3. Customer is then asked to select their bank account in Processor SDK for saving it with the PM auth processor.
4. Hyperswitch connects with the PM auth processor to get the necessary information about their bank accounts and saves it.
5. The customer can now select their saved bank account at hyperswitch to make payment.

{% embed url="https://www.youtube.com/watch?v=kBYx6VRM9xo" %}
