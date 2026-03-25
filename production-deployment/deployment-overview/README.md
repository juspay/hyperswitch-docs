---
icon: sign-posts-wrench
description: Implement security controls encryption and compliance measures to protect sensitive payment data and meet PCI DSS requirements
---

# Deployment Overview

For an Enterprise-grade production installation of Hyperswitch the recommended approach is to deploy Kubernetes on a managed cloud - Google Cloud Platform, Amazon Web Services or Microsoft Azure.

The following is the high-level flow for a Hyperswitch deployment:&#x20;

<figure><img src="../../.gitbook/assets/Deploy Hyperswitch-6.jpg" alt=""><figcaption></figcaption></figure>

The critical considerations to be made for the deployment are as follows:

- Choosing the deployment topology (Single-region, Multi-region, Active-Passive)
- Choosing the Hyperswitch environments to deploy (Test, Sandbox, Production)
- Kubernetes Cluster and Namespace separation strategy
- Helm Chart customization
- Scale and Upgrade strategy
- Ensuring security and compliance
- Setting up the monitoring stack

The recommendations for each of these considerations can be found in the subsequent sections.&#x20;
