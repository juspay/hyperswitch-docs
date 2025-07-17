---
icon: garage-car
---

# Platform Org and Merchant Setup

A PlatformOrg is a specialized organization type containing exactly one Platform Merchant, which has elevated privileges across its entire organization:

* **Create Merchant Accounts**: Dynamically spin up new child merchant accounts via API.
* **Manage Credentials**: Generate, revoke, and rotate API keys for child merchants programmatically.
* **Full Visibility & Control**: Process payments, refunds, and other operations across all your sub-merchants by using API keys generated specifically for each merchant through your Platform Merchant account.

### &#x20;Platform Org and Merchant Structure

```mermaid
flowchart TD
  PlatformOrg["PlatformOrg"] --> PlatformMerchant["Platform Merchant (single, privileged merchant)"]
  
  PlatformMerchant --> SubMerchant1["Sub-Merchant #1"]
  PlatformMerchant --> SubMerchant2["Sub-Merchant #2"]
  PlatformMerchant --> SubMerchant3["Sub-Merchant #3"]

  SubMerchant1 --> ProfileA["Profile A"]
  SubMerchant1 --> ProfileB["Profile B"]
  SubMerchant2 --> ProfileC["Profile C"]
  SubMerchant3 --> ProfileD["Profile D"]

```

#### **Explanation:**

* PlatformOrg hosts exactly one Platform Merchant with elevated privileges.
* Sub‑Merchants are standard merchant accounts managed by the Platform Merchant.
* Profiles are transactional endpoints under each sub‑merchant.

### Key Capabilities Comparison

| **Capability**                  | **Platform Merchant** | **Normal Org/Merchant** |
| ------------------------------- | --------------------- | ----------------------- |
| Merchant creation via API       | ✔                     | ✘(Dashboard only)       |
| Generate API keys for merchants | ✔                     | ✘ (Dashboard only)      |

### Typical API Workflows for Platform Merchant

1. **Create\_Platform**
   1. When you set up a new platform, an organization and its associated platform merchant account are automatically created.
   2. The platform merchant account holds elevated privileges for API-driven merchant management and operations.
2. **Generate Platform API Key (Dashboard Step)**
   1. Navigate to the[ Hyperswitch API Keys Dashboard](https://app.hyperswitch.io/dashboard/developer-api-keys).
   2. Click on "Create New API Key."
   3. Assign a name and description for your platform API key, then generate and securely store this key.
3. **Create\_Merchant**
   1. Using the Platform Merchant API key, you can dynamically create new merchant accounts within your platform.
   2. API link: [https://api-reference.hyperswitch.io/v1/merchant-account/merchant-account--create](https://api-reference.hyperswitch.io/v1/merchant-account/merchant-account--create)
4. **API\_keys**
   1. After creating merchant accounts, you can generate API keys specific to each merchant
   2. API link: [https://api-reference.hyperswitch.io/v1/api-key/api-key--create](https://api-reference.hyperswitch.io/v1/api-key/api-key--create)
5. **Mapping and Usage of API Keys**
   1. Maintain a secure internal mapping of generated API keys for each merchant account.
   2. Utilize these merchant-specific API keys to perform standard operations such as payments, refunds, and settlements on behalf of each sub-merchant.

#### Merchant Account Operations(Platform API Key)

* Create merchant accounts within the platform org
* List merchant accounts
* Retrieve a specific merchant account
* Update a merchant account

### Use Cases

* Vertical SaaS Onboarding: Automate merchant creation and key management for new sellers via your own dashboard
* Franchise Management: Centralized control over multiple franchise outlets.
* White-label Payments: Programmatically manage merchant accounts for various clients.
