---
description: Low-code solution to accept payments
---

# 🔗 Payment links

Introducing Payment Links – a game-changer in simplifying transactions. Seamlessly integrate into Hyperswitch without writing much code as this innovative tool allows you to generate secure and personalized payment links, enabling swift and hassle-free transactions for your customers. Elevate your payment experience with the efficiency and flexibility of Payment Links, streamlining the way you conduct business transactions.

## Who should use Payment links?

* If you have no website
* If you do a lot of email/SMS marketing.
* If you have multiple customer segments - to create tailored payment pages that are optimized for each bucket of customers.
* If you are fundraising or collecting donations.
* If you accept payments in person but don’t have the hardware.
* If your sales move fast - customers sign up for text updates for restock, and then send them payment links when it’s go time
* If you use Social Media Commerce
* If you use Chat bots
* If you use Voice recognition
* If you Upsell
* If you require Cross-channel customer reactivation
* If you use Automated Payment Reminders to automate collections: In certain European countries, such as Germany, a large percentage of ecommerce is still invoice-driven. The risk for merchants is that customer convenience becomes costly if invoice due dates are missed.
* If you need substitute for Cash-on-delivery and point-of-sale
* If you want to streamline in-person over the phone transactions: Telemarketing may not receive the cool headlines, but the sector is enormous. In the U.S alone, revenues are around $19.5bn per year."

## How to configure Payment links through Hyperswitch API?

Say you already have a profile created under your Hyperswitch account

### Step 1: Update [business profile ](https://api-reference.hyperswitch.io/api-reference/business-profile/business-profile--update)with a default payment\_link\_config by passing the below object in the request body

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



### Step 2: [Create a payment](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) by sending payment\_link as true which will create a payment link with default payment\_link\_configs configs set in business profile update mentioned in Step 1

Sample curl:

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
    "payment_link": true
}'
```

### Customizing Payment link while creating a payment:

You can also customize a specific payment link by including the payment\_link\_config object while creating a link during [payments/create](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) call as well. Except for domain\_name field from the same object in business\_profile/update, you could customize the remaining fields.

Sample curl:

```markup
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
"payment_link_config": {
      "theme":null,
      "logo":"https://i.pinimg.com/736x/4d/83/5c/4d835ca8aafbbb15f84d07d926fda473.jpg",
      "seller_name":"teeskraft”
}
}'
```



## FAQ?

### 1. Can I create a payment link pointing to my custom domain?

Yes. Your custom domain can be included in the default payment\_link\_config object as part of the business profile update.&#x20;

This involves adding CNAME records and TLS certificates which ends up being a slightly complex process. Please reach out to our [Support](https://join.slack.com/t/hyperswitch-io/shared\_invite/zt-1k6cz4lee-SAJzhz6bjmpp4jZCDOtOIg) to test this feature out with your custom domain.

### 2. Can I configure Payment links through Hyperswitch Control centre?

Currently, the Control centre's capability to create payment links is under development and will be available by Q1'24.
