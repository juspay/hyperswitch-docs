---
description: >-
  Juspay Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your checkout UI.
icon: block-brick
---

# Headless SDK

Fetch a customer's saved payment methods without rendering any UI, and even confirm one-click payments headlessly.

#### Customize the payment experience using Headless functions

**1. Initialize the Hyperswitch SDK**

Initialize Hyperswitch once using your publishable key and profile ID. Reuse the same initialized instance throughout your application.

```javascript
import { Hyperswitch } from "@juspay-tech/react-native-hyperswitch";

const hyperPromise = Hyperswitch.init({
      publishableKey: 'pk_snd_xxxxxxxx',   // from Hyperswitch dashboard
      profileId: 'pro_xxxxxxxx',           // your profile id
      // environment: 'SANDBOX',           // 'PROD' (default) | 'SANDBOX' | 'INTEG'
    });
```

**2 Get `sdk_authorization` from your Backend**

Call your payment-creation endpoint. Its JSON response must contain `sdk_authorization`.

```js
const response = await fetch('https://your-server.com/create-payment-intent', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ amount: 6500, currency: 'USD', customer_id: 'cust_123' }),
});

const { sdk_authorization } = await response.json();
```

**Important:** Never include your Hyperswitch secret API key in the React Native application. The payment must be created from your backend.

**3. Initialize your Payment Session or useHook inside HyperElements**

Create a payment session by passing the latest `sdk_authorization` returned by your backend to `initPaymentSession`.

<pre class="language-javascript"><code class="lang-javascript"><strong>// Option A
</strong><strong>const hyper = await hyperPromise;
</strong>const paymentSession = await hyper.initPaymentSession({
  sdkAuthorization: sdk_authorization,
});
// Option B
const paymentSession = usePaymentSession();
</code></pre>

```tsx
const methodsSession = await paymentSession.getCustomerSavedPaymentMethods({
  hiddenPaymentMethods: ['paypal', 'google_pay', 'apple_pay'], // optional filter
});
```

**4. Get the Customer Saved Cards**

```ts
// most recently used
const lastUsed  = await methodsSession.getCustomerLastUsedPaymentMethodData();
// customer default
const defaultPm = await methodsSession.getCustomerDefaultSavedPaymentMethodData(); 
// first saved method
const savedPm   = await methodsSession.getCustomerSavedPaymentMethodData();       
```

Each returns a `CustomerLastUsedPaymentMethod | null`, e.g.:

```ts
{
  payment_token: 'pt_xxx',
  payment_method_id: 'pm_xxx',
  customer_id: 'cust_123',
  payment_method: 'card',
  payment_method_type: 'credit',
  recurring_enabled: true,
  requires_cvv: true,
  card: {
    scheme: 'VISA',
    last4_digits: '4242',
    expiry_month: '12',
    expiry_year: '28',
    card_holder_name: 'John Doe',
    ...
  },
  billing: { address: { ... }, email: '...' },
  last_used_at: '2026-01-01T10:00:00Z',
  default_payment_method_set: true,
  ...
}

```

Typical pattern (from the example flow): if `lastUsed?.payment_method === 'card'` and `requires_cvv`, show `CardCVCElement` to collect CVC, then confirm headlessly.

#### 4.1 Headless confirm (one-click payment) <a href="#id-43-headless-confirm-one-click-payment" id="id-43-headless-confirm-one-click-payment"></a>

```ts
const result = await methodsSession.confirmWithCustomerLastUsedPaymentMethod({
  id: 'card-cvc-element', // id of a mounted CardCVCElement that collected the CVC
});

// or the customer's default method
const result2 = await methodsSession.confirmWithCustomerDefaultPaymentMethod({
  id: 'card-cvc-element',
});
```

The `id` must reference a mounted `CardCVCElement`, as the native SDK uses its CVC value to complete the payment confirmation. The method returns a `PaymentResult`, identical to the one returned by the `PaymentElement`.



