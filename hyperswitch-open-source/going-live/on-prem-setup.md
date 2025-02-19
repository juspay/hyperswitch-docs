---
description: >-
  Follow the below guidelines for going live with Hyperswitch on K8s in your own
  data center
icon: drone
---

# On-Prem Setup

{% hint style="info" %}
In this chapter, you will learn about  the various best practices to be followed while deploying Hyperswitch on your own on-premise k8s cluster. This will help secure your system and meet the PCI compliance standards
{% endhint %}

As an open-source payment orchestrator, Hyperswitch offers a flexible and scalable solution for managing payment transactions. Whether you are an organization handling payment transactions, a payment service provider or a financial institution, this guide will assist you in securely implementing Hyperswitch within your infrastructure while meeting PCI compliance standards.&#x20;

Let's get started on building a robust and secure payment environment with Hyperswitch and Helm.

1. **Hardened Machine Images**
   * Utilize hardened machine images for the nodes in the Kubernetes cluster, ensuring they include security tools such as an SIEM tool, anti-malware, and threat/intrusion detection and prevention system.
2. **Restricted Internet Access**
   * Configure the Kubernetes cluster to have no direct access to the internet to reduce attack surface.
   * Ensure that necessary updates and patches are applied through controlled channels.
3. **Private Docker Registry**
   * Host docker images used by the [Helm chart](https://github.com/juspay/hyperswitch-helm/tree/main/charts/incubator/hyperswitch-stack#readme) in a private registry within a private cloud environment.
   * This ensures control over image distribution and enhances security by limiting exposure.
4. **Outgoing Proxy**
   * Set up an outgoing proxy outside the Kubernetes cluster for all external communication originating from the Hyperswitch application.
   * Direct all outbound traffic through this proxy for monitoring and control purposes.
5. **Incoming Traffic Management**
   * Route incoming traffic to the Hyperswitch-server through an incoming proxy.
   * This proxy should handle traffic filtering(WAF), rate limiting, request validation, and integration with DDoS protection services before traffic reaches the Kubernetes cluster.
6. **IP Whitelisting**
   * Implement IP whitelisting on the Kubernetes cluster to restrict access to a predefined set of IPs, such as corporate VPN IPs or other trusted sources for accessing the cluster.
   * Note that this whitelisting is intended solely for managing the Kubernetes cluster by developers and does not apply to whitelisting API traffic.
7. **Separate Node group for Card vault**
   * Host the locker-service which is handling sensitive data in separate node group.
   * Ensure that this node group follows appropriate security measures and access controls.
8. **Separate Database for Card vault**
   * If you are installing the database for card vault inside k8s cluster, add it in the same node-group as the locker-service.
   * Ensure that database access is restricted and encrypted to maintain data integrity and security.
   * Implement encryption mechanisms for data at rest within your Kubernetes (K8s) cluster by leveraging encrypted storage solutions such as Kubernetes Secrets or encrypted persistent volumes (PVs). Encrypting sensitive data helps protect against unauthorized access to stored information, ensuring compliance with security standards like PCI DSS.

By following these steps, you can establish a secure and PCI-compliant environment for hosting Hyperswitch services on an on-premise Kubernetes cluster. Regular audits and updates should be conducted to maintain security posture and compliance.

{% hint style="info" %}
Since Hyperswitch handles sensitive card data, it is recommended to keep the Hyperswitch stack segregated from your other services to reduce the scope of PCI compliance thereby simplifying the process
{% endhint %}

\
