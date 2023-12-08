---
description: Deploy each Hyperswitch component individually
---

# Component-wise Deployment

{% hint style="info" %}
This section outlines the steps to deploy each component of Hyperswitch individually on AWS
{% endhint %}

For setting up each component in your preferred format, utilize only the essential requirements as outlined in the individual setup guides for each component:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Deploy app server</strong></td><td>The core payments engine responsible for managing payment flows, payment unification and smart routing</td><td></td><td><a href="../../../.gitbook/assets/Payment flow.png">Payment flow.png</a></td><td><a href="deploy-app-server.md">deploy-app-server.md</a></td></tr><tr><td><strong>Deploy control center</strong></td><td>A dashboard for payment analytics and operations, managing payment processors or payment methods and configuring payment routing rules</td><td></td><td><a href="../../../.gitbook/assets/Payment flow (1).png">Payment flow (1).png</a></td><td><a href="deploy-control-center.md">deploy-control-center.md</a></td></tr><tr><td><strong>Deploy web client</strong></td><td>An inclusive, consistent and blended payment experience optimized for the best payment conversions</td><td></td><td><a href="../../../.gitbook/assets/Payment flow (2).png">Payment flow (2).png</a></td><td><a href="../deploy-web-client/">deploy-web-client</a></td></tr><tr><td><strong>Deploy card vault</strong></td><td>A secure store for sensitive payment method information ready for PCI compliance</td><td></td><td><a href="../../../.gitbook/assets/24.jpg">24.jpg</a></td><td><a href="deploy-card-vault.md">deploy-card-vault.md</a></td></tr></tbody></table>
