---
description: Step-by-step guide to enable and configure Apple Pay via Cybersource in Hyperswitch
---

# Apple Pay

{% hint style="info" %}
This page consists of steps for how **Apple Pay** can be enabled in Hyperswitch via Cybersource
{% endhint %}

> This guide assumes that you have already configured Cybersource as a connector in your Hyperswitch Control Center. If not, please follow the steps mentioned [here](./)

### Steps to Configure Apple Pay

- On your Hyperswitch Control Center, click on `Connectors > Payment Processors`
- If you have already configured Cybersource successfully, you will land on the page as shown in the image below

  <figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.36.58 PM.png" alt=""><figcaption></figcaption></figure>

- Click on Cybersource and then click on `Edit Icon` to **Update** the configuration of the Cybersource connector.

  <figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.38.05 PM.png" alt=""><figcaption></figcaption></figure>

- Click on **Proceed** after making the necessary changes to your API Keys (if required).
- Select **Apple Pay** under the Wallet section to enable it.
- Prepare Apple Pay certificates for Cybersource by following the steps mentioned [here](apple-pay.md#steps-to-prepare-apple-pay-certificates-for-cybersource-integration).
- To configure these steps in the Hyperswitch dashboard, please follow the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#configuring-apple-pay-on-hyperswitch).
- Click on **Enable** and then **Proceed**, review your configuration and changes, and click **Done**.

#### Points to Remember for Apple Pay Payments via Cybersource

- Required fields for Apple Pay payment requests via Cybersource:
  - Email
  - Billing Address Details
    - First Name
    - Last Name
    - Address Line 1
    - Zip/Postal Code
    - City
    - State
    - Country

{% hint style="warning" %}
We recommend passing these fields when creating the Payment Intent with Hyperswitch. Otherwise, the Hyperswitch SDK will collect this information from the customer during payment, which may not provide the best experience.
{% endhint %}

### Steps to Prepare Apple Pay Certificates for Cybersource Integration

- Create an Apple Merchant ID by following the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#creating-an-apple-merchantid)
- Validate your merchant domain by following the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#validating-merchant-domain)
- Create Apple Merchant ID certificates by following the steps mentioned [here](../../../wallets/apple-pay/ios-application.md#creating-apple-merchantid-certificate-and-private-key)
- Log into your Cybersource Console and navigate to `Payment Configuration > Digital Payment Solutions`

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 3.26.23 PM.png" alt=""><figcaption></figcaption></figure>

- Click on **Configure** and add your Apple Merchant ID that you created in the steps above.

  <figure><img src="../../../../.gitbook/assets/Screenshot 2024-03-14 at 4.54.31 PM.png" alt=""><figcaption></figcaption></figure>

- Click on `Generate New Certificate Signing Request` and download the provided **.csr** file.
- Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to **Identifiers**, and select the Merchant ID you created previously.
- Under the **Apple Pay Payment Processing Certificate** section, click on **Create Certificate**.
- After answering whether the Merchant ID will be processed exclusively in China mainland, click on **Continue**.
- Upload the **.csr** file you received from your processor and click **Continue**.
- Click on **Download** — you will receive a **.cer** file.
- On the Cybersource Console, if prompted, upload the same **.cer** file (`apple_pay.cer`).
- Now configure the generated certificates into the Hyperswitch Control Center for Cybersource by following these [steps](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#configuring-apple-pay-on-hyperswitch).

{% hint style="info" %}
To enable Apple Pay in your iOS application, please refer to the steps mentioned [here](https://docs.hyperswitch.io/hyperswitch-cloud/payment-methods-setup/wallets/apple-pay/ios-application#integrate-with-xcode)
{% endhint %}
