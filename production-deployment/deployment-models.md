---
description: Set up automated reconciliation to match transactions across PSPs banks and internal systems to identify and resolve discrepancies quickly
icon: flux-capacitor
---
# Deployment Models

## Supported Deployment Models

The Juspay Hyperswitch platform supports multiple deployment models depending on the level of infrastructure control, compliance responsibility, and operational ownership required.

### Overview

| Model                                  | Best For                                                                                |
| -------------------------------------- | --------------------------------------------------------------------------------------- |
| **Self-Deployed (Enterprise Support)** | Enterprises that require full control over infrastructure and deployment                |
| **Hosted Offering (SaaS)**             | Organizations that want a fully managed payments platform                               |
| **Point Solutions**                    | Teams that only need specific capabilities such as reconciliation or cost observability |

### Self-Deployed (Enterprise Support)

> **Recommended for:** Enterprises requiring full infrastructure ownership and deployment flexibility.

#### Model

Merchant deploys and runs the platform within their own infrastructure environment, either **on-premise** or in a **cloud provider of their choice**.

#### Scope of Services

- Expert consultation from Juspay for deployment
- Assistance with production readiness
- Support during certification and go-live

#### PCI Compliance

Merchants can choose between:

- **Self-certifying PCI compliance**
- Using **Juspay’s hosted PCI / Tokenization service**

#### Reliability & Scalability

- Infrastructure owned and managed by the merchant
- Merchant responsible for scaling, monitoring, and reliability

### Hosted Offering (SaaS)

> **Recommended for:** Teams that want a fully managed platform with minimal operational overhead.

#### Model

Juspay operates the platform and exposes its capabilities through **hosted APIs and SDKs**.

#### Scope of Services

- Fully managed infrastructure
- Hosted APIs and SDK integrations
- Continuous platform maintenance and upgrades

#### PCI Compliance

- PCI compliance handled entirely by Juspay
- Out-of-the-box compliance for merchants

#### Reliability & Scalability

- **Guaranteed SLAs**
- **99.999% uptime**
- **Up to 3000 TPS processing capacity**

### Point Solutions

> **Recommended for:** Organizations that need specific tools without deploying the full platform.

#### Model

Fully managed service provided by Juspay for targeted operational capabilities.

#### Scope of Services

Self-serve dashboards and tooling for:

- **Reconciliation**
- **Cost observability**

#### PCI Compliance

- No PCI compliance requirements

#### Reliability & Scalability

- Juspay provides guaranteed service SLAs

### Feature Comparison

| Feature                       | Self-Deployed                   | Hosted Offering                 | Point Solutions     |
| ----------------------------- | ------------------------------- | ------------------------------- | ------------------- |
| Infrastructure Ownership      | Merchant                        | Juspay                          | Juspay              |
| Platform Operations           | Merchant                        | Juspay                          | Juspay              |
| PCI Compliance Responsibility | Merchant or Juspay Tokenization | Juspay                          | Not Required        |
| Scaling & Performance         | Merchant                        | Juspay                          | Juspay              |
| Typical Use Case              | Full platform deployment        | Managed payments infrastructure | Operational tooling |

***

This Production Deployment guide is to help merchants looking to self-deploy Hyperswitch in an enterprise-grade environment.&#x20;

It is designed to provide you detailed guidance on deploying and scaling Hyperswitch in a secure and compliant manner.&#x20;
