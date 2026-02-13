---
hidden: true
---

# In-App and Web Transactions Processed Using Merchant Decryption

### Direct Token Decryption: Pre-requisites

If you choose to handle Apple Pay decryption internally rather than through a Payment Service Provider (PSP), your infrastructure must meet the following criteria:

* Active Apple Developer Status: You must be enrolled in either the standard Apple Developer Program or the Enterprise Program.
* Dedicated Certificates: You are required to generate and manage your own Apple Pay Payment Processing Certificate.
* Compliance & Security: Your environment must be strictly PCI DSS compliant, as you will be interacting with sensitive, unencrypted cardholder information.
* Direct API Implementation: This workflow is intended for API-only integrations where the merchant server manages the full transaction lifecycle.

### Step-by-Step Decryption Workflow

The decryption sequence ensures the integrity and security of the payment data before it is submitted for processing.

#### 1. Verification and Setup

* **Validate the Certificate:** Confirm the authenticity of the Apple Pay certificate before attempting to unlock the token data.
* **Reference Apple’s Standard:** For specific cryptographic implementation details, consult the technical guides provided on the Apple Developer Portal.

#### 2. Key Restoration

* **Identify the Public Key:** Use the `publicKeyHash` found in the payment token to determine which of your merchant public keys was used by Apple.
* **Access Credentials**: Pull the corresponding private key and merchant public key certificate from your secure key management system.
* **Reconstruct the Symmetric Key:** Use the merchant private key and the ephemeral public key (from the token) to restore the shared symmetric key.

#### 3. Data Decryption

* **Extract the Data Key:** Apply the restored symmetric key to decrypt the encrypted `data` field within the token.
* **Retrieve Plaintext:** This reveals the actual payment details required for authorization.

#### 4. Integrity and Fraud Checks

* **Idempotency Check:** Verify the `transactionId` against your database to ensure this specific payment has not been previously processed or credited.
* **Request Validation:** Audit the original Apple Pay request to ensure all transaction details (amount, currency, etc.) align with the decrypted data.

#### 5. Final Processing

* **Execute Payment:** Use the now-decrypted data to trigger a payment authorization. For specific field mapping, refer to your API's technical documentation.



#### **API Mapping  -**&#x20;



<table><thead><tr><th>Parameter Name</th><th width="111.12890625">Required</th><th>Description</th></tr></thead><tbody><tr><td>payment_method_data.wallet.apple_pay.payment_data</td><td></td><td></td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method</td><td></td><td></td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method.display_name</td><td></td><td></td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method.network</td><td></td><td></td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method.type</td><td></td><td></td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method.card_exp_month</td><td></td><td>Use the <strong>applicationExpirationDate</strong> value, contained in the Apple Pay token.</td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method.card_exp_year</td><td></td><td><p></p><p>Use the <strong>applicationExpirationDate</strong> value, contained in the Apple Pay token.</p><p></p></td></tr><tr><td>payment_method_data.wallet.apple_pay.payment_method.auth_code</td><td></td><td></td></tr><tr><td>payment_method_data.wallet.apple_pay.transaction_identifier</td><td></td><td>Use the <strong>transactionId</strong> value, contained in the Apple Pay token.</td></tr></tbody></table>

