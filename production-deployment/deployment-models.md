---
icon: flux-capacitor
---

# Deployment Models

## TL;DR

Juspay hyperswitch offers three deployment models: **Self-Deployed** (you manage infrastructure), **Hosted SaaS** (we manage everything), and **Point Solutions** (specific tools only). Choose based on your compliance needs, team capabilities, and time-to-market requirements. Self-Deployed gives maximum control but requires in-house expertise; Hosted gets you live fastest with zero ops overhead; Point Solutions fills gaps in existing payment stacks.

---

## What Deployment Models Does Hyperswitch Support?

The Juspay hyperswitch platform supports multiple deployment models depending on the level of infrastructure control, compliance responsibility, and operational ownership required.

| Model | Best For |
|-------|----------|
| Self-Deployed (Enterprise Support) | Enterprises that require full control over infrastructure and deployment |
| Hosted Offering (SaaS) | Organisations that want a fully managed payments platform |
| Point Solutions | Teams that only need specific capabilities such as reconciliation or cost observability |

---

## What Is the Self-Deployed Model?

**Recommended for:** Enterprises requiring full infrastructure ownership and deployment flexibility.

### How Does It Work?

Merchant deploys and runs the platform within their own infrastructure environment, either on-premise or in a cloud provider of their choice.

### What Services Are Included?

- Expert consultation from Juspay for deployment
- Assistance with production readiness
- Support during certification and go-live

### How Is PCI Compliance Handled?

Merchants can choose between:
- Self-certifying **PCI DSS** (Payment Card Industry Data Security Standard) compliance
- Using Juspay's hosted PCI / Tokenization service

### Who Manages Reliability & Scalability?

- Infrastructure owned and managed by the merchant
- Merchant responsible for scaling, monitoring, and reliability

---

## What Is the Hosted Offering (SaaS)?

**Recommended for:** Teams that want a fully managed platform with minimal operational overhead.

### How Does It Work?

Juspay operates the platform and exposes its capabilities through hosted **APIs** (Application Programming Interfaces) and **SDKs** (Software Development Kits).

### What Services Are Included?

- Fully managed infrastructure
- Hosted APIs and SDK integrations
- Continuous platform maintenance and upgrades

### How Is PCI Compliance Handled?

- **PCI DSS** compliance handled entirely by Juspay
- Out-of-the-box compliance for merchants

### What About Reliability & Scalability?

- Guaranteed **SLAs** (Service Level Agreements)
- 99.999% uptime
- Up to 3000 **TPS** (Transactions Per Second) processing capacity

---

## What Are Point Solutions?

**Recommended for:** Organisations that need specific tools without deploying the full platform.

### How Does It Work?

Fully managed service provided by Juspay for targeted operational capabilities.

### What Services Are Included?

Self-serve dashboards and tooling for:
- Reconciliation
- Cost observability

### How Is PCI Compliance Handled?

- No **PCI DSS** compliance requirements

### What About Reliability & Scalability?

- Juspay provides guaranteed service **SLAs**

---

## How Do the Models Compare?

| Feature | Self-Deployed | Hosted Offering | Point Solutions |
|---------|---------------|-----------------|-----------------|
| Infrastructure Ownership | Merchant | Juspay | Juspay |
| Platform Operations | Merchant | Juspay | Juspay |
| PCI Compliance Responsibility | Merchant or Juspay Tokenization | Juspay | Not Required |
| Scaling & Performance | Merchant | Juspay | Juspay |
| Typical Use Case | Full platform deployment | Managed payments infrastructure | Operational tooling |

---

## Which Deployment Model Should I Choose?

### Decision Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│                    START: Assess Your Needs                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│     Do you need full payment orchestration capabilities?         │
└─────────────────────────────────────────────────────────────────┘
                    │                         │
                   NO                        YES
                    │                         │
                    ▼                         ▼
┌─────────────────────────┐      ┌─────────────────────────────────┐
│    POINT SOLUTIONS      │      │ Do you have dedicated DevOps/   │
│  (Reconciliation, Cost  │      │ SRE (Site Reliability Engineer) │
│   Observability tools)  │      │ teams and infrastructure        │
│                         │      │ expertise?                      │
└─────────────────────────┘      └─────────────────────────────────┘
                                              │
                                    NO        │        YES
                                              │
                                              ▼
                              ┌─────────────────────────────────┐
                              │ Do you require complete data    │
                              │ sovereignty or custom infra     │
                              │ configurations?                 │
                              └─────────────────────────────────┘
                                            │
                                  NO        │        YES
                                            │
                                            ▼
                              ┌─────────────────────────────────┐
                              │      SELF-DEPLOYED              │
                              │   (Maximum control, you manage  │
                              │    infrastructure & PCI)        │
                              └─────────────────────────────────┘
                                            │
                                            ▼
                              ┌─────────────────────────────────┐
                              │       HOSTED (SaaS)             │
                              │   (Fastest time-to-market,      │
                              │    Juspay manages everything)   │
                              └─────────────────────────────────┘
```

### Quick Guidance

**Choose Self-Deployed if:**
- You require complete data sovereignty
- You have dedicated DevOps/**SRE** teams
- You need custom infrastructure configurations
- You want to self-certify **PCI DSS** compliance
- You prefer **OSS** (Open Source Software) deployment flexibility

**Choose Hosted (SaaS) if:**
- You want to go live quickly
- You don't have dedicated infrastructure teams
- You prefer operational simplicity
- You want guaranteed **SLAs**

**Choose Point Solutions if:**
- You already have a payment processor
- You need specific tools (reconciliation, analytics)
- You don't need full payment orchestration

---

## What Does the Architecture Look Like?

### High-Level Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MERCHANT APPLICATION                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Your Web/Mobile App  ←───  Juspay hyperswitch SDK (if needed)      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DEPLOYMENT MODEL LAYER                             │
│  ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐ │
│  │   SELF-DEPLOYED     │  │   HOSTED (SaaS)     │  │   POINT SOLUTIONS   │ │
│  │                     │  │                     │  │                     │ │
│  │  ┌───────────────┐  │  │  ┌───────────────┐  │  │  ┌───────────────┐  │ │
│  │  │ Your Cloud    │  │  │  │ Juspay Cloud  │  │  │  │ Juspay Cloud  │  │ │
│  │  │ (AWS/GCP/Azure│  │  │  │ Infrastructure│  │  │  │ Infrastructure│  │ │
│  │  │  or On-Prem)  │  │  │  │               │  │  │  │               │  │ │
│  │  └───────────────┘  │  │  │ • API Gateway │  │  │  │ • Dashboard   │  │ │
│  │         │           │  │  │ • App Servers │  │  │  │ • Analytics   │  │ │
│  │  ┌──────▼──────┐    │  │  │ • Databases   │  │  │  │ • Reports     │  │ │
│  │  │ Hyperswitch │    │  │  │ • Cache Layer │  │  │  └───────────────┘  │ │
│  │  │  Platform   │    │  │  │               │  │  │                     │ │
│  │  │   (Docker/  │    │  │  │ PCI Compliant │  │  │  No PCI Required    │ │
│  │  │   K8s/VMs)  │    │  │  │ 99.999% SLA   │  │  │                     │ │
│  │  └─────────────┘    │  │  │ Up to 3000 TPS│  │  └─────────────────────┘ │
│  │                     │  │  └───────────────┘  │                          │
│  │ You manage:         │  │                     │                          │
│  │ • Infrastructure    │  │ Juspay manages:   │                          │
│  │ • Scaling           │  │ • Everything      │                          │
│  │ • PCI (optional)    │  │                   │                          │
│  └─────────────────────┘  └─────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PAYMENT CONNECTORS                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │
│  │  Stripe  │ │  Adyen   │ │  PayPal  │ │  Braintree│ │   50+ Global     │  │
│  │          │ │          │ │          │ │           │ │   Processors     │  │
│  └──────────┘ └──────────┘ └──────────┘ └───────────┘ └──────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Can I Migrate Between Models?

Yes — you can migrate between deployment models as your needs evolve. However, **migration complexity varies** depending on the direction:

| Migration Path | Complexity | Key Considerations |
|----------------|------------|-------------------|
| Hosted → Self-Deployed | **High** | Data export, infrastructure setup, PCI certification, API endpoint changes, cutover planning |
| Self-Deployed → Hosted | **Medium** | Data migration, configuration transfer, testing phase, DNS cutover |
| Any Model → Point Solutions | **Low** | API integration only, no data migration needed |
| Point Solutions → Full Platform | **Medium** | Full platform onboarding, may require PCI compliance |

### Important Migration Disclosures

1. **Data Migration**: Transaction history and configuration data may require manual export/import
2. **PCI Compliance**: Moving to Self-Deployed requires new PCI DSS certification (typically 3-6 months)
3. **API Changes**: Different models may have different API endpoints requiring code changes
4. **Downtime**: Planned maintenance windows may be required for cutover
5. **Support Required**: Contact Juspay support for migration assistance — this is not self-service

**Recommended Approach**: Start with Hosted for quick launch, then plan a phased migration to Self-Deployed if greater control is needed.

---

## What Are My Next Steps?

- [Deploy Hyperswitch on AWS](hyperswitch-open-source/deploy-hyperswitch-on-aws/)
- [Deploy Hyperswitch on GCP](hyperswitch-open-source/deploy-on-kubernetes-using-helm/deploy-on-gcp-using-helm-charts.md)
- [Deploy Hyperswitch on Azure](hyperswitch-open-source/deploy-on-kubernetes-using-helm/deploy-on-azure-using-helm-charts.md)
- [Get started with Hosted offering](https://app.hyperswitch.io/)

---

## Glossary

| Acronym | Definition |
|---------|------------|
| **API** | Application Programming Interface — a set of protocols for building software applications |
| **OSS** | Open Source Software — software with source code that anyone can inspect, modify, and enhance |
| **PCI DSS** | Payment Card Industry Data Security Standard — security standards for handling card payments |
| **SDK** | Software Development Kit — tools and libraries for building applications |
| **SLA** | Service Level Agreement — guaranteed uptime and performance commitments |
| **SRE** | Site Reliability Engineer — role focused on maintaining reliable systems at scale |
| **TPS** | Transactions Per Second — measure of processing capacity |
