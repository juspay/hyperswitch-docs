# JS

{% hint style="info" %}
This section covers different methods and their params of the Hyperswitch JS SDK
{% endhint %}

Hyperswitch's SDK come with many methods which you can use to customize your payments experience.

### Hyper()

This constructor gives you access to methods in Hyper API, which you can call. The API details are listed down below.

```js
let hyper = Hyper();
```

#### 1. `hyper.confirmPayment(options)`

Use `hyper.confirmPayment` to confirm a PaymentIntent using data collected by the Payment Element. When called, `hyper.confirmPayment` will attempt to complete any required actions, such as authenticating your user by displaying a 3DS dialog or redirecting them to a bank authorization page. Your user will be redirected to the return\_url you pass once the confirmation is complete.

| options (Required)     | Description                                                                                                                                                                                                                                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| elements (object)      | **Required**. The Elements instance that was used to create the Payment Element.                                                                                                                                                                                                                   |
| confirmParams (object) | Parameters that will be passed on to the Hyper API.                                                                                                                                                                                                                                                |
| redirect (string)      | **Can be either 'always' or 'if\_required'** By default, `hyper.confirmPayment` will always redirect to your `return_url` after a successful confirmation. If you set redirect: "if\_required", then hyper.confirmPayment will only redirect if your user chooses a redirect-based payment method. |

**ConfirmParams object**

| confirmParams                  | Description                                                                                                                                                                                                                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| return\_url(string)            | **Required**. The url your customer will be directed to after they complete payment.                                                                                                                                                                                                                                      |
| shipping (object)              | The shipping details for the payment, if collected.                                                                                                                                                                                                                                                                       |
| payment\_method\_data (object) | When you call `hyper.confirmPayment`, payment details are collected from the `HyperElement` and passed to the PaymentIntents confirm endpoint as the `payment_method_data` parameter. You can also include additional payment\_method\_data fields, which will be merged with the data collected from the `HyperElement`. |

#### 2. `hyper.elements(options)`

This method creates an Elements instance, which manages a group of elements.

| options (Required)    | Description                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| font (array)          | An array of custom fonts, which elements created from the Elements object can use. Fonts can be specified as CssFontSource or CustomFontSource objects.                                                                    |
| locale (string)       | A locale to display placeholders and error strings in. Default is auto (HyperSwitch detects the locale of the browser).                                                                                                    |
| clientSecret (string) | **Required** Required to use with the Unified Checkout and Hyper Widgets.                                                                                                                                                  |
| appearance (object)   | Match the design of your site with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.                                                       |
| loader (variants)     | **Can be either 'auto', 'always' or 'never'** Display skeleton loader UI while waiting for Elements to be fully loaded, after they are mounted. Default is 'auto' (HyperSwitch determines if a loader UI should be shown). |

#### 3.`hyper.confirmCardPayment(clientSecret,data?,options?)`

Use `hyper.confirmCardPayment` when the customer submits your payment form. When called, it will confirm the PaymentIntent with data you provide and carry out 3DS or other next actions if they are required.

`clientSecret` is a required string.

| data                    | Description                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| payment\_method(object) | An object containing data to create a PaymentMethod with.                            |
| shipping (object)       | The shipping details for the payment, if collected.                                  |
| return\_url (string)    | **Required**. The url your customer will be directed to after they complete payment. |

| options                | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| handleActions(boolean) | An object containing data to create a PaymentMethod with. |

`payment_method` example

```js
  payment_method: {
    card: "card",
    billing_details: {
      name: "Jenny Rosen",
    },
  },
```

#### 3. `hyper.retrievePaymentIntent(clientSecret)`

Retrieve a PaymentIntent using its client secret.

#### 4. `hyper.paymentRequest(options)`

Use `hyper.paymentRequest` to create a PaymentRequest object. Creating a PaymentRequest requires that you configure it with an options object.

| options (Required)          | Description                                                                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| country (string)            | **Required**. The two-letter country code of your HyperSwitch account (e.g., US).                                                                                                                                                                   |
| currency (string)           | **Required**. Three character currency code (e.g., USD).                                                                                                                                                                                            |
| total (object)              | **Required**. A PaymentItem object. This PaymentItem is shown to the customer in the browser’s payment interface.                                                                                                                                   |
| displayItems (array)        | An array of PaymentItem objects. These objects are shown as line items in the browser’s payment interface. Note that the sum of the line item amounts does not need to add up to the total amount above.                                            |
| requestPayerName (boolean)  | **recommended** By default, the browser‘s payment interface only asks the customer for actual payment information. A customer name can be collected by setting this option to true. This collected name will appears in the PaymentResponse object. |
| requestPayerEmail (boolean) | Request the payer's email-id.                                                                                                                                                                                                                       |
| requestPayerPhone (boolean) | request payer's phone number                                                                                                                                                                                                                        |
| requestShipping (boolean)   | request payer's shipping information                                                                                                                                                                                                                |
| shippingOptions (array)     | An array of ShippingOption objects. The first shipping option listed appears in the browser payment interface as the default option.                                                                                                                |
| disableWallets (array)      | An array of wallet strings. Can be one or more of applePay, googlePay, and browserCard. Use this option to disable Apple Pay, Google Pay, and/or browser-saved cards.                                                                               |

`clientSecret` is a required string.

### elements()

After calling the hyper.elements with your options, you will get access to the Elements API. This will have methods which are not specific to a particular payment element (UnifiedCheckout, HyperWidgets, etc. ) but are needed for the overall operation of them.&#x20;

```js
let elements = hyper.elements(options);
```

#### 1. `elements.getElement(type)`

This method retrieves a previously created Payment Element. Here the `type` is `payment` for Unified Checkout.

elements.getElement('payment') returns one of the following:

* An instance of a Unified Checkout.
* `null`, when no Unified Checkout has been created.

**2. `elements.create(type, options?)`**

This method creates an instance of an individual Element. It takes the type of Element to create as well as an options object.

The type can be ‘payment’ for UnifiedCheckout.

**Options object**

| options (Required) | Description                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| classes (object)   | Set custom class names on the container DOM element when the Hyper element is in a particular state.                                           |
| style              | Customize the appearance of this element using CSS properties passed in a Style object.                                                        |
| hidePostalCode     | Hide the postal code field. Default is false. If you are already collecting a full billing address or postal code elsewhere, set this to true. |
| iconStyle          | Appearance of the icon in the Element. Either solid or default.                                                                                |
| hideIcon           | Hides the icon in the Element. Default is false.                                                                                               |
| disabled           | Applies a disabled state to the Element such that user input is not accepted. Default is false.                                                |



**Classes object**

| classes  | Description                                                                              |
| -------- | ---------------------------------------------------------------------------------------- |
| base     | The base class applied to the container. Defaults to HyperElement.                       |
| complete | The class name to apply when the Element is complete. Defaults to HyperElement—complete. |
| focus    | The class name to apply when the Element is focused. Defaults to HyperElement--focus.    |
| invalid  | The class name to apply when the Element is invalid. Defaults to HyperElement--invalid.  |



**`3. element.update(options)`**

Updates the options the Element was initialized with. Updates are merged into the existing configuration.

If you collect certain information in a different part of your interface (e.g., ZIP or postal code), use element.update with the appropriate information.

The styles of an Element can be dynamically changed using element.update. This method can be used to simulate CSS media queries that automatically adjust the size of elements when viewed on different devices

| options               | Description                                                                                                                                                                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| locale (string)       | A locale to display placeholders and error strings in. Default is auto (Hyperswitch detects the locale of the browser).Setting the locale does not affect the behavior of postal code validation—a valid postal code for the billing country of the card is still required. |
| appearance (object)   | Supported for the Unified CheckoutMatch the design of your site with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.                                                                      |
| clientSecret (string) | Required to use with the Unified Checkout and the Hyper WidgetsThe client secret for a PaymentIntent                                                                                                                                                                        |

\
