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

<figure><img src="../../.gitbook/assets/Screenshot 2024-12-04 at 10.16.31 PM.png" alt=""><figcaption></figcaption></figure>

### Key benefits of the Click to Pay with Passkey Service:

**Seamless Checkout:** Once the user card is enrolled with Click2Pay, the user need not enter their card details again on the merchant checkout page. Click2Pay can fetch saved card details of the customers based on their mobile number or email address.

**Secured Transaction**: Cards are tokenized and saved at the network's end. Thus, raw card details are not passed around in the system, which inherently reduces the risk of the transaction. The transaction authentication happens through passkeys.Passkeys use public-private key cryptography, making it nearly impossible for attackers to intercept credentials.

**Improved authentication experience:** Customers need not wait for OTP or push provision to authenticate the transaction. With passkeys, the authentication is made simple via biometrics (finger print, face ID, etc).

**Liability Shift:** The merchant gets the benefit of chargeback liability shift to the issuer when the transactions are authenticated through Click to Pay with Passkeys service.

### What’s unique about Click to Pay via Hyperswitch?

**Passkeys Support:** Hyperswitch is one of the first certified Mastercard and Visa partners to onboard merchants for the latest Click to Pay with passkeys solution. The older version of Click to Pay does not have biometric authentication with passkeys experience, and the users have to go through the usual authentication - OTPs, push provisioning, etc.

**Unified SDK:** The merchant does not need to integrate multiple SDKs like Visa or Mastercard Click to Pay SDKs. With Hyperswitch SDK, they get access to both Visa and Mastercard systems and can support Visa, Mastercard, Amex and Discover cards on Click to Pay with a single integration. Hyperswitch intelligently falls back to the other system if one of the systems is down and lets the user complete the transaction. All this while ensuring a single, blended UI.

**Easier and Customizable Integration:** Hyperswitch absorbs all the integration complexity and offers a low code integration to the merchant. The merchant can blend click to pay in their checkout page with the cards section as well as offer it like a guest checkout button. Hyperswitch also offers UI customization options on click to pay to match and blend it with the merchant’s UI theme and style.

**Faster Go-live:** With Hyperswitch, the merchant does not have to worry about onboarding, testing and certification with Mastercard and Visa, which can take months to complete and significant merchant bandwidth. Since Hyperswitch is a certified partner, merchant onboarding and go-live can be completed in a matter of days.

By combining the tokenization of payment credentials with seamless biometric authentication, Click to Pay is bringing [EMVCo](https://www.emvco.com/), [World Wide Web Consortium](https://www.w3.org/) and the[ FIDO Alliance](https://fidoalliance.org/) industry standards together to speed and secure checkouts.&#x20;

On the customers' side, many are hesitant to enter their card details on a merchant website due to lack of trust and security concerns. With Click to Pay, these customers need not enter their card details manually, but fetch those from a secured, known EMVCo SRC system. This reduces the cart abandonment rate and increased sales for the merchants who offer Click to Pay.

{% content-ref url="../account-management/" %}
[account-management](../account-management/)
{% endcontent-ref %}
