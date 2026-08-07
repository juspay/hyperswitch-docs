---
description: Bank Redirects payment methods
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/banks/bank-redirects
---

# Bank Redirects

{% hint style="info" %}
Bank redirects will redirect the user to the respective bank's payment page to complete a debit payment.
{% endhint %}

Bank Redirects are one of the most preferred options for paying online across the world. Due to their highly secure nature, bank redirects are used extensively in countries like Germany, Netherlands, Asia, LATAM, etc.

### How do Bank Redirects work?

When customers select one of the Bank Redirects method on the checkout page, they are redirected to their online banking portal where they login and approve the transaction for which money is debited from their bank account. Post approval, they are redirected back to the shopping page. The transaction approval step might include two factor authentication in some bank redirects.

### Integrating Bank Redirects on Juspay Hyperswitch

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

---

### Connector Capability Matrix

Sourced from each connector's `SupportedPaymentMethods` implementation in `crates/hyperswitch_connectors`.

| Redirect Method | Connectors | Mandates | Refunds | Region |
| --- | --- | --- | --- | --- |
| **Sofort** | Stripe, Mollie | Stripe ✓ · Mollie ✗ | ✓ | Europe (13 countries) |
| **Giropay** | Stripe, Mollie | ✗ (both) | Stripe ✗ · Mollie ✓ | Germany |
| **iDEAL** | Stripe, Adyen, Mollie | Stripe ✓ · Adyen ✓ · Mollie ✗ | ✓ | Netherlands |
| **EPS** | Stripe, Adyen, Mollie | ✗ (all) | ✓ | Austria |
| **Przelewy24** | Stripe, Mollie | ✗ (both) | ✓ | Poland |
| **Bancontact** | Stripe, Adyen, Mollie | Stripe ✓ · Adyen ✓ · Mollie ✗ | ✓ | Belgium |
| **Blik** | Stripe, Adyen | ✗ (both) | ✓ | Poland |
| **Bizum** | Adyen | ✗ | ✓ | Spain |
| **Trustly** | Adyen | ✓ | ✓ | Nordics + Europe |
| **Open Banking UK** | Adyen | ✓ | ✓ | United Kingdom |
| **Online Banking FPX** | Stripe, Adyen | ✗ (both) | ✓ | Malaysia |
| **Online Banking (CZ/FI/PL/SK)** | Adyen | ✗ | ✓ | Central/Eastern Europe, Finland |
| **Online Banking Thailand** | Adyen | ✗ | ✓ | Thailand |

{% hint style="info" %}
**Mandate support on redirects:** Bank redirect mandates allow subsequent off-session charges using the same payment method without re-redirecting the customer. Only iDEAL (Stripe, Adyen), Bancontact (Stripe, Adyen), Sofort (Stripe), Trustly (Adyen), and Open Banking UK (Adyen) support mandate creation.
{% endhint %}

---

### Required API Fields

Bank redirect payments require `currency` and `billing.address.country` on every payment create call. Without these, Hyperswitch cannot determine which redirect methods are eligible to display.

```json
{
  "payment_method": "bank_redirect",
  "payment_method_data": {
    "bank_redirect": {
      "ideal": {
        "bank_name": "ing",
        "country": "NL"
      }
    }
  },
  "currency": "EUR",
  "billing": {
    "address": {
      "country": "NL"
    }
  }
}
```

---

### Common Failure Modes

**Method not shown at checkout**
Symptom: The bank redirect option is missing from the payment sheet. Fix: Confirm that `currency` and `billing.address.country` are present on the payment create call. Hyperswitch uses these to filter eligible redirect methods — a missing country means no redirect methods can be displayed.

**Redirect returns with error after bank approval**
Symptom: Customer approves at the bank portal but is returned to a failed state. Fix: Verify the `return_url` in the payment create matches a publicly reachable URL. Also check that the connector is enabled for the specific redirect type (e.g., Giropay must be enabled on your connector dashboard, not just the bank redirect category).

**Mandate setup fails on redirect method**
Symptom: `setup_future_usage: off_session` returns without a `mandate_id`. Fix: Not all connectors support mandates for all redirect types. Check the capability matrix — for example, Giropay and EPS do not support mandate creation on any connector. Use iDEAL or Bancontact on Stripe or Adyen if recurring off-session charges are needed.
