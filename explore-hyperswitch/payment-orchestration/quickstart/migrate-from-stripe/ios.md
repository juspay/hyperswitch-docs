---
description: >-
  Integrate mobile SDK to deliver seamless in-app payment experiences
---
# iOS

{% hint style="info" %}
Migrate from Stripe on your iOS app in less than 15 mins!
{% endhint %}

If you are already integrated with Stripe as your payment processor, we have made migrating to Hyperswitch much simpler for you. And we will be adding quick migration support for more leading payment processors in the near future. And once you migrate, get immediate access to 40+ payment processors and features such as Smart Router, Digital Payments Manager and many more.

### iOS - Node Backend and Swift Frontend

The code from your Stripe integration to be removed and replaced is explained below in a step by step manner.

**Step 1:** Install Hyperswitch’s SDK and server side dependencies from npm

```js
 $ npm install @juspay-tech/react-native-Hyperswitch $ npm install @juspay-tech/hyper-node --save-dev
```

Install peer dependencies:

```js
 $ npm install react-native-code-push react-native-gesture-handler react-native-inappbrowser-reborn react-native-pager-view react-native-safe-area-context react-native-screens react-native-svg
```

**Step 2:** Change the API key on the server side and modify the paymentIntent endpoint from your server side. You can get the API key from [Developers](https://app.hyperswitch.io/developers) page on the dashboard.

```js
// from
const Stripe = require("Stripe")("your_stripe_api_key");
// to
const Stripe = require("@juspay-tech/hyper-node")("your_hyperswitch_api_key");
```

**Step 3:** Add these sources at the beginning of you podfile

```ruby
source 'https://GitHub.com/Juspay/Hyperswitch-pods.git'
source 'https://cdn.cocoapods.org/'
```

_**Step 4:**_ Replace StripePaymentSheet with Hyperswitch in your podfile

```ruby
# from
pod 'StripePaymentSheet'
# to
pod 'Hyperswitch', '1.0.0-alpha01'
```

**Step 5:** Change these imports in your project

```swift
// from
import StripePaymentSheet
// to
import Hyperswitch
```

**Step 6:** Run your application to make a test payment. And verify the status of the transaction on Hyperswitch Dashboard and Stripe Dashboard. Congratulations ! You have successfully integrated Hyperswitch to your payments stack and you now have access to a suite of 40+ payment processors and acquirers.
