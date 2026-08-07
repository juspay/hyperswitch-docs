---
description: >-
  Configure Juspay Hyperswitch Vault on the dashboard — API key generation,
  profile settings, and external vault connections
icon: sliders
metaLinks:
  alternates:
    - configuration.md
---

# Vault Configuration

This page is the single canonical reference for all Vault configuration steps on the Hyperswitch Control Centre. Every integration guide in the Vault section links here instead of repeating these steps.

---

## 1. Generating Vault API Keys

#### **Step 1: Generate API Key**

1. **Access Dashboard** — Log into the Hyperswitch Control Centre.
2. **Navigate to API Keys** — In the left-hand navigation menu, select **Developers > API Keys**.
3. **Create Key** — Click **Create New API Key**.
4. **Secure Storage** — Copy the generated key immediately and store it securely (it will not be shown again). Use this key in the `Authorization: api-key=<YOUR_VAULT_API_KEY>` header for all Vault API calls.

<figure><img src="../../../.gitbook/assets/vault-api-keys.png" alt="API Keys Dashboard"><figcaption><p>Navigate to Developers > API Keys to create and manage your API credentials</p></figcaption></figure>


#### **Step 2: Access Profile ID**

1. **Navigate to Payment Settings** — In the left-hand navigation menu, select **Developers > Payment Settings**.
2. **Copy Profile ID** — Locate and copy your **Profile ID** from the Payment Settings page. This ID is required for API calls that need to specify which merchant profile to use.

<figure><img src="../../../.gitbook/assets/vault-profile-id.png" alt="Payment Settings - Profile ID"><figcaption><p>Navigate to Developers > Payment Settings to access your Profile ID</p></figcaption></figure>

---

## 2. Connecting External Vault Providers

Merchants who want to use a third-party vault (VGS, TokenEx, Voltage, HashiCorp, etc.) alongside Hyperswitch Orchestration can add external vault credentials from the dashboard.

**Steps:**

1. **Navigate to Vault Processor** — In the left-hand navigation menu, select **Connectors > Vault Processor**.
2. **Configure Vault Provider** — Add your third-party vault provider credentials and configuration.

<figure><img src="../../../.gitbook/assets/vault-enable-ext-vault.png" alt="Vault Processor Setup"><figcaption><p>Navigate to Connectors > Vault Processor to configure your third-party vault</p></figcaption></figure>

3. **Enable in Payment Settings** — Navigate to **Developers > Payment Settings**, under **Vault** tab, enable the external vault and choose the vault processor from the dropdown, then click **Update**.

<figure><img src="../../../.gitbook/assets/vault-enable-ext-vault-2.png" alt="Enable Vault in Payment Settings"><figcaption><p>Navigate to Developers > Payment Settings to enable your third-party vault</p></figcaption></figure>

4. Hyperswitch will now route tokenization and de-tokenization through your external vault.

Refer to [SaaS Orchestration with Third-Party Vault](saas-orchestration-with-third-party-vault.md) for the end-to-end payment flow once a provider is connected.

---

## 3. Vault Setup for Platform Organizations

If you operate a **Platform Organization** (multiple Connected merchants under one umbrella), note the following:

- **Vault API keys must be scoped to the correct merchant level.** Platform Merchants should generate a Platform-level Vault API key for managing cross-merchant tokens.
- **Connected merchants share Customer and Payment Method scope** — a `payment_method_id` created for one Connected merchant is accessible to the Platform Merchant and other Connected merchants.
- **Standard merchants maintain isolated vault scope** — their Payment Methods are never shared across merchants in the same organization.

For the full platform setup guide, see [Platform Org and Merchant Setup](../../account-management/multiple-accounts-and-profiles/platform-org-and-merchant-setup.md).

---

## 5. Quick Reference: Required Headers for Vault API Calls

```bash
# All Vault API requests require:
Authorization: api-key=<YOUR_VAULT_API_KEY>   # Generated from Vault section on dashboard
x-profile-id: <YOUR_PROFILE_ID>               # Found under Developers → Profile
Content-Type: application/json
```

**Sandbox base URL:** `https://sandbox.hyperswitch.io`

**Production base URL:** `https://api.hyperswitch.io`
