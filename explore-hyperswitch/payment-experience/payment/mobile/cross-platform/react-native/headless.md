---
description: >-
  Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your checkout UI.
icon: table-cells-large
---

# Headless SDK

### Customize the payment experience using Headless functions

#### 1. Initialize the Hyperswitch SDK

Initialize  Hyperswitch Headless SDK onto your app with your publishable key. To get a Publishable Key please find it [here](https://app.hyperswitch.io/developers).

```javascript
import { HyperProvider } from "@juspay-tech/hyperswitch-react-native ";

function App() {
  return (
    <HyperProvider publishableKey="YOUR_PUBLISHABLE_KEY">
      // Your app code here
    </HyperProvider>
  );
}
```

#### 2. Create a Payment Intent

Make a request to the endpoint on your server to create a new Payment. The `clientSecret` returned by your endpoint is used to initialize the payment session.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security
{% endhint %}

#### 3. Initialize your Payment Session

Initialize a Payment Session by passing the clientSecret to the `initPaymentSession`

```javascript
import { useHyper } from "@juspay-tech/react-native-hyperswitch";

const { initPaymentSession } = useHyper();
const [paymentSession,setPaymentSession] = React.useState(null);

const initializeHeadless = async() => {
  const { clientSecret } = await fetchPaymentParams();
  const params = {clientSecret:clientSecret}
  const paymentSession = await initPaymentSession(params);
  setPaymentSession(_ => paymentSession)
};

useEffect(() => {
  initializeHeadless();
}, []);

```

| options (Required)                  | Description                                                      |
| ----------------------------------- | ---------------------------------------------------------------- |
| `paymentIntentlientSecret (string)` | **Required.**  Required to use as the identifier of the payment. |

#### 4. Craft a customized payments experience

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

