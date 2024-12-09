---
description: Integrate Card widget to your React Native App using hyperswitch-node
---

# Card Widget

{% hint style="info" %}
This feature is currently in Beta. For access, please contact us at **hyperswitch@juspay.in**
{% endhint %}

{% hint style="info" %}
Hyperswitch recommends using the PaymentSheet instead of the Card Widget. Using only the Payment Element, you can accept multiple payment methods.
{% endhint %}

## 1. Build card widget on the client

### 1.1 Add `HyperProvider` to your React Native app

Use `HyperProvider` to ensure that you stay PCI compliant by sending payment details directly to Hyperswitch server.

```js
import { HyperProvider } from "@juspay-tech/react-native-hyperswitch";
```

### 1.2 Use `HyperProvider`

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

### 1.3 Fetch the PaymentIntent client Secret

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

### 1.4 Render your card widget

Use Hyperswitch `CardField` component to display a text field to securely collect card details. By using `CardField`, you guarantee that sensitive card details never touch your server.

<pre class="language-js"><code class="lang-js">import {CardField, useHyper} from '@stripe/stripe-react-native';

return(
 &#x3C;View>
      &#x3C;CardField
        postalCodeEnabled={true}
        placeholders={{
          number: '4242 4242 4242 4242',
        }}
        cardStyle={{
          backgroundColor: '#FFFFFF',
          textColor: '#000000',
        }}
        style={{
          width: '100%',
          height: 50,
          marginVertical: 30,
        }}
        onCardChange={cardDetails => {
          console.log('cardDetails', cardDetails);
        }}
        onFocus={focusedField => {
          console.log('focusField', focusedField);
        }}
<strong>        onBlur={blurField => {
</strong>          console.log('blurField', blurField);
        }}
      />
      &#x3C;Button onPress={handlePayPress} title="Pay" disabled={loading} />
    &#x3C;/View>
)
</code></pre>

### 1.5 Initiate payment session

Pass the PaymentIntent’s `clientSecret` to initPaymentSession() function. Hyperswitch SDK automatically collects the card details from `CardField` component.

```js
import {CardField, useHyper} from '@stripe/stripe-react-native';

const { initPaymentSession, confirmWithCardForm } = useHyper();
const [paymentSession,setPaymentSession]=React.useState(null);

const initializePaymentSession = async () => {
  const { clientSecret } = await fetchPaymentParams();
  const params={
      clientSecret: clientSecret,
  }
  const paymentSession = await initPaymentSession(params);
  await setPaymentSession(_=>paymentSession)
};

useEffect(() => {
  initializePaymentSheet();
}, []);
```



### 3.4 Confirm the payment

To confirm the Payment, integrate a "Pay Now" button within the checkout page, which, when clicked, invokes the confirmWithCardForm() function. This function will return an asynchronous payment response with various payment status.

```js
const handlePayPress = async () => {
  const status = await confirmWithCardForm(paymentSession);
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
    <Button variant="primary" title="Pay with card form" onPress={handlePayPress} />
  </Screen>
);
```

Congratulations! Now that you have integrated the Card Widget
