# Self-Hosted Orchestration with Outsourced PCI Vault

> **Deployment Model:** Merchant self-hosts Hyperswitch · **PCI Scope:** Outsourced to an external vault provider

### Overview

In this deployment model, merchants **self-host** the Hyperswitch orchestration layer on their own infrastructure while **outsourcing** all PCI DSS responsibilities to an external, PCI-compliant vault provider. Sensitive cardholder data (PAN, CVV, expiry) never touches the merchant's servers — instead, Hyperswitch routes all sensitive data operations through a **Vault Proxy** that handles tokenization and detokenization on behalf of the merchant.

This architecture gives merchants full control over orchestration logic, routing rules, and business configurations while eliminating the burden of achieving and maintaining PCI DSS Level 1 compliance in-house.

### Why This Model?

| Concern                     | How It's Addressed                                                                             |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| **PCI Compliance**          | Fully offloaded to the vault provider (Juspay Vault, VGS, Tokenex, etc.)                       |
| **Hosting Independence**    | Merchant retains complete control of the Hyperswitch deployment                                |
| **Sensitive Data Exposure** | Raw card data never enters the merchant's environment                                          |
| **Token Portability**       | `payment_method_id` unifies `vault_token` + `psp_token` + `customer_id` for cross-platform use |
| **Operational Simplicity**  | No need to manage HSMs, key rotation, or cardholder data environments                          |

### Vault Provider Options

#### 1. Juspay Hosted Vault

Juspay provides a fully managed, PCI DSS Level 1 certified vault with native Hyperswitch integration.

**Key benefits:**

* **Prebuilt connector** — Juspay Vault ships as a first-class vault connector inside Hyperswitch. Minimal configuration is needed.
* **Token lifecycle management** — Automatic handling of token creation, refresh, expiry, and deletion.
* **Vault Proxy endpoint** — Juspay Vault exposes a proxy endpoint that transparently replaces `vault_token` references with raw card data before forwarding requests to the PSP.
* **Network tokenization support** — Optionally leverage network tokens (Visa/Mastercard token services) for improved authorization rates.
* **Seamless upgrades** — Token format and security patches are managed by Juspay, requiring no action from the merchant.

**When to use:** Merchants who want a turnkey, zero-maintenance vault with the tightest integration to Hyperswitch.

#### 2. Third-Party Vaults (VGS, Tokenex, and others)

Merchants who already have an existing relationship with a third-party vault — or have regulatory/vendor requirements to use a specific provider — can integrate via the **Vault Proxy API** pattern.

**Supported providers include (but are not limited to):**

* **VGS (Very Good Security)** — Provides inbound/outbound proxy routes for card data. Hyperswitch sends PSP payloads through VGS's forward proxy, which replaces tokens with raw card data in transit.
* **Tokenex** — Offers a transparent gateway proxy. Hyperswitch sends tokenized payloads to Tokenex's proxy, which detokenizes and forwards to the PSP.
* **Any vault with a proxy/detokenize API** — Hyperswitch's modular vault architecture supports any vault that exposes a tokenize + proxy (or detokenize) HTTP API.

**When to use:** Merchants with existing vault contracts, multi-provider strategies, or specific compliance requirements that mandate a particular vault vendor.

### Architecture

```
┌─────────────┐        ┌──────────────────────┐        ┌─────────────────┐        ┌───────┐
│  End User /  │        │  Hyperswitch          │        │  External Vault  │        │  PSP  │
│  Browser/SDK │        │  (Self-Hosted)        │        │  (Juspay/VGS/   │        │       │
│              │        │                      │        │   Tokenex)       │        │       │
└──────┬───────┘        └──────────┬───────────┘        └────────┬────────┘        └───┬───┘
       │                           │                              │                    │
       │  1. Card details          │                              │                    │
       │  ───────────────────────► │                              │                    │
       │                           │                              │                    │
       │                           │  2. Tokenize card            │                    │
       │                           │  ──────────────────────────► │                    │
       │                           │                              │                    │
       │                           │  3. vault_token              │                    │
       │                           │  ◄────────────────────────── │                    │
       │                           │                              │                    │
       │                           │  4. PSP payload with         │                    │
       │                           │     vault_token (via proxy)  │                    │
       │                           │  ──────────────────────────► │                    │
       │                           │                              │                    │
       │                           │                              │  5. Detokenize &   │
       │                           │                              │     forward to PSP │
       │                           │                              │  ────────────────► │
       │                           │                              │                    │
       │                           │                              │  6. PSP response   │
       │                           │                              │  ◄──────────────── │
       │                           │                              │                    │
       │                           │  7. Payment result +         │                    │
       │                           │     psp_token                │                    │
       │                           │  ◄────────────────────────── │                    │
       │                           │                              │                    │
       │  8. payment_method_id     │                              │                    │
       │  ◄─────────────────────── │                              │                    │
       │                           │                              │                    │
```

### Integration Options

Hyperswitch supports **three integration patterns** when self-hosting with an outsourced vault. Each pattern varies in where card data is captured and who manages the vault SDK.

#### Option 1: Hyperswitch SDK + External Vault (Server-Side Tokenization)

In this approach, the **Hyperswitch SDK** captures card details from the end user. The Hyperswitch backend then tokenizes the card with the external vault **server-side** before (or after) processing the payment.

**New User Payment Flow**

1. The merchant loads the [Hyperswitch Payments SDK](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment) via a [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) request. The end user enters their card details.
2. The Hyperswitch SDK sends a [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request containing the raw card data to the self-hosted Hyperswitch backend.
3. Hyperswitch constructs the PSP payload and sends it to the downstream PSP for authorization.
4. Once the PSP responds with `approved` or `declined` (along with a `psp_token`), Hyperswitch sends the card data to the external vault for tokenization.
5. The external vault returns a `vault_token`.
6. Hyperswitch generates a `payment_method_id` — a universal token that links together:
   * `customer_id`
   * `vault_token`
   * `psp_token`
7. The `payment_method_id` is returned to the merchant via webhooks.

**Repeat User Payment Flow**

1. On repeat visits, the Hyperswitch SDK loads the customer's saved payment methods using the `customer_id` from the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) request.
2. The end user selects a saved payment method and enters their CVV.
3. The SDK sends a [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request.
4. Hyperswitch resolves the `payment_method_id` to retrieve the associated `vault_token`.
   * Hyperswitch uses the **detokenize** flow to exchange the `vault_token` for the raw card from the external vault.
   * The raw card is included in the PSP payload and sent to the downstream PSP.

**Merchant-Initiated Transaction (MIT) Flow**

1. The merchant triggers an [MIT or Recurring transaction](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments) using the `payment_method_id`.
2. Hyperswitch resolves the `payment_method_id` → `vault_token` → detokenizes via the vault → sends the raw card to the PSP.

> **Note:** In this pattern, raw card data transits through the self-hosted Hyperswitch server briefly during the first payment. If the merchant wants to avoid this entirely, see **Option 2** or **Option 3** below.

#### Option 2: Hyperswitch SDK Loading External Vault SDK (Client-Side Tokenization)

In this approach, the **External Vault SDK** is layered directly onto the Hyperswitch Unified Checkout SDK. The vault SDK captures and tokenizes card details **on the client side**, ensuring that **sensitive card data never touches the Hyperswitch server**.

**New User Payment Flow**

1. The merchant loads the [Hyperswitch Payments SDK](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment) via a [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) request. The Hyperswitch SDK in turn loads the external vault SDK configured in the merchant account.
2. The end user enters their card details directly into the external vault SDK's secure iframe/fields.
3. The external vault SDK tokenizes the card and returns a `vault_token` along with card metadata (last four digits, card brand, expiry) to the Hyperswitch SDK.
4. The Hyperswitch SDK sends a [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request containing the `vault_token` and card metadata to the self-hosted Hyperswitch backend.
5. Hyperswitch constructs the PSP payload using the `vault_token`.
6. The PSP payload (containing the `vault_token`) is sent to the **Proxy endpoint** of the external vault.
7. The external vault replaces the `vault_token` with the raw card data and forwards the request to the PSP.
8. The PSP responds with `approved` or `declined` along with a `psp_token`. The vault proxy relays this response back to Hyperswitch.
9. Hyperswitch generates a `payment_method_id` linking `customer_id`, `vault_token`, and `psp_token`.
10. The `payment_method_id` and `vault_token` are returned to the merchant via webhooks.

**Repeat User Payment Flow**

1. The Hyperswitch SDK loads stored payment methods using the `customer_id` from the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) request.
2. The end user selects a saved card and enters their CVV.
3. The SDK sends a [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request.
4. Hyperswitch resolves the `payment_method_id` to identify the associated `vault_token`.
   * Hyperswitch uses the **detokenize** flow to obtain the raw card in exchange for the `vault_token`, then sends the raw card credentials to the PSP downstream.

**Merchant-Initiated Transaction (MIT) Flow**

1. The merchant triggers an [MIT or Recurring transaction](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments) using the `payment_method_id`.
2. Hyperswitch resolves the token chain and processes the payment via the vault proxy.

> **Recommended for:** Merchants who want the convenience of the Hyperswitch Unified Checkout while ensuring zero PCI scope on their self-hosted infrastructure.

#### Option 3: External Vault SDK & Storage (Merchant-Managed Client)

The merchant integrates the external vault SDK **directly** (independent of Hyperswitch) and manages the card capture experience entirely on their own. The vault tokenizes the card, and the merchant passes the resulting token and metadata to Hyperswitch for payment processing.

**New User Payment Flow**

1. The merchant loads the external vault SDK in their checkout page.
2. The end user enters their card details directly in the external vault SDK.
3. The external vault SDK tokenizes the card and returns a `vault_token` and associated card metadata.
4. The merchant calls the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) to send the `vault_token` and card metadata to the self-hosted Hyperswitch backend.
5. Hyperswitch constructs the PSP payload using the `vault_token`.
6. The PSP payload (containing the `vault_token`) is sent to the **Proxy endpoint** of the external vault.
7. The external vault replaces the `vault_token` with the raw card and forwards the request to the PSP.
8. The PSP responds with `approved` or `declined` along with a `psp_token`. The vault proxy relays this response back to Hyperswitch.
9. Hyperswitch generates a `payment_method_id` linking `customer_id`, `vault_token`, and `psp_token`.
10. The `payment_method_id` and `vault_token` are returned to the merchant via webhooks.

**Repeat User Payment Flow**

1. The merchant retrieves the customer's stored payment methods using the [Payment Method — List Customer Saved Payment Methods](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--list-customer-saved-payment-methods-v1) API with the `customer_id`.
2. The end user selects a saved card and enters their CVV directly into elements provided by the external vault SDK.
3. The external vault tokenizes the CVV temporarily and returns a `temp_vault_token`.
4. The merchant calls the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) with the `vault_token` (for the card) and the `temp_vault_token` (for the CVV).
5. Hyperswitch constructs the PSP payload using both tokens.
6. The PSP payload (containing `vault_token` + `temp_vault_token`) is sent to the **Proxy endpoint** of the external vault.
7. The external vault replaces `vault_token` with the raw card and `temp_vault_token` with the CVV, then forwards the full payload to the PSP.
8. The PSP responds and the vault proxy relays the result back to Hyperswitch.

**Merchant-Initiated Transaction (MIT) Flow**

1. The merchant triggers an [MIT or Recurring transaction](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments) using the `vault_token` directly (since the merchant manages the vault relationship).

> **Best for:** Merchants with existing vault integrations who want to bring their own checkout UX and vault SDK.

### Key Concepts

#### `payment_method_id`

A **universal, portable token** generated by Hyperswitch that serves as the single reference for a stored payment method. It connects:

| Entity        | Description                                                         |
| ------------- | ------------------------------------------------------------------- |
| `customer_id` | The Hyperswitch customer identifier                                 |
| `vault_token` | The token issued by the external vault representing the stored card |
| `psp_token`   | The token issued by the PSP after a successful transaction          |

This abstraction allows merchants to:

* Switch PSPs without re-collecting card data.
* Switch vault providers without breaking existing customer references.
* Use a single identifier across all payment flows (first-time, repeat, MIT/recurring).

#### Vault Proxy

The **Vault Proxy** is an HTTP endpoint provided by the external vault (Juspay, VGS, Tokenex, etc.) that acts as a transparent man-in-the-middle:

1. Hyperswitch sends the PSP-bound request to the vault proxy endpoint instead of the PSP directly.
2. The proxy inspects the payload, replaces all `vault_token` references with the corresponding raw card data.
3. The proxy forwards the enriched payload to the actual PSP endpoint.
4. The PSP response is relayed back through the proxy to Hyperswitch.

This pattern ensures that:

* The self-hosted Hyperswitch server **never sees or handles raw card data** (in Options 2 and 3).
* The merchant's PCI scope is reduced to **SAQ-A** or **SAQ A-EP** level.
* No changes are needed on the PSP side — the PSP receives a standard card-present payload.

#### Tokenization vs. Detokenization

| Operation      | Description                                                     | When Used                                                                           |
| -------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Tokenize**   | Exchange raw card data for a `vault_token`                      | During the first payment or card-on-file enrollment                                 |
| **Detokenize** | Exchange a `vault_token` for raw card data                      | During repeat payments (when the PSP doesn't support network/vault tokens natively) |
| **Proxy**      | Vault transparently replaces tokens in a PSP payload in transit | During both first and repeat payments (Options 2 & 3)                               |

***

### Supported Advanced Flows

#### Proxy Payments

Hyperswitch supports **Proxy Payments** in this model — where the merchant provides pre-tokenized card data (from their vault) and Hyperswitch routes it through the vault proxy to the appropriate PSP. This is useful for:

* Merchants migrating from another orchestrator who already have vault tokens.
* Server-to-server payment flows where no SDK is involved.
* B2B payment scenarios with stored corporate cards.

#### Guest Checkout Tokenization

Even in guest checkout scenarios (where no `customer_id` exists upfront), Hyperswitch can:

1. Process the payment using the vault proxy pattern.
2. Optionally create a `customer_id` post-payment and associate the `vault_token` with it.
3. Return a `payment_method_id` so the merchant can prompt the guest to save their card for future use.

#### Recurring Payments & Subscriptions

The `payment_method_id` (or `vault_token` in Option 3) can be used for:

* **Customer-Initiated Transactions (CIT):** Repeat payments where the customer is present and selects a saved card.
* **Merchant-Initiated Transactions (MIT):** Subscription renewals, usage-based billing, or scheduled charges where no customer interaction is required.
* **Network Token-based Recurring:** If the vault supports network tokenization, Hyperswitch can leverage network tokens for improved authorization rates on recurring payments.

***

### Configuration Guide

#### Configuring the External Vault in Hyperswitch

To enable an external vault with your self-hosted Hyperswitch instance:

1. **Navigate to the Hyperswitch Dashboard:** `Orchestrator → Connector → Vault Processor`
2. **Select your vault provider** (Juspay Vault, VGS, Tokenex, or Custom).
3.  **Enter the required API credentials:**

    | Provider         | Required Credentials                                  |
    | ---------------- | ----------------------------------------------------- |
    | **Juspay Vault** | API Key, Merchant ID, Vault URL                       |
    | **VGS**          | Vault ID, Username, Password, Route ID                |
    | **Tokenex**      | Token Scheme, API Key, Tokenex ID                     |
    | **Custom**       | Tokenize URL, Detokenize URL, Proxy URL, Auth Headers |
4. **Configure the Vault Proxy route** — Map the PSP endpoints that should be proxied through the vault.
5. **Test the integration** — Use the Hyperswitch test mode to verify tokenize → proxy → PSP flows end-to-end.

#### Environment Variables (Self-Hosted)

When self-hosting, ensure the following environment configuration in your `config/development.toml` (or equivalent):

```toml
[vault]
# Enable external vault integration
enabled = true

# Vault provider: "juspay", "vgs", "tokenex", or "custom"
provider = "juspay"

# Base URL for the vault API
base_url = "https://vault.juspay.in"

# Base URL for the vault proxy endpoint
proxy_url = "https://proxy.vault.juspay.in"
```

> **Important:** Vault credentials should be stored securely (e.g., via environment variables or a secrets manager) and never committed to version control.

***

### Comparison: Self-Hosted Vault Deployment Models

| Feature                    | Self-Hosted + In-House PCI | Self-Hosted + Outsourced PCI (This Model) | SaaS + Outsourced PCI     |
| -------------------------- | -------------------------- | ----------------------------------------- | ------------------------- |
| **Hosting**                | Merchant                   | Merchant                                  | Juspay (SaaS)             |
| **PCI Scope**              | Merchant (Level 1)         | Vault Provider                            | Juspay + Vault Provider   |
| **Vault**                  | Merchant's own vault       | Juspay / VGS / Tokenex                    | Juspay / VGS / Tokenex    |
| **Card Data on Server**    | Yes                        | No (Options 2 & 3)                        | No                        |
| **Orchestration Control**  | Full                       | Full                                      | Managed                   |
| **Setup Complexity**       | High                       | Medium                                    | Low                       |
| **Compliance Maintenance** | High                       | Low                                       | None                      |
| **Token Portability**      | Depends                    | Yes (`payment_method_id`)                 | Yes (`payment_method_id`) |

***

### Security Considerations

* **TLS Everywhere:** All communication between Hyperswitch, the vault, and PSPs must use TLS 1.2+.
* **Credential Rotation:** Regularly rotate vault API keys and proxy credentials.
* **Audit Logging:** Enable Hyperswitch audit logs for all vault operations (tokenize, detokenize, proxy calls) to maintain compliance evidence.
* **Network Segmentation:** Even though PCI is outsourced, restrict network access between your Hyperswitch deployment and the vault to only the required endpoints and ports.
* **Webhook Verification:** Always verify webhook signatures for `payment_method_id` callbacks to prevent spoofing.

***

### FAQ

**Q: Does raw card data ever touch my self-hosted Hyperswitch server?** A: In **Option 1** (server-side tokenization), yes — briefly during the first payment before the card is tokenized. In **Options 2 and 3**, no — the card is tokenized on the client side or by the vault SDK before it reaches your server.

**Q: Can I switch vault providers without affecting existing customers?** A: Yes. Since Hyperswitch uses `payment_method_id` as the universal reference, you can migrate vault tokens between providers. Hyperswitch will update the internal mapping from `payment_method_id` → new `vault_token`.

**Q: What PCI SAQ level applies to me in this model?** A: Typically **SAQ A-EP** (if you host the checkout page) or **SAQ A** (if the vault SDK iframe handles all card input). Consult your QSA for a definitive assessment.

**Q: Is Juspay Vault free for self-hosted Hyperswitch users?** A: Refer to [Hyperswitch pricing](https://hyperswitch.io/pricing) or contact the Juspay team for vault pricing details.

**Q: Can I use multiple vault providers simultaneously?** A: Hyperswitch's modular vault architecture supports configuring multiple vault connectors. You can route different merchants or payment methods to different vaults based on your business logic.

***

### Related Documentation

* [Vault — Modular Vaulting in Hyperswitch](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault)
* [SaaS Orchestration with Third-Party Vault](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/saas-orchestration-with-third-party-vault)
* [Payments SDK Integration](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment)
* [Recurring Payments](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments)
* [PCI DSS 4.0 Compliance](https://hyperswitch.io/pci.pdf)
