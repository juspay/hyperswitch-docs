---
description: Customize your Android Unified checkout
---

# Customization

{% hint style="info" %}
You can customize the Android Unified Checkout to support your checkout context and brand guidelines by changing fonts, colors, shapes and layouts.
{% endhint %}

Create a `PaymentSheet.Configuration` object with an `appearance` object in order to be able to match the design of your app.

## Fonts

Set `typography.fontResId` to your custom font's resource ID to customize your font. Set a `typography.sizeScaleFactor` multiplier to increase or decrease the font size

```kotlin
val appearance = PaymentSheet.Appearance(
  typography = PaymentSheet.Typography(10.0f, R.font.MY_FONT)
)
```

## Colors

Modify the color categories in `PaymentSheet.Colors` to customize the colors on the mobile payment sheet as follows:

| Color Category   | Usage                                                                          |
| ---------------- | ------------------------------------------------------------------------------ |
| appBarIcon       | Color used for icons in the payment page ex: close (x) button                  |
| component        | Background color of inputs, tabs and other components                          |
| componentBorder  | Border color for inputs, tabs and other components                             |
| componentDivider | Color for divider lines used inside inputs, tabs and other components          |
| error            | Color for error messages to the user on the payment page                       |
| onComponent      | Color of text and other elements inside components                             |
| onSurface        | Color for items appearing on the surface of the payment page, Ex: text prompts |
| placeholderText  | Color for input fields placeholder text                                        |
| primary          | The primary color to be used across the payment page                           |
| subtitle         | Color of secondary text like prompts for input fields                          |
| surface          | Color of the payment page                                                      |

## Shapes

Modify the corner radius and border width used across the payment page using `appearance.shapes`.

| Shape Category      | Usage                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| borderStrokeWidthDp | Width of the border used to across input fields, tabs and other components of the payment page |
| cornerRadiusDp      | Corner radius of the input fields, tabs and other components                                   |

Now you can test the payments on your app and go-live!

## Next step:

{% content-ref url="../../../payment-orchestration/quickstart/payment-methods-setup/" %}
[payment-methods-setup](../../../payment-orchestration/quickstart/payment-methods-setup/)
{% endcontent-ref %}
