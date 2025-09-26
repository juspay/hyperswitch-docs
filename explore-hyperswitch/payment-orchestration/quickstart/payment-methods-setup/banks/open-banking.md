---
description: >-
  Account Verification and Payment Initiation Services using open banking
  providers
---

# Open Banking

### Overview

Open banking enables the sharing of financial data between banks and third-party providers via APIs.  It serves as a framework for services like bank-to-bank transfers and account verification, allowing customers to transfer funds to merchants directly from their bank accounts.

### Open Banking Use-Cases

#### Account Information Service

Account Information Services (AIS) in open banking allow authorized third-party providers to access and retrieve financial data from a user's bank account, with the customer's consent. This information can include transaction history, account balances, and spending patterns.

Regional Usage:

* **U.S.**: AIS is mostly employed for one-time account verification, especially in direct debit payments.
* **UK/EU**: AIS services are more widely adopted for a variety of use cases, like financial management, due to the robust open banking frameworks under PSD2.

#### Payment Initiation Service

Payment Initiation Services (PIS) in open banking allow authorized third-party providers to initiate payments directly from a customer's bank account, with their consent, without the need for traditional intermediaries like credit or debit card networks. PIS provides an alternative to conventional payment methods, making bank-to-bank transfers more seamless and efficient.

Regional Usage:

* **UK/EU**: PIS is mostly dominant across Europe. Adoption in other regions, such as the U.S., is slower due to less-developed open banking frameworks.

### **Steps to configure Account Verification for bank debits**

1. On the Hyperswitch dashboard, head to Connectors Tab
2. Head on to the PM Authentication Tab and select your Open Banking AIS connector
3. Add your credentials and you should be good to go.
4. Head on to Payment Processor and configure a Payment Processor, on select payment methods like Bank debits, you'll be asked to select a PM authentication connector to link with the payment Processor&#x20;
5. Select a existing PM auth connector (that you have already configured) and proceed with the rest of the steps.

### **Steps to configure Payment Initiation (via Plaid)**

1. On the Hyperswitch dashboard, head to Connectors Tab
2. Head on to the Payment Processor Tab and select Plaid.
3. Enter your client\_id and secret and select relevant payment methods.
4. Merchant's Bank account data needs to be provided in order to initiate transfer of funds to the merchant account. \
   Under the dropdown Open Banking Recipient Data,\
   One of the underlying options should be selected - \
   \- bank scheme, in which merchant's recipient account details needs to be provided (either sepa or   bacs)\
   \- Connector Recipient Id, in case the merchant already has a recipient id created with the connector
5. For Payment Initiation services, the payment method selected should be Open banking with payment method type as Open Banking PIS
6. Configure the rest and you should be good to go.

### **Payment flow for AIS based Bank debits:**

1. Customers select a Bank debit method on your checkout page
2. They are prompted to save the payment method with hyperswitch and your configured PM auth (open banking AIS) processor.
3. Customer is then asked to select their bank account in Processor SDK for saving it with the PM auth processor.
4. Hyperswitch connects with the PM auth processor to get the necessary information about their bank accounts and saves it.
5. The customer can now select their saved bank account at hyperswitch to make payment.

{% embed url="https://www.youtube.com/watch?v=T-UIaQWUQFY" %}

### **Payment flow for PIS based Open banking payments:**

1. Customers select a Open banking PIS method on hyperswitch checkout.
2. Customer is then asked to select their bank account in Processor SDK for authorizing the payment.
3. Once the customer authorizes the payment via Processor SDK, hyperswitch does a sync call with the Processor to update the status of the payment and displays the same to the customer.

{% embed url="https://www.youtube.com/watch?v=kBYx6VRM9xo" %}

### **FAQ**

1. Are there any other Open banking processors apart from Plaid? \
   \- Yes, Processors like TrueLayer and Tink provide the same services as Plaid. However,   Hyperswitch currently only supports an integration with Plaid. If there are other providers that you want to use please raise a Github Issue.
2. Any extra configuration required for Android or IOS platform?\
   \- If using Plaid, the android package name (for android) and redirect uri (Universal Link for your application) (for IOS) needs to be passed from the merchant SDK while invoking the Hyperswitch SDK.&#x20;
3. In which all geographies can I use open banking?
   1. Account Verification is currently available to verify bank accounts for direct debits via ACH, SEPA and BACS
   2. Payment Initiation is currently available for the UK and EU markets
