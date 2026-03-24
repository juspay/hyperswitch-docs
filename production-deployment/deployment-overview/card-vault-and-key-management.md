---
description: Configure secure key management and encryption for Juspay Hyperswitch Card Vault in enterprise environments
---

# Card Vault & Key Management

### Enterprise Key Management for Hyperswitch Card Vault and Application

This document describes how to configure **secure key management** for **Hyperswitch**deployments in enterprise environments.

Hyperswitch processes **highly sensitive data**, including:

* Payment card information
* Bank account details
* API credentials
* Database credentials
* Personally Identifiable Information (PII)

To ensure compliance with industry standards such as **Payment Card Industry Security Standards Council** requirements, encryption must be enforced across:

1. Data in transit
2. Data at rest
3. Key storage and access
4. Application-level encryption

Hyperswitch implements these protections through a **Card Vault**, **Key Manager**, and optional **external Key Management Systems**.

### 1. Encryption Architecture Overview

A secure enterprise deployment of Hyperswitch should implement the following architecture:

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Security layers:

| Layer                         | Protection                   |
| ----------------------------- | ---------------------------- |
| Transport security            | TLS / mTLS                   |
| Service-to-service encryption | JWE + JWS                    |
| Key protection                | Master encryption key        |
| Key storage                   | KMS / HSM / Vault            |
| Vault access                  | Dual custodian authorization |

This architecture ensures **no single component has access to raw card data and encryption keys simultaneously**.

### 2. Card Vault Security Features

The Hyperswitch Card Vault includes the following built-in protections.

#### 2.1 Key Custodian Protection

The vault requires **multiple key custodians** to unlock the master encryption key during initialization.

Purpose:

* Prevents unilateral access to sensitive data
* Enforces dual-control security policies
* Aligns with PCI DSS key management principles

At startup:

1. The vault loads encrypted master key material
2. Authorized custodians submit key shares
3. The system reconstructs the master key
4. Vault encryption services become operational

Production deployments should enforce **at least two custodians**.

#### 2.2 Vault API Encryption

All communication between the **Hyperswitch Router** and the **Card Vault** is encrypted and signed using:

* **JSON Web Encryption**
* **JSON Web Signature**

This provides:

* message confidentiality
* message integrity
* sender verification

This protection is applied **in addition to TLS**.

#### 2.3 External Key Management

For enterprise deployments, encryption keys should **not be stored locally on the vault or application servers**.

Instead, integrate Hyperswitch with an external Key Management System such as:

* **HashiCorp Vault**
* **AWS Key Management Service**
* **Google Cloud KMS**
* **Azure Key Vault**

These systems provide:

* Hardware-backed key storage
* Key rotation policies
* Access auditing
* Role-based access control

Hyperswitch retrieves encryption keys dynamically during runtime.

### 3. Master Key Generation

The **Master Key** encrypts all card vault data.

In enterprise environments, the master key **should be generated inside a secure key management system** rather than on application hosts.

Recommended approaches:

| Deployment Type              | Key Generation  |
| ---------------------------- | --------------- |
| Cloud infrastructure         | Cloud KMS       |
| Hybrid infrastructure        | HashiCorp Vault |
| Highly regulated environment | HSM-backed KMS  |

If external key managers are unavailable, Hyperswitch provides utilities to generate master keys locally. However, this approach should only be used in controlled environments and keys must be securely transferred into a secret management system.

Example utility command:

```
cargo install --git https://github.com/juspay/hyperswitch-card-vault --bin utils --root . \
&& ./bin/utils master-key
```

The command generates:

* Master encryption key
* Key custodian key shares

Immediately store these keys in a **secure secret management system**.

### 4. Service-to-Service Encryption Keys

Hyperswitch uses **RSA keys** for secure communication between services.

Two key pairs are required:

| Key Pair        | Purpose                          |
| --------------- | -------------------------------- |
| Vault key pair  | Decrypt vault requests           |
| Tenant key pair | Sign and encrypt router requests |

Example key generation:

```
openssl genrsa -out vault-private-key.pem 2048
openssl rsa -in vault-private-key.pem -pubout -out vault-public-key.pem

openssl genrsa -out tenant-private-key.pem 2048
openssl rsa -in tenant-private-key.pem -pubout -out tenant-public-key.pem
```

In production deployments:

* Store private keys in **secret management systems**
* Inject keys into Kubernetes using **secret volumes**
* Restrict access using RBAC

Keys must **never be stored in public repositories or container images**.

### 5. Deploying the Hyperswitch Key Manager

The Hyperswitch Key Manager acts as an intermediary between the application and external key stores.

It provides:

* centralized key access
* encryption services
* audit logging

The Key Manager should be deployed as an **independent Kubernetes service**.

### 6. Secure Service Communication (mTLS)

Communication between the following components must use **mutual TLS**:

* Router
* Card Vault
* Key Manager

mTLS ensures:

* encrypted communication
* service identity verification

Certificates can be issued using:

* **cert-manager**
* corporate PKI infrastructure
* service mesh certificate authorities

Example certificate generation script (for testing environments):

```
bash gen_certs.sh --namespace <namespace> --service <service-name>
```

Production clusters should use **automated certificate lifecycle management** rather than manual scripts.

### 7. Kubernetes Configuration

The following secrets must be configured within Kubernetes.

Key Manager configuration:

```
hyperswitch-key-manager:
  server:
    secrets:
      ca_cert: <CA certificate>
      tls_cert: <TLS certificate>
      tls_key: <TLS private key>
```

Card Vault configuration:

```
LOCKER__EXTERNAL_KEYMANAGER__URL=<keymanager-url>
LOCKER__EXTERNAL_KEYMANAGER__CERT=<ca-cert>
LOCKER__API_CLIENT__IDENTITY=<client-cert>
```

Router configuration:

```
hyperswitch-app:
  server:
    secrets:
      keymanager:
        ca: <ca-cert>
        cert: <client-cert>
```

Secrets should be injected using:

* Kubernetes Secrets
* External Secrets Operators
* Vault secret injection

Avoid using **environment variables for highly sensitive keys** where possible.

### 8. Vault Initialization (Custodian Authorization)

When the vault starts, custodians must unlock the vault using their key shares.

Example API calls:

Provide first key share:

```
POST /custodian/key1
```

Provide second key share:

```
POST /custodian/key2
```

Unlock vault:

```
POST /custodian/decrypt
```

Enterprise environments should restrict this operation to:

* designated security administrators
* audited secure access channels
* controlled operational procedures

### 9. Key Rotation Strategy

Regular key rotation is critical for maintaining cryptographic security.

Recommended rotation policies:

| Key Type              | Rotation Frequency |
| --------------------- | ------------------ |
| Master encryption key | Annual             |
| Vault API keys        | 90 days            |
| TLS certificates      | 60–90 days         |

Key rotation should be performed using:

* KMS rotation features
* automated certificate managers
* controlled deployment pipelines

### 10. Monitoring and Auditing

To detect unauthorized access attempts, enable logging and monitoring for:

* key access operations
* vault unlock attempts
* encryption failures
* certificate validation errors

Logs should be integrated with centralized logging systems such as:

* **Elastic Stack**
* **Grafana Loki**
* **Splunk**

Security alerts should be configured for suspicious activity.

### 11. Security Best Practices

Enterprises deploying Hyperswitch should enforce the following controls:

**Access control**

* restrict key access to minimal roles
* enforce multi-factor authentication
* use role-based access policies

**Secret protection**

* never store secrets in source code
* encrypt all secret storage
* use dedicated secret managers

**Infrastructure security**

* isolate vault components in private networks
* restrict external access
* enable firewall policies

**Operational controls**

* audit all administrative actions
* rotate credentials regularly
* monitor security logs continuously

### 12. Hardware Security Module (HSM) Backed Key Architecture

For highly regulated environments, encryption keys should be stored and managed within **Hardware Security Modules (HSMs)**.

An HSM is a dedicated cryptographic device designed to:

* securely generate encryption keys
* prevent key extraction
* perform cryptographic operations internally
* enforce access control and auditing

Common enterprise HSM-backed systems include:

* **AWS CloudHSM**
* **AWS Key Management Service**
* **Azure Key Vault**
* **Google Cloud KMS**
* **HashiCorp Vault**

### HSM-Based Key Hierarchy

Enterprise systems typically implement a **hierarchical key structure**.

<figure><img src="../../.gitbook/assets/image (3).png" alt="" width="181"><figcaption></figcaption></figure>

Explanation:

| Key                       | Purpose             |
| ------------------------- | ------------------- |
| Root key                  | Stored inside HSM   |
| Key Encryption Key (KEK)  | Encrypts other keys |
| Data Encryption Key (DEK) | Encrypts card data  |

Benefits:

* raw card encryption keys never leave the HSM
* key compromise blast radius is minimized
* cryptographic operations can be audited

### Integrating HSM with Hyperswitch

The Key Manager should:

* retrieve encryption keys from the KMS
* perform encryption operations through secure APIs
* cache keys in memory only for limited time

Keys should **never be written to disk**.

### 13. Tokenization and Re-Encryption

Tokenization replaces sensitive card data with a **non-sensitive token**.

Example:

<table data-full-width="true"><thead><tr><th width="246.47265625">Card Number</th><th width="175.8359375">Token</th></tr></thead><tbody><tr><td>4111 1111 1111 1111</td><td>tok_82d9f9d1</td></tr></tbody></table>

The token can safely be stored and used for:

* recurring payments
* refunds
* payment authorization

Only the vault can resolve the token to the original card data.

#### Re-Encryption During Key Rotation

When encryption keys rotate, stored card data must be **re-encrypted**.

Re-encryption process:

1. Encrypted card
2. Decrypt using old DEK
3. Encrypt using new DEK
4. Update storage

Best practices:

* perform re-encryption in controlled batches
* throttle operations to avoid database overload
* verify integrity after each batch

This process should run as a **background migration job**.

### 14. Disaster Recovery and Key Loss Protection

Loss of encryption keys can result in **permanent loss of card data**.

Enterprises must implement recovery procedures.

#### Key Backup Strategy

Key backups must follow strict security practices.

Recommended approach:

| Key Type  | Backup Strategy             |
| --------- | --------------------------- |
| Root keys | HSM-backed backup           |
| KEK       | encrypted backup            |
| DEK       | regenerated or re-encrypted |

Backups should be stored in:

* separate geographic region
* separate security domain
* encrypted storage

#### Multi-Region Key Replication

For highly available deployments, replicate key access across regions.

Example architecture:

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

This ensures the vault can operate even during regional outages.

#### Vault Recovery Procedure

In the event of vault failure:

1. Restore infrastructure
2. Restore encrypted database
3. Restore key manager configuration
4. Retrieve keys from KMS or HSM
5. Reinitialize the vault

If using key custodians:

1. Custodians provide key shares
2. Master key is reconstructed
3. Vault decrypts stored data

#### Break-Glass Access

Organizations should maintain **controlled emergency access** procedures.

Requirements:

* dual authorization
* full audit logging
* time-limited access
* security officer approval

Break-glass access should only be used during:

* disaster recovery
* vault corruption
* key recovery scenarios

### 15. Security Auditing and Compliance

To maintain compliance with payment security standards, organizations must implement continuous auditing.

Audit controls should cover:

| Area                 | Monitoring Requirement |
| -------------------- | ---------------------- |
| Key usage            | logged and monitored   |
| Vault access         | identity verified      |
| Custodian operations | multi-party approval   |
| Key rotation         | scheduled and audited  |

Logs should be integrated with centralized monitoring systems such as:

* **Elastic Stack**
* **Splunk**
* **Grafana Loki**

Security teams should regularly review logs for:

* unusual key access
* unauthorized vault access
* repeated authentication failures
