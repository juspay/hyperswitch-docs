---
icon: book-atlas
---

# React Native Reference

Complete reference of everything you pass **into** the SDK

Package: `@juspay-tech/react-native-hyperswitch`

## Hyperswitch React Native SDK — API Reference <a href="#hyperswitch-react-native-sdk--api-reference" id="hyperswitch-react-native-sdk--api-reference"></a>

Complete reference of everything you pass **into** the SDK: every configuration object, every prop, every option — plus what the SDK returns back to you.

Package: `@juspay-tech/react-native-hyperswitch`

***

### 1. `Hyperswitch.init(config)` — `HyperswitchConfiguration` <a href="#id-1-hyperswitchinitconfig--hyperswitchconfiguration" id="id-1-hyperswitchinitconfig--hyperswitchconfiguration"></a>

Called once to configure the SDK with your account credentials.

| Prop                     | Type                                  | Required | Default  | Description                                                                  |
| ------------------------ | ------------------------------------- | -------- | -------- | ---------------------------------------------------------------------------- |
| `publishableKey`         | `string`                              | Yes      | —        | Publishable key from the Hyperswitch dashboard (`pk_snd_...` / `pk_prd_...`) |
| `profileId`              | `string`                              | No       | —        | Business profile id (`pro_...`)                                              |
| `platformPublishableKey` | `string`                              | No       | —        | Optional platform-specific publishable key                                   |
| `environment`            | `'PROD' \| 'SANDBOX' \| 'INTEG'`      | No       | `'PROD'` | Target environment                                                           |
| `customEndpoints`        | `CommonEndpoint \| OverrideEndpoints` | No       | —        | Endpoint overrides (below)                                                   |

```ts
// CommonEndpoint
{ commonEndpoint: string }

// OverrideEndpoints
{
  overrideEndpoints: {
    customBackendEndpoint?: string;
    customLoggingEndpoint?: string;
    customAssetEndpoint?: string;
    customSDKConfigEndpoint?: string;
    customAirborneEndpoint?: string;
  }
}
```

**Example**

```ts
const hyper = await Hyperswitch.init({
  publishableKey: 'pk_snd_xxxxxxxx',
  profileId: 'pro_xxxxxxxx',
});
```

***

### 2. `initPaymentSession(options)` — `PaymentSessionConfiguration` <a href="#id-2-initpaymentsessionoptions--paymentsessionconfiguration" id="id-2-initpaymentsessionoptions--paymentsessionconfiguration"></a>

Creates a payment session from the client secret your backend returns after creating a Payment Intent (or calling `/payments/session`).

| Prop               | Type     | Required | Description                                                 |
| ------------------ | -------- | -------- | ----------------------------------------------------------- |
| `sdkAuthorization` | `string` | Yes      | Client secret / `sdk_authorization` returned by your server |

```ts
const paymentSession = await hyper.initPaymentSession({ sdkAuthorization });
```

The same object is accepted by `hyper.elements(options)` and by the `options` prop of `<HyperElements>`.

***

### 3. `presentPaymentSheet(configuration)` — `PaymentSheetConfiguration` <a href="#id-3-presentpaymentsheetconfiguration--paymentsheetconfiguration" id="id-3-presentpaymentsheetconfiguration--paymentsheetconfiguration"></a>

Passed to `paymentSession.presentPaymentSheet(...)` **and** as the `options` prop of `PaymentElement`, `ApplePayButton`, `GooglePayButton`.

| Prop                                           | Type                                                         | Required | Description                                                                                                                                                                                                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `merchantDisplayName`                          | `string`                                                     | Yes      | Your store name — shown in the sheet, wallet dialogs and 3DS screens                                                                                                                                                                                                       |
| `appearance`                                   | `Appearance`                                                 | No       | Theme, colors, shapes, fonts, pay-button & logo customization                                                                                                                                                                                                              |
| `paymentMethodLayout`                          | `PaymentMethodLayout`                                        | No       | Tabs/accordion layout + saved-method customization                                                                                                                                                                                                                         |
| `walletButtonsConfiguration`                   | `WalletButtonsConfiguration`                                 | No       | Wallet button type/style/visibility                                                                                                                                                                                                                                        |
| `subscribedEvents`                             | `SubscriptionEvent[]`                                        | No       | Events delivered through `onChange`                                                                                                                                                                                                                                        |
| `locale`                                       | `Locale`                                                     | No       | Sheet language: `'en'`, `'en-GB'`, `'fr'`, `'fr-BE'`, `'de'`, `'es'`, `'ca'`, `'pt'`, `'it'`, `'pl'`, `'nl'`, `'nI-BE'`, `'sv'`, `'ru'`, `'lt'`, `'cs'`, `'sk'`, `'ls'`, `'cy'`, `'el'`, `'et'`, `'fi'`, `'nb'`, `'bs'`, `'da'`, `'ms'`, `'tr-CY'`, `'ar'`, `'he'`, `'ja'` |
| `primaryButtonLabel`                           | `string`                                                     | No       | Custom pay-button text (e.g. `"Complete Purchase"`)                                                                                                                                                                                                                        |
| `paymentSheetHeaderLabel`                      | `string`                                                     | No       | Custom header of the payment sheet                                                                                                                                                                                                                                         |
| `savedPaymentSheetHeaderLabel`                 | `string`                                                     | No       | Custom header of the saved-methods screen                                                                                                                                                                                                                                  |
| `paymentMethodOrder`                           | `string[]`                                                   | No       | Payment method ordering, e.g. `['card', 'google_pay', 'apple_pay']`                                                                                                                                                                                                        |
| `paymentMethodsConfig`                         | `{ paymentMethod: string; message?: string }[]`              | No       | Per-method info messages                                                                                                                                                                                                                                                   |
| `displaySavedPaymentMethods`                   | `boolean`                                                    | No       | Show/hide the customer's saved payment methods section                                                                                                                                                                                                                     |
| `displaySavedPaymentMethodsCheckbox`           | `boolean`                                                    | No       | Show/hide the "save for future use" checkbox                                                                                                                                                                                                                               |
| `displayDefaultSavedPaymentIcon`               | `boolean`                                                    | No       | Show the default badge on the default saved method                                                                                                                                                                                                                         |
| `displayPayButton`                             | `boolean`                                                    | No       | Show/hide the internal pay button (hide it if you render your own)                                                                                                                                                                                                         |
| `stickyPayButton`                              | `boolean`                                                    | No       | Pin the pay button to the bottom                                                                                                                                                                                                                                           |
| `allowsDelayedPaymentMethods`                  | `boolean`                                                    | No       | Allow async payment methods (e.g. bank debits)                                                                                                                                                                                                                             |
| `allowsPaymentMethodsRequiringShippingAddress` | `boolean`                                                    | No       | Allow methods that require a shipping address                                                                                                                                                                                                                              |
| `disableBranding`                              | `boolean`                                                    | No       | Hide Hyperswitch branding                                                                                                                                                                                                                                                  |
| `preloadCardElement`                           | `boolean`                                                    | No       | Preload the card form for faster first paint                                                                                                                                                                                                                               |
| `redirectionInfo`                              | `'hidden' \| 'shown'`                                        | No       | Show/hide the redirection notice                                                                                                                                                                                                                                           |
| `opensCardScannerAutomatically`                | `boolean`                                                    | No       | Open the card scanner automatically on entry                                                                                                                                                                                                                               |
| `alwaysSendCustomerAcceptance`                 | `boolean`                                                    | No       | Always send save-for-future-use consent                                                                                                                                                                                                                                    |
| `customer`                                     | `{ id?: string; ephemeralKeySecret?: string }`               | No       | Customer override for this presentation                                                                                                                                                                                                                                    |
| `billingDetails`                               | `AddressDetails`                                             | No       | Pre-fill billing details                                                                                                                                                                                                                                                   |
| `shippingDetails`                              | `AddressDetails`                                             | No       | Pre-fill shipping details                                                                                                                                                                                                                                                  |
| `placeholder`                                  | `{ cardNumber?: string; expiryDate?: string; cvv?: string }` | No       | Custom input placeholders                                                                                                                                                                                                                                                  |
| `splitCardFields`                              | `boolean`                                                    | No       | Show card number / expiry / CVC as separate fields                                                                                                                                                                                                                         |
| `netceteraSDKApiKey`                           | `string`                                                     | No       | Netcetera 3DS SDK key, if applicable                                                                                                                                                                                                                                       |

#### 3.1 `Appearance` <a href="#id-31-appearance" id="id-31-appearance"></a>

```ts
type Appearance = {
  theme?: Theme;            // 'Default' | 'Light' | 'Dark' | 'Minimal' | 'FlatMinimal'
                            // | 'Brutal' | 'Glass' | 'Skeu' | 'Clay' | 'Charcoal' | 'Soft'
  colors?: ColorType;
  shapes?: Shapes;
  font?: Font;
  primaryButton?: PrimaryButton;
  logo?: LogoCustomization;
};
```

**`ColorType`** — separate palettes for light & dark:

```ts
{
  light?: Colors;
  dark?: Colors;
}

type Colors = {
  primary?: string;
  background?: string;
  componentBackground?: string;
  componentBorder?: string;
  componentDivider?: string;
  componentText?: string;
  primaryText?: string;
  secondaryText?: string;
  placeholderText?: string;
  icon?: string;
  error?: string;
  loaderBackground?: string;
  loaderForeground?: string;
  overlay?: string;
  selectedComponentBackground?: string;
  selectedComponentBorder?: string;
  selectedComponentBorderWidth?: number;
  selectedComponentDivider?: string;
  selectedComponentText?: string;
};
```

**`Shapes`**:

```ts
{
  borderRadius?: number;
  borderWidth?: number;
  inputHeight?: number;
  gap?: number;
  shadow?: ShadowConfig;
}

type ShadowConfig = {
  color?: string;
  opacity?: number;
  blurRadius?: number;
  intensity?: number;
  offset?: { x?: number; y?: number };
};
```

**`Font`**:

```ts
{
  family?: string;                    // custom font family name
  scale?: number;                     // global text scale
  headingTextSizeAdjust?: number;
  subHeadingTextSizeAdjust?: number;
  placeholderTextSizeAdjust?: number;
  buttonTextSizeAdjust?: number;
  errorTextSizeAdjust?: number;
  linkTextSizeAdjust?: number;
  modalTextSizeAdjust?: number;
  cardTextSizeAdjust?: number;
}
```

**`PrimaryButton`**:

```ts
{
  height?: number;
  shapes?: Shapes;
  colors?: {
    light?: { background?: string; text?: string; border?: string };
    dark?:  { background?: string; text?: string; border?: string };
  };
}
```

**`LogoCustomization`**:

```ts
{
  borderRadius?: number;
  colors?: {
    light?: { backgroundColor?: string; selected?: string; unselected?: string };
    dark?:  { backgroundColor?: string; selected?: string; unselected?: string };
  };
  checkedIconForSelection?: {
    size?: number;
    bottom?: number;
    right?: number;
    colors?: {
      light?: { color?: string; stroke?: string };
      dark?:  { color?: string; stroke?: string };
    };
  };
}
```

#### 3.2 `PaymentMethodLayout` <a href="#id-32-paymentmethodlayout" id="id-32-paymentmethodlayout"></a>

```ts
{
  type?: 'tabs' | 'accordion' | 'spacedAccordion';
  showOneClickWalletsOnTop?: boolean;
  paymentMethodsArrangementForTabs?: 'default' | 'grid';
  defaultCollapsed?: boolean;
  radios?: boolean;
  spacedAccordionItems?: boolean;
  maxAccordionItems?: number;
  cvcIcon?: 'shown' | 'hidden';
  cardBrandIcon?: 'hidden' | 'animated' | 'standard' | 'hideGeneric';
  showCheckedIconForSelection?: boolean;
  savedMethodCustomization?: SavedMethodCustomization;
}

type SavedMethodCustomization = {
  defaultCollapsed?: boolean;
  hideCardExpiry?: boolean;
  hideCVCError?: boolean;
  cvcIcon?: 'shown' | 'hidden';
  groupingBehavior?: {
    displayInSeparateScreen?: boolean;
    displayInSeparateSection?: boolean;
    groupByPaymentMethods?: boolean;
  };
  hiddenPaymentMethods?: string[];    // e.g. ['paypal', 'google_pay', 'apple_pay']
};
```

#### 3.3 `WalletButtonsConfiguration` <a href="#id-33-walletbuttonsconfiguration" id="id-33-walletbuttonsconfiguration"></a>

```ts
{
  googlePay?: GooglePayConfiguration;
  applePay?: ApplePayConfiguration;
  payPal?: PayPalConfiguration;
}

type GooglePayConfiguration = {
  visibility?: 'hidden' | 'shown';
  buttonType?: 'BUY' | 'BOOK' | 'CHECKOUT' | 'DONATE' | 'ORDER' | 'PAY' | 'SUBSCRIBE' | 'PLAIN';
  buttonStyle?: { light?: 'light' | 'dark'; dark?: 'light' | 'dark' };
};

type ApplePayConfiguration = {
  visibility?: 'hidden' | 'shown';
  buttonType?: 'buy' | 'setUp' | 'inStore' | 'donate' | 'checkout' | 'book' | 'subscribe' | 'plain';
  buttonStyle?: { light?: 'white' | 'whiteOutline' | 'black'; dark?: 'white' | 'whiteOutline' | 'black' };
};

type PayPalConfiguration = {
  visibility?: 'hidden' | 'shown';
  buttonType?: 'paypal' | 'checkout' | 'buynow' | 'pay';
  buttonSize?: 'small' | 'medium' | 'large';
  buttonStyle?: { light?: 'gold' | 'blue' | 'white' | 'black' | 'silver';
                  dark?:  'gold' | 'blue' | 'white' | 'black' | 'silver' };
};
```

#### 3.4 `SubscriptionEvent` <a href="#id-34-subscriptionevent" id="id-34-subscriptionevent"></a>

Passed via `subscribedEvents`, received via `onChange`.

| Event                                 | Payload                                                                                                          | Meaning                            |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `PAYMENT_METHOD_STATUS`               | `{ paymentMethod: string; paymentMethodType: string; isSavedPaymentMethod: boolean; isOneClickWallet: boolean }` | A payment method is selected/ready |
| `PAYMENT_METHOD_INFO_CARD`            | `CardInfo` → below                                                                                               | Live card input details            |
| `PAYMENT_METHOD_INFO_BILLING_ADDRESS` | `{ country: string; state: string; postalCode: string }`                                                         | Billing address inputs             |
| `FORM_STATUS`                         | `{ status: string }`                                                                                             | Overall form validity              |
| `CVC_STATUS`                          | `{ isCvcFocused: boolean; isCvcBlur: boolean; isCvcEmpty: boolean }`                                             | CVC widget state (CardCVCElement)  |

```ts
type CardInfo = {
  bin: string | undefined;
  last4: string | undefined;
  brand: string | undefined;
  expiryMonth: string | undefined;
  expiryYear: string | undefined;
  formattedExpiry: string | undefined;
  isCardNumberComplete: boolean;
  isCvcComplete: boolean;
  isExpiryComplete: boolean;
  isCardNumberValid: boolean;
  isExpiryValid: boolean;
};
```

#### 3.5 `AddressDetails` (billing / shipping pre-fill) <a href="#id-35-addressdetails-billing--shipping-pre-fill" id="id-35-addressdetails-billing--shipping-pre-fill"></a>

```ts
{
  email?: string;
  phone?: { number?: string; code?: string };
  address?: {
    first_name?: string;
    last_name?: string;
    line1?: string;
    line2?: string;
    line3?: string;
    city?: string;
    state?: string;
    postalCode?: string;
    country?: string;     // ISO 2-letter country code
  };
}
```

***

### 4. Components — props you pass <a href="#id-4-components--props-you-pass" id="id-4-components--props-you-pass"></a>

#### 4.1 `<HyperElements>` <a href="#id-41-hyperelements" id="id-41-hyperelements"></a>

Provider that creates the Elements context. Everything below only works inside it.

| Prop       | Type                                                        | Required | Description                      |
| ---------- | ----------------------------------------------------------- | -------- | -------------------------------- |
| `hyper`    | `HyperswitchSession \| Promise<HyperswitchSession> \| null` | Yes      | Initialized SDK (or its promise) |
| `options`  | `{ sdkAuthorization: string }`                              | Yes      | Client secret from your backend  |
| `children` | `ReactNode`                                                 | Yes      | Your checkout UI                 |

#### 4.2 `<PaymentElement>` <a href="#id-42-paymentelement" id="id-42-paymentelement"></a>

| Prop              | Type                                  | Required | Description                                                                         |
| ----------------- | ------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| `widgetId`        | `string`                              | Yes      | Unique id — can also be passed as a string to `elements.confirmPayment('widgetId')` |
| `options`         | `PaymentSheetConfiguration`           | No       | Everything from §3                                                                  |
| `onPaymentResult` | `(result: PaymentResult) => void`     | Yes      | Result when the internal pay button is used                                         |
| `onChange`        | `(event: PaymentEventResult) => void` | No       | Subscribed events (§3.4)                                                            |
| `onReady`         | `() => void`                          | No       | Native view mounted (use `PAYMENT_METHOD_STATUS` for full readiness)                |
| `style`           | `ViewStyle`                           | No       | Layout                                                                              |
| `ref`             | `PaymentElementHandle`                | No       | Imperative confirm, below                                                           |

```ts
type PaymentElementHandle = {
  confirmPayment(options?: any): Promise<PaymentResult>;
};
```

#### 4.3 `<CardCVCElement>` <a href="#id-43-cardcvcelement" id="id-43-cardcvcelement"></a>

| Prop              | Type                                  | Required             | Description                                                                      |
| ----------------- | ------------------------------------- | -------------------- | -------------------------------------------------------------------------------- |
| `id`              | `string`                              | For headless confirm | Widget id — must be passed to `confirmWithCustomerLastUsedPaymentMethod({ id })` |
| `options`         | `CvcWidgetOptions`                    | No                   | See below                                                                        |
| `onChange`        | `(event: PaymentEventResult) => void` | No                   | `CVC_STATUS` events                                                              |
| `onReady`         | `() => void`                          | No                   | Widget ready for input                                                           |
| `onFocus`         | `() => void`                          | No                   | CVC field focused                                                                |
| `onBlur`          | `() => void`                          | No                   | CVC field blurred                                                                |
| `onPaymentResult` | `(result: PaymentResult) => void`     | No                   | Result if this widget completes a payment                                        |
| `style`           | `ViewStyle`                           | No                   | Layout                                                                           |

```ts
type CvcWidgetOptions = {
  appearance?: {
    theme?: Theme;
    colors?: ColorType;
    shapes?: Shapes;
    font?: Pick<Font, 'family' | 'scale'>;
  };
  placeholder?: string;              // e.g. '123'
  cvcIcon?: 'hidden' | 'shown';
  subscribedEvents?: SubscriptionEvent[];
};
```

#### 4.4 `<ApplePayButton>` / `<GooglePayButton>` <a href="#id-44-applepaybutton--googlepaybutton" id="id-44-applepaybutton--googlepaybutton"></a>

Identical props for both:

| Prop              | Type                                  | Required | Description                                                       |
| ----------------- | ------------------------------------- | -------- | ----------------------------------------------------------------- |
| `widgetId`        | `string`                              | Yes      | Unique widget id                                                  |
| `options`         | `PaymentSheetConfiguration`           | No       | `merchantDisplayName` + appearance + `walletButtonsConfiguration` |
| `onPaymentResult` | `(result: PaymentResult) => void`     | Yes      | Wallet payment result                                             |
| `onChange`        | `(event: PaymentEventResult) => void` | No       | `PAYMENT_METHOD_STATUS` = wallet usable                           |
| `onReady`         | `() => void`                          | No       | Native view mounted                                               |
| `style`           | `ViewStyle`                           | No       | Layout                                                            |

`PaymentEventResult` (delivered to every `onChange`):

```ts
{ eventName: string; payload: JSON / JSON String  }
```

***

### 5. Methods & return types — what the SDK gives back <a href="#id-5-methods--return-types--what-the-sdk-gives-back" id="id-5-methods--return-types--what-the-sdk-gives-back"></a>

#### 5.1 `HyperswitchSession` <a href="#id-51-hyperswitchsession" id="id-51-hyperswitchsession"></a>

| Member                        | Type                                                        |
| ----------------------------- | ----------------------------------------------------------- |
| `publishableKey`              | `string`                                                    |
| `initPaymentSession(options)` | `({ sdkAuthorization: string }) => Promise<PaymentSession>` |
| `elements(options)`           | `({ sdkAuthorization: string }) => Promise<Elements>`       |

#### 5.2 `PaymentSession` <a href="#id-52-paymentsession" id="id-52-paymentsession"></a>

| Method                                     | Signature                                                                               | Returns                                  |
| ------------------------------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------- |
| `presentPaymentSheet(configuration?)`      | `(PaymentSheetConfiguration?) => Promise<PaymentResult>`                                | `PaymentResult`                          |
| `getCustomerSavedPaymentMethods(options?)` | `({ hiddenPaymentMethods?: string[] }?) => Promise<CustomerSavedPaymentMethodsSession>` | `CustomerSavedPaymentMethodsSession`     |
| `updateIntent(intentResolver)`             | `(() => Promise<{ sdkAuthorization: string } \| null>) => Promise<void>`                | Re-syncs all widgets with the new intent |

#### 5.3 `Elements` <a href="#id-53-elements" id="id-53-elements"></a>

| Method                                        | Signature                                                                                                                   |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `confirmPayment(paymentElementRef, options?)` | `({ current: PaymentElementHandle \| null } \| string, { confirmParams?: Record<string, any> }?) => Promise<PaymentResult>` |
| `presentPaymentSheet(configuration?)`         | `(PaymentSheetConfiguration?) => Promise<PaymentResult>`                                                                    |
| `updateIntent(intentResolver)`                | `(() => Promise<{ sdkAuthorization: string }>) => Promise<void>`                                                            |
| `getCustomerSavedPaymentMethods(options?)`    | `({ hiddenPaymentMethods?: string[] }?) => Promise<CustomerSavedPaymentMethodsSession>`                                     |

#### 5.4 Hooks <a href="#id-54-hooks" id="id-54-hooks"></a>

| Hook                  | Returns                  | Notes                                            |
| --------------------- | ------------------------ | ------------------------------------------------ |
| `usePaymentSession()` | `PaymentSession \| null` | Null until `HyperElements` finishes initializing |
| `useWidgets()`        | `Elements \| null`       | Alias: `useElements()`                           |

#### 5.5 `PaymentResult` — returned everywhere <a href="#id-55-paymentresult--returned-everywhere" id="id-55-paymentresult--returned-everywhere"></a>

```ts
type PaymentResult = {
  status: 'completed' | 'canceled' | 'failed';
  type?: string;      // error type when failed
  message?: string;
};
```

#### 5.6 `CustomerSavedPaymentMethodsSession` <a href="#id-56-customersavedpaymentmethodssession" id="id-56-customersavedpaymentmethodssession"></a>

| Method                                            | Signature                                              | Description                                                                            |
| ------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| `getCustomerLastUsedPaymentMethodData()`          | `() => Promise<CustomerLastUsedPaymentMethod \| null>` | Most recently used saved method                                                        |
| `getCustomerDefaultSavedPaymentMethodData()`      | `() => Promise<CustomerLastUsedPaymentMethod \| null>` | Customer's default saved method                                                        |
| `getCustomerSavedPaymentMethodData()`             | `() => Promise<CustomerLastUsedPaymentMethod \| null>` | First available saved method                                                           |
| `confirmWithCustomerLastUsedPaymentMethod(args?)` | `({ id?: string }?) => Promise<PaymentResult>`         | One-click confirm with last-used method. `id` = mounted `CardCVCElement` id (required) |
| `confirmWithCustomerDefaultPaymentMethod(args?)`  | `({ id?: string }?) => Promise<PaymentResult>`         | One-click confirm with default method                                                  |

#### 5.7 `CustomerLastUsedPaymentMethod` <a href="#id-57-customerlastusedpaymentmethod" id="id-57-customerlastusedpaymentmethod"></a>

```ts
{
  payment_token: string;
  payment_method_id: string;
  customer_id: string;
  payment_method: string;              // e.g. 'card', 'wallet', 'bank_debit'
  payment_method_type: string;         // e.g. 'credit', 'debit', 'google_pay'
  payment_method_issuer: string;
  payment_method_issuer_code: string | null;
  recurring_enabled: boolean;
  installment_payment_enabled: boolean;
  payment_experience: string[];
  requires_cvv: boolean;               // show CardCVCElement when true
  default_payment_method_set: boolean;
  last_used_at: string;
  created: string;
  card: {
    scheme: string;
    issuer_country: string;
    last4_digits: string;
    expiry_month: string;
    expiry_year: string;
    card_holder_name: string;
    card_network: string;
    card_isin: string;
    card_issuer: string;
    card_type: string;
    card_token: string | null;
    card_fingerprint: string | null;
    nick_name: string;
    saved_to_locker: boolean;
  } | null;
  bank: string | null;
  surcharge_details: string | null;
  metadata: string | null;
  billing: {
    email?: string;
    phone?: Record<string, unknown>;
    address?: {
      line1?: string; line2?: string; line3?: string;
      city?: string; state?: string; country?: string;
      first_name?: string; last_name?: string;
    };
  } | null;
}
```

***

### 6. Minimal cheat-sheet <a href="#id-6-minimal-cheat-sheet" id="id-6-minimal-cheat-sheet"></a>

| You want to…           | Pass this                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Initialize the SDK     | `Hyperswitch.init({ publishableKey, profileId })`                                                                                             |
| Start a payment        | `hyper.initPaymentSession({ sdkAuthorization })`                                                                                              |
| Drop-in checkout       | `session.presentPaymentSheet({ merchantDisplayName, appearance })`                                                                            |
| Custom checkout        | `<HyperElements hyper options={{ sdkAuthorization }}>` + `PaymentElement` / wallet buttons                                                    |
| Confirm manually       | `widgets.confirmPayment(paymentRef)` or `paymentRef.current.confirmPayment()`                                                                 |
| Saved card + CVC       | `session.getCustomerSavedPaymentMethods()` → `CardCVCElement id="x"` → `methodsSession.confirmWithCustomerLastUsedPaymentMethod({ id: 'x' })` |
| Change amount mid-flow | `session.updateIntent(async () => ({ sdkAuthorization: newSecret }))`                                                                         |
| Handle every result    | `PaymentResult.status` → `'completed' \| 'canceled' \| 'failed'`                                                                              |
