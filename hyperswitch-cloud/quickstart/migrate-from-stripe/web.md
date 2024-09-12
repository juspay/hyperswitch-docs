---
description: Migrate from Stripe on your web app
---

# Web

{% hint style="info" %}
Migrate from Stripe on your web app in less than 15 mins!
{% endhint %}

## Migrate from Stripe

If you are already integrated to Stripe as your payment processor, we have made migrating to Hyperswitch much simpler for you. And once you migrate, get immediate access to 40+ payment processors and features such as Smart Router, Unified analytics and many more.

{% hint style="info" %}
Stripe’s `paymentRequestButton` is available under Hyperswitch’s UnifiedCheckout, therefore importing UnifiedCheckout would be sufficient.
{% endhint %}

The code from your Stripe integration to be removed and replaced is explained below in a step by step manner for both React and HTML frontend. You can find the details for both below.

<details>

<summary>Web - Node Backend and React Frontend</summary>

**Step 1:** Install Hyperswitch's SDK and server side dependencies from npm

```js
  $ npm install @juspay-tech/react-hyper-js
  $ npm install @juspay-tech/hyper-js
  $ npm install @juspay-tech/hyperswitch-node
```

**Step 2:** Change the API key on the server side and modify the paymentIntent endpoint from your server side. You can get the API key from [Developers](https://app.hyperswitch.io/developers) page on the dashboard.

```js
// from
const stripe = require("stripe")("your_stripe_api_key");
// to
const hyper = require("@juspay-tech/hyperswitch-node")(
  "your_hyperswitch_api_key"
);
```

```js
// from
const paymentIntent = await stripe.paymentIntents.create({
// to
const paymentIntent = await hyper.paymentIntents.create({
```

**Step 3:** Call loadHyper() with your Hyperswitch publishable key to configure the SDK library, from your website

```js
// from
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
// to
import { loadHyper } from "@juspay-tech/hyper-js";
import { hyperElements } from "@juspay-tech/react-hyper-js";
```

```js
// from
const stripePromise = loadStripe("your_stripe_publishable_key");
// to
const hyperPromise = loadHyper("your_hyperswitch_publishable_key");
```

**Step 4:** Configure your checkout form to import from Hyperswitch

```js
//from
import {
  PaymentElement,
  useStripe,
  useElements,
} from "@stripe/react-stripe-js";
//to
import {
  UnifiedCheckout,
  useStripe,
  useElements,
} from "@juspay-tech/react-hyper-js";
```

**Step 5:** Run your application to make a test payment. And verify the status of the transaction on Hyperswitch Dashboard and Stripe Dashboard. Congratulations ! You have successfully integrated Hyperswitch to your payments stack and you now have access to a suite of 40+ payment processors and acquirers.

</details>

<details>

<summary>Web - Node Backend and HTML Frontend</summary>

**Step 1:** Install Hyperswitch's node server dependency from npm

```js
  $ npm install @juspay-tech/hyperswitch-node
```

**Step 2:** Change the API key on the server side and modify the paymentIntent endpoint from your server side

```js
// from
const stripe = require("stripe")("your_stripe_api_key");
// to
const hyper = require("@juspay-tech/hyperswitch-node")(
  "your_hyperswitch_api_key"
);
```

```js
// from
const paymentIntent = await stripe.paymentIntents.create({
// to
const paymentIntent = await hyper.paymentIntents.create({
```

**Step 3:** Load the Hyperswitch directly from beta.hyperswitch.io to remain PCI compliant while collecting the customer's payment details

```js
// from
<script src="https://js.stripe.com/v3/"></script>
// to
<script src="https://beta.hyperswitch.io/v1/HyperLoader.js"></script>
```

**Step 4:** Initiate the SDK with your Hyperswitch publishable key from your website

```js
// from
const stripe = Stripe("your_stripe_publishable_key");
// to
const hyper = Hyper("your_hyperswitch_publishable_key");
```

**Step 5:** Run your application to make a test payment. And verify the status of the transaction on Hyperswitch Dashboard and Stripe Dashboard. Congratulations ! You have successfully integrated Hyperswitch to your payments stack and you now have access to a suite of 40+ payment processors and acquirers.

</details>

Want an easy migration from Stripe for Apps? We got you covered. Follow the docs for Android, iOS and React Native apps.

