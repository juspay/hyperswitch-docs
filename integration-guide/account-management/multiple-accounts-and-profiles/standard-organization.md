---
description: Set up and operate a Standard Organization in Hyperswitch.
icon: building
---

# Standard Organization

A Standard Organization is the default account setup created when you sign up for Hyperswitch. It supports a single business or a business with multiple brands and business units, all without onboarding external sub-merchants. If you need to onboard sub-merchants programmatically with a shared customer pool or platform-initiated operations, see [Platform Organization](platform-organization-concepts.md) instead.

### What We'll Cover

In order:

1. **What a Standard Organization gives you** by default.
2. **Adding multiple merchant accounts** for separate brands or business lines.
3. **Adding multiple profiles** under a merchant account.
4. **Generating API keys** for programmatic access.
5. **Configuring connectors** under each profile.

***

### What You Get by Default

Signing up creates:

* One **Organization** representing your business.
* One **Merchant Account** under the Organization.
* One **Profile** under that merchant account.
* Your user, with the **Organization Admin** role.

That single merchant account already has its own API keys, and the default profile is ready to accept payments once you connect a processor. For the first-time walkthrough, see [Quick Start](quick-start.md).

[ASSET: `standard-org-default-state.png` : Control Centre after sign-up, showing the auto-created Organization, Merchant Account, and Profile in the sidebar]

***

### Adding Multiple Merchant Accounts

Use multiple merchant accounts when different business lines need their own API keys. For example, a retailer running Clothing, Shoes, and Bags as separate brands can create one merchant account per brand.

#### 1. Open the Merchant Dropdown

From the sidebar at the top-left of the dashboard, click the merchant account dropdown.

#### 2. Click "Create New Merchant"

Select **+ Create new** in the dropdown.

[ASSET: `standard-org-create-merchant.png` : merchant dropdown with the Create New option highlighted]

#### 3. Name and Confirm

Enter the merchant name (for example, "Shoes") and click **Add Merchant**. The new merchant appears in the sidebar dropdown and you can switch into its context immediately.

[ASSET: `standard-org-merchant-list.png` : sidebar dropdown listing multiple merchant accounts under the Standard Organization]

Each merchant account has its own API keys, profiles, and connectors. Customers and saved payment methods are isolated per merchant — they don't cross over between Standard merchants in the same Organization.

***

### Adding Multiple Profiles Under a Merchant

Profiles are the most granular level. Use multiple profiles under one merchant account when you want to share an API key across business units but apply different routing rules, connectors, or webhooks per unit.

#### 1. Open the Profile Dropdown

From the top-right of the dashboard, click the profile dropdown to see all profiles configured for the current merchant account.

#### 2. Click "Create New Profile"

Select **+ Create new** in the profile dropdown.

[ASSET: `standard-org-create-profile.png` : profile dropdown with the Create New option highlighted]

#### 3. Name and Confirm

Enter a profile name and click **Add**. A new profile is created with an automatically generated `profile_id`. Profile IDs are also listed under **Settings** then **Business Profiles**.

***

### Generating API Keys

API keys live at the merchant level. Each merchant account in your Standard Organization needs at least one API key to make API calls.

1. Switch to the merchant context for which you want to create the key.
2. Open **Developers** then **Keys** from the sidebar.
3. Click **Create API Key**, fill in the description and validity, and confirm.

[ASSET: `standard-org-api-key.png` : API Keys page with the Create API Key flow open]

{% hint style="warning" %}
The API key is shown only once. Download or copy it before closing the dialog. If you lose it, create a new one.
{% endhint %}

For the full API key flow, see [Quick Start: Create Your First API Key](quick-start.md#3.-create-your-first-api-key).

***

### Configuring Connectors

Connectors are configured **per profile** under each merchant account. From the merchant context:

1. Open **Connectors** in the sidebar.
2. Click the processor you want to connect.
3. Provide the credentials (API key, secret, etc.) and select which payment methods to enable.
4. Save.

[ASSET: `standard-org-connector-config.png` : Connectors page after adding a processor under a profile]

Each profile maintains its own connector configurations. A connector added under one profile cannot be used by another profile.

***

### Resource Behaviour

Within a Standard Organization:

* **Customers** are scoped per merchant account. A customer created on Merchant A is not visible on Merchant B.
* **Saved payment methods** follow the same rule: scoped per merchant account.
* **API keys** are per merchant account.
* **Routing, connectors, webhooks** are per profile.

If you later need to share customers and saved payment methods across merchants (for a marketplace or multi-tenant SaaS), you'll need to convert to a Platform Organization. See [Pick the Right Setup for Your Business](pick-the-right-setup.md) to confirm which path fits.

***

### Next Steps

* Set up your first connector and run a test payment: [Quick Start](quick-start.md).
* Understand how Org, Merchant, and Profile relate: [Organization, Merchant, and Profile](hyperswitch-account-structure.md).
* Considering a Platform setup instead: [Platform Organization](platform-organization-concepts.md).
