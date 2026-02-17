---
icon: container-storage
---

# Payments Suite

Hyperswitch is built with a modular architecture to support you at every stage of that journey. You can adopt the full stack for a unified payments experience or selectively integrate individual modules such as Vault or Smart Router based on your specific requirements.

To simplify decision-making, it helps to view the ecosystem as four core building blocks. By defining ownership of each block whether managed by Hyperswitch or your team you can quickly determine the architecture that best aligns with your technical and business goals.

{% hint style="info" %}
### Integration Paths

Choose the integration method that best aligns with your payment flow requirements:

#### 1. Client-Side SDK Payments (Tokenise Post Payment)

Refer to Payments (Cards) section  if your flow requires the SDK to initiate payments directly. In this model, the SDK handles the payment trigger and communicates downstream to the Hyperswitch server and your chosen Payment Service Providers (PSPs). This path is ideal for supporting dynamic, frontend-driven payment experiences.

#### 2. Server-to-Server (S2S) Payments (Tokenise Pre Payment)

Refer to the Payment Method (Cards) section if you intend to use the SDK exclusively for vaulting/storing card details. In this scenario, the actual payment execution is handled via S2S API calls from your backend to Hyperswitch, offering you more granular control over the transaction lifecycle.
{% endhint %}

#### **The Four Core Components**

**1.The SDK (Frontend) :** The entry point for your payment flow. It resides in your frontend and is responsible for securely capturing sensitive payment information.

**2. Intelligent Routing & Orchestration (Backend) :** The core of the operation. It manages the payment lifecycle, executes routing logic, and handles post-payment operations like refunds.

**3. Acquirer & Processor Connectivity (Connectors) :** The actual pipelines that translates the transaction (e.g., Stripe, Adyen, Worldpay).

**4. Vault (Card Data Storage) :**  The secure locker for sensitive card data to enable "One-Click" recurring payments without the user re-entering details.

Each Component can be handled by Hyperswitch, managed or self-deployed by your own team, or even sourced from a third-party provider e.g. Vault ([reference](https://docs.hyperswitch.io/~/revisions/wA01t1OV6BPUckMZ2Pvg/explore-hyperswitch/workflows/vault/connect-external-vaults-to-hyperswitch-orchestration))

#### **Integration Architecture**

With the components defined, the next step is to select your integration architecture. This choice hinges on a single question:  _Who controls the payment execution ?_

There are two primary integration Flow :

**1.** [**Payments**](https://docs.hyperswitch.io/~/revisions/QSGzCRIrWguIX4tCwjpZ/about-hyperswitch/payment-suite-1/orchestrator-model)**:** You leverage Hyperswitch Payments SDK or S2S APIs to manage the payment lifecycle. Hyperswitch Payments SDK or `/payments` API would route payments to the configured processor and perform the operation - Auth only, Capture, Set up recurring etc as per the API call.&#x20;

**2.** [**Payment Methods**](https://docs.hyperswitch.io/~/revisions/QSGzCRIrWguIX4tCwjpZ/about-hyperswitch/payment-suite-1/direct-payment-control-model)**:** You leverage Hyperswitch Payment Methods SDK or S2S APIs to manage the payment lifecycle. Hyperswitch SDK or `/payment-methods` API would tokenize the payment credential in Hyperswitch vault and return a token or `payment_method_id` . The merchant will use the PCI-compliant `payment_method_id`  to call  `/payments` API and route payments to the configured processor to perform the operation - Auth only, Capture, Set up recurring etc as per the API call.
