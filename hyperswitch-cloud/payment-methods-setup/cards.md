# 💳 Cards

![logo\_discord](https://hyperswitch.io/logos/logo\_diners.svg)![logo\_discord](https://hyperswitch.io/logos/logo\_visa.svg)![logo\_discord](https://hyperswitch.io/logos/logo\_mastercard.svg)![logo\_discord](https://hyperswitch.io/logos/logo\_amex.svg)

**Hyperswitch supports credit and debit card payments through all our payment processor connectors.** \
We accept cards from all major global and local card networks, such as Visa, Mastercard, American Express, Diners, Discover, JCB, Union Pay, etc. While Hyperswitch supports card payments in 135+ currencies and 150+ countries, each of these connectors and networks has limitations in terms of the number of countries and currencies they support.

Apart from regular one-time payments, Hyperswitch supports saving a card, recurring payments, and placing a hold for later capture.

### Integration Steps

1. Go to Hyperswitch dashboard and to connectors tab [here](https://app.hyperswitch.io/) and enable card.

### Saved Cards

You could use Hyperswitch’s PCI Compliant secure vault to safely store your customers’ card data and retrieve them when they return to pay on your website/app. In addition, our hyper SDK has a checkbox on the payment page that you can use to take customers’ consent to store their card data. To try out the save cards feature through API, include either of the values for the `setup_future_usage` field in your Payments API request body. This feature comes with [Unified Checkout](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb#unified-checkout).

### 1. Setup the server

#### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

#### 1.2 Create a customer and payment

Before creating a customer or payment, import the `hyperswitch-node` dependencies and initialize it with your API key. To get an API Key please find it here.

```js
const hyper = require("@juspay-tech/hyperswitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates the customer. Creating a customer will help save a card to its corresponding customer ID. Return the customer ID to the client.

```js
app.post("/create-customer", async (req, res) => {
  const { items } = req.body;
  const customer = await hyper.customers.create({
    description: "My First Test Customer",
    email: "johndoe@example.com",
  });
  res.send({
    customer: customer.id,
  });
});
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the `client_secret` obtained in the response to securely complete the payment on the client. Add in an extra parameter of `customer` to save the card for that particular customer.

```js
// Create a Payment with the order amount and currency
app.post("/create-payment", async (req, res) => {
  const { items } = req.body;

  // Create a PaymentIntent with the order amount and currency
  const paymentIntent = await hyper.paymentIntents.create({
    amount: 100,
    currency: "USD",
    automatic_payment_methods: {
      enabled: true,
    },
    payment_method_options: {
      card: {
        request_three_d_secure: "automatic",
      },
    },
    customer: "cus_4xmr0vzTfD7qvxiMTZ8P",
  });
  res.send({
    clientSecret: paymentIntent.client_secret,
  });
});

app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      amount: 100,
      currency: "USD",
      automatic_payment_methods: {
        enabled: true,
      },
      payment_method_options: {
        card: {
          request_three_d_secure: "automatic",
        },
      },
      customer: "cus_4xmr0vzTfD7qvxiMTZ8P",
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

Add an endpoint in the server to call the `listPaymentMethods` to send the customer ID. This will return you the payment information required to display saved cards by `HyperElement` through which that customer will be able to confirm their payment.

```js
app.post("/list-paymentmethods", async (req, res) => {
  const paymentMethods = await hyper.customers.listPaymentMethods(
    "cus_dOIqeb2odRbQ4ZQkiMo9",
    { type: "card" }
  );

  res.send({
    paymentMethods: paymentMethods,
  });
});
```

### 2. Build checkout page on the client

_Follow the integration steps of Unified Checkout_ [_here_](https://hyperswitch.io/docs/unifiedCheckoutWeb/) _for your respective stack_

#### 2.1 Pass the the `paymentMethods` data to `HyperElements`

```js
useEffect(() => {
    // Create PaymentIntent as soon as the page loads
    fetch("/list-paymentmethods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => res.json())
      .then((data) => {
        setCustomerPaymentMethods(data.customerPaymentMethods);
      });
  }, []);

let options = {
    //clientSecret,
    clientSecret,
    appearance: {
      theme: theme,
    },
    ...,
    customerPaymentMethods:customerPaymentMethods
  };
  <div className="App">
  {clientSecret && (
    <HyperElements options={options} hyper={hyperPromise}>
      <CheckoutForm />
    </HyperElements>
  )}
</div>

```

Now follow the rest of the integration steps to enable Unified Checkout.

### Recurring Payments - Mandate through cards

Currently, Hyperswitch supports the creation of mandates for card transactions through the following payment processors: - Adyen - Checkout

### Placing a hold for later capture

By default, all payments are auto-captured during authorization in Hyperswitch, but you can choose to separate capture from authorization by manually capturing an authorized payment later. Setting the ‘capture’ field in payments/confirm API to ‘manual’ will block the stated amount on the customer’s card without charging them. To charge the customer an amount equal to or lesser than the blocked amount, use the payments/capture endpoint with the relevant details.
