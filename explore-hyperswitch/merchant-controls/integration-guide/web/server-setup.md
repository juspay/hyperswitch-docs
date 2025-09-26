---
icon: server
---

# Server Setup

### Create a payment using S2S Call

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

### Integrate Web SDK

_To integrate Web SDK, follow React , HTML  and JS with REST API Integration._

### Integrate Mobile SDK

_To integrate mobile SDK, follow Kotlin, Swift_ , _React Native , and Flutter with REST API Integration_

{% hint style="info" %}
In case your integrating the ExpressCheckout (mentioned later below), instead of creating multiple paymentIntents for the same customer session, you can also use [paymentsUpdate API](https://api-reference.hyperswitch.io/api-reference/payments/payments--update) for better analytics.
{% endhint %}
