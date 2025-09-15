---
description: A brief summary of PCI compliance for Hyperswitch Cloud users
icon: credit-card
---

# PCI Compliance

Payment Card Industry Data Security Standard (PCI DSS) compliance ensures that sensitive cardholder data is securely processed, stored, and transmitted.&#x20;

**Hyperswitch Cloud provides out-of-the-box PCI DSS Level 1 compliance**—the highest level of certification—so you can handle payments securely without worrying about card storage or compliance complexities yourself.

### **Key Features of PCI Compliance on Hyperswitch Cloud**

**PCI DSS Level 1 Certification**\
Hyperswitch is validated as a **PCI DSS v4.0 Level 1 Service Provider**, the highest level of PCI certification for service providers. This ensures robust security controls for storing, processing, and transmitting cardholder data.

**Annual Audits**\
Hyperswitch undergoes an annual PCI DSS audit performed by an independent Qualified Security Assessor (QSA). In addition, quarterly vulnerability scans are conducted by a PCI-approved scanning vendor (ASV), as required by PCI DSS.

**Tokenization for Secure Card Handling**\
Hyperswitch tokenizes and stores customer card details in its cloud vault, reducing the need for merchants to store sensitive data.

### **Enabling Raw Card Acceptance with Payment Processors**

To process raw card data securely through Hyperswitch:

#### **Processor Configuration:**

Many payment processors disable raw card acceptance by default. To enable it:

* Share Hyperswitch’s PCI Attestation of Compliance (AOC) with your processor's support team.
* Request them to enable raw card processing for your merchant account.

#### **Stripe Integration Update:**

* Stripe no longer allows raw card acceptance via its Merchant Dashboard.
* If required, share Hyperswitch’s PCI DSS Attestation of Compliance (AOC) with Stripe support.

#### **Accessing the PCI AOC Document:**

* A redacted version of Hyperswitch’s PCI DSS Attestation of Compliance (AOC) is available to Cloud users under NDA. It can be downloaded from the Compliance section in the Dashboard.
* Alternatively, email **hyperswitch@juspay.in** for assistance.

### **Why Choose Hyperswitch for PCI Compliance?**

* Simplified compliance management with automatic tokenization and secure storage.
* Global security standards maintained across all integrations.
* Reduced complexity and liability for merchants in handling sensitive card data.
