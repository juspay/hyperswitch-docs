---
description: >-
  Hyperswitch SDK is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to handle your own UI.
---

# Headless

{% hint style="info" %}
This section covers different methods and their params of the Hyperswitch Headless SDK&#x20;
{% endhint %}

Hyperswitch  SDK comes with many methods which you can use to customize your payments experience. These methods are commonly available across Web and App integrations.

You can add a widget that can give your customers a one-click-checkout experience with their default saved payment method.&#x20;

You can access the following functions from `getCustomerSavedPaymentMethods` method to enable this experience:

```javascript
1. getCustomerDefaultSavedPaymentMethodData()
2. confirmWithCustomerDefaultPaymentMethod()
```

### Headless SDK functions for one-click-checkout experience

Initialize `Hyper` onto your app with your publishable key with the `Hyper` constructor. You’ll use `HyperLoader` which you can call to create a Headless Payment Session.  To get a Publishable Key please find it [here](https://app.hyperswitch.io/developers).

```js
hyper = Hyper.init(YOUR_PUBLISHABLE_KEY);
```

Immediately make a request to the endpoint on your server to create a new Payment as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security
{% endhint %}

Use `hyper.initPaymentSession` to initialize a Payment Session.

```javascript
paymentSession = hyper.initPaymentSession({
  clientSecret: client_secret,
});
```

| options (Required)      | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `clientSecret (string)` | **Required.**  Required to use as the identifier of the payment. |

Using the `paymentSession` object, the default customer payment method can be fetched, and a payment can be confirmed with it, if it is available.

```javascript
customerSavedPaymentMethods = await paymentSession.getCustomerSavedPaymentMethods();
if (customerSavedPaymentMethods.error) {
  handleError(customerSavedPaymentMethods.error.message);
} else {
  customer_default_saved_payment_method_data =
    customerSavedPaymentMethods.getCustomerDefaultSavedPaymentMethodData();
    handleDefaultPaymentMethod(customer_default_saved_payment_method_data); // handle customer default payment method data
  const { error, status } = await 
    customerSavedPaymentMethods.confirmWithCustomerDefaultPaymentMethod({
        confirmParams: {
          // Make sure to change this to your payment completion page
          return_url: "https://example.com/complete",
        },
      redirect: "always", // if you wish to redirect always, otherwise it is defaulted to "if_required"
    });
  if (error) {
    if (error.message) {
      setMessage(error.message); // handle error messages
    } else {
      setMessage("An unexpected error occurred.");
    }
  }
  if (status) {
    handlePaymentStatus(status); // handle payment status
  }
}
```

&#x20;**Payload for** `confirmWithCustomerDefaultPaymentMethod(payload)`

<table><thead><tr><th width="296">options (Required)</th><th>Description</th></tr></thead><tbody><tr><td><code>confirmParams (object)</code></td><td>Parameters that will be passed on to the Hyper API.</td></tr><tr><td><code>redirect (string)</code></td><td><strong>Can be either 'always' or 'if_required'</strong> By default, <code>confirmWithCustomerDefaultPaymentMethod()</code> will always redirect to your <code>return_url</code> after a successful confirmation. If you set redirect: "if_required", then this method will only redirect if your user chooses a redirection-based payment method.</td></tr></tbody></table>

**ConfirmParams object**

<table><thead><tr><th width="281">confirmParams</th><th>Description</th></tr></thead><tbody><tr><td><code>return_url(string)</code></td><td><strong>Required</strong>. The url your customer will be directed to after they complete payment.</td></tr><tr><td><code>shipping (object)</code></td><td>The shipping details for the payment, if collected.</td></tr></tbody></table>
