---
description: Integrate hyper SDK to any Web App using hyperswitch-node
---

# Vanilla JS and REST API Integration

**Before following these steps, please configure your payment methods** [here](https://hyperswitch.io/docs/paymentMethods/cards). Use this guide to integrate `hyperswitch` SDK to you app with any framework. If you are using React framework please go through [React ](node-and-react.md)Integration to use a dedicated wrapper.\


## [<mark style="color:blue;">Demo App</mark>](https://github.com/PritishBudhiraja/hyperswitch-demo-app/archive/refs/heads/master.zip)

## 1. Setup the server

Follow the [Server Setup](server-setup.md) section.

## 2. Build checkout page on the client

### 2.1 Define the payment form

{% hint style="info" %}
This step is recommended for the Unified Checkout for an enhanced user experience. In case you are integrating Express Checkout (mentioned later below), this step is not required.
{% endhint %}

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

{% tabs %}
{% tab title="UnifiedCheckout" %}
### 2.2 Fetch the Payment and create the Unified Checkout

<figure><img src="../../../../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

Immediately make a request to the endpoint on your server to create a new Payment as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Following this, create a `unifiedCheckout` and mount it to the placeholder `div` in your payment form. This embeds an iframe with a dynamic form that displays configured payment method types available from the `Payment`, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

Incase, you want the SDK to be loaded on a particular event (like button click), you can call the initialize function on that event.

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
      hyper = window.Hyper("YOUR_PUBLISHABLE_KEY",{
      customBackendUrl: "YOUR_BACKEND_URL",
      //You can configure this as an endpoint for all the api calls such as session, payments, confirm call.
      })
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

### 2.3 Additional Callback Handling for Wallets Payment Process

This document outlines the details and functionality of an optional callback `completeDoThis` and `onSDKHandleClick` that can be provided by merchants during the payment process. These callbacks allow merchants to hook into the payment flow at key stages and handle specific actions or events before continuing the normal flow.

* **onSDKHandleClick:** This callback is triggered immediately after the user clicks any wallet button.
* **completeDoThis:** This callback is triggered after the payment is completed, just before the SDK redirects to `walletReturnUrl` provided. It allows the merchant to handle actions post-payment. If not provided, the SDK's default flow will proceed.

{% hint style="warning" %}
**Redirection Handling:** The `onPaymentComplete` callback should handle redirection or any steps needed after payment, as the SDK no longer does this automatically. You must ensure to implement the necessary redirection logic.
{% endhint %}

{% hint style="info" %}
**Fallback:** If no callbacks are provided by the merchant, the SDK will continue with its default behaviour, including automatic redirection after payment completion.
{% endhint %}

{% hint style="danger" %}
The task within `onPaymentButtonClick` must be completed within 1 second. If an asynchronous callback is used, it must resolve within this time to avoid Apple Pay payment failures.
{% endhint %}

#### **Example Usage**

```javascript
const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);
unifiedCheckout.mount("#unified-checkout");

unifiedCheckout.onSDKHandleClick(()=>{
  // Add any custom logic for when the payment button is clicked, such as logging or tracking
  console.log("On Click Wallets")
})

unifiedCheckout.on("completeDoThis",()=>{
  console.log("On Payment Complete")
  // Add any custom post-payment logic here, such as redirection or displaying a success message
})
```
{% endtab %}

{% tab title="ExpressCheckout" %}
### 2.2 Fetch the Payment and create the Express Checkout

<figure><img src="../../../../.gitbook/assets/image (155).png" alt=""><figcaption></figcaption></figure>

> The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons. Supported payment methods include ApplePay, GooglePay and PayPal.

Make a request to the endpoint on your server to create a new Payment. The `clientSecret` returned by your endpoint is used to complete the payment.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Create an `expressCheckout` and mount it to the placeholder `div` in your payment form. This embeds an iframe that displays configured payment method types supported by the browser available for the payment, allowing your customer to select a payment method. The payment methods automatically collects the associated payment details for the selected payment method type.

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
      const expressCheckoutOptions = {
          wallets: {
              walletReturnUrl: "https://example.com/complete",
              //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
          },
      };
      const expressCheckout = widgets.create("expressCheckout", expressCheckoutOptions);
      expressCheckout.mount("#express-checkout");
  };
  document.body.appendChild(script);
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
