---
description: Integrate ApplePay via Cybersource in Hyperswitch
---

# Apple Pay

{% hint style="info" %}
This page consists of steps for how **ApplePay** can be enabled in Hyperswitch via Cybersource
{% endhint %}

> This guide assumes that you have alreaedy configured Cybersource as a connector in your Hyperswitch Control Center. If not please follow the steps mentioned [here](./)

### Steps to Configure ApplePay

* On your Hyperswitch Control Center, Click on [`Connectors > Payment Processors`](#user-content-fn-1)[^1]
*   If you have already configured Cybersource successfully, then you will land on the page as shown in the image below\
    \


    <figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.36.58 PM.png" alt=""><figcaption></figcaption></figure>
*   Click on Cybersource and then Click on `Edit Icon` to **Update** the Configuration of Cybersource Connector.\


    <figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.38.05 PM.png" alt=""><figcaption></figcaption></figure>
* Click on proceed after making the necessary changes to your API Keys (if required any).
* Select Apple Pay under Wallet Section to enable it.
* Prepare Apple Pay certificates for Cybersource by following the steps mentioned [here](apple-pay.md#steps-to-prepare-applepay-certificates-for-cybersource-integration).&#x20;
* To configure these steps in Hyperswitch dashboard please follow the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#configuring-apple-pay-on-hyperswitch).
* Click on Enable and then Proceed, review your configuration and changes and click Done.

#### Points to remember for ApplePay Payments via Cybersource

* Required fields for ApplePay Payments Request via Cybersource
  * Email
  * Billing Address Details
    * First Name
    * Last Name
    * Address Line 1
    * Zip/Postal Code
    * City
    * State
    * Country

{% hint style="warning" %}
We recommend to pass this fields while creating the Payment Intent with Hyperswitch, Else Hyperswitch SDK will collect this information from the customer while making the payment which might not be the best experience for the customer.
{% endhint %}

### Steps to prepare ApplePay certificates for Cybersource Integration

* Create an Apple Merchant ID by following the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#creating-an-apple-merchantid)
* Validate your merchant domain by following the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#validating-merchant-domain)
* Create Apple MerchantID certificates by following the steps mentioned [here](../../../payment-methods-setup/wallets/apple-pay/ios-application.md#creating-apple-merchantid-certificate-and-private-key)
* Log into your Cybersource Console, and navigate to `Payment Configuration > Digital Payment Solutions`

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 3.26.23 PM.png" alt=""><figcaption></figcaption></figure>

*   Click on Configure and add your Apple Merchant ID that you created in the above steps.\
    \


    <figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 4.54.31 PM.png" alt=""><figcaption></figcaption></figure>
* Click on `generate new certificate signing request`, and download the provided **.csr** file.
* Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
* Under the **Apple Pay Payment Processing Certificate** section, click on Create Certificate
* After answering whether the Merchant ID will be processed exclusively in China mainland, click on Continue
* Upload the **.csr** you received from your processor and click Continue.
* Click on Download, you will get a **.cer** file.
* On the Cybersource Console, if you are prompted to provide this file upload the same **.cer file** (apple\_pay.cer)
* Now you can configure the genreated certificates into Hyperswitch Control Center for Cybersource by following these [steps](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#configuring-apple-pay-on-hyperswitch).

[^1]: 
