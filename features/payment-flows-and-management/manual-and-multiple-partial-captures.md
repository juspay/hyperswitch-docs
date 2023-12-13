---
description: >-
  Place a hold on your customer's payment method and charge them later manually
  and multiple times
---

# Manual & Multiple Partial Captures

In most online payments use-cases, you would want to capture the funds from your customers in one-step as and when they authorize the payment. You can achieve this on Hyperswitch by setting "`capture_method" = automatic` in the payments API request you make to Hyperswitch. Since "capture\_method" defaults to "automatic", you can even skip the field and still the one-step authorize and capture would work.

**What is Manual Capture?**

In some cases, merchants prefer to authorize and place a hold on their customers' payment methods first and then charging/capturing the funds at a later stage once the goods/services are delivered. This flow is in general called the 'two-step' or 'Authorize and Capture flow'.  At Hyperswitch this is called the 'Manual Capture' flow.

**How to do a manual capture?**

1. **Create a payment from your server and set it as a 'manual' capture payment:**



1. **Confirm the payment from your SDK after collecting payment method information from your customer**
2. **Capture the payment later from merchant server**



