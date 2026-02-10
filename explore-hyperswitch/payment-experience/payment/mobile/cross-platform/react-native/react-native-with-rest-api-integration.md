---
description: Integrate hyperswitch SDK to your React Native App using hyperswitch-node
icon: puzzle-piece
---

# React Native with REST API Integration

{% hint style="info" %}
Use this guide to integrate `hyperswitch` SDK to your React Native app. You can use the following Demo App as a reference with your Hyperswitch credentials to test the setup.
{% endhint %}

## [<mark style="color:blue;">Demo App</mark>](https://github.com/juspay/hyperswitch-sdk-react-native)

**Before following these steps, please configure your payment methods** [here](../../../../../payment-orchestration/quickstart/payment-methods-setup/cards.md).

## Requirements

* Android 7.0 (API level 24) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 12.4 and above
* CocoaPods
* npm

## 1. Setup the server

Follow the [Server Setup](../../../server-setup.md) section.

## 2. Build checkout page on the client

### 2.1 Install the `hyperswitch-sdk-react-native` libraries

Install the packages and import it into your code

```bash
$ yarn add @juspay-tech/hyperswitch-sdk-react-native
or
$ npm install @juspay-tech/hyperswitch-sdk-react-native
```

### 2.2 Peer Dependencies

Install the following dependencies

```js
yarn add react-native-gesture-handler
yarn add react-native-inappbrowser-reborn
yarn add react-native-safe-area-context
yarn add react-native-svg
yarn add @sentry/react-native
yarn add react-native-pager-view
yarn add react-native-screens
yarn add react-native-hyperswitch-kount
```

### 2.3 iOS Only

Run `pod install` in iOS folder

```js
pod install
```

### 2.4 Use `HyperProvider`

To initialise Hyperswitch in your React Native app, wrap your payment screen with the HyperProvider component. Only the API publishable key in publishableKey is required. The following example shows how to initialise Hyperswitch using the HyperProvider component.

```js
import { HyperProvider } from '@juspay-tech/hyperswitch-sdk-react-native';
function App() {
  return (
    <HyperProvider publishableKey="YOUR_PUBLISHABLE_KEY">
      // Your app code here
    </HyperProvider>
  );
}
```

## 3. Complete the checkout on the client

### 3.1 import useHyper to your checkout page

In the checkout of your app, import useHyper() hook

```js
import { useHyper } from '@juspay-tech/hyperswitch-sdk-react-native';
```

### 3.2 Fetch the PaymentIntent client Secret

Make a network request to the backend endpoint you created in the previous step. The clientSecret returned by your endpoint is used to complete the payment.

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

### 3.3 Collect Payment details

Call initPaymentSession from the useHyper hook to customise paymentsheet, billing or shipping addresses and initialize paymentsheet

```js
const { initPaymentSession, presentPaymentSheet } = useHyper();
const [ paymentSession, setPaymentSession ]=React.useState(null);
const initializePaymentSheet = async () => {
  const { clientSecret } = await fetchPaymentParams();

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
      appearance: customAppearance,
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

### 3.4 Handle Payment Response

To display the Payment Sheet, integrate a "Pay Now" button within the checkout page, which, when clicked, invokes the presentPaymentSheet() function. This function will return an asynchronous payment response with various payment status.

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
          console.log('failed', `Payment is failed`);
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
Please retrieve the payment status from the Hyperswitch backend to get the terminal status of the payment. Do not rely solely on the status returned by the SDK, as it may not always reflect the final state of the transaction.
{% endhint %}

Congratulations! Now that you have integrated the payment sheet
