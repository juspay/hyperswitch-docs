---
icon: container-storage
---

# Payments Suite

Integrating a payment layer is a major milestone for any business. Hyperswitch is built with a modular architecture to support you at every stage of that journey. You can adopt the full stack for a unified payments experience or selectively integrate individual modules such as Vault or Smart Router based on your specific requirements.

To simplify decision-making, it helps to view the ecosystem as four core building blocks. By defining ownership of each block whether managed by Hyperswitch or your team you can quickly determine the architecture that best aligns with your technical and business goals.

#### **The Four Core Components**

**1.The SDK (Frontend) :** The entry point for your payment flow. It resides in your frontend and is responsible for securely capturing sensitive payment information.

**2. Intelligent Routing & Orchestration (Backend) :** The core of the operation. It manages the payment lifecycle, executes routing logic, and handles post-payment operations like refunds.

**3. Acquirer & Processor Connectivity (Connectors) :** The actual pipelines that process the transaction (e.g., Stripe, Adyen, Worldpay).

**4. Vault (Card Data Storage) :**  The secure locker for sensitive card data to enable "One-Click" recurring payments without the user re-entering details.

Each Component can be handled by Hyperswitch, managed by your own team, or even sourced from a third-party provider(e.g. Vault).

#### **Integration Architecture**

With the components defined, the next step is to select your integration architecture. This choice hinges on a single question:  _Who controls the orchestration and processing logic ?_

There are three primary integration Flow :

**1.** [**Payment with Vault**](https://docs.hyperswitch.io/~/revisions/QSGzCRIrWguIX4tCwjpZ/about-hyperswitch/payment-suite-1/orchestrator-model)**:** You leverage Hyperswitch’s intelligent core to manage the payment lifecycle. Hyperswitch route payments dynamically to global processors (Stripe, Adyen, etc.) using the pre-built Connectors.

**2.** [**Vault and Forward**](https://docs.hyperswitch.io/~/revisions/QSGzCRIrWguIX4tCwjpZ/about-hyperswitch/payment-suite-1/direct-payment-control-model)**:** You utilize Hyperswitch strictly as a secure infrastructure layer (Vault & Pipe). You act as the orchestrator, defining the specific destination yourself, while Hyperswitch securely forwards the payload along with sensitive card data via a Proxy API.

**3.** [**Vault with S2S flow**](https://docs.hyperswitch.io/~/revisions/QSGzCRIrWguIX4tCwjpZ/about-hyperswitch/payment-suite-1/token-first-model-setup)**:** In this model you store the card first during initial checkout without charging the customer and later leverage Hyperswitch’s intelligent core to manage the payment lifecycle.



