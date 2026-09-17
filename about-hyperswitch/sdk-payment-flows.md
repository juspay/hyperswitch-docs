---
icon: wave
metaLinks:
  alternates:
    - sdk-payment-flows.md
---

<!-- truth manifest; hyperswitch 5fb7e5598eadd8ed5fa42822427107f271a1e112; spec crates/openapi/src/routes/payments.rs@5fb7e5598eadd8ed5fa42822427107f271a1e112
     symbols: PaymentsResponse.payment_link = crates/api_models/src/payments.rs:7813-7814, struct PaymentsResponse at :7444
     symbols: PaymentLinkResponse.link = crates/api_models/src/payments.rs:13099-13100
     symbols: PaymentLinkResponse.secure_link = crates/api_models/src/payments.rs:13101-13102
     symbols: PaymentLinkResponse.payment_link_id = crates/api_models/src/payments.rs:13103-13104
     symbols: PaymentsRequest.payment_link = crates/api_models/src/payments.rs:1461
     symbols: PaymentsRequest.payment_link_config = crates/api_models/src/payments.rs:1464
     symbols: session_tokens.vault_details carries the vault SDK authorization = crates/router/src/core/payments/update_context.rs:277-281
     symbols: Web SDK source = hyperswitch-web@e8e869329c44aa769efe3df89f98e4fd51de6d04
     symbols: hyper.initPaymentMethodSession = hyperswitch-web src/hyper-loader/Hyper.res:841
     symbols: hyper instance exposes 13 members, elements, confirmPayment, initPaymentSession, initPaymentMethodSession among them = hyperswitch-web src/hyper-loader/Hyper.res:827-842
     symbols: paymentMethodSession exposes createCardForm, update, on, deinit, fields = hyperswitch-web src/hyper-loader/PaymentMethodSession.res:1074-1080
     symbols: cardForm exposes create, on, tokenize, deinit, update, fields = hyperswitch-web src/hyper-loader/PaymentMethodSession.res:1065-1072
     symbols: cardCvc mounted alone routes tokenize to flow update = hyperswitch-web src/hyper-loader/PaymentMethodSession.res:976-981
     symbols: cardNumber mounted routes tokenize to flow save = hyperswitch-web src/hyper-loader/PaymentMethodSession.res:971-973
     symbols: no field, or cardExpiry alone, returns incomplete_field_set = hyperswitch-web src/hyper-loader/PaymentMethodSession.res:939-949,970,974-975
     symbols: 15 element names accepted by elements.create, card, payment, paymentMethodsSDK, cardNumber, cardExpiry, cardCvc, googlePay, payPal, applePay, paymentMethodCollect, samsungPay, klarna, expressCheckout, paze, paymentMethodsManagement = hyperswitch-web src/Types/CardThemeType.res:106-120
     symbols: React Native SDK source = react-native-hyperswitch@8fc8e88552689fedadcd39ee602fe9f137f16b56
     symbols: @juspay-tech/react-native-hyperswitch version 1.3.4 = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/package.json
     symbols: Hyperswitch.init is loadHyper = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/index.ts:20-56
     symbols: HyperswitchConfiguration publishableKey, platformPublishableKey, profileId, environment, customEndpoints = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/types/definitions.ts:27-33
     symbols: HyperswitchEnvironment PROD, SANDBOX, INTEG with PROD the default = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/types/definitions.ts:19; src/index.ts:28
     symbols: PaymentSessionConfiguration.sdkAuthorization = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/types/definitions.ts:35-37
     symbols: 6 peerDependencies, @sentry/react-native, react, react-native, react-native-inappbrowser-reborn, react-native-svg, react-native-webview = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/package.json
     symbols: GooglePayButton, ApplePayButton, CardCVCElement, PaymentElement, HyperElements, usePaymentSession, useWalletSession, useElements = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/index.ts:60-83
     symbols: isPlatformPaySupported, isGooglePaySupported, isApplePaySupported, isWalletSupported = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/index.ts:72-77
     symbols: walletSession isWalletEligible, isGooglePayEligible, isApplePayEligible, launchWallet, launchGooglePay, launchApplePay = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/session/WalletSession.ts:13-45
     symbols: paymentSession presentPaymentSheet, getCustomerSavedPaymentMethods, getWalletSession, updateIntent = react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/types/definitions.ts:63-74
     symbols: 8 optional React Native companion packages, click-to-pay, netcetera-3ds, trident-3ds, samsung-pay, paypal, scancard, vault, payment-methods = react-native-hyperswitch packages/@juspay-tech/, one package.json each
     symbols: Web headless getCustomerSavedPaymentMethods, getCustomerDefaultSavedPaymentMethodData, confirmWithCustomerDefaultPaymentMethod, confirmWithLastUsedPaymentMethod = hyperswitch-docs integration-guide/payment-experience/pay-then-vault/web/headless-sdk.md
     derived: 15000 ms wallet session bootstrap bound = WALLET_SESSION_TIMEOUT_MS passed to withTimeout around getWalletSession, sources react-native-hyperswitch packages/@juspay-tech/react-native-hyperswitch/src/session/WalletSession.ts:48,50-68,78-86
     absent: SAQ-A boundary for the hosted SDK = checked hyperswitch-docs@670f0412f12a3c199368931f6939362214eb223d self-hosting-space/guides-for-self-hosting/security-and-compliance.md:141-154 plus a repo-wide grep for SAQ, no published Hyperswitch statement of an SAQ-A boundary for the hosted SDK found; the two SAQ-A sentences that exist are scoped to the external-vault model at integration-guide/workflows/vault/self-hosted-orchestration-with-external-or-third-party-pci-vault.md:165 and integration-space/cashier-payments/faqs.md:16
     absent: server-side confirmation of a standalone Web wallet button = checked hyperswitch-web@e8e869329c44aa769efe3df89f98e4fd51de6d04 src/hyper-loader/Hyper.res:483-505, src/Utilities/PaymentBody.res:315-324, src/Components/PayNowButton.res:20-59, no path found that hands the wallet token to the merchant server for confirmation there
     checked: 2026-09-17 -->

# SDK Payment flows

{% hint style="info" %}
If you're complete beginner to Digital Payments, take a look at this [Payments 101 ](https://hyperswitch.io/blogs/payments-101-for-a-developer)blog to get familiar with terminologies.
{% endhint %}

### **Payments flow**

There are multiple stages in a Payment flow depending on the payment methods that are involved. Considering an one-time payment method where there was no redirection involved, the following stages form the Payment flow:

**a) Creating a Payment:** When your customer wants to checkout, create a payment by hitting the payments/create endpoint. Fetch and store the payment\_id and client\_secret

**b) Loading the SDK:** After your customer checks out, load the Hyperswitch SDK by initiating it with the client\_secret and publishable\_key

**c) SDK being rendered:** After you initiate the SDK, the SDK makes several API calls involving the /sessions and /payment\_methods endpoints to load relevant payment methods and any saved cards associated with the customer

**d) Customer enters the payment method data:** After the SDK is fully rendered, your customer would choose a payment method and enter the relevant information and click pay

**e) Confirming the payment:** After the customer clicks pay, the SDK calls the payments/confirm endpoint with the customer's payment method details and post response, it displays the payment status

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Here's a more detailed version of the payment flow:

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#2563EB",
    "lineColor": "#2563EB",
    "secondaryColor": "#EFF6FF",
    "tertiaryColor": "#DBEAFE",
    "fontFamily": "Inter, system-ui, sans-serif",
    "fontSize": "14px",
    "textColor": "#000000",

    "actorBkg": "#346DDB",
    "actorBorder": "#999999",
    "actorTextColor": "#ffffff",

    "signalColor": "#000000",
    "signalTextColor": "#696969",

    "labelBoxBkgColor": "#346DDB",
    "labelBoxBorderColor": "#2563EB",
    "loopTextColor": "#000080"
  }
}}%%
sequenceDiagram
    participant MS as Merchant Server
    participant MC as Merchant Client
    participant SDK as Hyperswitch SDK
    participant HS as Hyperswitch Server
    participant PS as Processor Server

    MS->>HS: payments/create (amount, currency, api_key)
    HS-->>MS: payments/create response (payment_id, client_secret)
    MS->>MC: pass client_secret, publishable_key
    MC->>SDK: initiate SDK (client_secret, publishable_key)
    SDK->>HS: /payment_methods_list (client_secret)
    HS-->>SDK: /payment_methods_list response (eligible payment methods)
    Note over SDK: Display payment sheet with eligible methods
    Note over SDK: Customer selects desired payment method <br>(Say Card and Enters their Card Details)
    SDK->>HS: payments/confirm (client_secret, payment_method_data)
    HS->>PS: payments/confirm to processor (with merchant credentials)
    PS-->>HS: payments/confirm response (status)
    HS-->>SDK: payments/confirm response (status)
    SDK-->>MC: return to return_url with status
```

### **How does Payment flow vary across Payment methods?**

<table data-full-width="false"><thead><tr><th>Customer Action</th><th>Direct/Redirect flows</th><th>Payment- finalized immediately</th><th>Payment- finalized later</th></tr></thead><tbody><tr><td><strong>Customer action required before payments/ confirm</strong></td><td><strong>Within Hyperswitch SDK</strong></td><td><ul><li>Non 3DS Cards</li></ul></td><td><ul><li>Bank Debits like ACH Debit, BACS Debit, SEPA Debit</li></ul></td></tr><tr><td><strong>Customer action required before payments/ confirm</strong></td><td><strong>3rd party Redirect/SDK</strong></td><td><ul><li>Wallets like Apple Pay, Google pay, Paypal, AliPay</li><li>BNPL like Klarna, Afterpay, Affirm</li></ul></td><td><br></td></tr><tr><td><strong>Customer action required after payments/ confirm</strong></td><td><strong>3rd party Redirect</strong></td><td><ul><li>3DS cards</li><li>Bank Redirects like iDeal, Giropay, eps</li></ul></td><td><ul><li>Bank Transfers like ACH Transfer, SEPA Transfer, BACS Transfer, Multibanco</li><li>Crypto wallets like Cryptopay</li></ul></td></tr></tbody></table>

### **Functionalities provided by Hyperswitch**

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Accept online payments</strong></td><td>Get started with accepting one time payments globally on your online store</td><td></td><td><a href="../.gitbook/assets/onlinePayments.jpg">onlinePayments.jpg</a></td><td><a href="../other-features/payment-orchestration/quickstart/">quickstart</a></td></tr><tr><td><strong>Setup mandates &#x26; recurring payments</strong></td><td>Setup payments for a future date or charge your customers on a recurring basis</td><td></td><td><a href="../.gitbook/assets/recurringPayments.jpg">recurringPayments.jpg</a></td><td><a href="../integration-guide/payment-suite/payments/save-a-payment-method/">save-a-payment-method</a></td></tr><tr><td><strong>Manage payouts</strong></td><td>Facilitate payouts for global network of partners and service providers</td><td></td><td><a href="../.gitbook/assets/Payment flow (1) (1).jpg">Payment flow (1) (1).jpg</a></td><td><a href="../other-features/connectors/payouts/">payouts</a></td></tr><tr><td><strong>Save a card during payment</strong></td><td>Learn how you can save your customers' cards in a secure PCI compliant manner</td><td></td><td><a href="../.gitbook/assets/saveCard.jpg">saveCard.jpg</a></td><td><a href="../other-features/tokenization-and-saved-cards/">tokenization-and-saved-cards</a></td></tr><tr><td><strong>Manage payments on your platform / marketplace</strong></td><td>Accept payments from your customers and process payouts to the sellers on your marketplace</td><td></td><td><a href="../.gitbook/assets/marketplace.jpg">marketplace.jpg</a></td><td><a href="../integration-guide/account-management/multiple-accounts-and-profiles/">multiple-accounts-and-profiles</a></td></tr><tr><td><strong>Accept payments on your e-commerce platform</strong></td><td>Give your Wordpress store a lightweight and embedded payment experience with the Hyperswitch WooCommerce plugin</td><td></td><td><a href="../.gitbook/assets/WooComerce.jpg">WooComerce.jpg</a></td><td><a href="../other-features/e-commerce-platform-plugins/woocommerce-plugin/">woocommerce-plugin</a></td></tr><tr><td><strong>Create payment links</strong></td><td>Accept payments for your products through reusable links without writing any code</td><td></td><td><a href="../.gitbook/assets/paymentLinks.jpg">paymentLinks.jpg</a></td><td><a href="../integration-guide/payment-experience/payment/payment-links/">payment-links</a></td></tr></tbody></table>

### Which SDK surface to reach for

The stages above describe the full checkout sheet. Four other surfaces exist, and picking the wrong one costs a rewrite. Each row is the SDK source of truth, not a spec claim.

| You want | Surface | Where it lives |
| --- | --- | --- |
| The whole payment sheet, Hyperswitch renders it | Payment element | `elements.create("payment")` on Web, `PaymentElement` on React Native |
| One payment method, your own layout around it | Single element | `elements.create("cardNumber" \| "cardExpiry" \| "cardCvc")` |
| A wallet button on its own, no sheet | Wallet element | `elements.create("googlePay" \| "applePay" \| "payPal" \| "samsungPay" \| "paze" \| "expressCheckout")` |
| No Hyperswitch UI at all, saved methods only | Headless SDK | `hyper.initPaymentSession(...)` on Web, `Hyperswitch.init(...)` on React Native |
| Collect and vault a card with no payment attached | Payment method session | `hyper.initPaymentMethodSession(...)` |

`elements.create` accepts 15 names in all. The other four are `card`, `paymentMethodsSDK`, `paymentMethodCollect`, `klarna` and `paymentMethodsManagement`.

### Take React Native to production

The quickstart gets a sheet on screen. Four things separate that from a production app, and none of them are optional.

**Install the peer dependencies yourself.** `@juspay-tech/react-native-hyperswitch` declares 6 peer dependencies and bundles none of them: `@sentry/react-native`, `react`, `react-native`, `react-native-inappbrowser-reborn`, `react-native-svg`, `react-native-webview`. A build that resolves without them will fail at the first redirect.

**Add the companion package for every method you accept.** The base package does not carry wallets, 3DS or card scanning. Eight companion packages ship alongside it, one each for Click to Pay, Netcetera 3DS, Trident 3DS, Samsung Pay, PayPal, card scanning, vault and payment methods. Install only the ones you accept; each adds native weight.

**Set the environment explicitly.** `Hyperswitch.init` takes `environment`, one of `PROD`, `SANDBOX` or `INTEG`. It defaults to `PROD`. A sandbox build that forgets the field points at production.

**Create the session on your server.** `initPaymentSession` takes `sdkAuthorization`, not a client secret. Your backend creates the payment and returns that string. The secret API key never reaches the app.

Per-platform steps, Expo, over-the-air updates and customization are in the [React Native guide](../integration-guide/payment-experience/pay-then-vault/mobile/cross-platform/react-native/README.md).

### Collect a CVC for a saved card on the Web SDK

Use a payment method session, not the payment sheet. `hyper.initPaymentMethodSession(...)` returns a session that exposes `createCardForm`, and the form you build decides what happens on `tokenize()`:

* Mount `cardCvc` on its own and `tokenize()` runs the update flow against the saved card, which is the CVC-refresh case.
* Mount `cardNumber` and `tokenize()` runs the save flow, vaulting a new card.
* Mount nothing, or `cardExpiry` alone, and `tokenize()` returns `incomplete_field_set`.

So the CVC-only form is not a mode you switch on. It is what you get by mounting exactly one field. The session also exposes `update`, `on`, `deinit` and `fields`, and the form adds `create`, `on`, `tokenize`, `deinit`, `update` and `fields`.

### Mount a wallet button on its own

Both platforms let you put Apple Pay or Google Pay on a page that has no payment sheet.

On Web, create the element by name: `googlePay`, `applePay`, `payPal`, `samsungPay` or `paze`, or `expressCheckout` for the row of every eligible wallet. The button confirms the payment through the SDK.

On React Native, render `GooglePayButton` or `ApplePayButton`. Check eligibility first with `isGooglePaySupported`, `isApplePaySupported`, `isWalletSupported` or `isPlatformPaySupported`, because a button for a wallet the device cannot present is a dead button. `useWalletSession` gives you `launchGooglePay`, `launchApplePay` and `launchWallet` if you would rather drive the sheet from your own button. The wallet session has 15 seconds to bootstrap before it reports a timeout.

{% hint style="info" %}
**Confirming a standalone wallet button from your server is not documented.** We could not find a path in the Web SDK that hands the wallet token back to your backend for you to confirm there; the standalone buttons confirm through the SDK. If you need server-side confirmation, talk to your Hyperswitch contact before you build against it.
{% endhint %}

### Get the hosted payment link out of the create response

Send `payment_link: true` on `POST /payments` and the response carries a `payment_link` object. The hosted URL is `payment_link.link`. The object also carries `secure_link`, the URL for the secure variant, and `payment_link_id`.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "payment_link": {
    "link": "<hosted payment link url>",
    "secure_link": "<secure payment link url>",
    "payment_link_id": "plink_abcdefghijklmnop"
  }
}
```

`secure_link` is present only when the profile is configured for secure links. Send `payment_link_config` on the same request to theme the page. Configuration, theming and custom domains are in [Payment Links](../integration-guide/payment-experience/pay-then-vault/payment-links/README.md).

### What the Headless SDK exposes

The Headless SDK renders nothing. You get a customer's saved payment methods as data, and you draw the UI.

On Web, `hyper.initPaymentSession({ clientSecret })` returns a session whose `getCustomerSavedPaymentMethods()` gives you the saved method data, plus `confirmWithCustomerDefaultPaymentMethod` and `confirmWithLastUsedPaymentMethod` to confirm one of them.

On React Native, `Hyperswitch.init(...)` then `initPaymentSession({ sdkAuthorization })` returns a session exposing `presentPaymentSheet`, `getCustomerSavedPaymentMethods`, `getWalletSession` and `updateIntent`. The saved-methods session gives you the last-used and the default card.

It only covers already-saved methods. A first-time card still needs a card form, which means an element or the payment sheet.

Per-platform Headless guides live under [Payment Experience](../integration-guide/payment-experience/pay-then-vault/web/headless-sdk.md), one per platform.

### Questions this page does not answer

* **Where the PCI SAQ-A boundary sits when you use the hosted SDK.** Hyperswitch has not published a statement of that boundary, so this page does not state one. [Security and Compliance](https://docs.hyperswitch.io/self-hosting/guides-for-self-hosting/security-and-compliance) covers how PCI DSS assessment works, SAQ against ROC, and when a QSA is required. Your assessment level is a QSA question.
* **Driving checkout entirely from your backend.** That is [Server to Server Payments](../integration-guide/payment-suite/server-to-server-payments.md), which returns the payment, its payment-method list and the wallet session tokens in one call.
* **Refunding a payment made through the SDK.** The SDK plays no part; see [Refunds](../integration-guide/payment-suite/refunds.md).

### **What are `PaymentIntent` and `PaymentAttempt` objects and how do they work in Hyperswitch?**

Hyperswitch uses the `PaymentIntent` object to track the status of a payment initiated by you. Since, Hyperswitch enables retrying a single payment multiple times across different processors until a successful transaction, we track each of these payment attempts through separate `PaymentAttempt` objects.

While `PaymentIntent` and `PaymentAttempt` have their own state machines, the various states in `PaymentAttempt` are also constrained by their respective mapping to the `PaymentIntent` statuses.

#### **PaymentIntent state machine:**

The following is an abridged version of the `PaymentIntent` state machine flow that covers majority of the above payment use-cases.

```mermaid
flowchart TD
A{PaymentsAPI} --> |amount,currency|RequiresPaymentMethod 
RequiresPaymentMethod -->|payment_method| RequiresConfirmation 
RequiresConfirmation --> |confirm| Processing 
Processing --> AuthType{auth type\nselection} 
AuthType --> |3ds| RequiresCustomerAction 
AuthType --> |no-3ds| CaptureMethod{capture method\nselection}
CaptureMethod --> |manual| RequiresCapture
CaptureMethod --> |automatic| Succeeded
RequiresCustomerAction --> CustomerAction{customer_action\nresult}
CustomerAction -->|success| CaptureMethod
CustomerAction -->|failure| Failed

RequiresCapture --> |capture|Succeeded
```

#### **PaymentAttempt state machine:**

The following is an abridged version of the `PaymentAttempt` state machine flow that covers majority of the above payment use-cases.

```mermaid
flowchart TD

AuthenticationFailed
AuthenticationPending
AuthenticationSuccessful
Authorized
AuthorizationFailed
Charged
Voided
CaptureInitiated
CaptureFailed
Pending
PaymentMethodAwaited
ConfirmationAwaited
DeviceDataCollectionPending

A{PaymentsAPI} --> |amount,currency|PaymentMethodAwaited
PaymentMethodAwaited -->|payment_method| ConfirmationAwaited
ConfirmationAwaited --> |confirm| Pending

%% Before calling the connector change status to Pending
Pending --> CallConnector{CallConnector}
CallConnector -->|Success| AuthType{auth_type}
CallConnector -->|Fail| AuthorizationFailed
AuthType --> |no-3ds| CaptureMethod{capture_method} 
AuthType --> |3ds| DeviceDataCollectionPending
DeviceDataCollectionPending --> |CollectDeviceData|AuthenticationPending --> Authenticate{Authenticate}
Authenticate --> |Success| AuthenticationSuccessful --> CaptureMethod{capture method}
Authenticate --> |Failure| AuthenticationFailed

%% Capture
CaptureMethod --> |automatic| Charged
CaptureMethod --> |manual| Authorized

Authorized --> |capture| CaptureInitiated --> Capture{Capture at connector}
Capture -->|Success| Charged
Capture -->|Failed| CaptureFailed

%% Payment can be voided after calling the connector but not charged
%% This will not void the payment at connector
DeviceDataCollectionPending -->|void| Voided
AuthenticationPending -->|void| Voided

%% Voiding a payment after it is Authorized will void at connector

```
