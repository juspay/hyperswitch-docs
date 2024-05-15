---
description: Assign roles and permission to users
---

# 🛂 Manage your team

{% hint style="info" %}
Follow this guide to understand how to set up your team in Hyperswitch and to manage access through roles and permissions
{% endhint %}

You can manage your team - invite / add new users, assign roles and update roles (upcoming) - through the Hyperswitch control center. Currently, Hyperswitch provides 7 default roles for you to configure.

### Default Roles

Our system currently offers a set of default roles, each with predefined permissions:

#### 1. Organisation **Administrator (Organization Admin)**

* Full access to the platform, including user management, transaction oversight, and system configuration.
* Organization admins can create new merchants from the dashboard

#### 2. Merchant **Administrator (Admin)**

* Full access to merchant related information, including user management, transaction oversight, and system configuration.
* The only permission an admin doesn't have which the organization admin has is the ability to create merchants

#### 3. **Payments Operator (Operator)**

* A payment operator can view and edit payment related information including refunds, mandates and disputes
* View only access to other modules

#### 4. **Customer Support**&#x20;

* Access to transaction details and customer information necessary for handling queries and support issues.

#### 5. Developer

* A developer can create and manage API keys along with view access to other modules

#### 6. IAM

* An IAM user has access to invite / add user to the merchant and restricted access to all other modules

#### 7. View All (View only)

* A view only user has view access to all the modules within the hyperswitch control center

<table><thead><tr><th width="239">Permissions</th><th width="125" data-type="checkbox">Org Admin</th><th width="162" data-type="checkbox">Merchant Admin</th><th width="173" data-type="checkbox">Payment Operator</th><th width="169" data-type="checkbox">Customer Support</th><th width="113" data-type="checkbox">Developer</th><th width="68" data-type="checkbox">IAM</th><th data-type="checkbox">View All</th></tr></thead><tbody><tr><td>View operations</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td></tr><tr><td>Manage operations</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td></tr><tr><td>View connectors</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>true</td></tr><tr><td>Manage connectors</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td></tr><tr><td>View workflows (routing, 3DS)</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>true</td></tr><tr><td>Manage workflows</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td></tr><tr><td>View analytics</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>View team / user</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Manage team / users</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>true</td><td>false</td></tr><tr><td>View merchant details</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Manage merchant details</td><td>true</td><td>true</td><td>false</td><td>false</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Create a merchant</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td><td>false</td></tr></tbody></table>

These roles are designed to cater to the common operational hierarchies in most organizations.

### Custom Roles: Upcoming Feature for Tailored Access

Recognising the diverse needs of different businesses, our next update is set to introduce custom roles. This will allow organisations to create roles with specific permissions that perfectly align with their unique operational structures and requirements.

### Assigning Roles and Permissions: A Walkthrough

The process of assigning roles and permissions is straightforward:

1. **Accessing User Management**: Administrators can access the User Management section from the dashboard. Under Settings -> Team
2. **Creating / Inviting New Users**: Add new team members by entering their details and assigning them a role corresponding to their position in the organization. In case an email service is enabled, then an email is triggered to the invited users from where it can be accepted. If there is no email service, then the user is created for that merchant\_id with a random password that can be shared.
3. **Modifying Roles**: Existing users’ roles can be adjusted as needed, accommodating changes in responsibilities or positions. This is an upcoming feature.

