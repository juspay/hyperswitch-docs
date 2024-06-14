---
description: Integrate hyper SDK to your React Native App using hyperswitch-node
---

# React Native with Node Backend (Beta)



{% hint style="info" %}
Currently in beta please contact to get early access
{% endhint %}

{% hint style="info" %}
Use this guide to integrate `hyper` SDK to your React Native app. You can use the following Demo App as a reference with your Hyperswitch credentials to test the setup.
{% endhint %}

## [<mark style="color:blue;">Demo App</mark>](https://github.com/aashu331998/Hyperswitch-React-Native-demo-app/archive/refs/heads/main.zip)

**Before following these steps, please configure your payment methods** [here](../../payment-methods-setup/cards.md).

## Requirements

* Android 5.0 (API level 21) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 12.4 and above
* CocoaPods
* npm

## 1. Setup the server

### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

### 1.2 Create a payment

Before creating a payment, import the hyper dependencies and initialize it with your API key. Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

```js
const hyper = require("@juspay-tech/hyperswitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the client\_secret obtained in the response to securely complete the payment on the client.

```js
// Create a Payment with the order amount and currency
app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      currency: "USD",
      amount: 100,
    });
    // Send publishable key and PaymentIntent details to client
    res.send({
      clientSecret: paymentIntent.client_secret,
    });
  } catch (err) {
    return res.status(400).send({
      error: {
        message: err.message,
      },
    });
  }
});
```

## 2. Build checkout page on the client

### 2.1 Install the `react-native-hyperswitch` libraries

Install the packages and import it into your code

```js
$ npm install @juspay-tech/hyperswitch-sdk-react-native

```

### 2.2 Peer Dependencies

Install the following dependencies

```js
yarn add react-native-code-push
yarn add react-native-gesture-handler
yarn add react-native-inappbrowser-reborn
yarn add react-native-klarna-inapp-sdk
yarn add react-native-safe-area-context
yarn add react-native-svg
yarn add @sentry/react-native

```

### 2.3 iOS Only

Run `pod install` in iOS folder

```js
pod install
```

### 2.4 Android Only

In the Android Folder inside strings.xml file(android/app/src/main/res/values/strings.xml) add the below line

```js
<string name="CodePushDeploymentKey">HyperswitchRNDemo</string>
```

In the Android Folder inside settings.gradle file add the following line

```js
include(":react-native-code-push");

project(":react-native-code-push").projectDir = new File(
  rootProject.projectDir,
  "../node_modules/react-native-code-push/android/app"
);
```

### 2.5 Add `HyperProvider` to your React Native app

Use `HyperProvider` to ensure that you stay PCI compliant by sending payment details directly to Hyperswitch server.

```js
import { HyperProvider } from "@juspay-tech/react-native-hyperswitch";
```

### 2.6 Use `HyperProvider`

To initialize Hyperswitch in your React Native app, wrap your payment screen with the HyperProvider component. Only the API publishable key in publishableKey is required. The following example shows how to initialize Hyperswitch using the HyperProvider component.

```js
import { HyperProvider } from "@juspay-tech/react-native-hyperswitch ";

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
import { useHyper } from "@juspay-tech/react-native-hyperswitch";
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

Call initPaymentSheet from the useHyper hook to customise paymentsheet, billing or shipping addresses and initialize paymentsheet

```js
const { initPaymentSession, presentPaymentSheet } = useHyper();
const [paymentSession,setPaymentSession]=React.useState(null);
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
  const status = await presentPaymentSheet(paymentSession);
  console.log("presentPaymentSheet response: ", status);
  const { error, paymentOption } = status;
  if (error) {
    switch (error.code) {
      case "cancelled":
        Alert.alert("cancelled", `PaymentSheet was closed`);
        break;
      case "failed":
        Alert.alert("failed", `Payment failed`);
        break;
      default:
        Alert.alert("status not captured", "Please check the integration");
        break;
    }

    Alert.alert(`Error code: ${error.code}`, error.message);
  } else if (paymentOption) {
    switch (paymentOption.label) {
      case "succeeded":
        Alert.alert("succeeded", `Your order is succeeded`);
        break;
      case "requires_capture":
        Alert.alert("requires_capture", `Your order is requires_capture`);
        break;
      default:
        Alert.alert("status not captured", "Please check the integration");
        break;
    }
  } else {
    Alert.alert("Something went wrong", "Please check the integration");
  }
};

return (
  <Screen>
    <Button variant="primary" title="Checkout" onPress={openPaymentSheet} />
  </Screen>
);
```

Congratulations! Now that you have integrated the Android SDK, you can customize the payment sheet to blend with the rest of your app.&#x20;
