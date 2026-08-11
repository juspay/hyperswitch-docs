---
description: >-
  The Google Pay & Apple Pay Element provides a unified wallet payment component
  for collecting payments through the supported native wallets. Render this
  element to present the appropriate wallet optio
icon: wallet
---

# Google Pay & Apple Pay Element

The **Google Pay & Apple Pay Element** provides a unified wallet payment component for collecting payments through the supported native wallets. Render this element to present the appropriate wallet option based on the user's device and platform.

Use the wallet buttons when **all** of these are true:

1. You are building a **custom checkout UI** (Elements). If you use `presentPaymentSheet`, wallets already appear inside the sheet — don't add these buttons too.
2. You want **one-tap express payment** at the top of your checkout (best conversion), instead of making users fill the card form.
3. The wallet is actually **relevant for the device**:
   * `ApplePayButton` → iOS only (requires a real device — Apple Pay does not run on the iOS Simulator).
   * `GooglePayButton` → Android only.
4. The wallet is **enabled for this payment**: the connector must be configured on your Hyperswitch dashboard (Apple Pay / Google Pay enabled + merchant certificates set up) and the payment method must be returned for the intent.

#### Find the Demo App

Find the demo app [here](https://github.com/juspay/react-native-hyperswitch/tree/main/example)

#### 1. Basic Usage

**1.1 Install the react native sdk**

```shellscript
npm install @juspay-tech/react-native-hyperswitch
# or
yarn add @juspay-tech/react-native-hyperswitch
```

**1.1.1 Install Peer Dependencies**

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

**1.2 Initialize Hyperswitch**

Initialize Hyperswitch once using your publishable key and profile ID. Reuse the same initialized instance throughout your application.

```js
import { Hyperswitch } from "@juspay-tech/react-native-hyperswitch";

const hyperPromise = Hyperswitch.init({
      publishableKey: 'pk_snd_xxxxxxxx',   // from Hyperswitch dashboard
      profileId: 'pro_xxxxxxxx',           // your profile id
      // environment: 'SANDBOX',           // 'PROD' (default) | 'SANDBOX' | 'INTEG'
    });
```

Keep the Hyperswitch secret API key on your backend only. The app should never handle it.

**1.2 Get `sdk_authorization` from your Backend**

Call your payment-creation endpoint. Its JSON response must contain `sdk_authorization`.

```js
const response = await fetch('https://your-server.com/create-payment-intent', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ amount: 6500, currency: 'USD', customer_id: 'cust_123' }),
});

const { sdk_authorization } = await response.json();
```

**1.3 Wrap your app with** `HyperElements`

To use HyperSwitch hooks and the Embedded UI in a React Native application, wrap your payment screen with the **HyperElements** component. During initialization, you must provide the required `sdkAuthorization` prop to `HyperElements`. This authorization is necessary for the SDK to initialize correctly.

```js
import { HyperElements } from '@juspay-tech/react-native-hyperswitch';

<HyperElements hyper={hyperPromise} options={{ sdkAuthorization }}>
  <CheckoutScreen />
</HyperElements>
```

**1.4 Pick per platform:**

```tsx
import { Platform } from 'react-native';
import { ApplePayButton, GooglePayButton } from '@juspay-tech/react-native-hyperswitch';

const WalletButton = Platform.OS === 'ios' ? ApplePayButton : GooglePayButton;
```

**1.5 Render the button (always mounted).**&#x20;

Never conditionally unmount it — if it's not mounted, it can't tell you whether the wallet is available:

```tsx
const [walletReady, setWalletReady] = useState(false);

<WalletButton
  widgetId={Platform.OS === 'ios' ? 'apple-pay-button' : 'google-pay-button'}
  options={{
    merchantDisplayName: 'My Store',
    appearance: { primaryButton: { height: 58, borderRadius: 12 } },
    subscribedEvents: ['PAYMENT_METHOD_STATUS'],
  }}
  onChange={(event) => {
    if (event.eventName === 'PAYMENT_METHOD_STATUS') setWalletReady(true);
  }}
  onPaymentResult={handleResult}
  style={{ height: 58 }}
/>
```

**1.6 Handle the result:**

```typescript
async function handleResult(result: PaymentResult) {
  if (result.status === 'completed') {
    // payment succeeded
  } else if (result.status === 'canceled') {
    // user dismissed the sheet
  } else {
    console.log(`${result.type}: ${result.message}`);
  }
}
```

Congratulations! 🎉 You have successfully integrated the **One-Tap Wallet Element** into your application.

\
**Differences**

| Payment input | Native wallet sheet (no typing) | In-app form (cards, other PMs, saved methods)    |
| ------------- | ------------------------------- | ------------------------------------------------ |
| Confirmation  | Automatic on sheet approval     | You call `confirmPayment(...)`                   |
| Platform      | iOS-only / Android-only         | Both platforms                                   |
| Result        | via `onPaymentResult` prop      | via `onPaymentResult` or `confirmPayment` return |
|               |                                 |                                                  |

That's it — the wallet buttons are fully self-driving: mount, wait for `PAYMENT_METHOD_STATUS`, handle `onPaymentResult`.

***

<br>
