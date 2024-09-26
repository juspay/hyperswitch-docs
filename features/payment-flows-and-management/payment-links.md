---
description: Low-code solution to accept payments
---

# 🔗 Payment links

> This feature is still under development. We will update this section, as soon as it is live.

Introducing Payment Links – Seamlessly integrate into Hyperswitch without writing much code. This feature allows you to generate secure and personalised payment links, enabling swift and hassle-free transactions for your customers. Elevate your payment experience with the efficiency and flexibility of Payment Links, streamlining the way you conduct business transactions.

### Use cases for Payment links

* Email/SMS marketing or selling online with a website.
* Having multiple customer segments - to create tailored payment pages that are optimized for each bucket of customers.
* Fundraising or collecting donations.
* Accepting payments in person but don’t have the hardware.
* Social Media Commerce
* Cross-channel customer reactivation
* Automated Payment Reminders to automate collections
* Substitute for Cash-on-delivery and point-of-sale
* Streamlining over-the-phone transactions

{% embed url="https://www.youtube.com/watch?v=8SGyP3kIpQo" %}
API Level Overview of Payment Links with Hyperswitch
{% endembed %}

### How to configure Payment links through Hyperswitch API?

#### Prerequisites

* Create a Hyperswitch account via the [dashboard](https://app.hyperswitch.io/register) and create a profile ([read more](../account-management/multiple-accounts-and-profiles.md))
* Add a payment processor to you account

#### Using Payment links

> > Note: Domain name might vary based on the testing and production environment.

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

\- Set "payment\_link" = "true" to create a payment link with default **payment\_link\_configs** configs set in business profile update mentioned in Step 1

\- You can also pass the "session\_expiry" field in seconds to indicate the expiry of the payment link. By default it is 900 seconds (15 minutes)

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

You can also customize a specific payment link by including the **payment\_link\_config object** while creating a link during [payments/create](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) call as well. Except for domain\_name field from the same object in business\_profile/update, you could customize the remaining fields.

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

#### 4. How to use Wallets like Apple Pay & Google Pay in Payment Links?

To enable wallet flows such as Apple Pay or Google Pay for payment links, domain validation from Apple or Google is required respectively to obtain session tokens. This validation can be facilitated by utilizing the custom domain feature available for payment links, which can be configured at the business profile level.

For getting it configured you can contact us! Once done, we will configure your custom domain and give you a TLS certificate.

After you have setup custom domain in your cloud, you need to get respective Google pay, Apple pay certificate for your new domain, and register the same in our dashboard.

#### 5. **How to setup custom domain within your cloud**

* Identify your DNS provider

> First, determine which service is handling your DNS records. This will guide you to the correct platform where you can log in and set up the new records.

> Your DNS provider may be the same as your domain registrar, but it's possible they are different entities.

> If you're unsure about your DNS provider, you can search for your domain's nameservers using the following command, replacing "hyperswitch.com" with your own domain:

```shell
$ nslookup -querytype=NS hyperswitch.com
```

> You’ll see a list of name servers for your domain in the output.

* Create required DNS records

> In this segment, you'll generate the necessary DNS records to link your domain. Follow the following steps to enable the same

Step 1: Sign into your DNS provider

> DNS providers offer a control panel where you can log in to manage your DNS settings. Locate your provider’s control panel page and sign in.

Step 2: Locate the page to manage the DNS for your domain

> Now that you've successfully logged in, locate the section within your provider's control panel where you can manage the DNS records for your domain.

Step 3: Create CNAME record

> In your DNS control panel, create a new record that associates your chosen subdomain with 'hyperswitch payment link'. Your DNS provider will typically prompt you to specify the record type, name, value, and TTL (Time To Live) or expiration when adding a new record.

Enter the following values and save the new DNS record.

> \| FIELD | INSTRUCTIONS | DESCRIPTION | |----------|----------|----------| | Type | Select `CNAME` from the dropdown | What kind of DNS record this is. | | Name | if your custom domain is `paymentlink.xyz.com`, enter `paymentlink`| For CNAME records, this field is the first part of your subdomain (the part leading up to the first period).| | Value |Enter `sandbox.hyperswitch.io` | This is what the new subdomain record points to–in this case, Hyperswitch .Some providers may expect a trailing period (.) after the CNAME value. Make sure to verify that your CNAME value matches the format your provider expects. | | TTL/Expiry | Enter `300` | An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not allow you to change the TTL value. If this field is missing or you can’t change it, it’s safe to ignore this part of the configuration. |

Step 4: Create your TXT record

> Navigate to your DNS control panel and proceed to add a new TXT record.

> > This TXT record is essential for domain ownership verification. It's a necessary step to obtain TLS certificates for your domain, ensuring secure payment processing.

> Enter these values and save the new DNS record:

> \| FIELD | INSTRUCTIONS | DESCRIPTION | |----------|----------|----------| | Type | Select `TXT` from the dropdown | What kind of DNS record this is. | | Name | If your custom domain is `paymentlink.xyz.com`, enter \_acme-challenge.paymentlink| For TXT records, this field is the subdomain portion of your domain. | | Value | Copy the TXT value that is given by us and paste | This is a long, unique string used for domain verification | | TTL/Expiry | Enter `300` | An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not allow you to change the TTL value. If this field is missing or you can’t change it, it’s safe to ignore this part of the configuration.|

Step 5. Verify your CNAME record setup

> After you save your DNS record, verify that it has the correct values.

> > Please allow up to 10 minutes for your DNS provider to update its name servers. Replace "pay.xyz.com" with your custom domain in the command below, and then run it in your terminal:

```shell
$ nslookup -querytype=CNAME paymentlink.xyz.com
```

your should get a output like this

```shell
<your subdomain> 	canonical name = sandbox.hyperswitch.io.
```

Once you observe the output, proceed to the next step.

Step 6. Verify your TXT record

> After you save your DNS record, verify that it has the correct values.

> > Please allow up to 10 minutes for your DNS provider to update its nameservers. Replace pay.xyz.com with your custom domain in the following command and run it from your terminal:

```shell
$ nslookup -querytype=TXT _acme-challenge.paymentlink
```

your should get a output like this

```shell
_acme-challenge.<your domain>   text = "<your unique TXT record value>"
```

> If you don't observe your unique TXT record value in the output, please wait a little longer and then attempt running the command again.

> Upon completing this step, your DNS records will be configured.

* Now that you've established and verified your DNS records, Hyperswitch proceeds to verify the connection and provision your domain on our end. You will receive an email from us once the domain is ready for you to enable it.

### FAQ

<details>

<summary>Can I create a payment link pointing to my custom domain?</summary>

Yes. Your custom domain can be included in the default payment\_link\_config object as part of the business profile update.

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

Hyperswitch supports generation of the payment link. We are not integrated with any email servers. You'll need to have a mail server integration at your end and ingest the payment links to the emails being sent

</details>
