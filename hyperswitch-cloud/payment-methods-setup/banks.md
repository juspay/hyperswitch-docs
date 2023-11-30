# 🏦 Banks

## Banks

Apart from cards (47%) and digital wallets (28%), bank transfer (9%) is the third most used payment instrument in the US. Banks as a payment method has several payment flows across the world and Hyperswitch provides support for integrating the below three common flows:

1. Bank Redirects
2. Bank Transfers
3. Bank Debits

|                             | Bank Debits                                                                                                                                                       | Bank Redirects                                                                                                                                                                                                                  | Bank Transfers                                                                                                                                                                |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                 | Bank debits pull funds directly from the customer’s bank account. Customers provide their bank account information and agree to a mandate to debit their account. | Bank redirects add a layer of verification to complete a bank debit payment. Instead of entering their bank account information, customers are redirected to provide their online banking credentials to authorize the payment. | Credit transfers allow customers to push funds from their bank account to the merchant's. Customers are provided with the bank account information they should send funds to. |
| Payment confirmation        | Delayed                                                                                                                                                           | Immediate                                                                                                                                                                                                                       | Delayed                                                                                                                                                                       |
| Payment Type                | Pull                                                                                                                                                              | Pull                                                                                                                                                                                                                            | Pull                                                                                                                                                                          |
| Supports recurring payments | Yes                                                                                                                                                               | No                                                                                                                                                                                                                              | No                                                                                                                                                                            |
| Supports refunds            | Yes                                                                                                                                                               | No                                                                                                                                                                                                                              | No                                                                                                                                                                            |
| Supports disputes           | Yes                                                                                                                                                               | No                                                                                                                                                                                                                              | No                                                                                                                                                                            |



## Bank Redirects

Bank Redirects are one of the most preferred options for paying online across the world. Due to their highly secure nature, bank redirects are used extensively in countries like Germany, Netherlands, Asia, LATAM, etc.

**How do Bank Redirects work?**

When customers select one of the Bank Redirects method on the checkout page, they are redirected to their online banking portal where they login and approve the transaction for which money is debited from their bank account. Post approval, they are redirected back to the shopping page. The transaction approval step might include two factor authentication in some bank redirects.

**Integrating Bank Redirects on Hyperswitch:**

To enable Bank redirect on Unified Checkout, you need to enable the payment methods on the Hyperswitch Dashboard. Hyperswitch SDKs intelligently display the supported Bank redirect option(s) based on the currency and the country of the customer.

For Bank Redirects, it is **mandatory** for the merchants to send the Currency and Country parameters in the CreatePaymentsIntent call.

```js
// Create a Payment with the shipping country and currency
app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      currency: "EUR",
      amount: 100,
      shipping: {
        address: {
          country: "EU",
        },
      },
    });
    // Send publishable key and PaymentIntent details to client
    res.send({
      clientSecret: paymentIntent.client_secret,
    });
  } catch (err) {
    return res.status(400).send({
      error: {
        message: err.message,
      },
    });
  }
});
```

Hyperswitch currently supports the following Bank Redirects:

| **Bank** **Redirects**      | **Supported Customer Countries**                                                                                                     | **Supported Currencies** |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| [Sofort](banks.md#giropay)  | Austria, Belgium, Czech Republic, France, Germany, Hungary, Italy, Netherlands, Poland, Slovakia, Spain, Switzerland, United Kingdom | EUR, CHF, GBP            |
| [Giropay](banks.md#giropay) | Germany                                                                                                                              | EUR                      |
| [iDEAL](banks.md#ideal)     | Netherlands                                                                                                                          | EUR                      |
| [EPS](banks.md#eps)         | Austria                                                                                                                              | EUR                      |

### Sofort

Sofort, also known as directEbanking, is one of the most popular bank redirect methods in Europe where customers can transfer money from their banking account online. In 2014, Sofort was acquired by Klarna and Sofort Direct Banking was also made available through Klarna as Klarna Pay Now which lets customers pay online for their purchases using a fast and easy method using their banking details.

### Giropay

Giropay is a bank redirect payment method used in Germany. Here, the customers are redirected to a giropay banking portal where they provide their bank account details and acceptance for the payment to be deducted from their bank account. For some banks, customers also undergo two factor authentication to approve the transaction.

Giropay payments are instantly confirmed as success or failure post which the customers are redirected to the merchant's page.

### iDEAL

iDEAL is a bank redirect payment method used in the Netherlands and accounts for more than 50% of online transactions. All major Dutch banks support iDEAL which is run by the Currence association comprising these banks.

During checkout, the customers select one of their Dutch banks that supports iDEAL and they are taken to their bank's respective page where they login and confirm the payment to be deducted from their bank account. For some banks, customers also undergo two factor authentication to approve the transaction.

iDEAL payments are instantly confirmed as success or failure post which the customers are redirected to the merchant's page.

### EPS

EPS (Electronic Payment Standard) is a bank redirect payment method used in Austria operated by the Austrian Bank Association 'Stunza'. It lets Austrian customers pay securely from their bank accounts to most online retailers.

During checkout, the customers select one of their Austrian banks that supports EPS and they are taken to their bank's respective page where they login and confirm the payment to be deducted from their bank account. For some banks, customers also undergo two factor authentication to approve the transaction.

EPS payments are instantly confirmed as success or failure post which the customers are redirected to the merchant's page.

## Bank Debits

Bank Debits enables merchants to directly pull funds from the customers' bank accounts once the customers provide authorization for the same. It is primarily used for recurring transactions/mandates and for large ticket transactions like rent, fees, etc.

Bank debits are delayed notification payment methods (it might take up to 2-7 days for the payment status to be updated).

**Payments Flow:**

a. Customer selects bank debit on the checkout page

b. They are shown a form to enter their bank details followed by a checkbox to authorize the merchant to debit their bank account later. This authorization from the customer is called mandate

c. The customers are notified about the mandate setup and every time funds are debited from their account

d. The merchant can opt for microdeposits (only on Stripe) or allow the customer to link their bank account in order to verify the authenticity of the bank details.

| **Bank** **Debits** | **Supported Customer Countries** | **Supported Currencies** |
| ------------------- | -------------------------------- | ------------------------ |
| ACH                 | United States                    | USD                      |
| SEPA                | EU                               | EUR                      |
| BACS                | UK                               | GBP                      |
| BECS                | Austria                          | AUD                      |

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

## Bank Transfers

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
