---
description: Surcharge Manager Setup
---

# Surcharge Setup guide

{% hint style="info" %}
This section covers the steps to setup surcharge manager using the Hyperswitch Control Center
{% endhint %}

## Steps to setup a rule on Surcharge Manager?

**Step 1:** Go to Workflow -> Surcharge tab on the Hyperswitch Control Center

**Step 2:** Click on create new button&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-03-04 at 6.49.56 PM.png" alt=""><figcaption></figcaption></figure>

**Step 3:** Enter the rule name, description and configure your desired rule by selecting the operators and values for the various fields&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-03-04 at 5.42.22 PM (1).png" alt=""><figcaption></figcaption></figure>

**Step 5:** Add more rules using the plus icon on the top right of the current rule panel&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-03-04 at 6.38.04 PM.png" alt=""><figcaption></figcaption></figure>

**Step 6:** Click save to configure and activate the rule&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-04-15 at 1.38.07 PM.png" alt=""><figcaption></figcaption></figure>

**Step 7:** Your rule is now successfully configured and Surcharge would be applied to all payments conforming to this rule.&#x20;

To create a test payment, Go to Home and click on Try a test payment.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-07-02 at 1.04.09 PM.png" alt=""><figcaption><p>Test payment</p></figcaption></figure>

**Note:**&#x53;urcharge manager supports only one active configuration at a time. Multiple rules can be combined into a single configuration as shown in the example

### FAQs

1. What are some of the payment parameters that I can use to configure Surcharge rules?

* Available Parameters:
  * amount - set rules for a specific value or a range of values for the transaction amount
  * currency - select the currency of transaction
  * payment\_method - configure rules for different payment methods like card, wallet, direct bank debit etc.
  * card\_type - choose between credit and debit cards
  * card\_network - choose between card networks like visa, mastercard etc.
  * billing\_country - to select the billing\_country

2. How do I update the current configuration?\
   Click on Create New and configure a new rule that would replace the existing configuration
3. What happens if I pass `surcharge_details`  field in `/payments` request?\
   surcharge\_details if sent in payments create request, surcharge decision manager will be overridden and surcharge sent in the request will be applied.
