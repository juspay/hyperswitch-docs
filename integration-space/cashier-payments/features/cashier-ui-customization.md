---
description: Cashier UI customization for seamless deposits and withdrawals
---

# Cashier UI Customization

The cashier is the operator’s most-visited page. Every change to it moves revenue. Juspay’s cashier SDK is built on the principle that the operator knows their players better than the payments provider does - so the SDK exposes controls for the operator to express that knowledge.

What can be customized:

* **Theme** - colors, typography, button radius, dark / light mode, layout (tabs vs accordion). Configured via the appearance and variables objects in the PaymentElement options.
* **Payment method ordering** - operators specify the exact display order via the paymentMethodOrder array. Methods are rendered in that order regardless of internal priority.
* **Promoted payment methods** - visually elevate the methods the operator wants to push (typically the cheapest, fastest, or stickiest for repeat deposits). Promotion can be a highlighted background, a “Recommended” badge, or a larger button.
* **Grouping** - group payment methods by category (cards, wallets, bank transfers, vouchers, crypto) with operator-defined group names. Useful when offering 15+ methods in regulated markets.
* **One-click last-used checkout** - for returning players, the most recently used payment method is pre-selected and exposed as a single-tap checkout. Behind the scenes, this uses Juspay’s saved-payment-methods API and the network-tokenized COF.
* **Wallet visibility rules** - toggle Apple Pay, Google Pay, PayPal, Klarna on/off per device, region, and player segment.

A representative cashier mockup with these elements:

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

Below are real cashier surfaces built on the Juspay SDK - different themes, different layouts, different payment-method orderings, all configured from the same SDK options object. The same theming, payment-method ordering, grouping, promotion, and one-click last-used checkout APIs are available across Web, iOS, Android, React Native, Capacitor, and Flutter; every screenshot below can be reproduced on any of those platforms by changing configuration alone.

<div align="center"><figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2026-06-25 at 4.04.55 PM.png" alt=""><figcaption></figcaption></figure></div>

A representative configuration snippet - React PaymentElement:

`const paymentElementOptions = {`\
&#x20; `layout: { type: 'accordion', defaultCollapsed: false },`\
&#x20; `paymentMethodOrder: ['card', 'apple_pay', 'google_pay', 'trustly', 'paypal'],`\
&#x20; `paymentMethodPromotions: { trustly: { badge: 'RECOMMENDED', accent: '#10B981' } },`\
&#x20; `displaySavedPaymentMethods: true,`\
&#x20; `showCardFormByDefault: false,        // one-click COF surfaced first`\
&#x20; `wallets: {`\
&#x20;   `applePay: 'auto', googlePay: 'auto', payPal: 'auto', klarna: 'never',`\
&#x20; `},`\
&#x20; `appearance: {`\
&#x20;   `theme: 'night',`\
&#x20;   `variables: {`\
&#x20;     `colorPrimary: '#10B981',`\
&#x20;     `colorBackground: '#0F172A',`\
&#x20;     `borderRadius: '8px',`\
&#x20;     `fontFamily: 'Inter, system-ui, sans-serif',`\
&#x20;   `},`\
&#x20; `},`\
`};`

<br>
