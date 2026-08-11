---
description: The embedded CVC Element that collects the cvc number.
icon: input-password
---

# CVC Element

The standalone **CVC** field is used **only** for **saved card** payments. Do **not** use it when collecting details for a new card, as the `PaymentElement` already includes CVC collection.

#### Find the Demo App

Find the demo app [here](https://github.com/juspay/react-native-hyperswitch/tree/main/example)

**When to use it**

Use `CardCVCElement` when **all** of these are true:

1. You are building a custom saved-payment-methods screen (your own UI, not the drop-in sheet).
2. The customer has a **saved card** (check `lastUsed.payment_method === 'card'`).
3. The saved card **requires CVV** to confirm (check `lastUsed.requires_cvv === true`).

If none of these apply, skip this widget entirely.

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

**1.4 Fetch saved payment methods** (inside `HyperElements`):

```tsx
const paymentSession = usePaymentSession();

const methodsSession = await paymentSession.getCustomerSavedPaymentMethods({
  hiddenPaymentMethods: ['paypal', 'google_pay', 'apple_pay'],
});
const lastUsed = await methodsSession.getCustomerLastUsedPaymentMethodData();

// optional
const defaultUsed = await methodsSession.getCustomerDefaultSavedPaymentMethodData(); 
```

**1.5 Decide whether CVC is needed:**

```tsx
const requiresCvc = lastUsed?.payment_method === 'card'; // && lastUsed.requires_cvv
```

**1.6 Render the widget only when required.**&#x20;

Give it a stable `id` — you'll need the same id in step 1.8

```js
import { CardCVCElement } from '@juspay-tech/react-native-hyperswitch';

const [cvcReady, setCvcReady] = useState(false);

{requiresCvc && (
  <CardCVCElement
    id="card-cvc-element"                 // remember this id
    options={{
      placeholder: '123',
      cvcIcon: 'hidden',
      appearance: { theme: 'Light' },
      subscribedEvents: ['CVC_STATUS'],
    }}
    onReady={() => setCvcReady(true)}
    onChange={(event) => handleEvent(event)}
    onFocus={() => {}}
    onBlur={() => {}}
    style={{ minHeight: 50 }}
  />
)}
```

**1.6 Wait for readiness, then enable your Pay button:**

```tsx
<Button title="Pay" disabled={requiresCvc && !cvcReady} onPress={onPay} />
```

Also reset `cvcReady` to `false` whenever the underlying payment session or the selected saved method changes, so the user can't submit against a stale widget.

**1.7 Confirm headlessly with the same `id`:**

```typescript
const result = await methodsSession.confirmWithCustomerLastUsedPaymentMethod({
  id: 'card-cvc-element',   // must match the mounted CardCVCElement's id
});
handleResult(result);
```

**1.8 Handle the result:**

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

**Congratulations! You have successfully integrated the CVC Element into your application.**
