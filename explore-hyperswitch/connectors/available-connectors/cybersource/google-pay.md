---
description: Enable Google Pay as a payment method via CyberSource in Hyperswitch
---

# Google Pay

{% hint style="info" %}
This page describes how **Google Pay** can be enabled in Hyperswitch via CyberSource.
{% endhint %}

> This guide assumes that you have already configured CyberSource as a connector in your Hyperswitch Control Center. If not, follow the steps mentioned [here](./).

## Steps to Configure Google Pay

* On your Hyperswitch Control Center, click on [`Connectors > Payment Processors`](#user-content-fn-1)[^1]
*   If you have already configured CyberSource successfully, you will land on the page shown in the image below.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.36.58 PM.png" alt=""><figcaption></figcaption></figure>
*   Click on CyberSource and then click the `Edit` icon to **update** the configuration of the CyberSource connector.

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.38.05 PM.png" alt=""><figcaption></figcaption></figure>
* Click **Proceed** after making any necessary changes to your API keys.
* Select **Google Pay** under the **Wallet** section to enable it.
* Enter the Google Pay details in the overlay form and click **Proceed**:
  1. **Google Pay Merchant Key**: Your CyberSource Merchant ID.
  2. **Google Pay Merchant Name**: The display name that customers will see in their Google Pay app when making a payment.
  3. **Google Pay Merchant ID:** \[<mark style="color:red;">For Production Only</mark>] Your Google Pay Merchant ID provided by Google after you sign up and receive approval to use Google Pay in production.

{% hint style="success" %}
**\[SANDBOX ENV]:** For the sandbox test environment, you can enter any **dummy value** for **Google Pay Merchant ID** — it will not affect the payment experience.
{% endhint %}

<figure><img src="../../../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.46.32 PM.png" alt=""><figcaption></figcaption></figure>

* Click **Proceed**, review your changes, and click **Done**.

## Points to Remember for Google Pay Payments via CyberSource

* Required fields for a Google Pay payment request via CyberSource:
  * Email
  * Billing address details:
    * First Name
    * Last Name
    * Address Line 1
    * Zip/Postal Code
    * City
    * State
    * Country

{% hint style="warning" %}
We recommend passing these fields when creating the Payment Intent with Hyperswitch. Otherwise, the Hyperswitch SDK will collect this information from the customer at checkout, which may not provide the best payment experience.
{% endhint %}

[^1]: 
