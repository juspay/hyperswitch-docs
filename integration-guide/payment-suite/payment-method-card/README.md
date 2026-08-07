---
description: >-
  Vault a payment method first, then use the token to execute payments via
  Server-to-Server API — giving you granular control over the payment lifecycle
icon: hand-holding-circle-dollar
metaLinks:
  alternates:
    - ./
---

# Vault-Then-Pay

{% hint style="info" %}
**Choose this path when** you want to use the SDK exclusively for vaulting/storing card details. The actual payment is then executed via S2S API calls from your backend using the resulting `payment_method_id` token.

If you want payment and vaulting to happen together in a single SDK flow, see [Pay-Then-Vault](../payments/).
{% endhint %}

### The Two-Step Pattern

1. **Vault** — Capture card details using the [Vault SDK](https://docs.hyperswitch.io/integration-guide/workflows/vault/integration/sdk-integration) or the [Server-to-Server API](https://docs.hyperswitch.io/integration-guide/workflows/vault/integration/server-to-server-vault-tokenization). This generates a `payment_method_id`.
2. **Pay** — Pass the `payment_method_id` into the `/payments` API (or the Proxy endpoint) from your backend to execute the transaction.

### Payment Method Lifecycle

The `payment_method_id` is a unique, reusable token that maps a `customer_id` to a specific payment instrument (card, wallet, bank account). The same instrument from the same customer always resolves to the same ID.

| Customer ID | Payment Instrument        | Payment Method ID |
| ----------- | ------------------------- | ----------------- |
| 123         | Visa ending in 4242       | `PM1`             |
| 123         | Mastercard ending in 1111 | `PM2`             |
| 456         | Visa ending in 4242       | `PM3`             |
| 123         | PayPal (`user@email.com`) | `PM4`             |

### Integration Options in This Section

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Token Led Payment</strong></td><td>Execute a payment using a <code>payment_method_id</code> via S2S API</td><td><a href="payments.md">payments.md</a></td></tr><tr><td><strong>Proxy Payment</strong></td><td>Send PSP payment requests through the Vault Proxy — raw card data never leaves the Vault</td><td><a href="proxy.md">proxy.md</a></td></tr><tr><td><strong>Payment Methods Management</strong></td><td>Embed the Vault SDK widget to let customers view, add and delete saved cards</td><td><a href="payment-methods-management.md">payment-methods-management.md</a></td></tr></tbody></table>

### Vault Integration Reference

For the full SDK and API setup guides used in this flow, see:

* [Vault SDK Integration](https://docs.hyperswitch.io/integration-guide/workflows/vault/integration/sdk-integration) — React and Vanilla JS step-by-step
* [Server-to-Server Vault Tokenization](https://docs.hyperswitch.io/integration-guide/workflows/vault/integration/server-to-server-vault-tokenization) — direct API tokenization for PCI-certified backends
* Vault Configuration — API key generation and dashboard setup
