---
description: The complete guide to setting up & managing your own payments switch.
cover: ../.gitbook/assets/Frame.png
coverY: -1.5791666666666666
layout:
  cover:
    visible: true
    size: full
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

# 🛠️ Overview

{% hint style="info" %}
After going through this guide, you should be able to:

* Run Hyperswitch locally - Set up Hyperswitch on your local system & make a test payment
* Deploy Hyperswitch on AWS - Create a production-ready setup on cloud & make a test payment
* Go live - Go live with you own payments setup
{% endhint %}

This guide is designed for people with some coding experience, who want to learn about Payments Switches and deploy Hyperswitch in their preferred mode. You will then be able to make payments via Hyperswitch and try its different components.

## **Running Payments yourself**

Hyperswitch allows you to deploy and run your own payments stack. We offer support in terms answering queries, maintenance and feature enhancements.

Within 5 minutes, you should be able to deploy Hyperswitch in your local machine and can run payments through any payment provider of your choice. You'll be equipped to run payments for your own pet project, or a D2C website, or as an internship project, or just to learn Payments

### Learning Resources

In case you are completely new to payments - You can comeback to setup after reading the [Payment 101 Blog](https://github.com/juspay/hyperswitch/wiki/Payments-101-for-a-Developer), For more learning resources visit [Hyperswitch Blogs.](https://hyperswitch.io/blogs)

## Components and Setup methods -&#x20;

Hyperswitch has three components -&#x20;

* **App Server -** The core payments engine responsible for managing payment flows, payment unification and smart routing &#x20;
* **Web Client (SDK) -** An inclusive, consistent and blended payment experience optimized for the best payment conversions
* **Control center -** A dashboard for payment analytics and operations, managing payment processors or payment methods and configuring payment routing rules.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Run Hyperswitch locally</strong></td><td>Run the app server, control center and web client locally on your machine</td><td></td><td><a href="local-setup-guide/">local-setup-guide</a></td><td><a href="../.gitbook/assets/Payment flow (2) (1).png">Payment flow (2) (1).png</a></td></tr><tr><td><strong>Deploy Hyperswitch on AWS</strong></td><td>Deploy Hyperswitch on AWS either as an independent stack or as individual components</td><td></td><td><a href="deploy-hyperswitch-on-aws/">deploy-hyperswitch-on-aws</a></td><td><a href="../.gitbook/assets/aws.jpg">aws.jpg</a></td></tr><tr><td><strong>Deploy Hyperswitch on Kubernetes</strong></td><td>Install Hyperswitch on your K8s setup using our Helm charts</td><td></td><td><a href="deploy-on-kubernetes-using-helm.md">deploy-on-kubernetes-using-helm.md</a></td><td><a href="../.gitbook/assets/images.png">images.png</a></td></tr></tbody></table>
