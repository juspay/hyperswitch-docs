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

_To integrate Web SDK, follow_ [_React with Node Integration_](node-and-react.md)_,_ [_HTML with Node Integration_](node-and-html.md) _and_ [_JS with REST API Integration_](vanilla-js-and-rest-api-integration.md)_._

### Integrate Mobile SDK

_To integrate mobile SDK, follow_ [_Kotlin with Node Integration_](../mobile/android/kotlin-with-node-backend.md)_,_ [_Swift with Node Integration_](../mobile/ios/swift-with-node-backend.md), [_React Native with Node Integration_](../mobile/cross-platform/react-native/react-native-with-node-backend.md)_, and_ [_Flutter with Node Integration_](../mobile/cross-platform/react-native-1/react-native-with-node-backend.md)

{% hint style="info" %}
In case your integrating the ExpressCheckout (mentioned later below), instead of creating multiple paymentIntents for the same customer session, you can also use [paymentsUpdate API](https://api-reference.hyperswitch.io/api-reference/payments/payments--update) for better analytics.
{% endhint %}
