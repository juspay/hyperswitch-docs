---
description: Make your first payment and refund through Hyperswitch
---

# 💵 Test a payment

{% hint style="info" %}
Here, you'll be making a Payment using your Hyperswitch setup, via your preferred payment provider.&#x20;
{% endhint %}

***

## Test on web client <a href="#user-content-create-a-payment" id="user-content-create-a-payment"></a>

Once you have successfully run the web client, you should be able to test the payments.&#x20;

{% hint style="warning" %}
[Account setup ](account-setup/)is a pre-requisite before you can test the payments.
{% endhint %}

**Local:** After running the web client, you will see the demo web app (playground) running on `http://localhost:5252` where you can test your payments.

**Self Hosted Web App:** In case you have hosted the SDK and integrated it on your app, you can do a usual release of your app. Post successful deployment, you can test the payments on your app url.

**Playground deployment:** In case you have [deployed the demo app playground](deploy-hyperswitch-on-aws/component-wise-deployment/deploy-web-client/standalone-deployment-for-prototyping-optional.md), you will see the playground up and running on the public IP that you received after deployment.

<figure><img src="../.gitbook/assets/Screenshot 2023-11-09 at 5.25.15 PM.png" alt=""><figcaption></figcaption></figure>

You can test a successful payment on sandbox environment with the following test card -

```
Card Number - 4242 4242 4242 4242
Card Expiry - Any future date
CVC - Any 3 digits
```

On confirming the payment, you will see the the Payment confirmation screen.

<figure><img src="../.gitbook/assets/Screenshot 2023-11-09 at 5.42.53 PM.png" alt=""><figcaption></figcaption></figure>

Congrats! you have successfully tested an end-to-end payment with your own app server and a web client.

{% hint style="info" %}
In case you have integrated the web client on your app and want to test a payment, the payment status confirmation screen has to be handled by you. You will see that post payment confirmation.
{% endhint %}

The app server is more powerful than just processing the payments. You can test refunds, subscription payments and more using the app server.

## **Resources** <a href="#user-content-create-a-payment" id="user-content-create-a-payment"></a>

* To explore more of our APIs, please check the remaining folders in the [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3).
