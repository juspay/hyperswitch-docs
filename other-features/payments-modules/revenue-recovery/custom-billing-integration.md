---
description: >-
  Learn how to integrate your in-house billing engine with Revenue Recovery.
  This page explains the endpoints you need to integrate to handle the different
  scenarios in a recurring payment lifecycle.
---

# Custom Billing Integration

### What endpoints are required for this integration? <a href="#what-endpoints-are-required-for-this-integration" id="what-endpoints-are-required-for-this-integration"></a>

Revenue Recovery provides three endpoints to handle the flows involved in a recurring payment with your billing engine. Once integrated, they work together to stream information between Revenue Recovery and the billing engine seamlessly.

**1. Recovery Create API**

Configure this endpoint at your billing engine to stream transaction events into Revenue Recovery. For the request and response details, refer to the [Recovery Create API documentation](https://api-reference.hyperswitch.io/v2/revenue-recovery/revenue-recovery--create).

* Use it to stream all terminal transactions, including CIT and MIT. Non-terminal transactions, such as payment pending, need not be streamed.
* An invoice and a transaction are uniquely identified using `merchant_reference_id` and `connector_transaction_id`.
* Every transaction must have an invoice attached, sent in the `merchant_reference_id` field. All external retries made by the billing engine for an invoice must also be sent under the same `merchant_reference_id`. All retries made by Revenue Recovery are recorded under it as well.
* Transactions streamed through this API are stored as external transactions within Revenue Recovery. Transactions made by Revenue Recovery are considered internal transactions.

**2. Cancel API**

Configure this endpoint at your billing engine to notify Revenue Recovery of invoice cancellations. The invoice to cancel is identified using `merchant_reference_id`. For the request and response details, refer to the [Recovery Cancel API documentation](https://api-reference.hyperswitch.io/v2/revenue-recovery/revenue-recovery--cancel).

* Use it only where the recovery process needs to be stopped without any transaction being involved. These cases can be user driven, system driven or merchant internal operation driven cancellations.
* Once called, the invoice is marked as cancelled and closed. The recovery process cannot be restarted for it.

**3. Payments Webhook**

This is an outgoing webhook. Configure your webhook consumption endpoint in Revenue Recovery. Revenue Recovery uses it to stream all internal transactions made by it back to the billing engine, in both terminal and non-terminal states. For the webhook payload details, refer to the [Outgoing Webhook documentation](https://api-reference.hyperswitch.io/v2/schemas/outgoing--webhook).

### **How do I get started with Revenue Recovery?**

Once your Revenue Recovery merchant account is created, an onboarding flow sets up everything you need to start recovering failed payments. After onboarding is complete, you can manage all your settings from one place.

**1. Complete first-time onboarding**

Follow the onboarding flow to connect Revenue Recovery with your billing setup.

* Add one payment processor that you work with. You can add more processors later.
* Create a custom billing connector reference, which represents your in-house billing engine within Revenue Recovery.
* Define your recovery criteria, which determine how Revenue Recovery handles failed payments.

**2. Manage your setup in Configuration Details**

After onboarding, use the Configuration Details section to update your setup at any time. From here, you can:

* Add more payment processors.
* Create API keys.
* Set up your webhook endpoint details.
* Change your recovery criteria.

**3. Get your integration details**

The Configuration Details section also has all the information you need to call the Revenue Recovery APIs, including your merchant connector account (MCA) details and API keys.

The following video walks through the onboarding flow and the Configuration Details section.

{% embed url="https://youtu.be/PkIAfVn7gHM" %}
