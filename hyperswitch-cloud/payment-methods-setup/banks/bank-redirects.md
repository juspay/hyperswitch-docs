---
description: Bank Redirects payment methods
---

# Bank Redirects

{% hint style="info" %}
Bank redirects will redirect the user to the respective bank's payment page to complete a debit payment.
{% endhint %}



Bank Redirects are one of the most preferred options for paying online across the world. Due to their highly secure nature, bank redirects are used extensively in countries like Germany, Netherlands, Asia, LATAM, etc.

### **How do Bank Redirects work?**

When customers select one of the Bank Redirects method on the checkout page, they are redirected to their online banking portal where they login and approve the transaction for which money is debited from their bank account. Post approval, they are redirected back to the shopping page. The transaction approval step might include two factor authentication in some bank redirects.

### **Integrating Bank Redirects on Hyperswitch:**

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

| **Bank** **Redirects**               | **Supported Customer Countries**                                                                                                     | **Supported Currencies** |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| [Sofort](bank-redirects.md#giropay)  | Austria, Belgium, Czech Republic, France, Germany, Hungary, Italy, Netherlands, Poland, Slovakia, Spain, Switzerland, United Kingdom | EUR, CHF, GBP            |
| [Giropay](bank-redirects.md#giropay) | Germany                                                                                                                              | EUR                      |
| [iDEAL](bank-redirects.md#ideal)     | Netherlands                                                                                                                          | EUR                      |
| [EPS](bank-redirects.md#eps)         | Austria                                                                                                                              | EUR                      |

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
