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

### What's in This Chapter

In order:

1. [**Quick Start: Create Your Hyperswitch Account**](quick-start.md). Sign up, generate your first API key, connect a processor.
2. [**Pick the Right Setup for Your Business**](pick-the-right-setup.md). Decide between Standard and Platform Organization based on your business model.
3. [**Organization, Merchant, and Profile**](hyperswitch-account-structure.md). Understand the three-level hierarchy and how multiple merchants vs multiple profiles compare.
4. [**Standard Organization**](standard-organization.md). Set up and operate a Standard Organization for direct-business and isolated multi-merchant scenarios.
5. [**Platform Organization**](platform-organization-concepts.md). Concepts and full workflow for onboarding sub-merchants programmatically, with shared customer pools and platform-on-behalf operations. Includes:
   * [Setting Up a Platform Organization](setting-up-platform-organization.md)
   * [Customers, Payment Methods, and Payments](customer-payment-methods-and-payments-for-platform.md)

### What Hyperswitch Supports

* Creating multiple merchant accounts under an organization (Organization → Merchant → Profile model).
* Creating multiple business profiles under each merchant account.
* Creating multiple instances of payment processors (Stripe, Adyen, etc.) under each business profile.
* Programmatically onboarding sub-merchant accounts via API under a Platform Organization, with automatic API key management and centralised visibility across all sub-merchants.

If you're not sure where to start, jump to [Pick the Right Setup for Your Business](pick-the-right-setup.md).
