---
description: Low-code solution to accept payments
---

# 🔗 Payment links

Introducing Payment Links – Seamlessly integrate into Hyperswitch without writing much code. This feature allows you to generate secure and personalised payment links, enabling swift and hassle-free transactions for your customers. Elevate your payment experience with the efficiency and flexibility of Payment Links, streamlining the way you conduct business transactions.

### Use cases for Payment links

* Email/SMS marketing or selling online with a website.
* Having multiple customer segments - to create tailored payment pages that are optimized for each bucket of customers.
* Fundraising or collecting donations.
* Accepting payments in person but don’t have the hardware.
* Social Media Commerce
* Cross-channel customer reactivation
* Automated Payment Reminders to automate collections
* A substitute for Cash-on-delivery and point-of-sale
* Streamlining  over-the-phone transactions

### How to configure Payment links through Hyperswitch API?

#### Prerequisites

* Create a Hyperswitch account via the [dashboard](https://app.hyperswitch.io/register) and create a profile ([read more](../account-management/multiple-accounts-and-profiles.md))
* Add a payment processor to you account

#### Using Payment links

#### 1. Update [business profile ](https://api-reference.hyperswitch.io/api-reference/business-profile/business-profile--update)with a default payment\_link\_config by passing the below object in the request body

{% code fullWidth="true" %}
```
“payment_link_config” : {
   “theme”: Option<String> // Custom theme color for your payment link, Can be any html color hex code Eg. #143F1E
   “logo”: Option<String> // Custom logo for your company; Can be any hosted image url Eg. “https://i.pinimg.com/736x/4d/83/5c/4d835ca8aafbbb15f84d07d926fda473.jpg”,
   “seller_name”: Option<String> // Name of your company;Eg: Shoekraft 
   “sdk_layout”: Option<String> // Custom sdk layout for your payment links: 'accordion', 'spaced_accordion', 'tabs'; 'tabs' is default
   “domain_name”: Option<String> // custom domain name of the merchant; Eg: pay.shoekraft.com     
}
```
{% endcode %}

#### 2. [Create a payment link ](https://api-reference.hyperswitch.io/api-reference/payments/payments--create)by using the same payments/create endpoint

\- Set "payment\_link" = "true" to create a payment link with default payment\_link\_configs configs set in business profile update mentioned in Step 1

\- You can also pass the  "session\_expiry" field in seconds to indicate the expiry of the payment link. By default it is 900 seconds (15 minutes)

```
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "amount": 1130,
    "currency": "USD",
    "confirm": false,
    "customer_id": "cus_123",
    "return_url": "https://hyperswitch.io",
    "description": "For selling Tshirt",
    "payment_link": true,
    "session_expiry": 2592000
}'
```

#### 3. Customizing a Payment link during creation:

You can also customize a specific payment link by including the payment\_link\_config object while creating a link during [payments/create](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) call as well. Except for domain\_name field from the same object in business\_profile/update, you could customize the remaining fields.

<pre class="language-markup"><code class="lang-markup">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "amount": 1130,
    "currency": "USD",
    "confirm": false,
    "customer_id": "cus_123",
    "return_url": "https://hyperswitch.io",
    "description": "For selling Tshirt",
    "payment_link": true,
    "session_expiry": 2592000,
<strong>    "payment_link_config": {
</strong>      "theme":"#014E28",
      "logo":"https://i.pinimg.com/736x/4d/83/5c/4d835ca8aafbbb15f84d07d926fda473.jpg",
      "seller_name":"teeskraft”,
      "sdk_layout":"tabs"
}
}'
</code></pre>

### FAQ

<details>

<summary>Can I create a payment link pointing to my custom domain?</summary>

Yes. Your custom domain can be included in the default payment\_link\_config object as part of the business profile update.&#x20;

This involves adding CNAME records and TLS certificates which ends up being a slightly complex process. Please reach out to our [Support](https://join.slack.com/t/hyperswitch-io/shared\_invite/zt-1k6cz4lee-SAJzhz6bjmpp4jZCDOtOIg) to test this feature out with your custom domain.

</details>

<details>

<summary>Can I configure Payment links through Hyperswitch Control centre?</summary>

Currently, the Control centre's capability to create payment links is under development and will be available by Q1'24.

</details>

<details>

<summary>Can I create a static payment link which can be used across users?</summary>

No, at the moment we do not support creation of static payment links ([request for feature](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests))

</details>

<details>

<summary>How long is the Payment link valid for?</summary>

The payment link is valid for 15-minutes by default. However you can increase the validity to upto 3-months (7890000) by passing the time in seconds in`session expiry` in the create payment link call

</details>

<details>

<summary>How can I send Payment links via Emails?</summary>

Hyperswitch supports generation of the payment link. We are not integrated with any email servers. You'll need to  have a mail server integration at your end and ingest the payment links to the emails being sent

</details>
