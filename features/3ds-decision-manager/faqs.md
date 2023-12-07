---
description: Quick Answers to commonly asked questions about 3DS Decision Manager
---

# FAQs

{% hint style="info" %}
This section covers the frequently asked questions you might have around 3DS Decision Manager. We regularly update the common questions here.
{% endhint %}

### FAQs

What are the parameters that I can use to configure 3DS rules?

* amount - set rules for a specific value or a range of values for the transaction amount
* currency - select the currency of transaction
* card\_type - choose between credit and debit cards
* card\_network - choose between card networks like visa, mastercard etc.
* billing\_country - to select the billing\_country

2. How do I update the current configuration?\
   Click on Create New and configure a new rule that would replace the existing configuration
3. What happens if I set `authentication_type` as `no_three_ds` in `/payments` request?\
   3D Secure will be enforced even if the payment request parameters conform to any one of the rules in the active 3DS Decision Manager
