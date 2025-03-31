---
description: Integrate hyperswitch SDK to your React Native App using hyperswitch-node
---

# React Native with Node Backend

{% hint style="info" %}
Use this guide to integrate `hyperswitch` SDK to your React Native app. You can use the following Demo App as a reference with your Hyperswitch credentials to test the setup.
{% endhint %}

## [<mark style="color:blue;">Demo App</mark>](https://github.com/juspay/hyperswitch-sdk-react-native)

**Before following these steps, please configure your payment methods** [here](../../../payment-flows-and-management/quickstart/payment-methods-setup/cards.md).

## Requirements

* Android 5.0 (API level 21) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 12.4 and above
* CocoaPods
* npm

## 1. Setup the server

Follow the [Server Setup](../web/server-setup.md) section.

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
yarn add react-native-code-push
yarn add react-native-gesture-handler
yarn add react-native-inappbrowser-reborn
yarn add react-native-safe-area-context
yarn add react-native-svg
yarn add @sentry/react-native
yarn add react-native-pager-view
yarn add react-native-screens
yarn add react-native-hyperswitch-kount
yarn add react-native-klarna-inapp-sdk
```

**Note:** If you encounter any issues with `react-native-klarna-inapp-sdk`, please remove it from the dependencies.

### 2.3 iOS Only

Run `pod install` in iOS folder

<pre class="language-js"><code class="lang-js"><strong>pod install
</strong></code></pre>

### 2.4 Android Only

In the Android Folder inside strings.xml file `(android/app/src/main/res/values/strings.xml)` add the below line

```
<string name="CodePushDeploymentKey">HyperswitchRNDemo</string>
```

In the `android/settings.gradle` file, add the following line to link react-native-code-push:

```
include(":react-native-code-push");

project(":react-native-code-push").projectDir = new File(
  rootProject.projectDir,
  "../node_modules/react-native-code-push/android/app"
);
```

In the Android folder inside main (android/app/src/main/AndroidManifest.xml) add these below lines to the existing code.

```
<manifest xmlns:tools="http://schemas.android.com/tools">
  <application
    tools:replace="android:allowBackup">
    <!-- Other existing elements in the <application> tag -->
  </application>
</manifest>
```

### 2.5 Add `HyperProvider` to your React Native app

Use `HyperProvider` to ensure that you stay PCI compliant by sending payment details directly to Hyperswitch server.

```js
import { HyperProvider } from "@juspay-tech/hyperswitch-sdk-react-native";
```

### 2.6 Use `HyperProvider`

To initialize Hyperswitch in your React Native app, wrap your payment screen with the HyperProvider component. Only the API publishable key in publishableKey is required. The following example shows how to initialize Hyperswitch using the HyperProvider component.

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
  const paymentSession = await initPaymentSession(params);
  setPaymentSession(_=>paymentSession)
};

useEffect(() => {
  initializePaymentSheet();
}, []);
```

### 3.4 Handle Payment Response

To display the Payment Sheet, integrate a "Pay Now" button within the checkout page, which, when clicked, invokes the presentPaymentSheet() function. This function will return an asynchronous payment response with various payment status.

```js
  const openPaymentSheet = async () => {
    console.log("Payment Session Params --> ", paymentSession);
    const status = await presentPaymentSheet(paymentSession);
    console.log('presentPaymentSheet response: ', status);
    const {error, paymentOption} = status;
    if (error) {
      switch (error.code) {
        case 'cancelled':
          console.log('cancelled', `PaymentSheet was closed`);
          break;
        case 'failed':
          console.log('failed', `Payment failed`);
          break;
        default:
          console.log('status not captured', 'Please check the integration');
          break;
      }

      console.log(`Error code: ${error.code}`, error.message);
    } else if (paymentOption) {
      switch (paymentOption.label) {
        case 'succeeded':
          console.log('succeeded', `Your order is succeeded`);
          break;
        case 'requires_capture':
          console.log('requires_capture', `Your order is requires_capture`);
          break;
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

Congratulations! Now that you have integrated the payment sheet&#x20;
