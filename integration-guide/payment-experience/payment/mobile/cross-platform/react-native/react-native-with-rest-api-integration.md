---
description: >-
  Integrate Juspay Hyperswitch SDK to your React Native App using
  hyperswitch-node
icon: puzzle-piece
metaLinks:
  alternates:
    - react-native-with-rest-api-integration.md
---

# React Native with REST API Integration

{% hint style="info" %}
Use this guide to integrate the Juspay Hyperswitch React Native SDK to your React Native app. You can use the following Demo App as a reference with your Hyperswitch credentials to test the setup.
{% endhint %}

### Find the Demo App

Find the demo app [here](https://github.com/juspay/react-native-hyperswitch)

Before proceeding with these steps, please ensure that your payment methods are configured [here](../../../../../../other-features/payment-orchestration/quickstart/payment-methods-setup/cards.md).

### Requirements

* Android 7.0 (API level 24) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 12.4 and above
* CocoaPods
* npm

### 1. Setup the server

Follow the [Server Setup](../../../server-setup.md) section.

### 2. Build checkout page on the client

#### 2.1 Install the `@juspay-tech/react-native-hyperswitch` library

Install the packages and import it into your code

```bash
yarn add @juspay-tech/react-native-hyperswitch
or
npm install @juspay-tech/react-native-hyperswitch
```

#### 2.2 Peer Dependencies

Install the following dependencies

```js
yarn add react-native-inappbrowser-reborn
yarn add react-native-svg
yarn add @sentry/react-native
```

#### 2.3 iOS Only

Run `pod install` in iOS folder

```js
pod install
```

#### 2.4 Use `HyperProvider`

To initialize Juspay Hyperswitch in your React Native app, wrap your payment screen with the **HyperProvider** component. The only required configuration is the **API publishable key**, which should be provided through the `publishableKey` prop.

```js
import { HyperProvider } from '@juspay-tech/react-native-hyperswitch';
function App() {
  return (
    <HyperProvider publishableKey="YOUR_PUBLISHABLE_KEY" profileId="YOUR_PROFILE_ID">
      // Your app code here
    </HyperProvider>
  );
}
```

### 3. Complete the checkout on the client

#### 3.1 import useHyper to your checkout page

In your checkout screen, import and use the **`useHyper()`** hook to access Juspay Hyperswitch payment methods and functionality.

```js
import { useHyper } from '@juspay-tech/react-native-hyperswitch';
```

#### 3.2 Fetch the PaymentIntent client Secret

Send a network request to the backend endpoint created in the previous step to retrieve the **clientSecret**. The **clientSecret** returned by this endpoint is required to complete the payment.

```js
const fetchPaymentParams = async () => {
  const response = await fetch(`${API_URL}/create-payment`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ items: [{ id: "xl-tshirt" }], country: "US" }),
  });
  const val = await response.json();
  return val;
};
```

#### 3.3 Collect Payment details

Call **`initPaymentSession`** from the **`useHyper`** hook to initialize the Payment Sheet and configure options such as **appearance, billing details, or shipping address** before presenting the payment flow.

```js
const { initPaymentSession, presentPaymentSheet } = useHyper();
const [ paymentSession, setPaymentSession ]=React.useState(null);
const initializePaymentSheet = async () => {
  const { clientSecret, sdkAuthorization } = await fetchPaymentParams();

  const customAppearance = {
    colors: {
      light: {
        primary: "#00FF00",
      },
    },
  };
  const params={
      merchantDisplayName: "Example, Inc.",
      clientSecret: clientSecret,
      sdkAuthorization: sdkAuthorization,
      appearance: customAppearance
  }
  const result = await initPaymentSession(params);
  if (result.error) {
        console.error('Payment session initialization failed:', result.error);
  } else {
      setPaymentSession(_ => paymentSession)
  }
};

useEffect(() => {
  initializePaymentSheet();
}, []);
```

#### 3.4 Handle Payment Response

To display the **Payment Sheet**, add a **"Pay Now"** button to your checkout page. When the button is pressed, call the **`presentPaymentSheet()`** function.

This function returns an **asynchronous response** containing the payment result, including the payment status.

```js
  const openPaymentSheet = async () => {
    const result = await presentPaymentSheet(paymentSession);

    if (result.error) {
      console.log(`Error code: ${error.code}`, error.message);
    } else if (result.status) {
      switch (result.status) {
        case 'succeeded':
          console.log('succeeded', `Your order is succeeded`);
          break;
        case 'requires_capture':
          console.log('requires_capture', `Your order is requires_capture`);
          break;
        case 'cancelled':
          console.log('cancelled', `Payment is cancelled`);
        case 'failed':
          console.log('failed', `Payment is failed');
        default:
          console.log('status not captured', 'Please check the integration');
          break;
      }
    } else {
      console.log('Something went wrong', 'Please check the integration');
    }
  };


return (
  <Screen>
    <Button variant="primary" title="Checkout" onPress={openPaymentSheet} />
  </Screen>
);
```

{% hint style="danger" %}
Retrieve the **payment status from the Juspay Hyperswitch backend** to determine the final (terminal) status of the transaction. Do not rely solely on the status returned by the SDK, as it may not always represent the definitive outcome of the payment.
{% endhint %}

Congratulations! Now that you have integrated the payment sheet
