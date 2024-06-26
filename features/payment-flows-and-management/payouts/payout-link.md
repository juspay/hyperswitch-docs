---
description: Low-code solution to accept payouts
---

# 🔗 Payout links

Introducing Payout Links - Make sending out money to beneficiaries, simple and easy. Improve customer / vendor / partner's experience by making instant payouts in their preferred mode of transaction with preferred processor.

### Use cases for Payout links

- Corporates - Pay marketing affiliates and reimburse employees.
- BFSI - Settle insurance claims and pay DSA incentives.
- Healthcare - Pay field agents, handle reimbursements, and issue refunds.
- Travel and Hospitality - Pay commissions to vendors, handle reimbursements and do refunds.
- Rental Business - Process Security Deposit Refunds for all rental business like car, housing, furniture and appliances.
- Online gaming - Distribute prize money to players.
- NGOs & Political Organisations - Reimburse field agents and volunteers.

### How to configure Payout links through Hyperswitch API?

#### Prerequisites

- Create a Hyperswitch account via the [dashboard](https://app.hyperswitch.io/register) and create a profile ([read more](../account-management/multiple-accounts-and-profiles.md))
- Add a payout processor to your account

#### Using Payout links

> Note: Domain name might vary based on the testing and production environment.

#### 1. Update [business profile](https://api-reference.hyperswitch.io/api-reference/business-profile/business-profile--update) with a default payout_link_config by passing the below object in the request body

{% code fullWidth="true" %}

```jsonc
"payout_link_config": {
   "theme": "#143F1E", // Custom theme color for your payout link. Can be any html color hex code. Optional.
   "logo": "https://hyperswitch.io/favicon.ico", // Custom logo for your company. Can be any hosted image URL. Optional.
   "merchant_name": "Shoekraft", // Name of your company. Optional.
}
```

{% endcode %}

#### 2. [Create a payout link](https://api-reference.hyperswitch.io/api-reference/payouts/payouts--create) by using the create payouts endpoint

\- Set "payout_link" = "true" to create a payout link with default **payout_link_config** set in business profile update mentioned in Step 1

\- You can also pass the "session_expiry" field in seconds to indicate the expiry of the payout link. By default it is 900 seconds (15 minutes)

```shell
curl --location 'https://sandbox.hyperswitch.io/payouts/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "amount": 100,
    "currency": "EUR",
    "customer_id": "cus_123",
    "name": "John Doe",
    "phone": "999999999",
    "phone_country_code": "+65",
    "description": "Its my first payout request",
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "CA",
            "zip": "94122",
            "country": "US",
            "first_name": "John",
            "last_name": "Doe"
        },
        "phone": {
            "number": "8056594427",
            "country_code": "+91"
        }
    },
    "payout_link" : true,
    "confirm": false,
    "session_expiry":2592000
}'
```

#### 3. Customizing a payout link during creation:

You can also customize a specific payout link by including the **payout_link_config** object while creating a link during [payouts/create](https://api-reference.hyperswitch.io/api-reference/payouts/payouts--create) call as well. The UI is customizable during link creation. However, domain_name cannot be customized and is always read from a business profile's config.

<pre class="language-markup"><code class="lang-markup">curl --location 'https://sandbox.hyperswitch.io/payouts/create' \
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
    "payout_link": true,
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "CA",
            "zip": "94122",
            "country": "US",
            "first_name": "John",
            "last_name": "Doe"
        },
        "phone": {
            "number": "8056594427",
            "country_code": "+91"
        }
    },
    "session_expiry": 2592000,
<strong>    "payout_link_config"</strong>: {
        "merchant_logo": "https://i.imgur.com/N18JAS2.jpg",
        "color_scheme": {
            "background_primary_color": "#36D399",
            "sdk_theme": "#36D399"
        }
    }
}'
</code></pre>

<figure><img src="../../../.gitbook/assets/payout_links.png" alt=""><figcaption></figcaption></figure>

### FAQ

<details>

<summary>Can I create a payout link pointing to my custom domain?</summary>

Yes. Your custom domain can be included in the default payout_link_config object as part of the business profile update.

This involves adding CNAME records and TLS certificates which ends up being a slightly complex process. Please reach out to our [Support](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-1k6cz4lee-SAJzhz6bjmpp4jZCDOtOIg) to test this feature out with your custom domain.

</details>

<details>
<summary>What are the benefits of using a Payout link?</summary>
Payout links simplify the process of sending money, eliminating the operational complexities of bank transfers or payouts. With just a few clicks, you can create a payout link. Once generated, we notify the recipient, who can redeem the money at their convenience.
</details>

<details>

<summary>How long is the Payout link valid for?</summary>

The payout link is valid for 15 minutes by default. However you can increase the validity to upto 3 months (7890000) by passing the time in seconds in `session_expiry` in the create payout link call

</details>

<details>

<summary>How can I send Payout links via Emails?</summary>

Hyperswitch supports generation of the payout link. We are not integrated with any email servers. You'll need to have a mail server integration at your end and ingest the payout links to the emails being sent

</details>
