---
icon: plug-circle-bolt
---

# Hyperwidget Integration Guide

Once the merchant signs up onto the unified dashboard, they’ll get their API keys and can enable the APMs <> PSP combinations that they would like to provide on their checkout.&#x20;

Hyperswitch provides a code transformer that allows the merchant to leverage their existing integration (with PSP or middle layer) and make a call to Hyperswitch server with minimal changes. Hyperwidget acts as a Unified wrapper on top of all major APMs and simplifies up-scaling or down-scaling of these APMs across one or multiple PSPs.&#x20;

The unified dashboard offers the merchants ability to enable or disable APMs via any PSP. The dashboard also offers capabilities like - Analytics, Operations, Refunds, Chargebacks, and Reconciliation.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Supported APM features:

| Payment Method | Region  | Type         | Supported flow          | Shipping Address availability | Billing address availability |
| -------------- | ------- | ------------ | ----------------------- | ----------------------------- | ---------------------------- |
| Paypal         | US + EU | Wallet       | SDK flow, Redirect flow | Yes\*                         | Yes                          |
| Apple Pay      | US + EU | Wallet       | SDK flow                | Yes\*                         | Yes                          |
| Google Pay     | US + EU | Wallet       | SDK flow                | Yes\*                         | Yes                          |
| Paze           | US + EU | Wallet       | SDK flow                | No                            | Yes                          |
| Samsung Pay    | US + EU | Wallet       | SDK flow                | No                            | No                           |
| Ali Pay        | US + EU | Wallet       | Redirect flow           | Yes                           | Yes                          |
| WeChat Pay     | US + EU | Wallet       | Redirect flow           | Yes                           | Yes                          |
| Affirm         | US + EU | BNPL         | Redirect flow           | Yes                           | Yes                          |
| Klarna         | US + EU | BNPL         | SDK flow, Redirect flow | Yes\*                         | Yes                          |
| Afterpay       | US + EU | BNPL         | Redirect flow           | Yes                           | Yes                          |
| iDEAL          | EU      | Bank-to-bank | Redirect flow           | Yes                           | Yes                          |
| SEPA           | EU      | Bank-to-bank | Redirect flow           | Yes                           | Yes                          |

\*only in the SDK flow

### Steps to integrate Hyperwidgets:&#x20;

To start collecting payments via the APM of your choice, follow these simple steps: ​

* [Install the Hyperwidgets SDK following these steps. ​](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/web/node-and-react)
* [For customization and depending upon the merchant requirements for JS and React Integration.​](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide/web)

#### For React Integration:

```javascript
npm install @juspay-tech/hyper-js
npm install @juspay-tech/react-hyper-js
```

```javascript
import React, { useState, useEffect } from "react";
import { loadHyper } from "@juspay-tech/hyper-js";
import { hyperElements } from "@juspay-tech/react-hyper-js";
​
const hyperPromise = loadHyper("YOUR_PUBLISHABLE_KEY",{
   customBackendUrl: "YOUR_BACKEND_URL",
   //You can configure this as an endpoint for all the api calls such as session, payments, confirm call.
});
​
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
​
<div className="App">
 {clientSecret && (
   <HyperElements options={options} hyper={hyperPromise}>
     <CheckoutForm />
   </HyperElements>
 )}
</div>
```

Now add this component to the PaymentElement -&#x20;

```javascript
var unifiedCheckoutOptions = {
 wallets: {
   walletReturnUrl: "https://example.com/complete",
   //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
 },
};

<UnifiedCheckout id="unified-checkout" options={unifiedCheckoutOptions} />

```

{% content-ref url="../../../explore-hyperswitch/merchant-controls/click-to-pay/" %}
[click-to-pay](../../../explore-hyperswitch/merchant-controls/click-to-pay/)
{% endcontent-ref %}
