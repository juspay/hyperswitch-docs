---
description: Test your first payment and refund through Juspay Hyperswitch using test card credentials
---

# Test a Payment

{% hint style="info" %}
Here, you'll be making a Payment using your local Juspay Hyperswitch setup, via your preferred payment provider. The open source repositories for Dashboard will be available soon.
{% endhint %}

## Test on Web Client

Once you have successfully run the web client, you should be able to test the payments.

After running the web client, you will see the demo web app (playground) running on `http://localhost:4242` where you can test your payments.

<figure><img src="../.gitbook/assets/Screenshot 2023-11-09 at 5.25.15 PM.png" alt=""><figcaption></figcaption></figure>

You can test a successful payment with the following test card:

```
Card Number - 4242 4242 4242 4242
Card Expiry - Any future date
CVC - Any 3 digits
```

On confirming the payment, you will see the Payment confirmation screen.

<figure><img src="../.gitbook/assets/Screenshot 2023-11-09 at 5.42.53 PM.png" alt=""><figcaption></figcaption></figure>

## Success

Congrats! You have successfully tested an end-to-end payment with your own app server and a web client.

The app server is more powerful than just processing the payments. You can test refunds, subscription payments and more using the app server.

## Resources

- To explore more of our APIs, please check the remaining folders in the [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3).
