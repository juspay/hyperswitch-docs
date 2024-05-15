---
description: Integrate hyper SDK to your React Web App using Hyperswitch-node
---

# Node And React

{% hint style="info" %}
In this section, you will get details to Integrate Unified Checkout using Node Backend and React Frontend
{% endhint %}

**Before following these steps, please configure your payment methods** here. Use this guide to integrate `hyper` SDK to your React app. You can also use this demo app as a reference with your Hyperswitch credentials to test the setup.

## [<mark style="color:blue;">Demo App</mark>](https://github.com/aashu331998/hyperswitch-react-demo-app/archive/refs/heads/main.zip)

### 1. Setup the server

#### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

#### 1.2 Create a payment

Before creating a payment, import the hyper dependencies and initialize it with your API key. Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

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

Call `loadHyper` with your publishable API keys to configure the library. To get an publishable Key please find it [here](https://app.hyperswitch.io/developers).

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

#### 2.5 Initialise `HyperElements`

Pass the promise from `loadHyper` to the `HyperElements` component. This allows the child components to access the Hyper service via the `HyperElements` parent component. Additionally, pass the client secret as an [options](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/customization) to the `HyperElements` component.

```js
<div className="App">
  {clientSecret && (
    <HyperElements options={options} hyper={hyperPromise}>
      <CheckoutForm />
    </HyperElements>
  )}
</div>
```

#### 2.6 Setup the state (optional)

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

#### 3.1 Add the UnifiedCheckout

Add the `UnifiedCheckout` to your Checkout. This embeds an iframe with a dynamic form that displays configured payment method types available from the Payment, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

(Optional) Define paymentElementOptions:

```js
var unifiedCheckoutOptions = {
  wallets: {
    walletReturnUrl: "https://example.com/complete",
    //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
  },
};
```

```js
<UnifiedCheckout id="unified-checkout" options={unifiedCheckoutOptions} />
```

#### 3.2 Complete the payment and handle errors

Call `confirmPayment()`, passing along the `UnifiedCheckout` and a return\_url to indicate where `hyper` should redirect the user after they complete the payment. For payments that require additional authentication, `hyper` redirects the customer to an authentication page depending on the payment method. After the customer completes the authentication process, they’re redirected to the return\_url.

If there are any immediate errors (for example, your customer’s card is declined), `hyper-js` returns an error. Show that error message to your customer so they can try again.

```js
const handleSubmit = async (e) => {
  setMessage("");
  //e.preventDefault();

  if (!hyper || !widgets) {
    return;
  }
  setIsLoading(true);

  const { error, status } = await hyper.confirmPayment({
    elements,
    confirmParams: {
      // Make sure to change this to your payment completion page
      return_url: "https://example.com/complete",
    },
    redirect: "always", // if you wish to redirect always, otherwise it is defaulted to "if_required"
  });

  if (error) {
    if (error.type === "card_error" || error.type === "validation_error") {
      setMessage(error.message);
    } else {
      if (error.message) {
        setMessage(error.message);
      } else {
        setMessage("An unexpected error occurred.");
      }
    }
  }
  if (status) {
    handlePaymentStatus(status); //handle payment status
  }
  setIsLoading(false);
};
```

<details>

<summary>Alternate Implementation: SDK handles the Confirm Button</summary>

For SDK to render the confirm button and handle the confirm payment, in  paymentElementOptions, you can send:

```javascript
var unifiedCheckoutOptions = {
  ...,
  sdkHandleConfirmPayment: {
     handleConfirm: true,
     buttonText: "SDK Pay Now",
     confirmParams: {
       return_url: "https://example.com/complete",
     },
   },
};
```

1. **`handleConfirm (required)`** - A boolean value indicating whether the SDK should handle the confirmation of the payment.
2. **`confirmParams (required)`** - It’s an object which takes return\_url. return\_url parameter specifies the URL where the user should be redirected after payment confirmation.
3. **`buttonText (optional)`** -  The text to display on the payment button. \
   Default value: **Pay Now**

For customization, please follow the [`Customization docs`](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/web/customization#id-5.-confirm-button).

</details>

#### 3.3 Display payment status message

When Hyperswitch redirects the customer to the `return_url`, the `payment_client_secret` query parameter is appended by hyper-js. Use this to retrieve the Payment to determine what to show to your customer.

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

### 4. Elements Events

Some events are emitted by payment elements, listening to those events is the only way to communicate with these elements. All events have a payload object with the type of the Element that emitted the event as an elementType property. Following events are emitted by payment elements.

* change
* ready
* focus
* blur

#### 4.1 Calling Elements events

First create instance of widgets using `getElement` function. It will return `null` if no matching type is found.

```js
// Create instance of widgets
var paymentElement = widgets.getElement("payment");

// handle event
if (paymentelement) {
  // in place of "EVENT" use "change", "ready", "focus" etc.
  paymentElement.on("EVENT", callbackFn);
}
```

#### 4.2 "change" event

The "change" event will be triggered when value changes in Payment element.

```js
paymentElement.on("change", function (event) {
  // YOUR CODE HERE
});
```

Callback function will be fired when the event will be triggered. When called it will be passed an event object with the following properties.

```js
{
  elementType: 'payment',   // The type of element that emitted this event.
  complete: false,          // If all required field are complete
  empty: false,             // if the value is empty.
  value: { type: "card" },  // current selected payment method like "card", "klarna" etc
}
```

#### 4.3 "ready" event

The "ready" event will be triggered when payment element is full rendered and can accept "focus" event calls.

Callback for ready event will be triggered with following event object

```js
{
  ready: boolean,   // true when payment element is full rendered
}
```

#### 4.4 "focus", "blur" event

Focus and blur event triggered when respective event will be triggered in payment element.

Callback for these event will be triggered with following event object.

```js
// Event object for focus event
{
  focus: boolean,   // true when focused on payment element
}

// Event object for blur event
{
  blur: boolean,
}
```

Congratulations! Now that you have integrated the  unified checkout on your app, you can customize the payment elements to blend with the rest of your app.&#x20;

## Next step:

{% content-ref url="../../payment-methods-setup/" %}
[payment-methods-setup](../../payment-methods-setup/)
{% endcontent-ref %}
