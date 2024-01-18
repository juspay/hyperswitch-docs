---
description: Integrate hyper SDK to any Web App using hyperswitch-node
---

# Vanilla JS and REST API Integration&#x20;

{% hint style="info" %}
In this section, you will get details to Integrate Unified Checkout using Node Backend and Vanilla JS&#x20;
{% endhint %}

**Before following these steps, please configure your payment methods** [here](https://hyperswitch.io/docs/paymentMethods/cards). Use this guide to integrate `hyperswitch` SDK to you app with any framework. If you are using React framework please go through [React ](node-and-react.md)Integration to use a dedicated wrapper.\


## [<mark style="color:blue;">Demo App</mark>](https://github.com/aashu331998/hyperswitch-html-demo-app/archive/refs/heads/main.zip)

## 1. Setup the server

### 1.1 Create a payment

Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the `client_secret` obtained in the response to securely complete the payment on the client.

```js
// Create a Payment intent
const app = express();

app.post("/create-payment", async (req, res) => {
  try {
    const response = await fetch(`https://sandbox.hyperswitch.io/payments`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json", "api-key": "YOUR_API_KEY" },
        body: JSON.stringify(req.body),
      });
    const paymentIntent = await response.json()
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

## 2. Build checkout page on the client

### 2.1 Define the payment form

Add one empty placeholder `div` to your checkout form for each Widget that you’ll mount. `HyperLoader` inserts an iframe into each `div` to securely collect the customer’s email address and payment information.&#x20;

```js
<form id="payment-form">
  <div id="unified-checkout">
   <!--HyperLoader injects the Unified Checkout-->
  </div>
  <button id="submit">
    <div class="spinner hidden" id="spinner"></div>
    <span id="button-text">Pay now</span>
  </button>
  <div id="payment-message" class="hidden"></div>
</form>
```

### 2.2 Fetch the Payment and create the Unified Checkout

Immediately make a request to the endpoint on your server to create a new Payment as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Following this, create a `unifiedCheckout` and mount it to the placeholder `div` in your payment form. This embeds an iframe with a dynamic form that displays configured payment method types available from the `Payment`, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

```js
// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({currency: "USD",amount: 100}),
  });
  const { clientSecret } = await response.json();
  
  // Initialise Hyperloader.js
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = "https://beta.hyperswitch.io/v1/HyperLoader.js";
 
  let hyper; 
  script.onload = () => {
      hyper = window.Hyper("YOUR_PUBLISHABLE_KEY")
      const appearance = {
          theme: "midnight",
      };
      const widgets = hyper.widgets({ appearance, clientSecret });
      const unifiedCheckoutOptions = {
          layout: "tabs",
          wallets: {
              walletReturnUrl: "https://example.com/complete",
              //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
          },
      };
      const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);
      unifiedCheckout.mount("#unified-checkout");
  };
  document.body.appendChild(script);
}
```

## 3. Complete payment on the client

### 3.1 Handle the submit event and complete the payment

Listen to the form’s submit event to know when to confirm the payment through the hyper API.

Call `confirmPayment()`, passing along the `unifiedCheckout` and a `return_url` to indicate where Hyper should redirect the user after they complete the payment. Hyper redirects the customer to an authentication page depending on the payment method. After the customer completes the authentication process, they’re redirected to the `return_url`.

```js
async function handleSubmit(e) {
  setMessage("");
  e.preventDefault();

  if (!hyper || !widgets) {
    return;
  }
  setIsLoading(true);

  const { error, status } = await hyper.confirmPayment({
    widgets,
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
}
```

Also if there are any immediate errors (for example, your customer’s card is declined), `HyperLoader` returns an error. Show that error message to your customer so they can try again.

### 3.2 Display a payment status message

When Hyper redirects the customer to the `return_url`, the `payment_intent_client_secret` query parameter is appended by `HyperLoader`. Use this to retrieve the `Payment` to determine what to show to your customer.

```js
// Fetches the payment status after payment submission
async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get(
    "payment_intent_client_secret"
  );

  if (!clientSecret) {
    return;
  }

  const { payment } = await hyper.retrievePayment(clientSecret);

  switch (payment.status) {
    case "succeeded":
      showMessage("Payment succeeded!");
      break;
    case "processing":
      showMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      showMessage("Your payment was not successful, please try again.");
      break;
    default:
      showMessage("Something went wrong.");
      break;
  }
}
```

Congratulations! Now that you have integrated the  unified checkout on your app, you can customize the payment elements to blend with the rest of your app.&#x20;
