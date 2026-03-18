---
icon: react
description: Integrate Hyperswitch with Expo to enable payments in React Native apps built with Expo.
---
# Expo integration

{% hint style="info" %}
**Note:** **Expo Go is not supported.**\
The Hyperswitch SDK uses native modules, so the app must be built with native Android and iOS code.
{% endhint %}

## 1. Install Required Dependencies

The Hyperswitch SDK has peer dependencies that must be installed before installing the SDK.

```
# Install peer dependencies
yarn add @sentry/react-native react-native-inappbrowser-reborn react-native-svg

# Install Hyperswitch SDK
yarn add @juspay-tech/react-native-hyperswitch
```

### 2. Prebuild the App

Generate the native **Android** and **iOS** folders:

```
npx expo prebuild --clean
```

This command will:

* Generate **Android and iOS native folders**
* Run **CocoaPods** for iOS dependencies
* Configure **TurboModule code generation**
* **Auto-link native modules**

### 3. Implement the Payment Flow

After completing the Expo setup, **follow the same steps as the React Native integration** to implement the payment flow:

1. Wrap your app with **HyperProvider**
2. Use the **useHyper()** hook
3. Initialize the payment session using **initPaymentSession**
4. Present the payment sheet using **presentPaymentSheet**

Refer to the [**React Native integration steps**](react-native-with-rest-api-integration.md) for the complete payment flow implementation.

