---
description: Implement Juspay Hyperswitch React SDK for seamless payment integration in React web applications
icon: bars-progress
---

# Customization

{% hint style="info" %}
You can customize the React Native Unified Checkout to supports visual customization, which allows you to match the design of your app
{% endhint %}

## Appearance

Use the `appearance` parameter to customize colors, fonts, and more when calling `initPaymentSheet()` or via the `options` prop when using `PaymentWidget`.

## Colors

Customize the colors in the mobile Payment Element by modifying the color categories. Each color category determines the color of one or more components in the UI. For example, primary defines the color of the Pay button

<table><thead><tr><th width="274.89453125">Color Category</th><th>Usage</th></tr></thead><tbody><tr><td>primary</td><td>Primary defines the color of the Pay button and selected items</td></tr><tr><td>background</td><td>The color used for the background of your Payment page</td></tr><tr><td>componentBackground</td><td>The color used for the background of inputs, tabs, and other components</td></tr><tr><td>componentBorder</td><td>The color used for the external border of inputs, tabs, and other components in your PaymentSheet</td></tr><tr><td>componentDivider</td><td>The color used for the internal border (meaning the border is shared with another component) of inputs, tabs, and other components in your PaymentSheet</td></tr><tr><td>primaryText</td><td>The color of the header text in your Payment page</td></tr><tr><td>secondaryText</td><td>The color of the label text of input fields</td></tr><tr><td>componentText</td><td>The color of the input text in your PaymentSheet components, such as the user's card number or zip code</td></tr><tr><td>placeholderText</td><td>The color of the placeholder text of input fields</td></tr><tr><td>icon</td><td>The color used for icons in your Payment Sheet, such as the close (x) button</td></tr><tr><td>error</td><td>The color used to indicate errors or destructive actions in your Payment Sheet</td></tr></tbody></table>

```js
appearance: {
   colors: {
   primary: '#F8F8F2',
   background: '#ffffff',
   componentBackground: '#E6DB74',
   componentBorder: '#FD971F',
   componentDivider: '#FD971F',
   primaryText: '#F8F8F2',
   secondaryText: '#75715E',
   componentText: '#AE81FF',
   placeholderText: '#E69F66',
   icon: '#F92672',
   error: '#FF0000',
 }
}
```

> Note : To support dark mode, pass maps for both `light` and `dark` colors maps to `colors`

```js
colors: {
   light:{
      primary: '#F8F8F2',
      background: '#00FF00',
      componentBackground: '#E6DB74',
      componentBorder: '#FD971F',
      componentDivider: '#FD971F',
      primaryText: '#F8F8F2',
      secondaryText: '#75715E',
      componentText: '#AE81FF',
      placeholderText: '#E69F66',
      icon: '#F92672',
      error: '#F92672',
   },
   dark: {
      primary: '#00ff0099',
      background: '#ff0000',
      componentBackground: '#ff0080',
      componentBorder: '#62ff08',
      componentDivider: '#d6de00',
      primaryText: '#5181fc',
      secondaryText: '#ff7b00',
      componentText: '#00ffff',
      placeholderText: '#00ffff',
      icon: '#f0f0f0',
      error: '#0f0f0f',
    },
 },
```

## Shapes

Customize the border radius, border width, and shadow used across the payment UI.

| Shape Category | Usage                                                             |
| -------------- | ----------------------------------------------------------------- |
| borderRadius   | Corner radius of input fields, tabs, and other components.        |
| borderWidth    | Border thickness across input fields, tabs, and other components. |

```js
shapes: {
    borderRadius: 10,
    borderWidth: 1,
  },
```

## Specific UI components

The sections above describe customization options that affect the mobile Payment Element broadly, across multiple UI components. We also provide customization options specifically for the primary button (for example, the Pay button).

Customization options for specific UI components take precedence over other values. For example, `primaryButton.shapes.borderRadius` overrides the value of `shapes.borderRadius`.

### Primary Button

Overrides global `colors` and `shapes` for the primary button (e.g. the Pay button). Takes precedence over global values.

```js
primaryButton: {
    colors: {
      background: '#000000',
      text: '#ffffff',
      border: '#ff00ff',
    },
    shapes: {
      borderRadius: 10,
      borderWidth: 1.5,
    },
  },

```

#### Google Pay Button

```
googlePay: {
  buttonType: 'BUY',   // BUY | BOOK | CHECKOUT | DONATE | ORDER | PAY | SUBSCRIBE | PLAIN
  buttonStyle: {
    light: 'dark',
    dark: 'light',
  }
}
```

### Apple Pay Button

```
applePay: {
  buttonType: 'buy',   // buy | setUp | inStore | donate | checkout | book | subscribe | plain
  buttonStyle: {
    light: 'black',    // white | whiteOutline | black
    dark: 'white',
  }
}
```

Now you can test the payments on your app and go-live!
