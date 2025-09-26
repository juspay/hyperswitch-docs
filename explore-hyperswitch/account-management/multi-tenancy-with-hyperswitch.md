---
icon: cubes-stacked
---

# Multi-Tenancy

## What is Multi-Tenancy?

Multi-tenancy refers to an architecture where a single instance of the software and its infrastructure serves multiple tenants. Multi-tenancy in Hyperswitch enables each of it's tenants to have customised offering of the Hyperswitch stack without the overhead of software and infrastructure maintenance.

Each tenant operates in a logically isolated environment but shares the underlying infrastructure i.e. the data and customisations of each tenant are kept separate and secure, even though they use the same software instance. Hyperswitch uses a single application and multiple storage schema approach for multi-tenancy.

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkf7BGdsPkCw9nalhAIlE%2Fuploads%2FFEv2dQi7YAjfPthCFfXl%2FScreenshot%202024-10-11%20at%202.28.06%E2%80%AFAM.png?alt=media&#x26;token=a4cc712a-665b-492c-ad5c-d105446d0b23" alt="" width="563"><figcaption></figcaption></figure>

## Benefits of Multi-tenancy with Hyperswitch

1. **Configuration Options**: Hyperswitch provides configurable settings that allow tenants to customise the look and feel of the application, such as -&#x20;
   * Branding (logo, colors, themes)&#x20;
   * Email templates
   * Language preferences&#x20;
   * Feature toggles&#x20;

&#x20;       _These configurations can be managed by tenant users and will apply to merchants of tenants._

2. **Tenant-Specific Extensions**: Tenants can extend the functionality of the Hyperswitch application to tailor it to their specific needs by installing or developing custom plugins, modules, or integrations. These extensions can be developed using standardised APIs, SDKs, or scripting languages, and should adhere to security and performance best practices.
3. **Permission-Based Customisations**: Hyperswitch administrators manage access to control which customisations are available to each tenant. This ensures that tenants can only modify the aspects of the application they are authorised to, ensuring privacy and preventing access by unauthorised parties.
4. **Testing and Sandbox Environments**: Hyperswitch provides sandbox environments for tenants to experiment with any features or customisations safely, without affecting the production environment. This allows tenants to validate changes and ensure they meet their requirements before deploying them to production.
5. **Documentation and Support**: Tenants can have their own version of developer docs white-listed on their hosts. Comprehensive documentation, tutorials, and support resources are provided to help tenants understand how to onboard and integrate merchants. This includes documentation for APIs, SDKs, best practices, and troubleshooting guides.
6. **Tenant <> Merchant Communication** - Based on tenant's requirements, Hyperswitch can trigger SMS and Email notification on behalf of the tenant to the customers and merchants by integrating with their service provider.

## Hierarchy of Entities in Hyperswitch

A tenant’s scope will include multiple organizations and their associated entities, such as merchant accounts, business profiles, and other hierarchical elements lower in the structure. Each tenant would have  tenant admins who can create organizations under the scope of that tenant.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2024-10-11 at 2.24.26 AM.png" alt=""><figcaption></figcaption></figure>

## Tenant Management

### Tenant Onboarding:&#x20;

Each tenant onboarded on Hyperswitch will have white-labeled links for the following applications:

* **Hyperswitch’s S2S APIs**
* **Payment Page**
* **Dashboard**

Once these white-labeled endpoints are available, tenants will be onboarded on Dashboard. Link to set credentials will be sent via email. Post logging in to Dashboard, tenants can onboard merchants.

{% content-ref url="../payment-orchestration/" %}
[payment-orchestration](../payment-orchestration/)
{% endcontent-ref %}
