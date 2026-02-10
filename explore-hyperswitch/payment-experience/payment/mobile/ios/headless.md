---
description: >-
  Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your checkout UI.
icon: table-cells-large
---

# Headless SDK

### Customize the payment experience using Headless functions

#### 1. Initialize the Hyperswitch SDK

Initialize  Hyperswitch Headless SDK onto your app with your publishable key. To get a Publishable Key please find it [here](https://app.hyperswitch.io/developers).

```swift
// pod 'hyperswitch-sdk-ios'
paymentSession = PaymentSession(publishableKey: publishableKey)
```

#### 2. Create a Payment Intent

Make a request to the endpoint on your server to create a new Payment. The `clientSecret` returned by your endpoint is used to initialize the payment session.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security
{% endhint %}

#### 3. Initialize your Payment Session

Initialize a Payment Session by passing the clientSecret to the `initPaymentSession`

```swift
paymentSession?.initPaymentSession(paymentIntentClientSecret: paymentIntentClientSecret)
```

| options (Required)      | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `clientSecret (string)` | **Required.**  Required to use as the identifier of the payment. |

#### 4. Craft a customized payments experience

Using the `paymentSession` object, the default customer payment method data can be fetched, using which you can craft your own payments experience. The `paymentSession` object also exposes a `confirmWithCustomerDefaultPaymentMethod` function, using which you can confirm and handle the payment session.

<pre class="language-swift"><code class="lang-swift">private var handler: PaymentSessionHandler?
 
func initSavedPaymentMethodSessionCallback(handler: PaymentSessionHandler)-> Void {
    self.handler = handler
}
    
@objc func launchHeadless(_ sender: Any) {
    paymentSession!.getCustomerSavedPaymentMethods(initSavedPaymentMethodSessionCallback)
<strong>}
</strong>
@objc func confirmPayment(_ sender: Any) {
    let paymentMethod = self.handler!.getCustomerLastUsedSavedPaymentMethodData(callback)
}
    
@objc func confirmPayment(_ sender: Any) {
    self.handler!.confirmWithLastUsedSavedPaymentMethodData(callback)
}
</code></pre>

&#x20;

**Payload for** `confirmWithCustomerLastUsedPaymentMethod(callback)`

<table><thead><tr><th width="296">options (Required)</th><th>Description</th></tr></thead><tbody><tr><td><code>callback (function)</code></td><td>Callback to get confirm response.</td></tr></tbody></table>

