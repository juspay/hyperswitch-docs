---
icon: code-compare
---

# Payment Workflows

Hyperswitch’s three-level profile architecture enables support for composable payment workflows, fulfilling the majority of use cases for a Vertical SaaS platform.&#x20;

These workflows can be modularly organized to meet diverse business needs and provide flexibility based on client requirements. Here’s a breakdown of key workflows:

### Possible Scenerios:

**Direct Payments:** In the case of a client using a Vertical SaaS (VSaaS) platform, the client may prefer to authorize the customer’s card only after the service is fulfilled. Therefore, the Vertical SaaS solution will need to verify and vault the card with the PSP, returning the PSP card token to the client.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-06 at 2.31.01 AM.png" alt=""><figcaption></figcaption></figure>

**Customer Acquisition Payments:** For a client using a VSaaS platform, the primary goal is to acquire more customers. Thus, the client may rely on the platform to secure initial customer payments, while recurring payments are directly processed by the client through its PSP of choice.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-06 at 2.31.30 AM.png" alt=""><figcaption></figcaption></figure>

**End-to-End Payments:** In cases where a client uses a Vertical SaaS platform to design new subscriptions and distribute them to customers, payments need to be more tightly integrated with the platform. As a result, the client may expect the platform to handle both customer acquisition and renewal payments through the PSP of choice on the client’s behalf.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-11-06 at 2.31.56 AM.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="../exporting-payments-data.md" %}
[exporting-payments-data.md](../exporting-payments-data.md)
{% endcontent-ref %}
