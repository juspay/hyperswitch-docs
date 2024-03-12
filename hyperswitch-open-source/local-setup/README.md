---
description: >-
  This guide will walk you through the process of setting up and running the app
  server, web client, and control center on your local machine.
---

# 💻 Local setup

{% hint style="info" %}
This section will walk you through the process of setting up and running Hyperswitch on your local machine
{% endhint %}

Hyperswitch has 3 major components, the app server, the control center and the web client. You can refer to the following documents to run all three of them locally to make your first test payment

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Run App Server</strong></td><td>The core payments engine responsible for managing payment flows, payment unification and smart routing</td><td></td><td><a href="../../.gitbook/assets/Payment flow.png">Payment flow.png</a></td><td><a href="run-app-server.md">run-app-server.md</a></td></tr><tr><td><strong>Run Web Client</strong></td><td>An inclusive, consistent and blended payment experience optimized for the best payment conversions</td><td></td><td><a href="../../.gitbook/assets/Payment flow (2).png">Payment flow (2).png</a></td><td><a href="run-web-client.md">run-web-client.md</a></td></tr><tr><td><strong>Run Control Center</strong></td><td>A dashboard for payment analytics and operations, managing payment processors or payment methods and configuring payment routing rules</td><td></td><td><a href="../../.gitbook/assets/Payment flow (1).png">Payment flow (1).png</a></td><td><a href="run-control-center.md">run-control-center.md</a></td></tr></tbody></table>

Following are the system requirements to run Hyperswitch locally. To quickly get started with running Hyperswitch, we recommend using `docker-compose`.

| Parameters | Minimum |
| ---------- | ------- |
| CPU        | 2 cores |
| Memory     | 2 GB    |
