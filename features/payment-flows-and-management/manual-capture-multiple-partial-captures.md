---
description: >-
  Understand how to place a hold on your customers' funds and capture them later
  either fully or partially and either in one-go or multiple times
---

# Manual Capture/Multiple Partial Captures

## What is Manual Capture?

In most online payments use-cases, a merchant would want to capture the funds from their customers' accounts in one-step after the issuer authorizes the payment. This is called '**one-step'** payments flow and at Hyperswitch we term this the '**Automatic Capture**' flow.&#x20;

But in some cases, merchants would like to place a hold on the customer's funds post authorization so that they can capture the funds at a later time once they deliver the goods and services. This is called the '**two-step**' flow or '**Auth and Capture**' flow in general payments parlance. Here at Hyperswitch, we call this the '**Manual Capture'** flow.

## **How to do Manual Capture?**

### 1. Create a payment from your server with "`capture_method" = "manual"`

The 'capture\_method' field determines the type of capture for a particular payment and it defaults to 'automatic' if not passed. So, to do manual capture, set "`capture_method" = "manual"` when creating a payment from your server

**Sample curl:**



### 2. Confirm the payment after collecting payment\_method details

Confirm the payment after collecting the payment\_method details from your customer and informing them that the funds in their account would be blocked and charged later once the goods and services are delivered. Unified checkout handles this for automatically.

**Sample curl:**



### 3. Capture the payment after delivering the goods and services:

After delivering the goods and services, capture the payment by passing the payment\_id from above step to `payments/capture API endpoint`

### **'Full' vs 'Partial' Capture:**

Now, the merchant can either:

* capture the full amount that was authorized - '**Full capture'**. Here the payments status transitions to 'SUCCEEDED'.
* capture only a partial amount that was authorized - '**Partial Capture**'. Here the payments status transitions to 'PARTIALLY\_CAPTURED' and the remaining amount is automatically voided at the processor's end.

