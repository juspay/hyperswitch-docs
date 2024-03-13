---
description: >-
  Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your payments experience.
---

# Headless

{% hint style="info" %}
This section guides you through the integration of Hyperswitch Headless for both web and mobile clients
{% endhint %}

### Customize the payment experience using Headless functions

#### 1. Initialize the Hyperswitch SDK

Initialize `Hyper` onto your app with your publishable key with the `Hyper` constructor. You’ll use `HyperLoader` which you can call to create a Headless Payment Session.  To get a Publishable Key please find it [here](https://app.hyperswitch.io/developers).

{% tabs %}
{% tab title="HTML + JavaScript" %}
<pre class="language-javascript"><code class="lang-javascript"><strong>// Source Hyperloader on your HTML file using the &#x3C;script /> tag
</strong>hyper = Hyper.init(YOUR_PUBLISHABLE_KEY);
</code></pre>
{% endtab %}

{% tab title="Flutter" %}
```dart
// dependencies: flutter_hyperswitch: ^version_number
// run the following command to fetch and install the dependencies flutter pub get
import 'package:flutter_hyperswitch/flutter_hyperswitch.dart';
_hyper.init(HyperConfig(publishableKey: 'YOUR_PUBLISHABLE_KEY'));
```
{% endtab %}
{% endtabs %}

#### 2. Create a Payment Intent

Make a request to the endpoint on your server to create a new Payment. The `clientSecret` returned by your endpoint is used to initialize the payment session.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security
{% endhint %}

#### 3. Initialize your Payment Session

Initialize a Payment Session by passing the clientSecret to the `initPaymentSession`

{% tabs %}
{% tab title="JavaScript" %}
```javascript
paymentSession = hyper.initPaymentSession({
  clientSecret: client_secret,
});
```
{% endtab %}

{% tab title="Flutter" %}
```dart
Session paymentSession = await hyper.initPaymentSession(PaymentMethodParams(clientSecret: 'YOUR_PAYMENT_INTENT_CLIENT_SECRET'));
```
{% endtab %}
{% endtabs %}

| options (Required)      | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `clientSecret (string)` | **Required.**  Required to use as the identifier of the payment. |

#### 4. Craft a customized payments experience

Using the `paymentSession` object, the default customer payment method data can be fetched, using which you can craft your own payments experience. The `paymentSession` object also exposes a `confirmWithCustomerDefaultPaymentMethod` function, using which you can confirm and handle the payment session.

{% tabs %}
{% tab title="JavaScript" %}
```javascript
paymentMethodSession = await paymentSession.getCustomerSavedPaymentMethods();

if (paymentMethodSession.error) {
    // handle the case where no default customer payment method is not present
} else {
    // use the customer_default_saved_payment_method_data to fulfill your usecases (render UI)
    const customer_default_saved_payment_method_data =
        paymentMethodSession.getCustomerDefaultSavedPaymentMethodData();
}

//handle press for pay button 
function handlePress() { 
    if (paymentMethodSession.error) {
        // handle the case where no default customer payment method is not present
    } else {
        // use the confirmWithCustomerDefaultPaymentMethod function to confirm and handle the payment session response
        const { error, status } = await
        paymentMethodSession.
            confirmWithCustomerDefaultPaymentMethod({
                confirmParams: {
                    // Make sure to change this to your payment completion page
                    return_url: "https://example.com/complete"
                },
                // if you wish to redirect always, otherwise it is defaulted to "if_required"
                redirect: "always",
            });

        // use error, status to complete the payment journey
        if (error) {
            if (error.message) {
                // handle error messages
                setMessage(error.message);
            } else {
                setMessage("An unexpected error occurred.");
            }
        }
        if (status) {
            // handle payment status
            handlePaymentStatus(status);
        }
    }
}
```
{% endtab %}

{% tab title="Flutter" %}
<pre class="language-dart"><code class="lang-dart">paymentMethodSession = await paymentSession.getCustomerSavedPaymentMethods();

// use the customer_default_saved_payment_method_data to fulfill your usecases
Object customer_default_saved_payment_method_data = paymentMethodSession?.getCustomerDefaultSavedPaymentMethodData();

if (customer_default_saved_payment_method_data is Card) {
<strong>    displayCard(customer_default_saved_payment_method_data);
</strong>} else if (customer_default_saved_payment_method_data is Wallet) {
    displayWallet(customer_default_saved_payment_method_data);
} else if (customer_default_saved_payment_method_data is Error) {
    // handle the case where no default customer payment method is not present
    handleError(customer_default_saved_payment_method_data);
}

// use the confirmWithCustomerDefaultPaymentMethod function to confirm and handle the payment session response
Future&#x3C;void> onPress() async {
    PaymentResult confirmWithCustomerDefaultPaymentMethodResponse = await paymentMethodSession?.confirmWithCustomerDefaultPaymentMethod();
    var status = confirmWithCustomerDefaultPaymentMethodResponse.status;
    var message = confirmWithCustomerDefaultPaymentMethodResponse.message;
    
    // use paymentSheetResponseType, paymentSheetResponseMessage to complete the payment journey
    switch (status) {
      case "cancelled":
        // handle cancelled case
        break;
      case "failed":
        // handle failed case
        break;
      case "completed":
          switch (message) {
              case "succeeded":
                // handle succeeded case
                break;
              case "processing":
                // handle requires_capture case
                break;
              default:
                // handle the default case
                break;
        }
        break;
    }
}
</code></pre>
{% endtab %}
{% endtabs %}

&#x20;**Payload for** `confirmWithCustomerDefaultPaymentMethod(payload)`

<table><thead><tr><th width="296">options (Required)</th><th>Description</th></tr></thead><tbody><tr><td><code>confirmParams (object)</code></td><td>Parameters that will be passed on to the Hyper API.</td></tr><tr><td><code>redirect (string)</code></td><td><strong>(web only)</strong> <strong>Can be either 'always' or 'if_required'</strong> By default, <code>confirmWithCustomerDefaultPaymentMethod()</code> will always redirect to your <code>return_url</code> after a successful confirmation. If you set redirect: "if_required", then this method will only redirect if your user chooses a redirection-based payment method.</td></tr></tbody></table>

**ConfirmParams object**

<table><thead><tr><th width="281">confirmParams</th><th>Description</th></tr></thead><tbody><tr><td><code>return_url(string)</code></td><td><strong>(web only)</strong> The url your customer will be directed to after they complete payment.</td></tr></tbody></table>
