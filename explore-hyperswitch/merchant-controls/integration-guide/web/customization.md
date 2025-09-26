---
description: Customize your Web unified checkout
icon: bars-progress
---

# Customization

## 1. Layouts

Choose a layout that fits well with your UI pattern. There are two types of layout options as listed below. The layout defaults to accordion if not explicitly specified.

### 1.1 Accordion layout

The accordion layout displays payment methods vertically using an accordion. To use this layout, set the value for layout to accordion. You also have the option to specify other properties, such as those shown in the following example.

```js
var paymentElementOptions = {
 layout: {
   type: 'accordion',
   defaultCollapsed: false,
   radios: true,
   spacedAccordionItems: false
 },
}

—------or—---------


var paymentElementOptions = {
 layout: 'accordion'
}

<PaymentElement id="payment-element" options={paymentElementOptions} />
```

### 1.2 Tabs layout

The tabs layout displays payment methods horizontally using tabs. To use this layout, set the value for layout to tabs. You also have the option to specify other properties, such as tabs or collapsed.

```js
var paymentElementOptions = {
 layout: 'tabs'
}

<PaymentElement id="payment-element" options={paymentElementOptions} />
```

## 2. Wallets

The wallet customization feature lets users configure payment options like Apple Pay, Google Pay, PayPal, and Klarna. It includes a `walletReturnUrl` for post-payment redirects and a `style` property to customize the wallet's appearance, offering flexibility for seamless integration.

<pre class="language-javascript"><code class="lang-javascript">var paymentElementOptions = {
    wallets: {
      walletReturnUrl: `${window.location.origin}`,
      applePay: "auto",
      googlePay: "auto",
      payPal: "auto",
      klarna: "never",
      style: {
        theme: "dark",
        type: "default",
        height: 55,
        buttonRadius: 4,
      },
    },
  }
  
<strong>&#x3C;PaymentElement id="payment-element" options={paymentElementOptions} />
</strong></code></pre>

| Variable                                                                                                    | Description                                                                                                                                                                                                                                                                                                                           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| walletReturnUrl: string                                                                                     | Defines the URL to redirect users to after completing a payment.                                                                                                                                                                                                                                                                      | This will take a **URL string** as its value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <p>applePay: showType<br>googlePay: showType<br>payPay: showType<br>klarna: showType</p>                    | Determines the visibility of Apple Pay, Google Pay, Paypal and Klarna.                                                                                                                                                                                                                                                                | <p></p><p><code>showType</code> can take two values:</p><ul><li><code>"auto"</code>: Display when supported.</li><li><code>"never"</code>: Always hidden</li></ul>                                                                                                                                                                                                                                                                                                                                                                                             |
| <p>style: {<br>   theme: theme,<br>   type: styleType,<br>   height: int,<br>   buttonRadius: int,<br>}</p> | <p></p><p>Configures the wallet's appearance with the following options:</p><ul><li><code>theme</code>: Sets the theme.</li><li><code>type</code>: Defines the style type (e.g. buy).</li><li><code>height</code>: Specifies the height of the wallet.</li><li><code>buttonRadius</code>: Adjusts the button corner radius.</li></ul> | <p><code>theme</code>: It can take values as <code>dark</code>, <code>light</code>, or <code>outline</code>.<br><br><code>type</code>: Specifies the wallet button style with options including <code>checkout</code>, <code>pay</code>, <code>buy</code>, <code>installment</code>, <code>default</code>, <code>book</code>, <code>donate</code>, <code>order</code>, <code>addmoney</code>, <code>topup</code>, <code>rent</code>, <code>subscribe</code>, <code>reload</code>, <code>support</code>, <code>tip</code>, and <code>contribute</code>.<br></p> |

## 3. Styling variables

The Styling APIs could be used to blend the Unified Checkout with the rest of your app or website.

| Variable              | Description                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| fontFamily            | The font family is used throughout Widgets. Widget supports css fonts and custom fonts by passing the fonts option; reference to elements consumer                 |
| fontSizeBase          | The font size that's set on the root of the Widget. By default, other font size variables like fontSizeXs or fontSizeSm are scaled from this value using rem units |
| spacingUnit           | The base spacing unit that all other spacing is derived from. Increase or decrease this value to make your layout more or less spacious                            |
| borderRadius          | The border radius used for tabs, inputs, and other components in the Widget                                                                                        |
| colorPrimary          | A primary color used throughout the Widget. Set this to your primary brand color                                                                                   |
| colorBackground       | The color used for the background of inputs, tabs, and other components in the Widget                                                                              |
| colorText             | The default text color used in the Widget                                                                                                                          |
| colorDanger           | A color used to indicate errors or destructive actions in the Widget                                                                                               |
| fontVariantLigatures  | The font-variant-ligatures setting of text in the Widget                                                                                                           |
| fontVariationSettings | The font-variation-settings setting of text in the Widget                                                                                                          |
| fontWeightLight       | The font weight used for light text                                                                                                                                |
| fontWeightNormal      | The font weight used for normal text                                                                                                                               |
| fontWeightMedium      | The font weight used for medium text                                                                                                                               |
| fontWeightBold        | The font weight used for bold text                                                                                                                                 |
| fontLineHeight        | The line-height setting of text in the Widget                                                                                                                      |
| fontSizeXl            | The font size of extra-large text in the Widget. By default this is scaled from var(--fontSizeBase) using rem units                                                |
| fontSizeLg            | The font size of large text in the Widget. By default this is scaled from var(--fontSizeBase) using rem units                                                      |
| fontSizeSm            | The font size of small text in the Widget. By default this is scaled from var(--fontSizeBase) using rem units                                                      |
| fontSizeXs            | The font size of extra-small text in the Widget. By default this is scaled from var(--fontSizeBase) using rem units                                                |
| fontSize2Xs           | The font size of double-extra small text in the Widget. By default this is scaled from var(--fontSizeBase) using rem units                                         |
| fontSize3Xs           | The font size of triple-extra small text in the Widget. By default this is scaled from var(--fontSizeBase) using rem units                                         |
| colorSuccess          | A color used to indicate positive actions or successful results in the Element                                                                                     |
| colorWarning          | A color used to indicate potentially destructive actions in the Element                                                                                            |
| colorPrimaryText      | The color of text appearing on top of any a var(--colorPrimary) background                                                                                         |
| colorBackgroundText   | The color of text appearing on top of any a var(--colorBackground) background                                                                                      |
| colorSuccessText      | The color of text appearing on top of any a var(--colorSuccess) background                                                                                         |
| colorDangerText       | The color of text appearing on top of any a var(--colorDanger) background                                                                                          |
| colorWarningText      | The color of text appearing on top of any a var(--colorWarning) background                                                                                         |
| colorTextSecondary    | The color used for text of secondary importance. For example, this color is used for the label of a tab that isn’t currently selected                              |
| colorTextPlaceholder  | The color used for input placeholder text in the Widget                                                                                                            |

## 4. Rules

The rules option is a map of CSS-like selectors to CSS properties, allowing granular customization of individual components. After defining your theme and variables, use rules to seamlessly integrate Elements to match the design of your site. The selector for a rule can target any of the public class names in the Element, as well as the supported states, pseudo-classes, and pseudo-elements for each class. For example, the following are valid selectors:

* .Tab, .Label, .Input, .InputLogo, .SaveWalletDetailsLabel, .OrPayUsingLabel, .TermsTextLabel, .InfoElement, .OrPayUsingLine
* .Tab:focus
* .Input--invalid, .Label--invalid, .InputLogo--invalid
* .Input::placeholder
* .billing-section, .billing-details-text
* .Input--empty, .InputLogo--empty



Each class name used in a selector supports an allowlist of CSS properties that you specify using camel case (for example, boxShadow for the box-shadow property). The following is the complete list of supported class names and corresponding states, pseudo-classes, and pseudo-elements.

### Tabs

<figure><img src="https://hyperswitch.io/img/site/rulesTabs.png" alt=""><figcaption></figcaption></figure>

| Class Name   | States     | Pseudo-Classes                     | Pseudo-Elements |
| ------------ | ---------- | ---------------------------------- | --------------- |
| .Tabs        | --selected | :hover, :focus, :active, :disabled |                 |
| fontSizeBase | --selected | :hover, :focus, :active, :disabled |                 |
| spacingUnit  | --selected | :hover, :focus, :active, :disabled |                 |

* .Tab, .Label, .Input
* .Tab:focus
* .Input--invalid, .Label--invalid
* .Input::placeholder

Each class name used in a selector supports an allowlist of CSS properties that you specify using camel case (for example, boxShadow for the box-shadow property). The following is the complete list of supported class names and corresponding states, pseudo-classes, and pseudo-elements.

```js
const appearance = {
  variables: {
    buttonBackgroundColor: "#FFFFFF",
    buttonTextColor: "#000000",
    // ... along with other variables
  },
  rules: {
    ".TabLabel": {
      overflowWrap: "break-word",
    },
    ".Tab--selected": {
      display: "flex",
      gap: "8px",
      flexDirection: "row",
      justifyContent: "center",
      alignItems: "center",
      padding: "15px 32px",
      background: "linear-gradient(109deg,#f48836,#f4364c)",
      color: "#ffffff",
      fontWeight: "700",
      borderRadius: "25px",
    },
    ".Tab--selected:hover": {
      display: "flex",
      gap: "8px",
      flexDirection: "row",
      justifyContent: "center",
      alignItems: "center",
      padding: "15px 32px",
      background: "linear-gradient(109deg,#f48836,#f4364c)",
      borderRadius: "25px",
      color: "#ffffff !important",
      fontWeight: "700",
    },
  },
};

const elements = hyper.elements({ clientSecret, appearance });
```

### Form Inputs

<figure><img src="../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

| Class Name | States             | Pseudo-Classes                       | Pseudo-Elements            |
| ---------- | ------------------ | ------------------------------------ | -------------------------- |
| .Label     | --empty, --invalid |                                      |                            |
| .Input     | --empty, --invalid | :hover, :focus, :disabled, :autofill | ::placeholder, ::selection |
| .Error     |                    |                                      |                            |

### Checkbox

<figure><img src="../../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

| Class Name     | States    | Pseudo-Classes | Pseudo-Elements |
| -------------- | --------- | -------------- | --------------- |
| .Checkbox      | --checked | :hover         |                 |
| .CheckboxLabel | --checked | :hover         |                 |
| .CheckboxInput | --checked | :hover         |                 |

### InputLogo

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-06 at 2.03.21 PM.png" alt=""><figcaption></figcaption></figure>

| Class Name | States    | Pseudo-Classes | Pseudo-Elements |
| ---------- | --------- | -------------- | --------------- |
| .InputLogo |           | :hover         |                 |
| .InputLogo | --invalid | :hover,        |                 |
| .InputLogo | --empty   | :hover         |                 |

### SaveWalletDetailsLabel

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-06 at 2.12.07 PM.png" alt=""><figcaption></figcaption></figure>

| Class Name              | States | Pseudo-Classes | Pseudo-Elements |
| ----------------------- | ------ | -------------- | --------------- |
| .SaveWalletDetailsLabel |        | :hover         |                 |

### OrPayUsingLabel

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-06 at 2.12.07 PM.png" alt=""><figcaption></figcaption></figure>

| Class Name       | States | Pseudo-Classes | Pseudo-Elements |
| ---------------- | ------ | -------------- | --------------- |
| .OrPayUsingLabel |        | :hover         |                 |

### OrPayUsingLine

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-10 at 3.02.49 PM.png" alt=""><figcaption></figcaption></figure>

| Class Name      | States | Pseudo-Classes | Pseudo-Elements |
| --------------- | ------ | -------------- | --------------- |
| .OrPayUsingLine |        | :hover         |                 |

### TermsTextLabel

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-06 at 2.18.00 PM.png" alt=""><figcaption></figcaption></figure>

| Class Name      | States | Pseudo-Classes | Pseudo-Elements |
| --------------- | ------ | -------------- | --------------- |
| .TermsTextLabel |        | :hover         |                 |

### InfoElement

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-06 at 2.21.32 PM.png" alt=""><figcaption></figcaption></figure>

| Class Name   | States | Pseudo-Classes | Pseudo-Elements |
| ------------ | ------ | -------------- | --------------- |
| .InfoElement |        | :hover         |                 |

## 5. Languages

Hyperswitch Unified Checkout supports localization in 6 languages. By default, the Unified Checkout SDK will detect the locale of the customer’s browser and display the localized version of the payment sheet if that locale is supported. In case it is not supported, we default to English. To override, you can send locale in [hyper.elements (options)](../../../../learn-more/sdk-reference/node.md)

We support the following locales -

* Arabic (ar)
* Catalan (ca)
* Chinese (zh)
* Deutsch (de)
* Dutch (nl)
* English (en)
* EnglishGB (en-GB)&#x20;
* FrenchBelgium (fr-BE)
* French (fr)
* Hebrew (he)
* Italian (it)
* Japanese (ja)&#x20;
* Polish (pl)
* Portuguese (pt)&#x20;
* Russian (ru)
* Spanish (es)
* Swedish (sv)

If you need support for locales other than the ones mentioned above, please contact the Hyperswitch team. Now you can test the payments on your app and go-live!

## 6. Confirm Button

The Styling APIs could be used to blend the Confirm Payment Button (handled by SDK) with your app.

| Variable              | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| buttonBackgroundColor | Sets the background color of the payment button                    |
| buttonHeight          | Define the height of the payment button                            |
| buttonWidth           | Specify the width of the payment button                            |
| buttonBorderRadius    | Adjust the border radius of the payment button for rounded corners |
| buttonBorderColor     | Sets the color of the border surrounding the payment button        |
| buttonTextColor       | Define the color of the text displayed on the payment button       |
| buttonTextFontSize    | Customize the font size of the text on the payment button          |
| buttonTextFontWeight  | Specify the font weight of the text on the payment button          |
| buttonBorderWidth     | Specify the border width of the button                             |

## 7. More Configurations

### Branding

You can decide whether to display the Hyperswitch branding using the `branding` prop

<pre class="language-javascript"><code class="lang-javascript"><strong>var paymentElementOptions = {
</strong> ...,
 branding: "never", // choose between "never" and "always"
}

&#x3C;PaymentElement id="payment-element" options={paymentElementOptions} />
</code></pre>

### Payment Methods Header Text

Customize the header text for the section displaying available payment methods.

<pre class="language-javascript"><code class="lang-javascript"><strong>var paymentElementOptions = {
</strong> ...,
 paymentMethodsHeaderText: "Select Payment Method",
}

&#x3C;PaymentElement id="payment-element" options={paymentElementOptions} />
</code></pre>

### Saved Payment Methods Header Text

Customize the header text for the section displaying saved payment methods.

<pre class="language-javascript"><code class="lang-javascript"><strong>var paymentElementOptions = {
</strong> ...,
 savedPaymentMethodsHeaderText: "Saved Payment Methods",
}

&#x3C;PaymentElement id="payment-element" options={paymentElementOptions} />
</code></pre>

### Custom Message for Card Terms

We provide a default message for card terms i.e.

```rescript
`By providing your card information, you allow ${company_name} to charge your card for future payments in accordance with their terms.`
```

If you would like to customize this message, you can do so by using the `customMessageForCardTerms` property in the `paymentElementOptions` object.

<pre class="language-javascript"><code class="lang-javascript"><strong>var paymentElementOptions = {
</strong> ...,
 customMessageForCardTerms: "Custom message for Card terms",
}

&#x3C;PaymentElement id="payment-element" options={paymentElementOptions} />
</code></pre>

### Hide Card Nickname Field

The `hideCardNicknameField` property allows you to hide the card nickname field when saving a card.

```javascript
var paymentElementOptions = {
  ...,
  hideCardNicknameField: true,  // default - false
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Hide Expired Saved Payment Methods

The `hideExpiredPaymentMethods` property allows you to control whether expired saved payment methods are hidden or not.

```javascript
var paymentElementOptions = {
  ...,
  hideExpiredPaymentMethods: false, // default - false
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Show Card Form by Default

The `showCardFormByDefault` property determines whether the card form is displayed by default or not.

```javascript
var paymentElementOptions = {
  ...,
  showCardFormByDefault: true,
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Terms

The `terms` property allows you to configure the display of terms for various payment methods.

```javascript
var paymentElementOptions = {
  ...,
  terms: {
    auBecsDebit: "always",
    bancontact: "auto",
    card: "never",
    ideal: "auto",
    sepaDebit: "always",
    sofort: "never",
    usBankAccount: "auto",
  },
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Display Saved Payment Methods

The `displaySavedPaymentMethods` property determines whether saved payment methods are displayed.

```javascript
var paymentElementOptions = {
  ...,
  displaySavedPaymentMethods: false,
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Display Saved Payment Methods Checkbox

The `displaySavedPaymentMethodsCheckbox` property determines whether the "Save payment methods" checkbox is displayed.

```javascript
var paymentElementOptions = {
  ...,
  displaySavedPaymentMethodsCheckbox: false, 
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Payment Method Order

The `paymentMethodOrder` property allows you to specify the order in which payment methods are displayed.

```javascript
var paymentElementOptions = {
  ...,
  paymentMethodOrder: ["card", "ideal", "sepaDebit", "sofort"],
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Business

The `business` property allows you to specify a business name to be attached to the terms. By default merchant name will be taken as business name.

```javascript
var paymentElementOptions = {
  ...,
  business: {
    name: "Example Business",
  },
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

### Read Only

The `readOnly` property puts the SDK into read-only mode, disabling all interactions.

<pre class="language-javascript"><code class="lang-javascript">var paymentElementOptions = {
  ...,
  readOnly: true,
};
<strong>
</strong>&#x3C;PaymentElement id="payment-element" options={paymentElementOptions} />;
</code></pre>

### Show Short Surcharge Message

The `showShortSurchargeMessage` property allows merchants to display a short message when a surcharge is applied, instead of the default message provided by the SDK.

{% hint style="success" %}
The short message format will be: **`Fee: {Currency} {Amount}`**
{% endhint %}

```javascript
var paymentElementOptions = {
  ...,
  showShortSurchargeMessage: true, // default - false
};

<PaymentElement id="payment-element" options={paymentElementOptions} />;
```

## Next step:

{% content-ref url="../../../payment-orchestration/quickstart/payment-methods-setup/" %}
[payment-methods-setup](../../../payment-orchestration/quickstart/payment-methods-setup/)
{% endcontent-ref %}
