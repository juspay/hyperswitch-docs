---
description: Make your first payment and refund through Hyperswitch
icon: money-bills
---

# Test a payment

{% hint style="info" %}
Here, you'll be making a payment using your Hyperswitch setup, via your preferred payment provider.
{% endhint %}

## Test on web client <a href="#user-content-create-a-payment" id="user-content-create-a-payment"></a>

Once you have successfully run the [control centre](../local-setup-guide/), you should be able to test the payments.&#x20;

{% hint style="warning" %}
[Account setup ](./)is a pre-requisite before you can test the payments.
{% endhint %}

**Local:** Once you have got the Control Centre running (at [http://localhost:9000](http://localhost:9000/dashboard/home)) and have configured your payment processor via it. You can go to Home section in Control Centre, and you will find a "try it out" button (Highlighted with blue colour in the image below).

**Self Hosted Web App:** In case you have hosted the SDK and integrated it on your app, you can do a usual release of your app. Post successful deployment, you can test the payments on your app url.

**Playground deployment:** In case you have [deployed the demo app playground](../deploy-hyperswitch-on-aws/component-wise-deployment/deploy-web-client/playground-deployment-for-prototyping-optional.md), you will see the playground up and running on the public IP that you received after deployment.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-29 at 9.35.09 PM.png" alt=""><figcaption></figcaption></figure>

You can test a successful payment on Control Centre with the following test card -

```
Card Number - 4242 4242 4242 4242
Card Expiry - Any future date
CVC - Any 3 digits
```

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-29 at 9.46.28 PM.png" alt=""><figcaption></figcaption></figure>

On confirming the payment, you will see the the Payment confirmation screen.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-29 at 9.49.06 PM.png" alt=""><figcaption></figcaption></figure>

Congrats! You have successfully tested an end-to-end payment with your own app server and the control centre

{% hint style="warning" %}
In case you have integrated the web client on your app and want to test a payment, the payment status confirmation screen has to be handled by you. You will see that post payment confirmation.
{% endhint %}

The app server is more powerful than just processing the payments. You can test refunds, subscription payments and more using the app server.

<details>

<summary>Troubleshooting/FAQs</summary>

1. **I cannot see the Web app playground running on `http://localhost:5252`**\
   This can happen when the playground's server or client are not run properly. Please check your terminal for any errors. The errors are directive, and should be able to pinpoint the issue. You can restart the playground using `npm run start:playground`\
   Please make sure that you are sending the publishable key correctly.
2. **I have hosted the web client successfully, but cannot see the payment element**\
   Please check the console errors. Please make sure that the publishable key and api key are correct. Please verify if the web client is initiated with a valid client secret.\
   Also make sure that HyperLoader.js is hosted successfully. You can open that URL on browser and see if the bundle is correct. In Network tab, check if the HyperLoader.js is called correctly. If not, please verify the env file and make sure that the correct URL is set.
3. **I am unable to complete the payment**\
   There can be multiple reasons for this. Please make sure that you have correctly followed all the steps in [account setup ](./)section.\
   Also make sure that you have configured at least 1 connector.
4. **After payment, I see a `Page Not Found` error.**\
   This can be a demo playground issue and not an issue with the web client. Please make sure that the return URL is correctly set.
5. **My transactions are  failing.** \
   This can happen when the connector is not correctly configured. Please make sure that the configured API keys are correct. In case of card payments, make sure that you have enabled raw card processing on the connector dashboard.\
   An exhaustive list of error and the corrective items are [here](https://api-reference.hyperswitch.io/essentials/error_codes).

</details>

## Next step:

{% content-ref url="../going-live/" %}
[going-live](../going-live/)
{% endcontent-ref %}
