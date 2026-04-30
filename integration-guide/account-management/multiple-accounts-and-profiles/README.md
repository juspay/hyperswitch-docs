---
description: >-
  Set up your Hyperswitch account, choose between Standard and Platform setups,
  and configure organizations, merchants, and profiles for your business.
icon: file-user
metaLinks:
  alternates:
    - ./
---

# Account Setup and Structure

This chapter covers how to set up your Hyperswitch account end to end: signing up, choosing the right account setup for your business, and structuring your organization, merchants, and profiles.

{% hint style="warning" %}
If a merchant account has more than one business profile, passing `profile_id` is mandatory when creating a payment.
{% endhint %}

### What Hyperswitch Supports

* Creating multiple merchant accounts under an organization (Organization → Merchant → Profile model).
* Creating multiple business profiles under each merchant account.
* Connecting multiple payment processors under each business profile.
* Programmatically onboarding sub-merchant accounts via API under a Platform Organization for your VSaaS Setup, with automatic API key management and centralised visibility across all sub-merchants.

### What's in This Chapter

* [Quick Start: Create Your Hyperswitch Account](quick-start.md)
* [Pick the Right Setup for Your Business](pick-the-right-setup.md)
* [Organization, Merchant, and Profile](hyperswitch-account-structure.md)
* [Standard Organization](standard-organization.md)
* [Platform Organization](platform-organization-concepts.md)
  * [Setting Up a Platform Organization](setting-up-platform-organization.md)
  * [Customers, Payment Methods, and Payments](customer-payment-methods-and-payments-for-platform.md)

If you're not sure where to start, jump to [Pick the Right Setup for Your Business](pick-the-right-setup.md).
