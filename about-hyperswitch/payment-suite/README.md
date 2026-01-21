---
icon: container-storage
---

# Payments Suite

Integrating a payment layer is a significant milestone. That is why Hyperswitch is modular by design: you can adopt the full stack for a unified experience, or selectively integrate specific modules like Vault or Smart Router.

Navigating these choices is easier when you view the ecosystem as four main blocks. By defining who owns which block—Hyperswitch or your team—you can quickly identify the architecture that suits your needs.

#### **The Four Core Components**

**1.The SDK (Frontend) :** The entry point for your payment flow. It resides in your frontend and is responsible for securely capturing sensitive payment information.

**2. Intelligent Routing & Orchestration (Backend) :** The core of the operation. It manages the payment lifecycle, executes routing logic, and handles post-payment operations like refunds.

**3. Acquirer & Processor Connectivity (Connectors) :** The actual pipelines that process the transaction (e.g., Stripe, Adyen, Worldpay).

**4. Vault (Card Data Storage) :**  The secure locker for sensitive card data to enable "One-Click" recurring payments without the user re-entering details.

Each Component can be handled by Hyperswitch, managed by your own team, or even sourced from a third-party provider(e.g. Vault).

#### **Integration Architecture**

With the components defined, the next step is to select your integration architecture. This choice hinges on a single question:  _Who controls the orchestration and processing logic?_

There are two primary integration models:

**1.** [**Orchestrator Model** ](https://docs.hyperswitch.io/~/revisions/ym3YeydjfXLSnBIreBYp/about-hyperswitch/payment-suite/orchestrator-model)**:** You leverage Hyperswitch’s intelligent core to manage the payment lifecycle. Hyperswitch route payments dynamically to global processors (Stripe, Adyen, etc.) using the pre-built Connectors.

**2.** [**Vault and Proxy Model**](https://docs.hyperswitch.io/~/revisions/ym3YeydjfXLSnBIreBYp/about-hyperswitch/payment-suite/vault-and-proxy-model) **:** You utilize Hyperswitch strictly as a secure infrastructure layer (Vault & Pipe). You act as the orchestrator, defining the specific destination yourself, while Hyperswitch securely forwards the payload along with sensitive card data via a Proxy API.

