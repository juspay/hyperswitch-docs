# Server Setup

### 1. Create a payment using S2S Call (Recommended)

_<mark style="color:blue;">(We highly recommend using this S2S method for all production activities and functionalities, as it offers greater scalability and enhanced features designed for production environments)</mark>_

To create a payment intent, send a request to either our sandbox or production endpoint. For detailed information, refer to the [**API Reference**](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) documentation.

Upon successful creation, you will receive a `client_secret`, which must be provided to the SDK to render it properly.

```javascript
// Example Usage :- Can be Modified
async function createPaymentIntent(request) {
  /* Add respective env enpoints
   - Sandbox - https://sandbox.hyperswitch.io
   - Prod - https://api.hyperswitch.io
  */
  const url = "https://sandbox.hyperswitch.io";
  const apiResponse = await fetch(`${url}/payments`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "api-key": `API_KEY`,
    },
    body: JSON.stringify(request),
  });
  const paymentIntent = await apiResponse.json();

  if (paymentIntent.error) {
    console.error("Error - ", paymentIntent.error);
    throw new Error(paymentIntent?.error?.message ?? "Something went wrong.");
  }
  return paymentIntent;
}
```

### 2. Create a payment using Hyperswitch Node SDK

_<mark style="color:blue;">(We recommend using this method for local development and quick integration to test various use cases.)</mark>_

#### 2.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```bash
npm install @juspay-tech/hyperswitch-node
```

#### 2.2 Create a payment

Before creating a payment, import the hyper dependencies and initialize it with your API key. Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

```js
const hyper = require("@juspay-tech/hyperswitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the client\_secret obtained in the response to securely complete the payment on the client.

```javascript
// Example Usage :- Can be Modified
async function createPaymentIntent(request) {
  /* Add respective env enpoints
   - Sandbox - https://sandbox.hyperswitch.io
   - Prod - https://api.hyperswitch.io
  */
  const url = "https://sandbox.hyperswitch.io";
  const apiResponse = await fetch(`${url}/payments`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "api-key": `API_KEY`,
    },
    body: JSON.stringify(request),
  });
  const paymentIntent = await apiResponse.json();

  if (paymentIntent.error) {
    console.error("Error - ", paymentIntent.error);
    throw new Error(paymentIntent?.error?.message ?? "Something went wrong.");
  }
  return paymentIntent;
}
```

### 3. Integrate Web SDK

_To integrate Web SDK, follow_ [_Node And React_](node-and-react.md)_,_ [_Node and HTML_](node-and-html.md) _and_ [_Vanilla JS and REST API Integration_](vanilla-js-and-rest-api-integration.md)_._

{% hint style="info" %}
In case your integrating the ExpressCheckout (mentioned later below), instead of creating multiple paymentIntents for the same customer session, you can also use [paymentsUpdate API](https://api-reference.hyperswitch.io/api-reference/payments/payments--update) for better analytics.
{% endhint %}
