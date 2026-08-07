---
hidden: true
---

# Settings & Administration

## Settings & Administration

**Settings** is the admin backstage. It's where owners and admins manage the **account hierarchy**, invite teammates and control what they can do, secure their own accounts, and handle **compliance**. Most people visit it rarely — but the choices made here govern everyone's access.

This section covers:

* Organization, Merchant & Profile settings
* Team & user management
* Roles & permissions (RBAC)
* Personal profile & security
* Compliance

***

### Organization, Merchant & Profile settings

Recall the hierarchy from Getting Started: **Organization → Merchant → Business Profile**. This is where you manage each level.

* **Organization settings** — top-level details for your company/tenant.
* **Merchant settings** — details for a business unit under the org; you can have multiple merchants.
* **Business Profile settings** — the level connectors, routing, API keys, and webhooks attach to; a merchant can have several profiles.

#### The Organization chart

The **Organization chart** visualizes your whole hierarchy — every merchant and profile in one tree. Use it to understand how your account is structured and to navigate to the right place, especially in larger setups.

> Use the **switcher** near the top of the sidebar to move between merchants and profiles at any time. Remember: connectors and settings are profile-scoped.

***

### Team & user management

Bring your team into the Control Center and manage their access.

* **Invite users** by email; they receive an invitation to join.
* See **pending invitations** and **active members**.
* **Assign a role** to each user (see below) that determines what they can see and do.
* **Remove** users who no longer need access.

***

### Roles & permissions (RBAC)

Hyperswitch uses **role-based access control** — each user is assigned a **role**, and the role defines their permissions across modules (payments, connectors, settings, and so on).

* **Built-in roles** cover common needs (e.g. admin/owner, operations, view-only).
* **Custom roles** (where available) let you grant exactly the permissions a team needs — for example, "can issue refunds but can't edit connectors."
* Permissions are granular: **view** vs. **manage** on different resources.

#### Least-privilege in practice

* Give support staff refund/dispute access without connector or key management.
* Restrict **API key** creation/revocation and **Vault** access to a small group.
* Reserve org/merchant/profile administration for owners.

> 🛡️ Access is scoped by the hierarchy too — a user's role applies within the merchants/profiles they're granted. Combine roles with the right scope for tight control.

***

### Personal profile & security

Every user manages their own account here.

* Update your **personal profile** details.
* Change your **password**.
* Enable **two-factor authentication (2FA)** for an extra layer of login security — strongly recommended, especially for admins.

***

### Compliance

For teams with regulatory obligations, the **Compliance** area helps you manage certificates and related documentation.

* View and manage **compliance certificates** associated with your account.
* Keep the documentation your business needs to meet payment-industry requirements in one place.

> Compliance features may vary based on your plan and configuration.

***

### Where to go next

* **Developers → API Keys** → restrict who can manage keys via roles set here.
* **Getting Started** → revisit the hierarchy concept these settings manage.
* **Vault** → lock down access to stored credentials with the right roles.
