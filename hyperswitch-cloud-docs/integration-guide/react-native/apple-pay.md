# Apple Pay

Allow customers to securely make payments using Apple Pay on their iPhone, iPad.

Apple Pay seamlessly integrates with Hyperswitch, providing you with the flexibility to replace conventional payment forms whenever it is feasible and appropriate.

**Accept a payment using Apple Pay in your iOS app**

## Register for an Apple Merchant ID

Obtain an Apple Merchant ID by [registering for a new identifier](https://developer.apple.com/account/resources/identifiers/add/merchant) on the Apple Developer website.

## Create a new Apple Pay certificate

Create a certificate for your app to encrypt payment data. In the Dashboard’s Apple Pay Settings, click Add new application and follow the guide. Download a Certificate Signing Request (CSR) file to get a secure certificate from Apple that allows you to use Apple Pay.

## Integrate with Xcode

Add the Apple Pay capability to your app. In Xcode, open your project settings, click the Signing & Capabilities tab, and add the Apple Pay capability. You might be prompted to log in to your developer account at this point. Select the merchant ID you created earlier, and your app is ready to accept Apple Pay.

<figure><img src="https://hyperswitch.io/img/site/applepay.png" alt=""><figcaption></figcaption></figure>
