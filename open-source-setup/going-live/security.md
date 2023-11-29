---
description: Better safe than sorry!
---

# 🔐 Security

{% hint style="info" %}
In this chapter, you will learn how to secure your application. Let's break down the setup into its constituents and understand how they can be secured
{% endhint %}

***

## **Cloud**&#x20;

* The Cloud Provider that you are planning to use, should provide guarantees around data handling and how security is implemented for the hardware machine in their data centers.
* For business requirements, the cloud provider must facilitate ways to perform compliance checks on infrastructure.
* IAM must be used throughout the application to make sure that each component of application must only have access to actions that it’s supposed to perform. Limiting policies per IAM role would benefit the application. To allow very specific policies for specific application residing in Kubernetes using service account instead of providing the policy to all the nodes in the Kubernetes is preferred.

***

## **Networking**

* The infrastructure that is used internally must not be exposed to the internet directly. Measures should be taken to add a DMZ layer on-top of the application infrastructure.
* Communication between critical services must be end-to-end encrypted with TLS. For infrastructure components that resides in Kubernetes this can be achieved using service mesh (Istio / Linkerd).
* Adding separate subnets for different layers of the application will provide modularity around how the networking will take place between components.
* Communications with managed components must be explicitly defined around the use-cases. It should not be exposed by default.
* The application and storage layer must reside in a private subnet with no connection to the internet. Any traffic inbound/outbound from outside must pass though proxies to provide more control on data that is flowing through the application
* Firewalls must be used to prevent any unwanted/malicious traffic from entering the application network.

***

## **Storage**&#x20;

* The storage layer must be isolated from other infrastructure, preventing any direct access from the internet.
* The snapshots of the database must be stored securely.

***

## **Application**&#x20;

* Using secure passwords for internal applications. Using Key Management Utilities (similar to KMS).
* The application container image must be verified before running and must be managed securely.
* Sensitive data that is to be passed to the application must be managed in secrets and the access should be restricted based on Roles.
* The application data that is sensitive and contains PII (Personally Identifiable Information) is to be encrypted and multiple level encryption is to be maintained to protect details in merchant confidentiality and customer data.
* Sensitive data, i.e. payment related data that is being passed through the system must be protected and should not leave any trace behind once it exits the system.

{% hint style="danger" %}
Security considerations for the web client and the dashboard will be updated soon!
{% endhint %}
