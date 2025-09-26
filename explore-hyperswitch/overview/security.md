---
description: Comprehensive measures safeguarding Data Integrity within Hyperswitch
icon: cloud-check
---

# Data Security

At Hyperswitch, we prioritize data security and adhere to PCI DSS standards to protect sensitive information. Our platform is engineered with a robust multi-layered encryption framework to secure sensitive data, including API credentials, RSA certificates, database passwords, and Personally Identifiable Information (PII), throughout its lifecycle.

### **Benefits of Our Security Framework**

* **Compliance and Trust**: We comply with PCI DSS 4.0 and ISO 27001:2022 standards, ensuring international best practices for data protection.
* **Enhanced Data Security**: Hyperswitch employs advanced encryption layers to secure data during transmission and storage.
* **Fraud Prevention**: Through secure card vaulting and tokenization, we minimize fraud risks.
* **Operational Transparency**: With merchant-specific encryption, we ensure your data remains confidential and protected.

## Handling Sensitive Data

The Hyperswitch application employs multiple layers of encryption to safeguard sensitive card information during transmission between components as explained below. Our security framework is designed to meet PCI standards, ensuring maximum protection and confidentiality for all card-related data.

<figure><img src="../../.gitbook/assets/system1.jpg" alt=""><figcaption></figcaption></figure>

#### **1. Accepting Card Data**

Card information is initially received from the Hyperswitch SDK. This data is encrypted using SSL/TLS protocols, ensuring end-to-end encryption during transmission between the SDK and the Hyperswitch backend. This guarantees that sensitive card data is secure from the point of collection.

#### **2. Storing Card Data (Vaulting)**

When a payment is made using a saved card, the card details are securely stored in the Hyperswitch Card Vault. This process involves multiple steps to ensure the confidentiality and integrity of the data:

**Card Data Preparation:**

* **Signing for Integrity**: The Hyperswitch App Server signs the card details using its private key, ensuring the data has not been altered.
* **Encryption for Confidentiality**: The signed details are encrypted using the public key of the Card Vault (locker), securing the data during transmission.

**Data Storage Process:**

1. **Validation**: The Hyperswitch Card Vault validates the signed data using the public key of the Hyperswitch App Server. This step ensures the integrity of the transmitted data.
2. **Decryption**: The Card Vault decrypts the received data to make it usable for storage.
3. **Secure Storage**:
   * The decrypted data is re-encrypted internally using AES encryption.
   * This securely encrypted data is then stored in the database.
   * The database itself is encrypted at rest, providing an additional layer of security for the stored information.

For more technical details about how the Hyperswitch Card Vault manages encryption and decryption, you can visit the [Hyperswitch Card Vault GitHub repository](https://github.com/juspay/hyperswitch-card-vault).

**3. Using Card Data for Analytics and Payment Operations**

To provide insights and analytics without compromising sensitive information, only partially masked card details (e.g., the first 4 and last 4 digits) are sent to the Hyperswitch Control Centre. This approach offers merchants a high-level view of transactions while preserving customer confidentiality.

## Data Encryption Overview

At Hyperswitch, we place the utmost importance on safeguarding sensitive data, including `external API credentials, customer information, and card details`. Our application employs a multi-layered encryption approach to ensure security during data transmission and storage.

* **Masked Transmission**: All sensitive data remains masked during transmission and is never permanently stored on local systems.
* **Multi-Layered Encryption**: Data is encrypted at every critical juncture, ensuring robust protection against breaches.

<figure><img src="../../.gitbook/assets/Key Manager Service (1).jpg" alt=""><figcaption></figcaption></figure>

## Key Management System (KMS) Encryption

Hyperswitch employs AWS Key Management System (KMS) to securely manage sensitive keys required for the application’s operation.

1. **Startup Encryption**: Sensitive keys, such as database passwords and RSA certificates, are encrypted at the startup.
2. **Secure Storage**: These encrypted keys are securely stored in environment variables or configuration files, ensuring their confidentiality and protection against unauthorized access.

## Key Manager Service Encryption

**Merchant-Specific Encryption**

Hyperswitch utilizes a **Key Manager Service** to ensure the secure generation and storage of a **unique Data Encryption Key (DEK)** for each merchant.&#x20;

These merchant-specific DEKs undergo further encryption using a secrets manager, such as **AWS KMS**, to provide an additional layer of security.

**Data Encryption for Each Merchant Account**

Data associated with individual merchant accounts is encrypted using the unique DEK for that merchant. This approach ensures robust protection of:

* **Connector API Keys**: Critical credentials for third-party integrations.
* **Confidential Merchant Information**: Business-sensitive data that needs stringent security.
* **Customer Personally Identifiable Information (PII)**: Data such as customer names, email addresses, and other sensitive details.

The encryption process ensures:

* **Data Segmentation and Authorized Access Only**: Each merchant's data is encrypted with their specific DEK, ensuring that each set of data remains protected and is accessible only to authorized parties associated with that merchant. Data can only be decrypted by entities possessing the appropriate credentials tied to that merchant's DEK.

### Concealing Sensitive Data in Logs

At Hyperswitch, we take extra care to protect sensitive information, even in system logs. Our application framework uses a **wrapper type** to classify all sensitive data as `Secret`.

* **Leveraging Rust's Advantages**: Hyperswitch uses Rust, a strongly typed programming language, to create a robust mechanism (`Secret<T>`) for handling sensitive data.
* **Masked Logging**: Instead of exposing sensitive details such as passwords or Personally Identifiable Information (PII), we log only the data type (e.g., `*** alloc::string::String ***`).
* **Source-Level Protection**: By masking sensitive data at its source, we ensure that sensitive information is never inadvertently exposed, even in debug outputs or logs.

{% hint style="info" %}
#### Database at Rest Encryption

At Hyperswitch, we encrypt database instances in our cloud-hosted environments to protect sensitive information, including card details and merchant data. For self-hosted setups, we recommend adopting similar encryption practices to ensure robust security.
{% endhint %}
