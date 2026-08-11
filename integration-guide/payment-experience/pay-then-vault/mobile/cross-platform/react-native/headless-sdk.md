---
description: >-
  Juspay Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your checkout UI.
icon: block-brick
---

# Headless SDK

#### Customize the payment experience using Headless functions

**1. Initialize the Hyperswitch SDK**

Initialize Hyperswitch once using your publishable key and profile ID. Reuse the same initialized instance throughout your application.

```javascript
import { Hyperswitch } from "@juspay-tech/react-native-hyperswitch";

const hyper = await Hyperswitch.init({
  publishableKey: "pk_snd_...",
  profileId: "pro_...",
});
```

Keep the Hyperswitch secret API key on your backend only. The React Native application must never handle or store it.

**2. Get `sdk_authorization` from your Backend**

Call the payment-creation endpoint on your backend. Its JSON response must contain `sdk_authorization`.

```javascript
const response = await fetch(`${API_URL}/create-payment`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    amount: 100,
    currency: "USD",
  }),
});

const { sdk_authorization } = await response.json();
```

\
**Important:** Never include your Hyperswitch secret API key in the React Native application. The payment must be created from your backend.

**3. Initialize your Payment Session**

Create a payment session by passing the latest `sdk_authorization` returned by your backend to `initPaymentSession`.

```javascript
const paymentSession = await hyper.initPaymentSession({
  sdkAuthorization: sdk_authorization,
});
```

Create a new payment session for every payment using the latest `sdk_authorization` returned by your backend.

| Options                     | Description                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------ |
| `sdkAuthorization (string)` | **Required.** The latest SDK authorization returned by your backend for the payment. |

**4. Craft a customized payments experience**

Using the `paymentSession` object, the default customer payment method data can be fetched, using which you can craft your own payments experience. The `paymentSession` object also exposes a `confirmWithCustomerDefaultPaymentMethod` function, using which you can confirm and handle the payment session.

```javascript
import { useHyper } from "@juspay-tech/react-native-hyperswitch";

const { getCustomerSavedPaymentMethods,
        getCustomerDefaultSavedPaymentMethodData,
        confirmWithCustomerDefaultPaymentMethod } = useHyper();

const [defaultPaymentMethodData,setDefaultPaymentMethodData]=React.useState(null)

React.useEffect(()=>{
    const getPaymentMethods = async() => {
        const paymentMethodSession 
                = await getCustomerSavedPaymentMethods(paymentSession);
        const customer_default_saved_payment_method_data 
                = await getCustomerLastUsedSavedPaymentMethodData(paymentMethodSession);
        setDefaultPaymentMethodData(_=>customer_default_saved_payment_method_data)
    }
    getPaymentMethods()
},[])

let confirmDefaultPaymentMethod = () => {
const status = await confirmWithCustomerLastUsedPaymentMethod(paymentMethodSession);
    // handle status of payment   
    if (status != null) {
        const message = status.message;
        console.log(message)
    }
}

return (
    //build the ui using defaultPaymentMethodData
    //on click of pay use confirmDefaultPaymentMethod()
)
```

**Payload for** `confirmWithCustomerLastUsedPaymentMethod(callback)`

<table><thead><tr><th width="296">options (Required)</th><th>Description</th></tr></thead><tbody><tr><td><code>callback (function)</code></td><td>Callback to get confirm response.</td></tr></tbody></table>
