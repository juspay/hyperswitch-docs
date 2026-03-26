---
description: Set up the Hyperswitch backend application to handle payment processing and orchestration
icon: input-numeric
---

# Payment Widget

The **PaymentWidget** component renders an **embedded, inline payment form directly inside your screen**, instead of opening a modal payment sheet. This approach is useful for **custom checkout pages** where you want full control over layout and UI.

## Find the demo app [here](https://github.com/juspay/react-native-hyperswitch/tree/main/example)

## 1. Basic Usage

### 1.1 Install the react native sdk

```shellscript
npm install @juspay-tech/react-native-hyperswitch
# or
yarn add @juspay-tech/react-native-hyperswitch
```

#### 1.1.1 Install Peer Dependencies

The SDK requires the following peer dependencies to be installed in your project:

```shellscript
yarn add react-native-inappbrowser-reborn
yarn add react-native-svg
yarn add @sentry/react-native
# or
npm install react-native-inappbrowser-reborn
npm install react-native-svg
npm install @sentry/react-native
```

### 1.2 Wrap your app with `HyperProvider`

To initialize Hyperswitch in a React Native application, wrap your payment screen with the **HyperProvider** component. The **publishable key** is required and must be provided to the `HyperProvider` during initialization.

```js
import { HyperProvider } from "@juspay-tech/react-native-hyperswitch ";

function App() {
  return (
    <HyperProvider publishableKey="YOUR_PUBLISHABLE_KEY" profileId="YOUR_PROFILE_ID">
      // Your app code here
    </HyperProvider>
  );
}
```

### 1.3 Fetch the PaymentIntent client Secret

Send a network request to the backend endpoint created in the previous step to retrieve the **clientSecret**. This **clientSecret** returned from the endpoint is required to complete the payment.

```js
useEffect(() => {
    fetch('https://your-server.com/create-payment-intent', { method: 'POST' })
      .then((res) => res.json())
      .then(({ clientSecret, sdkAuthorization, }) => {
        setClientSecret(clientSecret));
        setAuthorization(sdkAuthorization);
      }
}, []);
```

### 1.4 Render your Payment widget

Use the **Hyperswitch `PaymentWidget`** component to render an embedded payment form

```js
import { PaymentWidget } from '@juspay-tech/react-native-hyperswitch';

export default function PaymentUI() {
  // rest of your logic
  return (
    <PaymentWidget
      widgetId="checkout-widget"
      options={{
        clientSecret,
        sdkAuthorization,
        appearance: { theme: 'light' },
      }}
      onPaymentResult={(result) => {
        if (result.errorMessage) {
          // Payment failed
          console.error('Payment failed:', result.errorMessage);
        } else if (result.status === 'succeeded') {
          // Payment succeeded
          console.log('Payment succeeded!');
        } else if (result.status === 'cancelled') {
          // User cancelled the payment
        }
      }}
      style={{ width: '100%', height: 600 }}
    />
  );
}
```

Avoid placing the `PaymentWidget` inside a `ScrollView`. If necessary, ensure that the parent scroll is disabled while the user interacts with the widget to prevent scrolling conflicts.

### 1.5 `onPaymentResult` Callback

The `onPaymentResult` callback is triggered when the payment flow finishes. It provides a result object containing the payment outcome.

```
onPaymentResult={(result) => {
  console.log(result);
}}
```

```
// type PaymentWidgetResult:  {
    status?: string;        // "succeeded", "cancelled", or "Failed"
    errorMessage?: string;  // Present if an error occurred
}
```

#### **Congratulations! You have successfully integrated the Payment Widget into your application.**

### Props

**`widgetId`** `string` · Required

A unique identifier for the widget instance.

### 

**`options`** `PresentPaymentSheetParams` · Required

Configuration and appearance options.&#x20;

When using `PaymentWidget`, pass the `clientSecret` & `sdkAuthorization` here.

For more customizations follow [this](customization.md)

### 

**`onPaymentResult`** `(result: PaymentWidgetResult) => void` · Optional

Callback triggered when the payment completes, fails, or is cancelled.

### 

**`style`** `StyleProp<ViewStyle>` · `width` & `height` required

Defines the size and layout of the widget container.

