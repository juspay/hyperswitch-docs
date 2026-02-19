---
description: Open, Modular, Self-Hostable Payment Infrastructure
icon: container-storage
---

# Payments Suite

Hyperswitch is built for teams that want engineering-grade control over payments.

To simplify architectural decisions, the ecosystem can be viewed as four independent building blocks.\
By defining ownership of each block — Hyperswitch-managed, self-hosted, or third-party — you can design an architecture aligned with your compliance posture, performance requirements, and internal engineering capabilities.



### **The Four Core Components**

#### **The SDK (Frontend) :**&#x20;

The entry point for your payment flow. It resides in your frontend and is responsible for securely capturing sensitive payment information.

#### **Intelligent Routing & Orchestration (Backend) :**&#x20;

The core of the operation. It manages the payment lifecycle, executes routing logic, and handles post-payment operations like refunds.

#### **Acquirer & Processor Connectivity (Connectors) :**

The actual pipelines that translates the transaction (e.g., Stripe, Adyen, Worldpay).

#### **Vault (Card Data Storage) :**&#x20;

The secure locker for sensitive card data to enable "One-Click" recurring payments without the user re-entering details.



Each Component can be handled by Hyperswitch, managed or self-deployed by your own team, or even sourced from a third-party provider e.g. Vault ([reference](https://docs.hyperswitch.io/~/revisions/wA01t1OV6BPUckMZ2Pvg/explore-hyperswitch/workflows/vault/connect-external-vaults-to-hyperswitch-orchestration))

***

### Integration Architecture

With the components defined, the next step is to select your integration architecture. This choice hinges on a single question:  Who controls the payment execution ?

Choose the integration method that best aligns with your payment flow requirements:

#### Integration Model 1: Client-Side SDK Payments

(Tokenize Post-Payment | SDK-Initiated Execution)

#### When to Choose This Model

* You want dynamic, frontend-driven payment experiences
* You prefer minimal backend orchestration logic
* You want SDK-triggered payment confirmation
* You are optimizing for rapid checkout implementation

#### High-level Flow

1. Merchant will call the [/payments](https://api-reference.hyperswitch.io/v1/payments/payments--create) API and load the [Payment SDK](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment).
2. SDK securely collects payment details.
3. SDK triggers payment confirmation.
4. SDK communicates with Hyperswitch backend.
5. Hyperswitch:
   * Applies [routing logic](https://docs.hyperswitch.io/~/revisions/iPtyU5MKxmgIsGywgRhI/explore-hyperswitch/workflows/intelligent-routing)
   * Sends request to configured PSP
   * Manages authorization/capture
   * Returns final payment status

***

#### Integration Model 2: Server-to-Server (S2S) Payments

(Tokenize Pre-Payment | Backend-Controlled Execution)

#### When to Choose This Model

* You want granular control over transaction timing
* You require backend-driven orchestration logic
* You want to tokenize credentials before execution
* You prefer decoupling vaulting from transaction processing

#### High-level Flow

**Tokenisze Card :**&#x20;

* Tokenize payment credentials using - [Vault SDK](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment-method/web) or backend call to [/payment-methods](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--create-v1)
*   Hyperswitch securely stores the credential and returns a reusable identifier - `payment_method_id`.



**Trigger Payment Execution :**&#x20;

*   Option A: Process via Hyperswitch Orchestration by calling /payments API.

    *   Use this option if you want Hyperswitch to:

        * Apply [routing logic](https://docs.hyperswitch.io/~/revisions/iPtyU5MKxmgIsGywgRhI/explore-hyperswitch/workflows/intelligent-routing)
        * Select the optimal connector
        * Manage [retries](https://docs.hyperswitch.io/~/revisions/iPtyU5MKxmgIsGywgRhI/explore-hyperswitch/workflows/smart-retries) and failover
        * Handle authorization and capture lifecycle

        This is the recommended model for merchants adopting Hyperswitch orchestration.


* Option B: Process via Proxy API by calling [/proxy](https://docs.hyperswitch.io/~/revisions/wbGQKlHTQ8NT2yPUGcD2/about-hyperswitch/payment-suite-1/payment-method-card/proxy) API.&#x20;
  *   Use this option if:

      * You do not want to change your existing PSP integration immediately
      * You want Hyperswitch to act as a passthrough layer
      * You are incrementally migrating to full orchestration

      In this mode:

      * Your existing integration contract remains unchanged
      * Hyperswitch forwards requests to the configured processor
      * You can progressively enable routing and orchestration features
