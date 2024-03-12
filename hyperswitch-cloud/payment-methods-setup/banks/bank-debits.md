---
description: Bank Debits payment method
---

# Bank Debits

{% hint style="info" %}
Bank debits pull funds directly from the customer’s bank account. Customers provide their bank account information and agree to a mandate to debit their account at specified intervals and amount.
{% endhint %}



Bank Debits enables merchants to directly pull funds from the customers' bank accounts once the customers provide authorization for the same. It is primarily used for recurring transactions/mandates and for large ticket transactions like rent, fees, etc.

Bank debits are delayed notification payment methods (it might take up to 2-7 days for the payment status to be updated).

## **Payments Flow**

a. Customer selects bank debit on the checkout page

b. They are shown a form to enter their bank details followed by a checkbox to authorize the merchant to debit their bank account later. This authorization from the customer is called mandate

c. The customers are notified about the mandate setup and every time funds are debited from their account

d. The merchant can opt for microdeposits (only on Stripe) or allow the customer to link their bank account in order to verify the authenticity of the bank details.

| **Bank** **Debits** | **Supported Customer Countries** | **Supported Currencies** |
| ------------------- | -------------------------------- | ------------------------ |
| ACH                 | United States                    | USD                      |
| SEPA                | EU                               | EUR                      |
| BACS                | UK                               | GBP                      |
| BECS                | Australia                        | AUD                      |

Hyperswitch currently supports the following Bank Direct Debits:

### ACH

US based Bank Debit payment method that is extensively used for recurring payments use cases where payments from customers with US bank accounts are debited through the Automated Clearing House (ACH) payments system operated by Nacha.

Since ACH Direct Debit is a delayed notification payment method, it can take up to 4 business days for the payment status to be updated.

### SEPA

SEPA allows direct bank debits payment for EUR denominated bank accounts in the SEPA region (list of countries). The customer accepts a mandate that authorizes the merchant to debit the account.

Since SEPA Direct Debit is a delayed notification payment method, it can take upto 14 business days for the payment status to be updated after initiating a debit from the customer’s account.

### BACS

BACS is a popular bank debit payment method for customers with UK bank accounts where the customers authorize a mandate for debit through the Bankers' Automated Clearing Services (BACS).

Since BACS Direct Debit is a delayed notification payment method, it can take upto 6 business days for the payment status to be updated after initiating a debit from the customer’s account.

### BECS

BECS is a bank debit that is used for recurring payments for customers with Australian bank accounts who authorize a mandate for debit through the Bulk Electronic Clearing System (BECS).

Since BECS Direct Debit is a delayed notification payment method, it can take upto 3 business days for the payment status to be updated after initiating a debit from the customer’s account.
