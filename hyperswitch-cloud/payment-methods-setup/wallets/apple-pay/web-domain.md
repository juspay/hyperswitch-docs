# Web Domain

**Steps to configure Apple Pay on Hyperswitch**

* Login to [Hyperswitch control center](https://app.hyperswitch.io/)
* In the Processor tab, select desired connector
* While selecting Payment Methods, click on Apple Pay in the Wallet section
* Select the Web Domain option

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-12-07 at 7.41.02 PM.png" alt="" width="563"><figcaption></figcaption></figure>

* Download the domain verification file using the button available
* Host this file on your server at _`merchant_domain`_`/.well-known/apple-developer-merchantid-domain-association`
* Enter the domain name where you have hosted the domain verification file
* Click on verify and enable to complete your setup

