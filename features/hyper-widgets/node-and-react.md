---
description: Integrate Hyper Widgets using Node Backend and React Frontend
---

# Node and React

{% hint style="info" %}
In this section, we will integrate hyper SDK to your React app using Node by setting up the server, building the checkout page to complete a payment on the client.

&#x20;You can also use this [demo app](https://github.com/aashu331998/hyperswitch-react-demo-app/archive/refs/heads/main.zip) as a reference with your Hyperswitch credentials to test the setup.
{% endhint %}

## [Demo App](https://github.com/aashu331998/Hyperswitch-Android-Demo-App/archive/refs/heads/main.zip)

### 1. Setup the server

#### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

#### 1.2 Create a payment

Before creating a payment, import the hyper dependencies and initialize it with your API key. To get an API Key please find it here.

```js
const hyper = require("@juspay-tech/hyperswitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the client\_secret obtained in the response to securely complete the payment on the client.

```js
// Create a Payment with the order amount and currency
app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      currency: "USD",
      amount: 100,
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

### 2. Build checkout page on the client

#### 2.1 Install the `hyper-js` and `react-hyper-js` libraries

Install the packages and import it into your code

```js
$ npm install @juspay-tech/hyper-js
$ npm install @juspay-tech/react-hyper-js
```

#### 2.2 Add `hyper` to your React app

Use `hyper-js` to ensure that you stay PCI compliant by sending payment details directly to Hyperswitch server.

```js
import React, { useState, useEffect } from "react";
import { loadHyper } from "@juspay-tech/hyper-js";
import { hyperElements } from "@juspay-tech/react-hyper-js";
```

#### 2.3 Load `hyper-js`

Call `loadHyper` with your publishable API keys to configure the library. To get an publishable Key please find it here.

```js
const hyperPromise = loadHyper("YOUR_PUBLISHABLE_KEY");
```

#### 2.4 Fetch the Payment and Initialise `hyperElements`

Immediately make a request to the endpoint on your server to create a new Payment as soon as your checkout page loads. The clientSecret returned by your endpoint is used to complete the payment.

```js
useEffect(() => {
  // Create PaymentIntent as soon as the page loads
  fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: [{ id: "xl-tshirt" }], country: "US" }),
  })
    .then((res) => res.json())
    .then((data) => setClientSecret(data.clientSecret));
}, []);
```

#### 2.5 Initialise `hyperElements`

Pass the promise from `loadHyper` to the `hyperElements` provider. This allows the child components to access the Hyper service via the `hyperElements` consumer. Additionally, pass the client secret as an [options](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/customization) to the `hyperElements` provider.

```js
<div className="App">
  {clientSecret && (
    <HyperElements options={options} hyper={hyperPromise}>
      <CheckoutForm />
    </HyperElements>
  )}
</div>
```

#### 2.6 Setup the state

Initialize a state to keep track of payment, display errors and control the user interface.

```js
const [message, setMessage] = useState(null);
const [isLoading, setIsLoading] = useState(false);
```

#### 2.7 Store a reference to `Hyper`

Access the `hyper-js` library in your CheckoutForm component by using the `useHyper()` and `useWidgets()` hooks. If you need to access Widgets via a class component, use the `WidgetsConsumer` instead. If you need to access Widgets via a class component, use the `WidgetsConsumer` instead. You can find the API for these methods here.

```js
const hyper = useHyper();
const widgets = useWidgets();
```

### 3. Complete the checkout on the client

#### 3.1 Add the widgets

Add the card widget of your choice to your Checkout. This embeds an iframe with dynamic forms that securely collect your customer's card details.

Single line card widget:

```js
<CardWidget id="card-widget" />
```

Card number widget:

```js
<CardNumberWidget id="card-number-widget" />
```

Card expiry widget:

```js
<CardExpiryWidget id="card-expiry-widget" />
```

Card CVC widget:

```js
<CardCVCWidget id="card-CVC-widget" />
```

#### 3.2 Complete the payment and handle errors

Call `confirmPayment()`, passing along the widgets and a `return_url` to indicate where `hyper` should redirect the user after they complete the payment. For payments that require additional authentication, `hyper` redirects the customer to an authentication page depending on the payment method. After the customer completes the authentication process, they’re redirected to the return\_url.

If there are any immediate errors (for example, your customer’s card is declined), `hyper-js` returns an error. Show that error message to your customer so they can try again.

```js
const handleSubmit = async (e) => {
  e.preventDefault();

  if (!hyper || !widgets) {
    // hyper-js has not yet loaded.
    // Make sure to disable form submission until hyper-js has loaded.
    return;
  }

  setIsLoading(true);

  const { error } = await hyper.confirmPayment({
    widgets,
    confirmParams: {
      // Make sure to change this to your payment completion page
      return_url: "http://example.com/complete",
    },
  });

  // This point will only be reached if there is an immediate error occurring while confirming the payment. Otherwise, your customer will be redirected to your `return_url`

  // For some payment flows such as Sofort, iDEAL, your customer will be redirected to an intermediate page to complete authorization of the payment, and then redirected to the `return_url`.

  if (error.type === "validation_error") {
    setMessage(error.message);
  } else {
    setMessage("An unexpected error occurred.");
  }
  setIsLoading(false);
};
```

#### 3.3 Display payment status message

When Hyperswitch redirects the customer to the `return_url`, the `payment_client_secret` query parameter is appended by `hyper-js`. Use this to retrieve the Payment to determine what to show to your customer.

```js
//Look for a parameter called `payment_intent_client_secret` in the url which gives a payment ID, which is then used to retrieve the status of the payment

const paymentID = new URLSearchParams(window.location.search).get(
  "payment_intent_client_secret"
);

if (!paymentID) {
  return;
}

hyper.retrievePaymentIntent(paymentID).then(({ paymentIntent }) => {
  switch (paymentIntent.status) {
    case "succeeded":
      setMessage("Payment succeeded!");
      break;
    case "processing":
      setMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      setMessage("Your payment was not successful, please try again.");
      break;
    default:
      setMessage("Something went wrong.");
      break;
  }
});
```

Congratulations! Now that you have succesfully integrated the widgets, you can go ahead and[ test a payment.](../../hyperswitch-open-source/test-a-payment.md)
