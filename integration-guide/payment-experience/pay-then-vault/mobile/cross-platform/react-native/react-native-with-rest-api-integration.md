---
description: >-
  Integrate Juspay Hyperswitch SDK to your React Native App using
  hyperswitch-node
icon: puzzle-piece
---

# React Native with REST API Integration

{% hint style="info" %}
Use this guide to integrate the Juspay Hyperswitch React Native SDK to your React Native app. You can use the following Demo App as a reference with your Hyperswitch credentials to test the setup.
{% endhint %}

#### Find the Demo App

Find the demo app [here](https://github.com/juspay/react-native-hyperswitch)

Before proceeding with these steps, please ensure that your payment methods are configured here.

#### Requirements

* Android 7.0 (API level 24) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 12.4 and above
* CocoaPods
* npm

#### 1. Setup the server

Follow the Server Setup section.

#### 2. Build checkout page on the client

**2.1 Install the `@juspay-tech/react-native-hyperswitch` library**

Install the packages and import it into your code

```bash
yarn add @juspay-tech/react-native-hyperswitch
or
npm install @juspay-tech/react-native-hyperswitch
```

**2.2 Peer Dependencies**

Install the following dependencies

```js
yarn add react-native-inappbrowser-reborn
yarn add react-native-svg
yarn add @sentry/react-native
```

**2.3 iOS Only**

Run `pod install` in iOS folder

```js
pod install
```

**2.4 Initialize Hyperswitch**

Initialize Hyperswitch once using your publishable key and profile ID. Reuse the same initialized instance throughout your application.

```js
import { Hyperswitch } from "@juspay-tech/react-native-hyperswitch";

const hyper = await Hyperswitch.init({
      publishableKey: 'pk_snd_xxxxxxxx',   // from Hyperswitch dashboard
      profileId: 'pro_xxxxxxxx',           // your profile id
      // environment: 'SANDBOX',           // 'PROD' (default) | 'SANDBOX' | 'INTEG'
    });
```

Keep the Hyperswitch secret API key on your backend only. The app should never handle it.

#### 3. Complete the checkout on the client

**3.1 Get `sdk_authorization` from your Backend**

Call your payment-creation endpoint. Its JSON response must contain `sdk_authorization`.

```js
const response = await fetch('https://your-server.com/create-payment-intent', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ amount: 6500, currency: 'USD', customer_id: 'cust_123' }),
});

const { sdk_authorization } = await response.json();
```

**3.2 Create a Payment Session**

Pass the `sdk_authorization` returned by your backend to `initPaymentSession`.

```js
const session = await hyper.initPaymentSession({
  sdkAuthorization: sdk_authorization,
});
```

**3.3 Present the Payment Sheet**

Call `presentPaymentSheet()` on the payment session and handle the returned result.

```js
const checkout = async () => {
  const result = await session.presentPaymentSheet({
    merchantDisplayName: 'My Store',            // required
    appearance: { theme: 'Glass' },
  });

  if (result.status === "completed") {
    // The Payment Sheet completed the payment flow.
  } else if (result.status === "canceled") {
    // The customer canceled or closed the Payment Sheet.
  } else {
    // The payment flow failed. See result.message.
    console.log(result.message);
  }
};

return (
  <Screen>
    <Button
      variant="primary"
      title="Checkout"
      onPress={openPaymentSheet}
    />
  </Screen>
);
```

**3.4 Handle the Result**

| `result.status` | Meaning                                            | Recommended app behavior                                                           |
| --------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `completed`     | The Payment Sheet completed the payment flow.      | Show a success state and ask the backend to verify the payment before fulfillment. |
| `canceled`      | The customer closed or canceled the Payment Sheet. | Return to checkout and allow the customer to try again.                            |
| `failed`        | The payment flow failed.                           | Display `result.message` when appropriate and allow a retry.                       |

{% hint style="danger" %}
Retrieve the **payment status from the Juspay Hyperswitch backend** to determine the final (terminal) status of the transaction. Do not rely solely on the status returned by the SDK, as it may not always represent the definitive outcome of the payment.
{% endhint %}

{% hint style="warning" %}
**Collect Billing Address From Wallet** should be enabled in the Hyperswitch Dashboard for wallet payment methods to work.
{% endhint %}

**Important Notes**

* Initialize Hyperswitch once and reuse the same instance throughout the application.
* Create a new payment session using the latest `sdk_authorization` returned by the backend.
* Do not place the Hyperswitch secret API key in the React Native application.

Congratulations! Now that you have integrated the payment sheet
