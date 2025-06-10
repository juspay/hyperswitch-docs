---
description: Integrate GooglePay (AndroidPay) via Cybersource in Hyperswitch
---

# Google Pay

{% hint style="info" %}
This page consists of steps for how **GooglePay** can be enabled in Hyperswitch via Cybersource
{% endhint %}

> This guide assumes that you have alreaedy configured Cybersource as a connector in your Hyperswitch Control Center. If not please follow the steps mentioned [here](./)

### Steps to Configure GooglePay

* On your Hyperswitch Control Center, Click on [`Connectors > Payment Processors`](#user-content-fn-1)[^1]
*   If you have already configured Cybersource successfully, then you will land on the page as shown in the image below\
    \


    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.36.58 PM.png" alt=""><figcaption></figcaption></figure>
*   Click on Cybersource and then Click on `Edit Icon` to **Update** the Configuration of Cybersource Connector.\


    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.38.05 PM.png" alt=""><figcaption></figcaption></figure>
* Click on proceed after making the necessary changes to your API Keys (if required any).
* Select Google Pay under Wallet Section to enable it.
* Enter the below mentioned GooglePay details in the overlay form and click `Proceed`
  1. **Google Pay Merchant Key**: This is your Cybersource Merchant ID
  2. **Google Pay Merchant Name**: This is your display name that the customer will see on his GooglePay App while making the payment.
  3. **Google Pay Merchant ID:** \[<mark style="color:red;">For Production Only</mark>] Enter your GooglePay Merchant ID provided by Google when you signup and get approvals for using GooglePay on production.

{% hint style="success" %}
**\[SANDBOX ENV]:** For sandbox test environment, you can put any **dummy value** in **Google Pay Merchant ID** it won't affect the payments experience.
{% endhint %}

<figure><img src="../../../../../../.gitbook/assets/Screenshot 2024-03-14 at 1.46.32 PM.png" alt=""><figcaption></figcaption></figure>

* Click on Proceed, review your changes and click Done

### Points to remember for GooglePay Payments via Cybersource

* Required fields for GooglePay Payments Request via Cybersource
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



[^1]: 
