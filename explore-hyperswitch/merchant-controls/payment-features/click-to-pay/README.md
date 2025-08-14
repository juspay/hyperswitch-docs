---
icon: chevrons-right
---

# Click To Pay

{% hint style="info" %}
This feature is currently in Beta. For access, please contact us at **hyperswitch@juspay.in**
{% endhint %}

Click to Pay is a secure and user-friendly digital payment solution designed to simplify the online checkout process. With Click to Pay, consumers can use their saved payment cards without manually entering card details or recalling a password for each purchase. All payment information is securely stored within a single, centralized profile tied to the user via an email/phone, making it easy to manage various payment methods.

This solution is built on [EMVCo](https://www.emvco.com/) standards and is supported by major global card networks, enabling international interoperability and secure transaction acceptance. By streamlining the payment process, Click to Pay reduces cart abandonment, providing a smooth user experience while strengthening security through [tokenization](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/tokenization-and-saved-cards).

### Payment Journey for Click to pay signed up users

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-12-04 at 10.16.31 PM.png" alt=""><figcaption></figcaption></figure>

### What Makes Hyperswitch’s Implementation Unique?

#### Passkeys Support

* Hyperswitch is among the first certified Mastercard and Visa partners for the passkey-enabled Click to Pay solution.
* Unlike the older Click to Pay versions, which required OTPs or push provisioning, Hyperswitch enables seamless biometric authentication using passkeys.

#### Unified SDK

* A single integration with the Hyperswitch SDK supports Visa, Mastercard, Amex, and Discover cards on Click to Pay.
* Hyperswitch ensures business continuity by intelligently switching between card systems if one network becomes unavailable, all while maintaining a single, blended UI.

#### Easier and Customizable Integration

* Hyperswitch simplifies integration with low-code options, allowing merchants to blend Click to Pay into their checkout page as part of the card section or offer it as a guest checkout button.
* Offers UI customization to align with the merchant’s branding for a seamless user experience.

#### Faster Go-live

* Certified partnerships with Mastercard and Visa enable Hyperswitch to help merchants go live in days rather than months, minimizing merchant effort.

### Benefits for Merchants

#### Seamless Checkout

* Eliminates the need for customers to re-enter card details after initial enrollment.
* Fetches stored card details based on the customer’s email or phone number.

#### Secured Transactions

* Cards are tokenized and securely stored at the network's end.
* Authentication is managed via passkeys using public-private key cryptography, making interception nearly impossible.

#### Enhanced Authentication

* Passkeys enable a quick and secure authentication process using biometrics (e.g., fingerprint, face ID) instead of OTPs or push notifications.

#### Liability Shift

* Merchants benefit from a chargeback liability shift to the issuer when transactions are authenticated via Click to Pay with Passkeys.

By combining the tokenization of payment credentials with seamless biometric authentication, Click to Pay is bringing [EMVCo](https://www.emvco.com/), [World Wide Web Consortium](https://www.w3.org/) and the[ FIDO Alliance](https://fidoalliance.org/) industry standards together to speed and secure checkouts.&#x20;

On the customers' side, many are hesitant to enter their card details on a merchant website due to lack of trust and security concerns. With Click to Pay, these customers need not enter their card details manually, but fetch those from a secured, known EMVCo SRC system. This reduces the cart abandonment rate and increased sales for the merchants who offer Click to Pay.

{% content-ref url="../../../account-management/" %}
[account-management](../../../account-management/)
{% endcontent-ref %}
