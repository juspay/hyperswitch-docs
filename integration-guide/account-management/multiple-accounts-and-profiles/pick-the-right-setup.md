---
description: Decide between a Standard Organization and a Platform Organization based on how your business operates.
icon: signs-post
---

# Pick the Right Setup for Your Business

Hyperswitch supports two account setups: a **Standard Organization** and a **Platform Organization**. The right choice depends on whether you're running payments for a single business (with one or more brands) or operating as a parent that onboards other merchants.

This page lays out both paths and helps you pick.

### Two Setups, One Decision

| Setup | Use this when |
| --- | --- |
| **Standard Organization** | You run payments for your own business, possibly across multiple brands or business units, but you don't onboard external merchants. |
| **Platform Organization** | You manage payments for multiple sub-merchants programmatically (a marketplace, a multi-tenant SaaS, a vertical SaaS handling its tenants' payments). |

***

### When to Choose a Standard Organization

A Standard Organization is the default when you sign up. It fits these scenarios:

* **Single merchant.** One business, one brand, one set of API keys.
* **Multiple brands or business units.** A single business operating multiple storefronts (e.g., a retailer with separate clothing, shoes, and accessories lines). Use multiple **merchant accounts** under the same Standard Org, each with its own API keys, or multiple **profiles** under one merchant account if you want to share an API key across business units.
* **Vertical SaaS with isolated tenants.** Each tenant runs payments on its own account, with no shared customers or saved cards across tenants. Each tenant maps to a merchant account under your Standard Org.

[ASSET: `setup-standard-org-diagram.png` : diagram showing a Standard Organization with multiple merchant accounts and profiles, each operating independently]

For setup details, see [Standard Organization](standard-organization.md).

***

### When to Choose a Platform Organization

A Platform Organization is for businesses that **onboard sub-merchants programmatically** and want to manage them from a central control plane. Two flavours of sub-merchants are supported, and you can mix them in the same Platform Org:

#### Connected Merchants (shared resources)

Use **Connected Merchants** when you want sub-merchants to share customers and saved payment methods. Choose this if:

* You operate a **marketplace** where the same end-customer might pay multiple sellers (e.g., booking platforms, multi-vendor commerce).
* You're a **multi-tenant SaaS** that wants a unified customer experience: a customer who saves their card on Tenant A can reuse it on Tenant B.
* You want the **platform to initiate operations on behalf of** a sub-merchant: payments, refunds, captures, disputes, connector configuration. The Platform API Key acts as a privileged credential across the connected group.

#### Standard Merchants under a Platform Org (isolated)

Use **Standard Merchants** under a Platform Org when you want central account management but **no resource sharing** between sub-merchants. Choose this if:

* You're a **VSaaS or franchise operator** where each sub-merchant must keep its customers and saved cards isolated for compliance, contractual, or data-boundary reasons.
* You want the platform to **provision accounts and generate API keys** for sub-merchants programmatically, but day-to-day payment operations stay with the sub-merchant.

[ASSET: `setup-platform-org-diagram.png` : diagram showing a Platform Organization with one Platform Merchant, two Connected Merchants sharing a customer pool, and two isolated Standard Merchants]

For concepts and setup, see [Platform Organization](platform-organization-concepts.md) followed by [Setting Up a Platform Organization](setting-up-platform-organization.md).

***

### Quick Comparison

| Capability                                              | Standard Organization | Platform Organization              |
| ------------------------------------------------------- | --------------------- | ---------------------------------- |
| Onboard sub-merchants programmatically                  | No                    | Yes                                |
| Generate sub-merchant API keys via API                  | No                    | Yes (Platform API Key)             |
| Shared customer pool across sub-merchants               | No                    | Yes (Connected Merchants only)     |
| Shared saved payment methods across sub-merchants       | No                    | Yes (Connected Merchants only)     |
| Platform initiates payments on behalf of sub-merchants  | No                    | Yes (Connected Merchants only)     |
| Multiple merchant accounts under one organization       | Yes                   | Yes                                |
| Multiple profiles per merchant account                  | Yes                   | Yes                                |

***

### Examples by Business Type

| Business type                                                  | Recommended setup                                   |
| -------------------------------------------------------------- | --------------------------------------------------- |
| Single-business e-commerce store                               | Standard Organization                               |
| Retailer with multiple brand storefronts                       | Standard Organization, multiple merchants/profiles  |
| VSaaS with fully isolated tenants (e.g., per-clinic billing)   | Standard Organization or Platform Org with Standard Merchants |
| Marketplace with shared customer view (e.g., multi-vendor commerce) | Platform Organization with Connected Merchants |
| Multi-tenant SaaS with unified saved-card experience           | Platform Organization with Connected Merchants      |
| Franchise operator centralising onboarding but keeping data isolated | Platform Organization with Standard Merchants  |

***

### Still Not Sure?

Start with a Standard Organization and convert to a Platform Organization later if your business model evolves. Conversion requires assistance from your administrator. If you're already certain about the platform model, set up a Platform Organization from the start to avoid migration overhead.

### Next Steps

* For a Standard setup: [Standard Organization](standard-organization.md).
* For a Platform setup: [Platform Organization](platform-organization-concepts.md), then [Setting Up a Platform Organization](setting-up-platform-organization.md).
* To understand the building blocks first: [Organization, Merchant, and Profile](hyperswitch-account-structure.md).
