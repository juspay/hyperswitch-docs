---
description: Assign roles and permission to users
icon: screen-users
---

# Manage Your Team

You can manage your team - invite / add new users, assign roles and update roles (upcoming) - through the Hyperswitch control center. Currently, Hyperswitch provides 7 default roles for you to configure.

### Default Roles

Our system currently offers a set of default roles, each with predefined permissions:

**1. Organization Admin**

* Full access to the platform, including user management, transaction oversight, system configuration, and reconciliation.
* Can create new merchants from the dashboard.

***

**2. Merchant Admin**

* Full access to merchant-related information, including user management, transaction oversight, and system configuration.
* Cannot create new merchants but can manage all other merchant operations.

***

**3. Profile Admin**

* Full control over profile-level operations, connectors, workflows, analytics, users, and merchant details.
* Can manage and configure all aspects of the profile.

***

**4. Merchant Developer**

* Can create and manage API keys.
* Has view access to operations, connectors, analytics, users, and merchant details, with the ability to manage merchant details.

***

**5. Profile Developer**

* Can create and manage API keys for the profile.
* Has view and manage access to operations, connectors, analytics, users, and merchant details.

***

**6. Merchant Operator**

* Can view and manage payment-related information, including refunds, mandates, and disputes.
* Has view-only access to workflows, connectors, analytics, users, and merchant details.

***

**7. Profile Operator**

* Can manage payment-related operations for the profile.
* Has view access to connectors, workflows, analytics, users, and merchant details.

***

**8. Merchant IAM**

* Can invite or add users to the merchant account.
* Has restricted access to other modules, including operations, analytics, and merchant details.

***

**9. Profile IAM**

* Can invite or manage users within the profile.
* Has restricted access to operations, analytics, and merchant details.

***

**10. Profile View Only**

* View-only access to all modules, including operations, connectors, workflows, analytics, users, and merchant details.

***

**11. Merchant View Only**

* View-only access to all modules within the merchant, including operations, connectors, workflows, analytics, users, and merchant details.

***

**12. Profile Customer Support**

* Can view transaction details and customer information necessary for handling queries and support issues.
* View access to operations, analytics, users, and merchant details.

***

**13. Customer Support**

* Can access transaction details and customer information needed for handling support queries.
* View access to merchant operations, analytics, users, and merchant details.

<table><thead><tr><th width="239">Permissions</th><th width="40" data-type="checkbox">Org Admin</th><th width="162" data-type="checkbox">Merchant Admin</th><th width="173" data-type="checkbox">Payment Operator</th><th width="169" data-type="checkbox">Customer Support</th><th width="113" data-type="checkbox">Developer</th><th width="68" data-type="checkbox">IAM</th><th data-type="checkbox">View All</th></tr></thead><tbody><tr><td>View operations</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td></tr><tr><td>Manage operations</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td></tr><tr><td>View connectors</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>true</td></tr><tr><td>Manage connectors</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td></tr><tr><td>View workflows (routing, 3DS)</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>true</td></tr><tr><td>Manage workflows</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td></tr><tr><td>View analytics</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>View team / user</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Manage team / users</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>true</td><td>false</td></tr><tr><td>View merchant details</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Manage merchant details</td><td>true</td><td>true</td><td>false</td><td>false</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Create a merchant</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td></tr></tbody></table>

These roles are designed to cater to the common operational hierarchies in most organizations.

### Custom Roles:

This feature allows organisations to create roles with specific permissions that perfectly align with their unique operational structures and requirements. Custom roles can only be created at merchant roles.

#### Steps to create a custom role -&#x20;

* Go to Settings -> Users in the Hyperswitch Dashboard.
* Switch to the Roles tab, and click on Create Custom Roles.

<figure><img src="../../.gitbook/assets/Screenshot 2024-09-11 at 12.57.58 PM (2).png" alt=""><figcaption></figcaption></figure>

* Define scope, and set permissions for the custom role you want to create.

<figure><img src="../../.gitbook/assets/Screenshot 2024-09-11 at 1.11.44 PM.png" alt=""><figcaption></figcaption></figure>

### Assigning Roles and Permissions: A Walkthrough

The process of assigning roles and permissions is straightforward:

1. **Accessing User Management**: Administrators can access the User Management section from the dashboard. Under Settings -> Team
2. **Creating / Inviting New Users**: Add new team members by entering their details and assigning them a role corresponding to their position in the organization. In case an email service is enabled, then an email is triggered to the invited users from where it can be accepted. If there is no email service, then the user is created for that merchant\_id with a random password that can be shared.

<figure><img src="../../.gitbook/assets/Screenshot 2024-09-11 at 1.20.54 PM 2 (1).png" alt=""><figcaption></figcaption></figure>

3. **Modifying Roles**: Existing users’ roles can be adjusted as needed, accommodating changes in responsibilities or positions. This is an upcoming feature.

