---
description: Open Banking payment methods
---

# Open Banking

In financial services, open banking allows for financial data to be shared between banks and third-party service providers through the use of application programming interfaces (APIs). Traditionally, banks have kept customer financial data within their own closed systems. Open banking allows customers to share their financial information securely and electronically with other banks or other authorized financial organizations such as payment providers, lenders and insurance companies. Open Banking is a framework for bank-to-bank transfers and other related bank services. They allow customers to push funds from their bank account to the merchant's while also allow for other services.
like bank account verification.
Open banking enables interoperable financial services through the use of APIs. These APIs facilitate the secure exchange of financial information between banks and authorised third-party providers. Unlike traditional banking services, which often operate within a closed environment, open banking decentralises financial services.

Open banking mandates standardised data formats and secure communication protocols. This creates a level playing field where third-party services can integrate with multiple banks under a common set of rules, regulations and technical standards.&#x20;

Open banking are used by merchants who want Open banking services like account verification, or bank-to-bank transfers. There are two major categories of Open banking solutions namely AIS (for account verification) and PIS (for payment Initiation, bank transfer like services).
A common use case for AIS is once time account verification for Direct debit payments. It is mostly used in the US markets for bank account verifications for bank debits.
The market for PIS however, is mostly constrained around UK/EU where the infrastructure for Open banking payments is more prominent.

**Steps to configure Open Banking AIS for direct debit payments:**

1. On the Hyperswitch dashboard, head to Connectors Tab
2. Head on to the PM Authentication Tab and select your Open Bnaking AIS connector
3. Add your credentials and you should be good to go.
4. Head on to Payment Processor and configure a Payment Processor, on select payment methods like Bank debits, you'll be asked to select a PM authentication connector to link with the payment Processor
5. Select a PM auth connector and and configure the rest of the steps.

**Payment flow for AIS based Bank debits:**

1. Customers select a Bank debit method on your checkout page
2. They are prompted to save the payment method with hyperswitch and your configured PM auth (open banking AIS) processor.
3. Customer is then asked to select their bank account in Processor SDK for saving it with the PM auth processor.
4. Hyperswitch connects with the PM auth processor to get the necessary information about their bank accounts and saves it.
5. The customer can now select their saved bank account at hyperswitch to make payment.

{% embed url="https://www.youtube.com/watch?v=T-UIaQWUQFY" %}

**Payment flow for PIS based Open banking payments:**

1. Customers select a Open banking PIS method on hyperswitch
2. They are prompted to save the payment method with hyperswitch and your configured PM auth (open banking AIS) processor.
3. Customer is then asked to select their bank account in Processor SDK for saving it with the PM auth processor.
4. Hyperswitch connects with the PM auth processor to get the necessary information about their bank accounts and saves it.
5. The customer can now select their saved bank account at hyperswitch to make payment.

{% embed url="https://www.youtube.com/watch?v=kBYx6VRM9xo" %}