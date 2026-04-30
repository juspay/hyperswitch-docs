---
description: How the Platform Merchant initiates operations on behalf of a Connected Merchant using the Platform API Key.
icon: user-shield
---

# On-Behalf-of Operations

Apart from a Connected Merchant initiating its own operations, the **Platform Merchant** can act on behalf of any Connected Merchant using the Platform API Key. This is not limited to payments. The platform can perform the full operational surface for a Connected Merchant from one credential, with every action recorded against the correct Connected Merchant for attribution and settlement.

{% hint style="info" %}
On-behalf-of operations are currently API-only. Set up your Platform Organization first if you haven't already. See [Setting Up a Platform Organization](setting-up-platform-organization.md).
{% endhint %}

The walkthrough below uses a payment as the example, but the same authentication pattern applies to every supported on-behalf operation.

***

### 1. Authenticate with the Platform API Key

Use the Platform API Key (generated from the Platform Merchant context) to authenticate the request. See [Generating a Platform API Key](platform-organization-concepts.md#2.-generate-a-platform-api-key) for how to create one.

### 2. Identify the Connected Merchant in the Request

When making the API call, identify which Connected Merchant the operation is for. The request is authorised by the platform but executed against the Connected Merchant's context, using its connector credentials for payment-side operations and scoping configuration changes to that Connected Merchant.

### 3. Inspect the Response

The response includes both the Platform Merchant and the Connected Merchant the operation was performed for, along with the initiator of the call. For every operation you can tell who initiated it and which merchant it was executed against.

For request and response schemas across the supported operations, see the [Hyperswitch API Reference](https://api-reference.hyperswitch.io/).

***

### What This Enables

* **Centralized orchestration**: the platform can run payments, refunds, captures, disputes, connector setup, and account management for any Connected Merchant from one credential.
* **Clear attribution**: every operation records both the initiator (Platform) and the executing merchant (Connected), so reporting, settlement, and audit stay unambiguous.
* **Same shared customer and payment method pool**: on-behalf operations use the shared pool, so saved cards and customers are immediately reusable across the group. Cards can also be saved during a platform-initiated on-behalf payment, since these are the same payments a Connected Merchant would run itself, just initiated by the Platform Merchant. The saved card lands in the same shared pool. See [Sharing Customers and Payment Methods](sharing-customers-and-payment-methods.md) for the sharing model in detail.

{% hint style="info" %}
On-behalf-of is **not** available for Standard Merchants. The Platform Merchant can still manage a Standard Merchant's account (creation, API key generation, and connector setup programmatically), but the Platform API Key cannot perform payments, refunds, captures, or disputes on a Standard Merchant's behalf. Those must be initiated by the Standard Merchant directly using its own API key.
{% endhint %}

***

### Quick Reference

| Scenario                                                          | Initiated by | Executed against | Customer Scope       | Payment Method Scope |
| ----------------------------------------------------------------- | ------------ | ---------------- | -------------------- | -------------------- |
| Connected Merchant runs its own operation                         | Connected    | Connected        | Shared pool          | Shared pool          |
| Platform initiates an operation on behalf of a Connected Merchant | Platform     | Connected        | Shared pool          | Shared pool          |
| Standard Merchant runs its own operation                          | Standard     | Standard         | Isolated to Standard | Isolated to Standard |

The Platform-on-behalf path applies to the full operational surface, not payments alone: payments, refunds, captures, disputes, connector setup, profile management, and API key management.
