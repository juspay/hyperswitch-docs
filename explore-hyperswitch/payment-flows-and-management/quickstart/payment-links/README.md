---
description: Low-code solution to accept payments
icon: link
---

# Payment Links

Introducing Payment Links - Seamlessly integrate into Hyperswitch without writing much code. This feature allows you to generate secure and personalised payment links, enabling swift and hassle-free transactions for your customers. Elevate your payment experience with the efficiency and flexibility of Payment Links, streamlining the way you conduct business transactions.

### Use cases for Payment links

* Email/SMS marketing or selling online with a website.
* Having multiple customer segments - to create tailored payment pages that are optimized for each bucket of customers.
* Fundraising or collecting donations.
* Accepting payments in person but don't have the hardware.
* Social Media Commerce
* Cross-channel customer reactivation
* Automated Payment Reminders to automate collections
* Substitute for Cash-on-delivery and point-of-sale
* Streamlining over-the-phone transactions

{% embed url="https://www.youtube.com/watch?v=8SGyP3kIpQo" %}
API Level Overview of Payment Links with Hyperswitch
{% endembed %}

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

## Next step:

{% content-ref url="./configurations.md" %}
[Configure Payment links](./configurations.md)
{% endcontent-ref %}
