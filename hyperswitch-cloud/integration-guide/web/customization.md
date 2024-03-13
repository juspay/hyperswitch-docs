---
description: Customize your Web unified checkout
---

# Customization

{% hint style="info" %}
You can customize the Unified Checkout to support your checkout context and brand guidelines by using Layouts and Styling APIs
{% endhint %}

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

## 2. Styling variables

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

## 3. Rules

The rules option is a map of CSS-like selectors to CSS properties, allowing granular customization of individual components. After defining your theme and variables, use rules to seamlessly integrate Elements to match the design of your site. The selector for a rule can target any of the public class names in the Element, as well as the supported states, pseudo-classes, and pseudo-elements for each class. For example, the following are valid selectors:

* .Tab, .Label, .Input
* .Tab:focus
* .Input--invalid, .Label--invalid
* .Input::placeholder

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

### Tabs

<figure><img src="../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

| Class Name   | States     | Pseudo-Classes                     | Pseudo-Elements |
| ------------ | ---------- | ---------------------------------- | --------------- |
| .Tabs        | --selected | :hover, :focus, :active, :disabled |                 |
| fontSizeBase | --selected | :hover, :focus, :active, :disabled |                 |
| spacingUnit  | --selected | :hover, :focus, :active, :disabled |                 |

```js
const appearance = {
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

const elements = hyper.elements({ clientSecret, appearance });
```

### Form Inputs

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

| Class Name | States             | Pseudo-Classes                       | Pseudo-Elements            |
| ---------- | ------------------ | ------------------------------------ | -------------------------- |
| .Label     | --empty, --invalid |                                      |                            |
| .Input     | --empty, --invalid | :hover, :focus, :disabled, :autofill | ::placeholder, ::selection |
| .Error     |                    |                                      |                            |

### Checkbox

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

| Class Name     | States    | Pseudo-Classes | Pseudo-Elements |
| -------------- | --------- | -------------- | --------------- |
| .Checkbox      | --checked | :hover         |                 |
| .CheckboxLabel | --checked | :hover         |                 |
| .CheckboxInput | --checked | :hover         |                 |

## 4. Languages

Hyperswitch Unified Checkout supports localization in 6 languages. By default, the Unified Checkout SDK will detect the locale of the customer’s browser and display the localized version of the payment sheet if that locale is supported. In case it is not supported, we default to English. To override, you can send locale in [hyper.elements (options)](../../../learn-more/sdk-reference/node.md)

We support the following locales -

* Arabic (ar)
* Hebrew (he)
* French (fr)
* German (de)
* English (en)
* Japanese (ja)

If you need support for locales other than the ones mentioned above, please contact the Hyperswitch team. Now you can test the payments on your app and go-live!

## 5. Confirm Button

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

## 6. Handle Saved Payment Methods

### Screen

You can enable/disable saved payment methods screen using the following prop:

```javascript
var paymentElementOptions = {
 ...,
 displaySavedPaymentMethods: true,
}

<PaymentElement id="payment-element" options={paymentElementOptions} />
```

### Checkbox

You can stop your users from saving their payment methods using the following prop:

```javascript
var paymentElementOptions = {
 ...,
 displaySavedPaymentMethodsCheckbox: false,
}

<PaymentElement id="payment-element" options={paymentElementOptions} />
```

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

## Next step:

{% content-ref url="../../payment-methods-setup/" %}
[payment-methods-setup](../../payment-methods-setup/)
{% endcontent-ref %}
