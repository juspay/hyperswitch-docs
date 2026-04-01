---
description: Integrate web client for a seamless, blended and a unified payment experience
---

# Integrate web client on your web app

> ℹ️ **Info:** In this section, you will learn to integrate the web client on your web app

Assuming that the web client is hosted successfully, you can now integrate the web client on your HTML web app with the following steps.

> ℹ️ **Info:** If your web app is in other tech stack (for eg., React, Angular, etc.), you can follow our [documentation](https://app.gitbook.com/o/JKqEWJaaVJcFy28N5Z3d/s/kf7BGdsPkCw9nalhAIlE/) for reference integrations.

### 1. Build checkout page on the client

#### 1.1 Load HyperLoader

Use `HyperLoader` to accept payment details from your customer and send them to the your hosted app server. Load `HyperLoader` from `https://{{YOUR_WEB_CLIENT_URL}}/HyperLoader.js`

```html
<script src="https://{{YOUR_WEB_CLIENT_URL}}/HyperLoader.js"></script>
```

#### 1.2 Define the payment form

Add one empty placeholder `div` to your checkout form for each Widget that you'll mount. `HyperLoader` inserts an iframe into each `div` to securely collect the customer's email address and payment information.

```html
<form id="payment-form">
  <div id="unified-checkout">
   <!--hyperLoader injects the Unified Checkout-->
  </div>
  <button id="submit">
    <div class="spinner hidden" id="spinner"></div>
    <span id="button-text">Pay now</span>
  </button>
  <div id="payment-message" class="hidden"></div>
</form>
```

#### 1.3 Initialize HyperLoader

Initialize `HyperLoader` onto your app with your publishable key with the `Hyper` constructor. You'll use `HyperLoader` to create the Unified Checkout and complete the payment on the client.

```javascript
const hyper = Hyper("YOUR_PUBLISHABLE_KEY");
```

#### 1.4 Fetch the Payment and create the Unified Checkout

Immediately make a request to the endpoint on your server to create a new `Payment` as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

Following this, create a `UnifiedCheckout` and mount it to the placeholder `div` in your payment form. This embeds an iframe with a dynamic form that displays configured payment method types available from the `Payment`, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

```javascript
async function initialize() {
  const response = await fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: [{ id: "xl-tshirt" }], country: "US" }),
  });
  const { client_secret } = await response.json();

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

### 2. Complete payment on the client

#### 2.1 Handle the submit event and complete the payment

Listen to the form's submit event to know when to confirm the payment through the hyper API.

Call `confirmPayment()`, passing along the `UnifiedCheckout` and a `return_url` to indicate where Hyper should redirect the user after they complete the payment. Hyper redirects the customer to an authentication page depending on the payment method. After the customer completes the authentication process, they're redirected to the `return_url`.

```javascript
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

> ℹ️ **Info:** Also if there are any immediate errors (for example, your customer's card is declined), `HyperLoader` returns an error. Show that error message to your customer so they can try again.

#### 2.2 Display a payment status message

When Hyper redirects the customer to the `return_url`, the `payment_intent_client_secret` query parameter is appended by `HyperLoader`. Use this to retrieve the Payment to determine what to show to your customer.

```javascript
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

> ✅ **Success:** That's it! You have successfully integrated your hosted web client on your web app. Now you can collect payments from your customers in a secure way.

The web client allows you to customize the appearance according to your web app for a better blended UI. Please check the [customization options](../../../../explore-hyperswitch/payment-experience/payment/web/customization.md) for more details.

<details>

<summary>Troubleshooting/ FAQs</summary>

* **I am getting an error while loading the HyperLoader.js script**\
  Please ensure that the path URL is correct and HyperLoader.js is present on that path. You can check it by opening the URL in a browser.\
* **I am unable to see the SDK running, or it is in a perpetual loading state**\
  Please make sure that the correct publishable key is used to instantiate the SDK.\
* **After completing the payment, I am redirected to a non existent web page**\
  Please make sure that the correct return URL is sent in confirm parameters and the payment statuses are correctly handled post redirection.

</details>

### Next step

[Account Setup](../../../account-setup/)
