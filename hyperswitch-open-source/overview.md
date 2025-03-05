---
icon: screwdriver-wrench
cover: ../.gitbook/assets/Hero visual V6 (2).png
coverY: 0
layout:
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Overview

At Juspay, we believe payment infrastructure should be transparent, adaptable, and under merchants' control—not confined by vendor restrictions. That's why we've made the bold move to open-source our Payment Orchestrator.​

This modular, composable platform allows you to deploy on-premise for full access or select only the components you need.&#x20;

To run Hyperswitch locally, follow our Docker setup guide. Alternatively, explore our cloud deployment guides for additional options. ​

## Local Setup

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Unified Local Setup using Docker</strong></mark></td><td>Simplified local setup of all components, using a single command with the help of docker.</td><td></td><td><a href="local-setup-guide/unified-local-setup-using-docker.md">unified-local-setup-using-docker.md</a></td><td><a href="../.gitbook/assets/HS x Docker.png">HS x Docker.png</a></td></tr><tr><td><mark style="color:blue;"><strong>Local Setup of Individual Components</strong></mark></td><td>Customised local setup to fulfil different use-cases.</td><td></td><td><a href="local-setup-guide/local-setup-using-individual-components/">local-setup-using-individual-components</a></td><td><a href="../.gitbook/assets/HS + Components (3).png">HS + Components (3).png</a></td></tr></tbody></table>

## Cloud Setup

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Deploy Hyperswitch on AWS</strong></mark></td><td>Deploy Hyperswitch on AWS either as an independent stack or as individual components.</td><td></td><td><a href="deploy-hyperswitch-on-aws/">deploy-hyperswitch-on-aws</a></td><td><a href="../.gitbook/assets/HS x AWS.png">HS x AWS.png</a></td></tr><tr><td><mark style="color:blue;"><strong>Deploy Hyperswitch on Kubernetes</strong></mark></td><td>Install Hyperswitch on GCP or Azure using our Helm charts.</td><td></td><td><a href="deploy-on-kubernetes-using-helm/">deploy-on-kubernetes-using-helm</a></td><td><a href="../.gitbook/assets/HS x Kubernates.png">HS x Kubernates.png</a></td></tr></tbody></table>

{% hint style="success" %}
Want to try without deploying? Use our dashboard on [sandbox](https://app.hyperswitch.io/).
{% endhint %}

### Learning Resources

In case you are completely new to payments - You can comeback to setup after reading the [Payment 101 Blog](https://github.com/juspay/hyperswitch/wiki/Payments-101-for-a-Developer), For more learning resources visit [Hyperswitch Blogs.](https://hyperswitch.io/blogs)
