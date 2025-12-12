---
icon: compass
cover: .gitbook/assets/Hero visual V6 (2).png
coverY: 0
---

# Exploration Guide

Hyperswitch gives you full control over your payments infrastructure without the complexity of building from scratch. Whether you're validating a prototype or scaling globally, you can get started in minutes.

This guide helps you:

* Quickly install Hyperswitch with minimal setup
* Try your first hello world by making a payment
* Learn about Hyperswitch’s modular architecture
* Improve and streamline your checkout experience
* See how Hyperswitch embeds security, reliability, and scalability into its core architecture

***

### Try Hyperswitch Quickly

#### Get a Sandbox Ready in under 10 Minutes

Spin up a working integration with minimal effort. Choose the path that fits your needs:

<details>

<summary><strong>Cloud Sandbox (Hyperswitch Hosted Test Environment)</strong></summary>

[Try Hyperswitch →](hyperswitch-open-source/account-setup/using-hyperswitch-control-center.md)\
Launch a ready-to-use Control Center test environment. No setup required, just log in and run your first transaction.

</details>

<details>

<summary><strong>Local Deployment (Docker)</strong></summary>

[Set up Docker Locally →](hyperswitch-open-source/overview/unified-local-setup-using-docker.md)\
Perfect for developers who want local control and flexibility. You'll launch a ready-to-use Control Center environment.

</details>

<details>

<summary><strong>API-first Integration</strong></summary>

[API Reference →](hyperswitch-open-source/overview/local-setup-using-individual-components/backend/try-out-apis.md)\
[Use Postman Collection →](hyperswitch-open-source/account-setup/using-postman.md)\
Build a custom backend integration from scratch.

> ⚠️ To authenticate API requests, you’ll need a username and password from either:\
> • the [Cloud Sandbox](https://app.hyperswitch.io)\
> • or your [Docker setup](https://docs.hyperswitch.io/hyperswitch-open-source/readme-1/unified-local-setup-using-docker)

</details>

<details>

<summary><strong>Launch a Scalable Hyperswitch Instance on AWS</strong></summary>

[AWS Deployment →](hyperswitch-open-source/deploy-hyperswitch-on-aws/)

Launch Hyperswitch on your own AWS infrastructure with our step-by-step deployment guide. Ideal for teams looking for flexibility, control, and production-ready scalability.

</details>

<details>

<summary><strong>Scalable, Self-Hosted Deployment | Helm Charts for GCP &#x26; Azure</strong></summary>

[Deploy on GCP or Azure →](hyperswitch-open-source/deploy-on-kubernetes-using-helm/deploy-on-gcp-using-helm-charts.md)

Install Hyperswitch on your cloud infrastructure using Helm charts for Kubernetes. This method gives you full control over your environment and is ideal for teams deploying on GCP, Azure, or any Kubernetes-compatible platform.

</details>

### Your first payment

See Hyperswitch in action by sending your first test transaction via the cloud sandbox, local Docker setup or directly via API.

<details>

<summary><strong>Test a payment | Your First Hello World with Hyperswitch</strong></summary>

[Control Center](hyperswitch-open-source/account-setup/test-a-payment.md) | Accessible through cloud sandbox or Docker

[API ](hyperswitch-open-source/account-setup/using-postman.md)| Accessible through the Postman Collection

[Learn how the SDK, control center and backend work together](hyperswitch-open-source/overview/local-setup-using-individual-components/)

</details>

### Hyperswitch Capabilities Overview

Power only what you need with Hyperswitch’s modular architecture. You can pick and integrate the components that solve your specific payment challenges without unnecessary overhead.

<details>

<summary><strong>Power Only What You Need with Hyperswitch’s Modular Architecture</strong></summary>

[Intelligent Routing →](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/intelligent-routing)

Dynamically route transactions based on geography, cost, or success rate to reduce failures and fees.

[Revenue Recovery →](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/revenue-recovery)

Recover failed payments using machine learning–based retry logic that adapts to card network behavior.

[Vault (Tokenization) →](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault)

Securely store and reuse payment credentials across providers — ideal for subscriptions and saved cards.

[Cost Observability →](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/ai-powered-cost-observability)

Gain real-time visibility into your processing costs and optimize spend across processors.

[Reconciliation →](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/reconciliation)

Automatically match transaction data across banks, PSPs, and internal systems to reduce manual effort.

[3DS Decision Manager →](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/3ds-decision-manager)

Apply 3DS only when necessary, minimizing friction while keeping fraud under control.

[Payment Orchestration →](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration)

Automate disbursements to vendors or sellers with rule-based routing logic.

</details>

### Explore Core Payment Flows and Capabilities

Power only what you need with Hyperswitch’s modular architecture. Integrate just the components that solve your payment challenges, without the extra overhead.

<details>

<summary><strong>Build Smarter Payment Flows</strong></summary>

[Payment Orchestration →](explore-hyperswitch/payment-orchestration/)

Automate and optimize how payments are routed, authorized, and split across providers with Hyperswitch’s flexible payment orchestration engine.

[Tokenization and Card Vault →](about-hyperswitch/payments-modules/vault/)

Securely store and reuse customer payment credentials across processors to reduce friction and improve retention.

[Get Started with Hyperswitch's Vault](https://deepwiki.com/search/how-do-i-setup-the-vault_f3aed139-6118-40aa-a066-55b9b90d6775).

[Routing →](explore-hyperswitch/payment-orchestration/smart-router.md)

Control how transactions flow across payment providers with configurable routing logic and fallback options

[Intelligent Routing →](about-hyperswitch/payments-modules/intelligent-routing/)

Automatically route transactions based on geography, success rate, or cost to maximize authorization rates.

[Smart Retries →](about-hyperswitch/payments-modules/revenue-recovery.md)

Recover failed payments using ML-driven retry strategies optimized for timing, issuer behavior, and card type.

[Payouts →](explore-hyperswitch/payment-orchestration/payouts/)

Easily manage and automate disbursements to sellers, vendors, or partners with flexible payout logic.

[Subscriptions →](explore-hyperswitch/payment-orchestration/subscriptions.md)

Handle recurring payments seamlessly with built-in support for subscription billing and invoicing.

[Split Payments →](explore-hyperswitch/payment-orchestration/split-payments/)

Divide transactions between multiple parties or accounts with precision and control.

</details>

### Improve Your Checkout and Payment Experience

Deliver seamless, flexible, and localized payment flows that drive higher conversion and customer trust.

<details>

<summary><strong>Create Seamless Checkout Experiences That Convert</strong></summary>

[Customizable Checkout SDK (Web) →](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide/web)\
Embed a native, responsive checkout experience into your website with full control over styling and flow.

[Click to Pay →](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup/wallets)\
Enable frictionless, one-click payments for returning users using wallets and saved cards.

[Payment Methods Management →](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup)\
Dynamically configure and prioritize payment methods based on geography, currency, and user preference.

[Alternate Payment Methods (APMs) →](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup)\
Offer support for UPI, wallets, and local payment options to meet your customers where they are.

[Integration Guide Overview →](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide)\
Explore the full set of tools and options to deliver a branded and consistent payment experience across platforms.

</details>

### Manage and Monitor Your Payment Operations

Operate at scale with tools to manage accounts, monitor transactions, handle disputes, and apply business rules.

<details>

<summary><strong>Operate and Monitor Your Payment Stack</strong></summary>

[Manage Accounts and Profiles →](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multi-tenancy-with-hyperswitch)\
Create, manage, and operate across multiple merchant accounts and profiles with full multi-tenancy support.

[Analytics and Operations →](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations)\
Gain real-time visibility into transaction performance, routing behavior, and operational metrics.

[Disputes and Chargebacks →](https://docs.hyperswitch.io/explore-hyperswitch/account-management/disputes)\
Monitor, respond to, and manage disputes or chargebacks from a centralized operations interface.

[Surcharge Management →](https://docs.hyperswitch.io/explore-hyperswitch/account-management/surcharge)\
Apply dynamic surcharges or convenience fees based on card type, geography, or business logic.

[Full Operations Overview →](https://docs.hyperswitch.io/explore-hyperswitch/account-management)\
Explore the complete set of tools available for scaling your payment operations with confidence.

</details>

### Scalability, Relability, and Security

Take your Hyperswitch integration to production with confidence. Set up environments, secure credentials, monitor performance, and scale seamlessly as your business grows.

<details>

<summary><strong>Explore Security, Reliability, and Scalability</strong></summary>

Build with confidence on an architecture designed for compliance, low-latency scaling, and enterprise-grade uptime.

[Security and Compliance →](https://docs.hyperswitch.io/explore-hyperswitch/overview/security)\
Protect sensitive data and meet global compliance standards like PCI DSS with secure-by-default components.

[Latency →](https://docs.hyperswitch.io/learn-more/hyperswitch-architecture/a-payments-switch-with-virtually-zero-overhead)\
Scale effortlessly with a stateless architecture designed to handle high-throughput payment workloads with near-zero overhead.

Here's how [Hyperswitch handles horizontal scaling under high throughput](https://deepwiki.com/search/how-does-hyperswitch-handle-ho_8bba708f-e768-465c-8e24-953f7a60da72#1)

[Reliability →](https://docs.hyperswitch.io/learn-more/hyperswitch-architecture)\
Achieve consistent uptime and resiliency through modular design and built-in fault tolerance.

Here's how [Hyperswitch handles idempotency and message ordering](https://deepwiki.com/search/what-guarantees-does-the-syste_1bc51ad9-d897-4d9a-bce6-7d0a19cf00c4#1).

</details>

### Go Live with Hyperswitch

<details>

<summary>Take Hyperswitch into production</summary>

[How to Go Live with Hyperswitch →](https://docs.hyperswitch.io/check-list-for-production/going-live)\
Follow our go-live checklist to launch with confidence — covering setup, credentials, security, and monitoring.

</details>

### Need Help?

* [Join our Slack Community →](https://inviter.co/hyperswitch-slack)\
  Ask questions, share ideas, and connect with other developers building on Hyperswitch.
* [Contact Us →](https://hyperswitch.io/contact-us)\
  Prefer direct support? We’re happy to help.

***

### Developer Resources

* [API Reference →](https://api-reference.hyperswitch.io/introduction)
* [SDK Documentation →](https://docs.hyperswitch.io/learn-more/sdk-payment-flows)
* [Postman Collection →](https://docs.hyperswitch.io/hyperswitch-open-source/exploration-guide#use-postman)
* [GitHub Repository →](https://github.com/juspay/hyperswitch)
