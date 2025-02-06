---
icon: vault
---

# Vault

Hyperswitch Vault Service is a standalone vault that allows you to tokenize and secure your customers' card data in our PCI-compliant vault without having to use our payment solutions.

With Hyperswitch Vault, you can:

* Use our PCI-compliant **Vault SDK** to collect and store card data securely, ensuring sensitive information never touches your systems.
* **Tokenize** cards across multiple payment processors through a **single unified API**.
* Generate **Network Tokens** to optimize payment operations and reduce costs with **automatic network token creation and updates**, powered by Juspay’s certified **Network Token Requestor** capabilities.

### Why Hyperswitch Vault?

#### Seamless and Universal Tokenization

* **Universal PSP Tokenization** – Store card data once and tokenize it instantly across **50+ payment providers**.
* **Network Token Management** – Increase transaction success rates and reduce interchange fees with **automatic network tokenization**.
* **Customizable Vault SDK** – Securely collect card details with **ready-to-use UI components**.
* **Flexible Token Generation** – Supports both **single-use and multi-use tokens** for various payment scenarios.

#### Security and Compliance – Zero Maintenance

* **PCI DSS v4.0 Certified** – Industry-leading payment security compliance.
* **ISO 27001:2022 Certified** – Global standard for information security management.
* **GDPR Compliant** – Ensures full compliance with EU data protection regulations.
* **SOC 2 Type II Compliant** – Stringent security controls for enterprise-grade safety.
* **256-bit AES Encryption** – Bank-grade encryption to protect stored data.

#### Enterprise-Grade Performance

* **99.999% Uptime SLA** – Highly reliable service availability.
* **Scales to 50,000 Transactions Per Second (TPS)** – Designed for high-volume transactions.
* **Sub-50ms Response Time** – Optimized for ultra-fast token generation and retrieval.

### How It Works?

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjHOvBRI1bfnMRf5zmWz9_yw4ieV0v5IEJUwhnBwu6iqxoI2yvHE-gfZ-du--dwemuLMv9AemXN5k0BubnmF0fqwO8gtGCyuRBT2L5DQW5DiFYgZmZpEEgSVXHJW1hTjqZJf4S?key=wWT-6TmmgS7GMTZGEfcB38Ke" alt=""><figcaption></figcaption></figure>

#### 1. Initial Vault Setup

* The **merchant server** sends a vaulting request with **tokenization preferences**.
* The **Vault server** responds with a **secure session ID** and **client secret**.
* All communication is **protected with end-to-end encryption**.

#### 2. Secure Card Capture

* The **Vault SDK** is initialized with **merchant credentials and session details**.
* Customers enter their **card details** using **secure SDK components**.
* Card data is transmitted **directly to the Vault server**, ensuring it never touches merchant systems.

#### 3. Vault Storage and Primary Tokenization

* Card data is **encrypted using bank-grade encryption** and stored in a **PCI-compliant vault infrastructure**.
* A **unique vault token** is generated as the primary reference for future transactions.

#### 4. PSP and Network Token Generation

* **Automated PSP-specific token creation** on demand.
* **Network tokens** are generated where supported (**Visa, Mastercard**).
* **Intelligent token mapping** and **lifecycle management** ensure seamless token utilization.
* **Continuous monitoring and automatic token updates** improve security and reliability.

#### 5. Flexible Payment Processing

* Use **vault tokens** directly with **PSP endpoints** or through **Hyperswitch**.
* Supports **recurring, one-time, and marketplace payments**.
* **Real-time token status tracking and updates**.
* **Automatic card updates** and **network token refreshes**.

### How to Integrate?

Hyperswitch Vault offers integration options tailored to different security and compliance needs.

#### **For Non-PCI Compliant Merchants**

Quickly integrate the **secure Vault SDK**.

* Collect card details without handling sensitive data.
* Maintain **full PCI compliance** without additional certification.

**For PCI Compliant Merchants**

**Direct server-to-server integration** for greater control.

* Securely send card data from your **own infrastructure** while maintaining existing security workflows.

#### Customizable Tokenization

* **Choose** specific **PSPs** for token generation.
* Enable **Network Tokenization** as needed.
* Generate **single-use or multi-use tokens** based on payment flow requirements.

{% content-ref url="intelligent-routing.md" %}
[intelligent-routing.md](intelligent-routing.md)
{% endcontent-ref %}
