---
description: 'Visual customization: Colors, shapes, specific UI components'
---

# Customization

You can customize the React Native Unified Checkout to supports visual customization, which allows you to match the design of your app. You can modify colors, fonts, and more by using the `appearance` parameter when you call `initPaymentSheet()`.

## Colors

Customize the colors in the mobile Payment Element by modifying the color categories. Each color category determines the color of one or more components in the UI. For example, primary defines the color of the Pay button

| Color Category      | Usage                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| primary             | Primary defines the color of the Pay button and selected items                                                                                          |
| background          | The color used for the background of your Payment page                                                                                                  |
| componentBackground | The color used for the background of inputs, tabs, and other components                                                                                 |
| componentBorder     | The color used for the external border of inputs, tabs, and other components in your PaymentSheet                                                       |
| componentDivider    | The color used for the internal border (meaning the border is shared with another component) of inputs, tabs, and other components in your PaymentSheet |
| primaryText         | The color of the header text in your Payment page                                                                                                       |
| secondaryText       | The color of the label text of input fields                                                                                                             |
| componentText       | The color of the input text in your PaymentSheet components, such as the user's card number or zip code                                                 |
| placeholderText     | The color of the placeholder text of input fields                                                                                                       |
| icon                | The color used for icons in your Payment Sheet, such as the close (x) button                                                                            |
| error               | The color used to indicate errors or destructive actions in your Payment Sheet                                                                          |

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

Note To support dark mode, pass maps for both light and dark colors to colors.

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

you can customize the border radius, border width, and shadow used throughout the mobile Payment Element.

| Shape Category | Usage                                                                                   |
| -------------- | --------------------------------------------------------------------------------------- |
| borderRadius   | radius of the border of the input fields, tabs and other components of the payment page |
| borderWidth    | width of the border used to across input fields, tabs and other components              |

```js
shapes: {
    borderRadius: 10,
    borderWidth: 1,
  },
```

## Specific UI components

The sections above describe customization options that affect the mobile Payment Element broadly, across multiple UI components. We also provide customization options specifically for the primary button (for example, the Pay button).

Customization options for specific UI components take precedence over other values. For example, `primaryButton.shapes.borderRadius` overrides the value of `shapes.borderRadius`.

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
