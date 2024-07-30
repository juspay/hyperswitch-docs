---
description: Hyperswitch is designed to facilitate the management of saved payment methods
---

# Payment Methods Management

{% hint style="info" %}
This section guides you through the integration of Hyperswitch Payment Methods Management
{% endhint %}

### 1. Setup the server

#### 1.1 Create an ephemeral key

Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

Add an endpoint on your server that creates an Ephemeral Key. An **ephemeral key** is a temporary, short-lived key used to securely manage sensitive operations, such as updating or deleting payment methods, without exposing full access credentials. It has a limited validity period and restricted capabilities, ensuring that it can only be used for specific tasks and not for initiating payments. This enhances security by minimizing the risk of unauthorized access and reducing the exposure of sensitive data. Return the `secret` obtained in the response to setup Payment Methods Management on client.

```js
// Create an Ephemeral Key
const app = express();

app.post("/create-ephemeral-key", async (req, res) => {
  try {
    const response = await fetch(`https://sandbox.hyperswitch.io/ephemeral_keys`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json", "api-key": "YOUR_API_KEY" },
        body: JSON.stringify(req.body),
      });
    const ephemeralKey = await response.json()
    // Send publishable key and PaymentIntent details to client
    res.send({
      ephemeralKey: ephemeralKey.secret,
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

### 2. Build Payment Management Page on the client

{% tabs %}
{% tab title="React" %}
#### 2.1 Install the `hyper-js` and `react-hyper-js` libraries

Install the packages and import it into your code

```js
$ npm install @juspay-tech/hyper-js
$ npm install @juspay-tech/react-hyper-js
```

#### 2.2 Add `hyper` to your React app

```js
import React, { useState, useEffect } from "react";
import { loadHyper } from "@juspay-tech/hyper-js";
import { HyperManagementElements } from "@juspay-tech/react-hyper-js";
```

#### 2.3 Load `hyper-js`

Call `loadHyper` with your publishable API keys to configure the library. To get an publishable Key please find it [here](https://app.hyperswitch.io/developers).

```js
const hyperPromise = loadHyper("YOUR_PUBLISHABLE_KEY");
```

#### 2.4 Fetch the Payment

Make a request to the endpoint on your server to create a new Ephemeral Key. The `ephemeralKey` returned by your endpoint is used to fetch all the customer saved payment methods.

```js
useEffect(() => {
  // Create PaymentIntent as soon as the page loads
  fetch("/create-ephemeral-key", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({customer_id: "hyperswitch_sdk_demo_id"}),
  })
    .then((res) => res.json())
    .then((data) => setEphemeralKey(data.ephemeralKey));
}, []);
```

#### 2.5 Initialise `HyperManagementElements`

Pass the promise from `loadHyper` to the `HyperManagementElements` component. This allows the child components to access the Hyper service via the `HyperManagementElements` parent component. Additionally, pass the `ephemeralKey` in [options](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/customization) to the `HyperManagementElements` component.

```js
<div className="App">
  {ephemeralKey && (
    <HyperManagementElements options={options} hyper={hyperPromise}>
      <PaymentMethodsManagementForm />
    </HyperManagementElements>
  )}
</div>
```

#### 2.6 Add the Payment Methods Management Element

Add the `PaymentMethodsManagementElement` to your Payment Management Form. This embeds an iframe with a dynamic form that displays saved payment methods, allowing your customer to see all their saved payment methods and delete them.

```js
<PaymentMethodsManagementElement id="payment-methods-management-element" />
```
{% endtab %}

{% tab title="Javascript" %}
#### 2.1 Define the Payment Methods Management Form

Add one empty placeholder `div` to your checkout form for each Widget that you’ll mount.

```js
<form id="payment-methods-management-form">
  <div id="payment-methods-management-element">
   <!--HyperLoader injects the Payment Methods Management-->
  </div>
</form>
```

#### 2.1 Fetch the Ephemeral Key and mount the Payment Methods Management Element

Make a request to the endpoint on your server to create a new Ephemeral Key. The `ephemeralKey` returned by your endpoint is used to fetch all the customer saved payment methods.

> Important: Make sure to never share your API key with your client application as this could potentially compromise your payment flow

Following this, create a `paymentMethodsManagement` and mount it to the placeholder `div` in your payment form. This embeds an iframe with a dynamic form that displays saved payment methods, allowing your customer to see all their saved payment methods and delete them.

```js
// Fetches an ephemeral key and captures the secret
async function initialize() {
  const response = await fetch("/create-ephemeral-key", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({customer_id: "hyperswitch_sdk_demo_id"}),
  });
  const { ephemeralKey } = await response.json();
  
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
      const paymentMethodsManagementElements = hyper.paymentMethodsManagementElements({ appearance, ephemeralKey });
      const paymentMethodsManagement = paymentMethodsManagementElements.create("paymentMethodsManagement");
      paymentMethodsManagement.mount("#payment-methods-management-element");
  };
  document.body.appendChild(script);
}
```
{% endtab %}
{% endtabs %}

Congratulations! Now that you have integrated the Hyperswitch Payment Methods Management on your app, you can customize the it to blend with the rest of your app.
