---
description: Route payments using merchant-defined conditions such as amount, currency, country, payment method, and customer context
icon: ruler
metaLinks:
  alternates:
    - rule-based-routing.md
---

# Rule-Based Routing

Rule-Based Routing lets you define explicit business logic for processor selection. Use it when a payment should go to a specific processor because of region, currency, payment method, transaction amount, card type, or a commercial agreement.

## When To Use It

Use Rule-Based Routing when you need deterministic control, for example:

* Send high-value payments to a processor with better risk handling.
* Route a country or currency to a local acquirer.
* Use a specific processor for a payment method.
* Keep a fallback list for a rule, so a failed or ineligible processor does not block the payment.

## How It Works

A routing rule has two parts:

* **Condition:** The payment attributes that must match, such as payment method, amount, currency, billing country, or card network.
* **Processor preference:** The processor or ordered processor list to use when the condition matches.

Rules are evaluated from top to bottom. The first matching rule is applied. If none match, Hyperswitch uses your [Default Fallback Routing](default-fallback-routing.md).

## Setup

1. Go to `Workflow` > `Routing`.
2. Choose `Rule-Based Routing`.
3. Create a rule with the required conditions.
4. Select the processor preference for that rule.
5. Save and activate the routing configuration.

{% hint style="info" %}
Screenshot placeholder: Rule builder screen with one condition and a processor preference.
{% endhint %}

## Good Practices

Keep the most specific rules at the top and broad rules lower in the list. Always configure Default Fallback Routing so payments have a backup path when a rule output is not eligible for the payment.
