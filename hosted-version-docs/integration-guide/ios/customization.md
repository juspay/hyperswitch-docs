# Customization

You can customize the iOS Unified Checkout to support your checkout context and brand guidelines by chenging fonts, colours, shapes and layouts(coming soon).

Create a `PaymentSheet.Configuration` object with an `appearance` object in order to be able to match the design of your app.

## Fonts

Set `typography.fontResId` to your custom font’s resource ID to customize your font. Set a `typography.sizeScaleFactor` multiplier to increase or decrease the font size

```swift
var configuration = PaymentSheet.Configuration()
configuration.appearance.font.base = UIFont(name: "Helvetica", size: UIFont.systemFontSize)!
configuration.allowsDelayedPaymentMethods = true
configuration.defaultBillingDetails =
    ["address":
      [ "city": "San Fransico",
        "country": "US",
        "line1": "1467",
        "line2": "Harrison Street",
        "postalCode": "94122",
        "state": "California"
      ],
      "email": "johndoe@hyperswitch.io",
      "name": "John",
      "phone": "1234567890"
    ]
```

## Colors

Modify the colour categories in `PaymentSheet.Colors` to customize the colours on the mobile payment sheet as follows:

| Colour Category  | Usage                                                                          |
| ---------------- | ------------------------------------------------------------------------------ |
| appBarIcon       | Color used for icons in the payment page ex: close (x) button                  |
| component        | Background colour of inputs, tabs and other components                         |
| componentBorder  | Border color for inputs, tabs and other components                             |
| componentDivider | Color for divider lines used inside inputs, tabs and other components          |
| error            | Color for error messages to the user on the payment page                       |
| onComponent      | Color of text and other elements inside components                             |
| onSurface        | Color for items appearing on the surface of the payment page, Ex: text prompts |
| placeholderText  | Color for input fields placeholder text                                        |
| primary          | The primary color to be used across the payment page                           |
| subtitle         | Color of secondary text like prompts for input fields                          |
| surface          | Color of the payment page                                                      |

## shapes

Modify the corner radius and border width used across the payment page using `appearance.shapes`.

| Shape Category      | Usage                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| borderStrokeWidthDp | Width of the border used to across input fields, tabs and other components of the payment page |
| cornerRadiusDp      | Corner radius of the input fields, tabs and other components                                   |
