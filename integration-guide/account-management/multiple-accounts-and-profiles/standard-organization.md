---
description: Set up and operate a Standard Organization in Hyperswitch.
icon: building
---

# Standard Organization

A Standard Organization is the default account setup created when you sign up. It supports a single business or a business with multiple brands and business units, governed entirely from the Control Centre dashboard. If you need to onboard sub-merchants programmatically with a shared customer pool or platform-initiated operations, see [Platform Organization](platform-organization-concepts.md) instead.

***

### What You Get By Default

Signing up creates:

* One **Organization** representing your business.
* One **Merchant Account** under the Organization.
* One **Profile** under that merchant account.
* Your user, with the **Organization Admin** role.

[ASSET: `standard-org-default-state.png` : Control Centre after sign-up, showing the auto-created Organization, Merchant Account, and Profile in the sidebar]

***

### Structure of a Standard Organization

A Standard Organization follows the standard three-level hierarchy:

* **Organization** at the top, containing one or more merchant accounts.
* **Merchant Account** under the organization, each with its own API keys.
* **Profile** under each merchant, where routing, connectors, webhooks, and return URLs are configured.

For the full hierarchy reference, including how to add merchants and profiles via the dashboard, see [Organization, Merchant, and Profile](hyperswitch-account-structure.md).

***

### Resource Scoping

Customers and saved payment methods in a Standard Organization are scoped at the **merchant** level:

* All profiles under the same merchant account share customer and payment-method data.
* Different merchant accounts in the same Organization are isolated. A customer or saved card on Merchant A is not visible from Merchant B.
* API keys are issued per merchant account.
* Connectors and routing are configured per profile.

If you later need cross-merchant sharing of customers and saved payment methods (for a marketplace or platform model), you'll need to convert to a Platform Organization. See [Pick the Right Setup for Your Business](pick-the-right-setup.md).

***

### Managing the Organization

Everything in a Standard Organization is administered from the Control Centre dashboard, governed by user roles:

* Create additional merchant accounts and profiles.
* Connect payment processors per profile.
* Generate and manage API keys for each merchant.
* Invite team members and grant roles at the org, merchant, or profile level.

For role-based access details, see [Manage Your Team](../manage-your-team.md).

***

### Next Steps

* Run your first payment: [Quick Start: Make a Payment](quick-start.md#5.-make-a-payment).
* Understand the Org / Merchant / Profile hierarchy in depth: [Organization, Merchant, and Profile](hyperswitch-account-structure.md).
* Considering a Platform setup instead: [Pick the Right Setup for Your Business](pick-the-right-setup.md).
