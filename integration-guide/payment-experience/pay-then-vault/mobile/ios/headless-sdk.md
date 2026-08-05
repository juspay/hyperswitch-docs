---
description: >-
  Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your checkout UI.
icon: block-brick
---

# Headless SDK

#### Customize the payment experience using Headless functions

**1. Initialize the Juspay Hyperswitch SDK**

Initialize Hyperswitch Headless SDK onto your app with your publishable key.&#x20;

To get a `publishableKey` and `profileId`, refer to your Hyperswitch dashboard [here](https://app.hyperswitch.io/developers).

```swift
// pod 'hyperswitch-sdk-ios'
import Hyperswitch

let hyperswitchConfiguration = HyperswitchConfiguration(
    publishableKey: publishableKey,
    profileId: profileId
)
let hyperswitch = Hyperswitch(configuration: hyperswitchConfiguration)
```

**2. Create a Payment Intent**

Make a request to the endpoint on your server to create a new Payment. The `sdkAuthorization` returned by your endpoint is used to initialize the payment session.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security.
{% endhint %}

**3. Initialize your Payment Session**

Initialize a Payment Session by passing the clientSecret to the `initPaymentSession`

```swift
let paymentSessionConfiguration = PaymentSessionConfiguration(
    sdkAuthorization: sdkAuthorization
)

let paymentSession = hyperswitch.initPaymentSession(
    configuration: paymentSessionConfiguration
)
```

| options (Required)          | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| `sdkAuthorization (string)` | **Required.** Required to use as the identifier of the payment. |

**4. Craft a customized payments experience**

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

**Payload for** `confirmWithCustomerLastUsedPaymentMethod(callback)` &#x20;

| options (Required)    | Description                       |
| --------------------- | --------------------------------- |
| `callback (function)` | Callback to get confirm response. |
