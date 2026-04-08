---
description: Explore composable payment workflows for Vertical SaaS platforms
icon: code-compare
metaLinks:
  alternates:
    - payment-workflows.md
---

# Supported Payment Workflows

Juspay Hyperswitch's three-level profile architecture enables support for composable payment workflows, fulfilling the majority of use cases for a Vertical SaaS platform.

These workflows can be modularly organized to meet diverse business needs and provide flexibility based on client requirements. Here's a breakdown of key workflows:

### Possible Scenarios

**Direct Payments:** In the case of a client using a Vertical SaaS (VSaaS) platform, the client may prefer to authorize the customer's card only after the service is fulfilled. Therefore, the Vertical SaaS solution will need to verify and vault the card with the PSP, returning the PSP card token to the client.

**Customer Acquisition Payments:** For a client using a VSaaS platform, the primary goal is to acquire more customers. Thus, the client may rely on the platform to secure initial customer payments, while recurring payments are directly processed by the client through its PSP of choice.

**End-to-End Payments:** In cases where a client uses a Vertical SaaS platform to design new subscriptions and distribute them to customers, payments need to be more tightly integrated with the platform. As a result, the client may expect the platform to handle both customer acquisition and renewal payments through the PSP of choice on the client's behalf.

{% content-ref url="../../../integration-guide/account-management/analytics-and-operations/exporting-payments-data.md" %}
[exporting-payments-data.md](../../../integration-guide/account-management/analytics-and-operations/exporting-payments-data.md)
{% endcontent-ref %}
