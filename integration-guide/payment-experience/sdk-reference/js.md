# JS

Hyperswitch's JS SDK come with many methods which you can use to customize your payments experience. You can use the props to change the appearance, reorder payment methods and much more to suit your business needs.

### Hyper()

This constructor gives you access to methods in Hyper API, which you can call. The API details are listed down below.

```js
let hyper = Hyper();
```

#### 1. `hyper.confirmPayment(options)`

Use `hyper.confirmPayment` to confirm a PaymentIntent using data collected by the Payment Element. When called, `hyper.confirmPayment` will attempt to complete any required actions, such as authenticating your user by displaying a 3DS dialog or redirecting them to a bank authorization page. Your user will be redirected to the return\_url you pass once the confirmation is complete.

| options (Required)       | Description                                                                                                                                                                                                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `elements (object)`      | **Required**. The Elements instance that was used to create the Payment Element.                                                                                                                                                                                                                   |
| `confirmParams (object)` | Parameters that will be passed on to the Hyper API.                                                                                                                                                                                                                                                |
| `redirect (string)`      | **Can be either 'always' or 'if\_required'** By default, `hyper.confirmPayment` will always redirect to your `return_url` after a successful confirmation. If you set redirect: "if\_required", then hyper.confirmPayment will only redirect if your user chooses a redirect-based payment method. |

**ConfirmParams object**

| confirmParams        | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| `return_url(string)` | **Required**. The url your customer will be directed to after they complete payment. |

#### 2. `hyper.elements(options)`

This method creates an Elements instance, which manages a group of elements.

| options (Required)      | Description                                                                                                                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `font (array)`          | An array of custom fonts, which elements created from the Elements object can use. Fonts can be specified as CssFontSource or CustomFontSource objects.                                                                    |
| `locale (string)`       | A locale to display placeholders and error strings in. Default is auto (HyperSwitch detects the locale of the browser).                                                                                                    |
| `clientSecret (string)` | **Required** Required to use with the Unified Checkout and Hyper Widgets.                                                                                                                                                  |
| `appearance (object)`   | Match the design of your site with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.                                                       |
| `loader (variants)`     | **Can be either 'auto', 'always' or 'never'** Display skeleton loader UI while waiting for Elements to be fully loaded, after they are mounted. Default is 'auto' (HyperSwitch determines if a loader UI should be shown). |

#### 3.`hyper.confirmCardPayment(clientSecret,data?,options?)`

Use `hyper.confirmCardPayment` when the customer submits your payment form. When called, it will confirm the PaymentIntent with data you provide and carry out 3DS or other next actions if they are required.

`clientSecret` is a required string.

| data                     | Description                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------ |
| `payment_method(object)` | An object containing data to create a PaymentMethod with.                            |
| `shipping (object)`      | The shipping details for the payment, if collected.                                  |
| `return_url (string)`    | **Required**. The url your customer will be directed to after they complete payment. |

| options                  | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| `handleActions(boolean)` | An object containing data to create a PaymentMethod with. |

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

| options (Required)            | Description                                                                                                                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `country (string)`            | **Required**. The two-letter country code of your HyperSwitch account (e.g., US).                                                                                                                                                                   |
| `currency (string)`           | **Required**. Three character currency code (e.g., USD).                                                                                                                                                                                            |
| `total (object)`              | **Required**. A PaymentItem object. This PaymentItem is shown to the customer in the browser’s payment interface.                                                                                                                                   |
| `displayItems (array)`        | An array of PaymentItem objects. These objects are shown as line items in the browser’s payment interface. Note that the sum of the line item amounts does not need to add up to the total amount above.                                            |
| `requestPayerName (boolean)`  | **recommended** By default, the browser‘s payment interface only asks the customer for actual payment information. A customer name can be collected by setting this option to true. This collected name will appears in the PaymentResponse object. |
| `requestPayerEmail (boolean)` | Request the payer's email-id.                                                                                                                                                                                                                       |
| `requestPayerPhone (boolean)` | request payer's phone number                                                                                                                                                                                                                        |
| `requestShipping (boolean)`   | request payer's shipping information                                                                                                                                                                                                                |
| `shippingOptions (array)`     | An array of ShippingOption objects. The first shipping option listed appears in the browser payment interface as the default option.                                                                                                                |
| `disableWallets (array)`      | An array of wallet strings. Can be one or more of applePay, googlePay, and browserCard. Use this option to disable Apple Pay, Google Pay, and/or browser-saved cards.                                                                               |

`clientSecret` is a required string.\
\
5\.  `hyper.initiateUpdateIntent()`

Use `hyper.initiateUpdateIntent()` just before you start updating the payment intent on your end. It doesn't require any input. When invoked, it signals the system to prepare for the update process and returns a confirmation message indicating that the update has been initiated.

#### 6.  `hyper.completeUpdateIntent(clientSecret)`

Use `hyper.completeUpdateIntent(clientSecret)` after you’ve completed the payment intent update process on your side. It takes the updated `clientSecret` as input and signals the system to complete the update flow. It returns a response with a confirmation message indicating the update has been processed.

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

| options (Required)                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `layout (accordion/tabs/objects)` | <p>Specify the layout for the Payment Element. If you only pass a layout type (<code>'accordion'</code> or <code>‘tabs’</code>) without any additional parameters, the Payment Element renders using that layout and the default values associated with it.</p><p>An object can also be passed to specify the layout with additional configuration.</p>                                                                                                                                                                                                                                               |
| `defaultValues (object)`          | Provide initial customer information that will be displayed in the Payment Element. The form will render with empty fields if not provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `business (object)`               | Provide information about your business that will be displayed in the Payment Element. This object contains a key value pair of `name` which is a string                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `paymentMethodOrder (array)`      | <p>By default, the Payment Element will use a dynamic ordering that optimizes payment method display for each user.</p><p>You can override the default order in which payment methods are displayed in the Payment Element with a list of payment method types.</p><p>If the associated PaymentIntent has payment method types not specified in <code>paymentMethodOrder</code>, they will be displayed after the payment methods you specify. If you specify payment method types not on the associated PaymentIntent, they will be ignored.</p>                                                     |
| `fields (object)`                 | <p>By default, the Payment Element will collect all necessary details to complete a payment.</p><p>For some payment methods, this means that the Payment Element will collect details like name or email that you may have already collected from the user. If this is the case, you can prevent the Payment Element from collecting these data by using the fields option.</p><p>If you disable the collection of a certain field with the fields option, you must pass that same data to hyper.confirmPayment or the payment will be rejected.</p>                                                  |
| `terms (object)`                  | Control how mandates or other legal agreements are displayed in the Payment Element. Use never to never display legal agreements. The default setting is auto, which causes legal agreements to only be shown when necessary.                                                                                                                                                                                                                                                                                                                                                                         |
| `wallets (object)`                | <p>By default, the Payment Element will display all the payment methods that the underlying Payment Intent was created with.</p><p>However, wallets like Apple Pay and Google Pay are not payment methods per the Payment Intent API. They will show when the Payment Intent has the card payment method and the customer is using a supported platform and have an active card in their account. This is the auto behavior, and it is the default for choice for all wallets.</p><p>If you do not want to show a given wallet as a payment option, you can set its property in wallets to never.</p> |



**Layout object**

| layout                                | Description                                                                                                                                                                                                                                                                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type (accordion/tabs)`               | Defines the layout to render the Payment Element.                                                                                                                                                                                                                                                          |
| `defaultCollapsed (boolean)`          | Controls if the Payment Element renders in a collapsed state (where no payment method is selected by default). When you leave this undefined, Hyperswitch renders the experience that it determines will have the best conversion.                                                                         |
| `radios (boolean)`                    | <p>Renders each Payment Method with a radio input next to its logo. The radios visually indicate the current selection of the Payment Element.</p><p><em>This property is only applicable to the accordion layout.</em></p>                                                                                |
| `spacedAccordionItems (boolean)`      | <p>When true, the Payment Methods render as standalone buttons with space in between them.</p><p><em>This property is only applicable to the accordion layout.</em></p>                                                                                                                                    |
| `visibleAccordionItemsCount (number)` | <p>Sets the max number of Payment Methods visible before using the "More" button to hide additional Payment Methods. Set this value to 0 to disable the "More" button and render all available Payment Methods. Default is 5.</p><p><em>This property is only applicable to the accordion layout.</em></p> |



**defaultValues object**

| defaultValues             | Description                                                                                                                                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `billingDetails (object)` | Specify customer's billing details, which lets you pre-fill a customer’s name, email, phone number and address if required by payment method. Pre-filling as much information as possible streamlines the checkout process. |

| billingDetails     | Description |
| ------------------ | ----------- |
| `name (string)`    |             |
| `email (string)`   |             |
| `phone (string)`   |             |
| `address (object)` |             |

| address            | Description |
| ------------------ | ----------- |
| `line1 (string)`   |             |
| `line2 (string)`   |             |
| `city (string)`    |             |
| `state (object)`   |             |
| `country (string)` |             |
| `postal_code`      |             |

**fields object**

| layout                                   | Description                                                                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `billingDetails (never / auto / object)` | Please refer the above written structure of billingDetails, expect of them being string, they will be either never or auto |

**terms object**

| terms                                   | Description |
| --------------------------------------- | ----------- |
| `usBankAccount (auto / always / never)` |             |
| `card (auto / always / never)`          |             |
| `auBecsDebit (auto / always / never)`   |             |
| `bancontact (auto / always / never)`    |             |
| `ideal (auto / always / never)`         |             |
| `sepaDebit (auto / always / never)`     |             |
| `sofort (auto / always / never)`        |             |

**wallets object**

| wallets                    | Description                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| `applePay (auto / never)`  |                                                                                                |
| `googlePay (auto / never)` |                                                                                                |
| `walletReturnUrl (string)` | This is the URL which you will get redirected to post a successful confirmation of a payment.  |
| `style (object)`           | This gives the style to the wallet buttons in the Payment Element.                             |



**`3. elements.update(options)`**

Updates the options the Element was initialized with. Updates are merged into the existing configuration.

If you collect certain information in a different part of your interface (e.g., ZIP or postal code), use element.update with the appropriate information.

The styles of an Element can be dynamically changed using element.update. This method can be used to simulate CSS media queries that automatically adjust the size of elements when viewed on different devices

| options                 | Description                                                                                                                                                                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale (string)`       | A locale to display placeholders and error strings in. Default is auto (Hyperswitch detects the locale of the browser).Setting the locale does not affect the behavior of postal code validation—a valid postal code for the billing country of the card is still required. |
| `appearance (object)`   | Supported for the Unified CheckoutMatch the design of your site with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.                                                                      |
| `clientSecret (string)` | Required to use with the Unified Checkout and the Hyper WidgetsThe client secret for a PaymentIntent                                                                                                                                                                        |

### paymentElement()

After calling the elements.create with your type and options, you will get access to the PaymentElements API. This will provide you the exact Payment Element you want (UnifiedCheckout, CardElement, etc. ) and functions attached to it by which you can perform various operations

```js
let paymentElement = elements.create("payment",options);
```

#### 1. `paymentElement.mount(domElement)`

This method attaches your Payment Element to the DOM. This only accepts a CSS seletor (eg, #unified-checkout) . You need to have created a DOM element in your HTML file where you think you can mount the Payment Element.&#x20;

#### 2. `paymentElement.blur()`

Blurs the Payment Element.&#x20;

#### 3. `paymentElement.clear()`

Clears the values of the Payment Element.&#x20;

#### 4. `paymentElement.destroy()`

Removes the Payment Element from the DOM and destroys it. A destroyed Element cannot be re-mounted to the DOM.&#x20;

#### 5. `paymentElement.focus()`

Focuses the Payment Element fields.&#x20;

#### 6. `paymentElement.unmount()`

Unmounts the Payment Element from the DOM. Call paymentElement.mount  to re-attach it to the DOM.&#x20;

#### 7. `paymentElement.update(options)`

Updates the options the Payment Element was initialized with. Updates are merged into the existing configuration. This uses the same API as elements.create().&#x20;

#### 8. `paymentElement.on(type, handler)`



