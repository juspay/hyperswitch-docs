---
description: Integrate Hyper Widgets using Rest APIs and HTML Frontend
---

# REST API and HTML

{% hint style="info" %}
In this section, we will cover how to integrate Hyperwidgets using REST API and HTML by setting up the Hyperswitch server, building the checkout page to complete a payment on the client.
{% endhint %}

### 1. Setup the server

#### 1.1 Create a payment

Add an endpoint on your server that creates a payment using the Payments API. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the `client_secret` obtained in the response to complete the payment on the client.

```js
// Create a Payment with the order amount and currency
curl --location --request POST 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <YOUR_API_KEY>' \
--data-raw '{
 "amount": 10,
 "currency": "USD"
}'
```

### 2. Build checkout page on the client

#### 2.1 Load HyperLoader

Use `HyperLoader` to ensure PCI compliant means of accepting payment details from your customer and sending it directly to the hyperswitch server. Always load `hyperLoader` from `https://beta.hyperswitch.io/v1/HyperLoader.js` to ensure compliance. Please refrain from including the script in a bundle or hosting it yourself.

```js
<script src="https://beta.hyperswitch.io/v1/HyperLoader.js"></script>
```

#### 2.2 Define the payment form

Add one empty placeholder `div` to your checkout form for each Widget that you’ll mount. `HyperLoader` inserts an iframe into each `div` to securely collect the customer’s email address and payment information.

```js
<form id="payment-form">
  <div id="card-widget">
   <!--HyperLoader injects the card Widget-->
  </div>
  <button id="submit">
    <div class="spinner hidden" id="spinner"></div>
    <span id="button-text">Pay now</span>
  </button>
  <div id="payment-message" class="hidden"></div>
</form>
```

#### 2.3 Initialize HyperLoader

Initialize `HyperLoader` with your publishable key. You’ll use `HyperLoader` to create the widgets and complete the payment on the client. To get an publishable Key please find it here.

```js
const hyper = hyper("YOUR_PUBLISHABLE_KEY");
```

#### 2.4 Fetch the Payment and create the Widgets

Immediately make a request to the endpoint on your server to create a new Payment as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Following this, create the widget of your choice and mount it to the placeholder `div` in your payment form. This embeds an iframe with a dynamic form that displays configured payment method types available from the `Payment`, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

```js
<script src="https://beta.hyperswitch.io/v1/HyperLoader.js"></script>;
// Fetches a payment intent and captures the client secret
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

  const hyperWidgets = widgets.create("payment");
  hyperWidgets.mount("#card-widget");
}
```

### 3. Complete payment on the client

#### 3.1 Handle the submit event and complete the payment

Listen to the form’s submit event to know when to confirm the payment through the hyper API.

Call `confirmPayment()`, passing along the widget and a `return_url` to indicate where Hyper should redirect the user after they complete the payment. Hyper redirects the customer to an authentication page depending on the payment method. After the customer completes the authentication process, they’re redirected to the `return_url`.

```js
sync function handleSubmit(e) {
e.preventDefault();
setLoading(true);

const { error } = await hyper.confirmPayment({
  widgets,
  confirmParams: {
    // Make sure to change this to your payment completion page
    return_url: "https://example.com/complete",
  },
});

// This point will only be reached if there is an immediate error occurring while confirming the payment. Otherwise, your customer will be redirected to your `return_url`

// For some payment flows such as Sofort, iDEAL, your customer will be redirected to an intermediate page to complete authorization of the payment, and then redirected to the `return_url`.

if (error.type === "validation_error") {
  showMessage(error.message);
} else {
  showMessage("An unexpected error occurred.");
}
  setLoading(false);
}
```

Also if there are any immediate errors (for example, your customer’s card is declined), `HyperLoader` returns an error. Show that error message to your customer so they can try again.

#### 3.2 Display a payment status message

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

Congratulations! Now that you have succesfully integrated the widgets, you can go ahead and[ test a payment.](../../hyperswitch-open-source/test-a-payment.md)
