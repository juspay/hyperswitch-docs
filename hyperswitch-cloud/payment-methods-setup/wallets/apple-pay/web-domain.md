---
description: Enable Apple pay on your web domains
---

# Web Domain

## **Steps to configure Apple Pay on Hyperswitch**

- Login to [Hyperswitch control center](https://app.hyperswitch.io/)
- In the Processor tab, select desired connector
- While selecting Payment Methods, click on Apple Pay in the Wallet section
- Select the Web Domain option

<div data-full-width="false">

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-12-07 at 7.41.02 PM.png" alt=""><figcaption></figcaption></figure>

</div>

- Download the domain verification file using the button available
- Host this file on your server at _`merchant_domain`_`/.well-known/apple-developer-merchantid-domain-association`
- Enter the domain name where you have hosted the domain verification file
- Click on verify and enable to complete your setup

{% hint style="warning" %}
Please note since the Apple Pay Web Domain flow involves decryption at Hyperswitch, you may need to write to your payment processor to get this feature enabled for your account. Stripe is one among them.
{% endhint %}

<details>

<summary>You can use the following text in the email</summary>

* Attach our PCI DSS AoC certificate and copy our Support team (biz@hyperswitch.io).

* Stripe Account id: <`Enter your account id:` you can find it [here](https://dashboard.stripe.com/settings/user)>

* A detailed business description:
<`One sentence about your business`>. The business operates across `xx` countries and has customers across the world.

* Feature Request:
We are using Hyperswitch, a Level 1 PCI DSS 3.2.1 compliant Payments Orchestrator, to manage payments on our website. In addition to Stripe, since we are using other processors as well to process payments across multiple geographies, we wanted to use Hyperswitch’s Payment Processing certificate to decrypt Apple pay tokens and send the decrypted Apple pay tokens to Stripe. So, please enable processing decrypted Apple pay token feature on our Stripe account. We’ve attached Hyperswitch’s PCI DSS AoC for reference.

</details>
