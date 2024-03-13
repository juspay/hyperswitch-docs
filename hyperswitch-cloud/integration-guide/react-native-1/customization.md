---
description: 'Visual customization: Colors, shapes, specific UI components'
---

# Customization

{% hint style="info" %}
You can customize the Flutter Unified Checkout to supports visual customization, which allows you to match the design of your app
{% endhint %}

You can modify colors, fonts, and more by using the instance of `appearance` class.&#x20;

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

For using custom colors for SDK, you should create an instance of `ColorsObject` class by passing the above attributes to its constructor. Now, you have to create an instance of `DynamicColors` class by invoking its constructor and passing the object of `ColorsObject` class created earlier. Finally, you have to create an instance of `Appearance` class by passing the object of `DynamicColors` class.

Consider the below code for your reference.

```dart
ColorsObject colorsObject = ColorsObject(
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
      error: '#F92672'
    );

    DynamicColors colors =
        DynamicColors(light: colorsObject);
    PrimaryButton primaryButton = PrimaryButton(colors: colors);

    Appearance appearance = Appearance(
      colors: colors,
      primaryButton: primaryButton,
    );
```

## Configuration and Appearance

Now, create an instance of `Configuration` class by invoking its constructor and passing the object of `Appearance` class created above. Then, you have to create an instance of `PaymentSheetParams` class by invoking its constructor and passing  the object of `Configuration` class created earlier.

Consider the below code for your reference.

```dart
  Configuration configuration= Configuration(appearance: appearance)
  configuration.displaySavedPaymentMethods: true,
  configuration.displaySavedPaymentMethodsCheckbox: true,
 
  PaymentSheetParams params = PaymentSheetParams(
      publishableKey: "YOUR_PUBLISHABLE_KEY",
      clientSecret: clientSecret,
      configuration: configuration,
    );
```

{% hint style="info" %}
Set `displaySavedPaymentMethods` to false to disable saved cards.

Set `displaySavedPaymentMethodsCheckbox` to false to stop your users from saving their payment methods.\
Set `disableBranding` to false to disable Hyperswitch branding.\
Set `primaryButtonLabel` to "Pay Button Text" to display custom text\
Set `paymentSheetHeaderLabel` to "Heading Text" to display custom heading
{% endhint %}



## Custom Placeholders And Branding

To set custom placeholder text for card number, expiry date or cvv input fields, you may set the `placeholder` property for these as shown below.

```dart
configuration.placeholder.cardNumber = "YOUR_CUSTOM_CARD_NUMBER_PLACEHOLDER"
configuration.placeholder.expiryDate = "YOUR_CUSTOM_EXPIRY_DATE_PLACEHOLDER"
configuration.placeholder.cvv = "YOUR_CUSTOM_CVV_PLACEHOLDER"
```

To disable Hyperswitch branding in the SDK, you may set the `disableBranding` property to true

```dart
configuration.disableBranding = true
```

Finally, you can pass the object of PaymentSheetParams to `initPaymentSheet` as shown in the previous [section](react-native-with-node-backend.md#id-3.3-collect-payment-details).&#x20;

{% hint style="info" %}
Note To support dark mode, pass objects of `ColorsObject` class for both light and dark colors to constructor of `DynamicColors` class like below.
{% endhint %}

```dart
ColorsObject lightColorsObject = ColorsObject(
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
      error: '#F92672'
    );
    
 ColorsObject darkColorsObject = ColorsObject(
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
    );

DynamicColors colors = DynamicColors(light: lightColorsObject,dark: darkColorsObject);

```

## Shapes

You can customize the border radius, border width, and shadow used throughout the mobile Payment Element. Using an Object of inbuilt class `Shapes`.

| Shape Category | Usage                                                                                   |
| -------------- | --------------------------------------------------------------------------------------- |
| borderRadius   | radius of the border of the input fields, tabs and other components of the payment page |
| borderWidth    | width of the border used to across input fields, tabs and other components              |

```dart
 Shapes shapes=Shapes(borderRadius:10.0 ,borderWidth: 10.0);
```

Now you can test the payments on your app and go-live!

## Languages

Hyperswitch Flutter SDK supports localization in 6 languages. The default locale is English (en). To override, you can send locale in the appearance object. You may refer the below code for your reference.

```dart
Appearance appearance = Appearance(
     ...
      locale: 'LOCALE_CODE'
    );
```

We support the following locales -

* Arabic (ar)
* Hebrew (he)
* German (de)
* English (en)
* English (en-GB )
* Japanese (ja)
* French (fr)
* French (Belgium) (fr-BE)
* Spanish (es)
* Catalan (ca)
* Portuguese (pt)
* Italian (it)
* Polish (pl)
* German (de)
* Dutch (nl)
* Dutch (Belgium) (nl-BE)
* Swedish (sv)
* Russian (ru)
* Lithuanian (lt)
* Czech (cs)
* Slovak (sk)
* Icelandic (is)
* Welsh (cy)
* Greek (el)
* Estonian (et)
* Arabic (ar)
* Finnish (fi)
* Norwegian (nb)
* Bosnian (bs)
* Danish (da)
* Malay (ms)
* Turkish (tr-CY)

## Next step:

{% content-ref url="../../payment-methods-setup/" %}
[payment-methods-setup](../../payment-methods-setup/)
{% endcontent-ref %}

