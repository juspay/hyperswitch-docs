---
description: 'Hyperswitch: Open-Source Payments Platform by Juspay'
icon: earth-asia
cover: .gitbook/assets/Hero visual V6 (2).png
coverY: 0
---

# Overview

[Hyperswitch](https://hyperswitch.io/) is an open-source payments platform from [Juspay](https://juspay.io/us), designed to simplify global payments for digital businesses. Juspay has been a global leader offering payment infrastructure solution for banks and merchants for 12+ years, processing over [300 Mn+ daily transactions](https://juspay.io/newsroom/juspay-secures-usd50-million-investment-from-westbridge-capital) and an annualized total payment value of $1 Tn+

### We offer two distinct solutions

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Payments Suite</strong></mark></td><td>An end-to-end orchestration layer that unifies payments across providers, networks, and channels. It enables seamless checkout, dynamic routing, retries and redundancy for reliability.</td><td><strong>Optimize payments at scale without adding complexity to your infrastructure.</strong></td><td></td><td><a href="about-hyperswitch/payment-suite/">payment-suite</a></td></tr><tr><td><mark style="color:blue;"><strong>Payment Modules</strong></mark></td><td>A flexible, modular approach to integrate only the payment capabilities you need. Choose from intelligent routing, vault, reconciliation, cost observability, smart retries, and APM widgets.</td><td><strong>Enhance performance without overhauling your existing payment stack.</strong></td><td></td><td><a href="about-hyperswitch/payments-modules/">payments-modules</a></td></tr></tbody></table>

### Enterprise Grade Open Payments Infrastructure

{% embed url="https://youtu.be/p6vqGHsoc0s?si=b6imHBVzZAcCQ2WB" %}

At Juspay, we believe that payments infrastructure should be transparent, adaptable, and built for merchant control—not vendor lock-in. That’s why we made the bold decision to take our Payment Orchestrator open source.

Enterprise merchants operate in a world where payment agility is a competitive advantage. Traditional closed-loop platforms dictate their own rules, pricing, and pace of innovation. Based on our 12-years of experience building and scaling global payment systems, we decided to take a different approach—giving merchants the power to customize, optimize, and scale payments to fit their unique business needs.

Guided by the learnings from our enterprise go-lives, we have been working on unbundling a range of stand-alone solutions from our broader technology stack to make them more accessible to merchants looking to expand their in-house system engineering capability. These stand-alone solutions range from services for [intelligent / dynamic payment routing](https://github.com/juspay/decision-engine), [payment methods vaulting](https://github.com/juspay/hyperswitch-card-vault), [cost observability](https://hyperswitch.io/cost-observability), [PSP-agnostic authentication](explore-hyperswitch/workflows/3ds-decision-manager/), and an [APMs widget ](explore-hyperswitch/payment-experience/payment/enable-alternate-payment-method-widgets/)that can be embedded anywhere.

<figure><img src=".gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

### Technical Foundation: Open System Architecture with Enterprise-Scale

Hyperswitch's technical architecture combines open source innovation with enterprise-grade reliability, built to power modern payment operations.

#### 1. Open-Source Transparency & Extensibility

* Complete Transparency & Confidence: Full visibility into payment orchestration with no black boxes, enabling informed decision-making and customization. Hyperswitch is maintained publicly on [GitHub](https://github.com/juspay/hyperswitch)
* [Open Roadmap & Innovation](about-hyperswitch/roadmap/): Collaborative development approach that allows merchants to influence and contribute to the platform's evolution
* Speed to Market: Accelerate implementation and changes by building consensus faster through transparent architecture

#### 2. Enterprise-Grade Reliability & Security Model

* Built on battle-tested systems by Juspay's 1000+ engineers, the same team that powers 300M+ transactions daily for [global enterprises](https://juspay.io/customer-stories) like Amazon, Agoda, Zurich and many more.
* [Comprehensive security framework](explore-hyperswitch/security-and-compliance/) including PCI compliance, tokenization, and security certifications
* Proven reliability at scale, designed for high-performance payment processing

### [Core System Architecture Principles](https://hyperswitch.io/blog/building-hyperswitch-the-world-s-first-open-source-payments-platform)

<table data-view="cards"><thead><tr><th align="center"></th><th></th></tr></thead><tbody><tr><td align="center"><strong>Reliability</strong></td><td><ul><li>Graceful degradation - Critical path stays intact; non-core flows are optional</li><li>Recover failed transactions through intelligent retry logic</li><li>Strongly typed Rust ensures safety at compile time</li><li>Staggered releases</li></ul></td></tr><tr><td align="center"><strong>Scalability</strong></td><td><ul><li>Horizontal scalable architecture</li><li>Supports peak loads up to ~10K TPS</li><li>Connection pooling</li><li>First class support for K-V mode</li></ul></td></tr><tr><td align="center"><a href="learn-more/hyperswitch-architecture/a-payments-switch-with-virtually-zero-overhead.md"><strong>Performance</strong></a></td><td><ul><li><p>Cache where-ever possible</p><ul><li>Configurations</li><li>Master data </li><li>Multi-level caching </li></ul></li></ul></td></tr><tr><td align="center"><strong>Modularity</strong></td><td><ul><li>Works with an <a href="explore-hyperswitch/workflows/vault/">external or an in-house Vault</a> or Tokenization service</li><li>Offers <a href="about-hyperswitch/payments-modules/">standalone products</a></li><li>Integrate with connectors <a href="explore-hyperswitch/connectors/">beyond Payment Service Providers</a></li></ul></td></tr><tr><td align="center"><a href="explore-hyperswitch/security-and-compliance/security.md"><strong>Security &#x26; Compliance</strong></a></td><td><ul><li>Hyperswitch suite is PCI SSS validated</li><li>Mask at Source</li><li>Isolation and Encryption</li></ul></td></tr><tr><td align="center"><strong>Observability</strong></td><td><ul><li>Business &#x26; Tech metrics</li><li>Point debugging</li><li>Application / Infrastructure alerts with custom pipelines</li><li>Remote monitoring for self-hosted merchants</li></ul></td></tr><tr><td align="center"><strong>Quality &#x26; Maintenance</strong> </td><td><ul><li>Strict PR checks</li><li>Automated E2E &#x26; Regression testing </li><li>Clear documentation with <a href="https://github.com/juspay/hyperswitch/releases">release notes</a></li></ul></td></tr></tbody></table>

**Get ready! We welcome you to the future of digital payments!**
