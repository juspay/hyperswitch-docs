---
description: Integrate hyper SDK to your HTML Web App using Hyperswitch-node
---

# Node and HTML

{% hint style="info" %}
In this section, you will get details to Integrate Hyperswitch SDK using Node Backend and HTML Frontend
{% endhint %}

**Before following these steps, please configure your payment methods** [here](https://hyperswitch.io/docs/paymentMethods/cards). Use this guide to integrate `hyperswitch` SDK to your HTML app. You can also use this demo app as a reference with your Hyperswitch credentials to test the setup.

## [<mark style="color:blue;">Demo App</mark>](https://github.com/aashu331998/hyperswitch-html-demo-app/archive/refs/heads/main.zip)

## 1. Setup the server

### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

### 1.2 Create a payment

Before creating a payment, import the `hyperswitch-node` dependencies and initialize it with your API key. Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

```js
const hyper = require("@juspay-tech/hyperswitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the `client_secret` obtained in the response to securely complete the payment on the client.

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

{% hint style="info" %}
In case your integrating the ExpressCheckout (mentioned later below), instead of creating multiple paymentIntents for the same customer session, you can also use [paymentsUpdate API](https://api-reference.hyperswitch.io/api-reference/payments/payments--update) for better analytics.
{% endhint %}

## 2. Build checkout page on the client

### 2.1 Load HyperLoader

Use `HyperLoader` to ensure PCI compliant means of accepting payment details from your customer and sending it directly to the hyperswitch server. Always load `hyperLoader` from `https://beta.hyperswitch.io/v1/HyperLoader.js` to ensure compliance. Please refrain from including the script in a bundle or hosting it yourself.

```js
<script src="https://beta.hyperswitch.io/v1/HyperLoader.js"></script>
```

### 2.2 Define the payment form

{% hint style="info" %}
This step is recommended for the Unified Checkout for an enhanced user experience. In case you are integrating Express Checkout (mentioned later below), this step is not required.
{% endhint %}

Add one empty placeholder `div` to your checkout form for each Widget that you’ll mount. `HyperLoader` inserts an iframe into each `div` to securely collect the customer’s email address and payment information.

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

### 2.3 Initialize HyperLoader

Initialize `HyperLoader` onto your app with your publishable key with the `Hyper` constructor. You’ll use `HyperLoader` to create the Unified Checkout and complete the payment on the client. To get a Publishable Key please find it [here](https://app.hyperswitch.io/developers).

```js
const hyper = Hyper("YOUR_PUBLISHABLE_KEY",{
    customBackendUrl: "YOUR_BACKEND_URL",
    //You can configure this as an endpoint for all the api calls such as session, payments, confirm call.
});
```

{% tabs %}
{% tab title="UnifiedCheckout" %}
### 2.4 Fetch the Payment and create the Unified Checkout

<figure><img src="../../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

Immediately make a request to the endpoint on your server to create a new Payment as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Following this, create a `unifiedCheckout` and mount it to the placeholder `div` in your payment form. This embeds an iframe with a dynamic form that displays configured payment method types available from the `Payment`, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

```js
<script src="https://beta.hyperswitch.io/v1/HyperLoader.js"></script>;
// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: [{ id: "xl-tshirt" }], country: "US" }),
  });
  const { clientSecret } = await response.json();

  const appearance = {
    theme: "midnight",
  };

  widgets = hyper.widgets({ appearance, clientSecret });

  const unifiedCheckoutOptions = {
    layout: "tabs",
    wallets: {
      walletReturnUrl: "https://example.com/complete",
      //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
    },
  };

  const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);
  unifiedCheckout.mount("#unified-checkout");
}
```
{% endtab %}

{% tab title="ExpressCheckout" %}
### 2.4 Fetch the Payment and create the Express Checkout

<figure><img src="../../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

> The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons. Supported payment methods include ApplePay, GooglePay and PayPal.

Make a request to the endpoint on your server to create a new Payment. The `clientSecret` returned by your endpoint is used to complete the payment.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Create an `expressCheckout` and mount it to the placeholder `div` in your payment form. This embeds an iframe that displays configured payment method types supported by the browser available for the payment, allowing your customer to select a payment method. The payment methods automatically collects the associated payment details for the selected payment method type.

```js
<script src="https://beta.hyperswitch.io/v1/HyperLoader.js"></script>;
// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: [{ id: "xl-tshirt" }], country: "US" }),
  });
  const { clientSecret } = await response.json();

  const appearance = {
    theme: "midnight",
  };

  widgets = hyper.widgets({ appearance, clientSecret });

  const expressCheckoutOptions = {
    wallets: {
      walletReturnUrl: "https://example.com/complete",
      //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
    },
  };

  const expressCheckout = widgets.create("expressCheckout", expressCheckoutOptions);
  expressCheckout.mount("#express-checkout");
}
```
{% endtab %}
{% endtabs %}

## 3. Complete payment on the client

### 3.1 Handle the submit event and complete the payment

> Note: This step is not required for ExpressCheckout

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

<details>

<summary>Alternate Implementation: SDK handles the Confirm Button</summary>

For SDK to render the confirm button and handle the confirm payment, in  paymentElementOptions, you can send:

```html
const unifiedCheckoutOptions = {
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

Congratulations! Now that you have integrated the Hyperswitch SDK on your app, you can customize the payment elements to blend with the rest of your app.&#x20;
