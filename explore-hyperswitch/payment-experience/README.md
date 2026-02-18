---
description: Learn about integration options for accepting payments online.
icon: sidebar-flip
---

# Payment Experience

Optimize your payments integration and unlock higher revenue with the Optimized Checkout Suite by Hyperswitch. It includes customizable payment UIs, dynamic payment method presentation, and one click checkout. Get started by choosing the integration that fits your business requirements

{% hint style="info" %}
[Explore the demo](https://hyperswitch-demo-store.netlify.app/)
{% endhint %}

### Learn which payments integration fits your business

Use Hyperswitch to accept payments for your business globally. The below variations allow you to learn about the different integration options available

#### [Accept payments without code](payment/payment-links/)

Use payment links to accept payments without building any integration onto a website or an app.

#### [Build a checkout](payment/web/)&#x20;

Integrate the checkout in your website and [customize](payment/web/customization.md) it as per your requirements.

#### [Build advanced integration](payment/web/headless.md)

Use our headless SDK to have full control over your checkout while using the payment-related functionalities in a decoupled architecture.

#### [Build an in-app integration ](payment/mobile/)

Use our mobile SDK to accept payments in [Android](payment/mobile/android/) or [iOS](payment/mobile/ios/) apps.

#### [Build an APM-only integration](payment/enable-alternate-payment-method-widgets/)

Use our Alternate Payment Method widget (APM widget) to power the global APMs in the unified format. This augments your existing checkout in a low code manner.

#### [Build a Vault SDK integration](payment-method/)

Use our Vault SDK to tokenize the card first and the proceed with payment using a vault token. The Vault SDK is flexible to work with [Hyperswitch unified payments API ](https://api-reference.hyperswitch.io/v1/payments/payments--create)as well as the [Proxy or forwarding](https://api-reference.hyperswitch.io/v2/proxy/proxy-v1) API of Hyperswitch

### Intelligent Payment Method Display & Experience

Our SDK intelligently displays payment methods based on device, geo, and merchant configuration:

<table data-view="cards"><thead><tr><th align="center"></th><th align="center"></th></tr></thead><tbody><tr><td align="center"><strong>Device-aware</strong></td><td align="center">Apple Pay and Google Pay are shown only on supported devices. The SDK auto-detects features like Touch ID / Face ID, no merchant logic needed.</td></tr><tr><td align="center"><strong>Geo-specific filtering</strong> </td><td align="center">Methods like EPS, Giropay, or SEPA and features such as co-brand cards are shown only in supported regions, using device location or merchant provided locale and conte</td></tr><tr><td align="center"><strong>Config-based enable or disable</strong></td><td align="center">Payment methods, card scanning, and third-party SDKs (e.g., Klarna, Netcetera) are enabled via static or connector-based configuration.</td></tr><tr><td align="center"><strong>Dynamic ordering</strong></td><td align="center">Methods can be prioritized based on rules. Presenting users with their preferred payment methods boosts convenience and conversion rates.</td></tr><tr><td align="center"><strong>Dynamic Fields</strong></td><td align="center">Fields like cardholder name, billing/shipping address, email, and phone are dynamically rendered based on connector requirements.</td></tr><tr><td align="center"><strong>Cross-platform &#x26; multi-tenant</strong></td><td align="center">Unified SDK across iOS, Android, Flutter, and React Native. Works across SaaS and self-hosted setups.</td></tr><tr><td align="center"><strong>Full Control Over Design &#x26; Functionality</strong></td><td align="center">Customize both the appearance and behavior of the checkout experience.</td></tr><tr><td align="center"><strong>Advanced Security, No Redirection</strong></td><td align="center">Seamlessly integrate native 3DS and Click to Pay for secure, frictionless transactions.</td></tr><tr><td align="center"><strong>Session level overrides</strong></td><td align="center">All configurations with respect to payment methods, design and ordering can be overriden at a payment session level</td></tr></tbody></table>
