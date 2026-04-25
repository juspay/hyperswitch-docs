---
description: Accept crypto payments on your application
icon: bitcoin-sign
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/crypto
---

# Crypto

Juspay Hyperswitch enables crypto payments—a modern way to pay using digital currencies like Bitcoin, Ethereum, and Litecoin. It's fast, cost-effective, and private compared to traditional payment methods. Crypto payments use blockchain technology to record transactions securely and transparently without the need for intermediaries like banks.

### How does a crypto payment work?

1. The customer selects the crypto payment option on the merchant's checkout page
2. The customer is redirected to the cryptocurrency wallet to complete the payment
3. The wallet generates a payment request and displays the payment amount and recipient's public address
4. The customer confirms the transaction in their wallet and sends the payment to the recipient's public address on the cryptocurrency network
5. Once the payment is confirmed and processed by the cryptocurrency network, the merchant can access the payment in their cryptocurrency wallet

### Configuring Crypto on Juspay Hyperswitch

You can configure Crypto on Juspay Hyperswitch by following the steps mentioned below:

1. Configure Crypto on the processor
2. Login to [Hyperswitch dashboard](https://app.hyperswitch.io/)
3. In the Connectors tab, select your processor
4. Enable currency as Crypto

**Note:** Billing address first name and description are mandatory fields for Crypto

---

### Connector Capability Matrix

Sourced from each connector's `SupportedPaymentMethods` implementation in `crates/hyperswitch_connectors`.

| Connector | Crypto Type | Mandates | Refunds | Notes |
| --- | --- | --- | --- | --- |
| **OpenNode** | CryptoCurrency (Bitcoin) | ✗ | ✗ | Bitcoin Lightning and on-chain; final settlement is irreversible on-chain |
| **Coinbase Commerce** | CryptoCurrency | ✗ | ✗ | Multi-currency (BTC, ETH, USDC, and others); Coinbase settles in fiat or crypto |

{% hint style="info" %}
Crypto payments are non-reversible at the network level — once a transaction is confirmed on-chain, funds cannot be clawed back. Hyperswitch does not support automated refunds for crypto payments. Any customer resolution must be handled out-of-band (manual crypto transfer or fiat refund).
{% endhint %}

---

### Common Failure Modes

**Payment not confirmed after customer sends funds**
Symptom: Payment remains in `processing` state even after the customer's wallet shows a completed transaction. Fix: On-chain Bitcoin and Ethereum transactions require network confirmations before a processor marks the payment settled. OpenNode and Coinbase wait for a minimum confirmation count (typically 1–3 blocks). This can take minutes to over an hour during network congestion. Ensure your webhook endpoint is configured to receive the `payment.succeeded` event.

**Wrong amount or currency received**
Symptom: Payment marked failed due to amount mismatch. Fix: Crypto payment amounts are denominated in the fiat currency you specified; the processor converts at the time of invoice creation. If the customer delays the transfer, exchange rate drift can cause an underpayment. Some processors (e.g., Coinbase) accept payments within a tolerance window — check the connector's documentation for underpayment handling.

**Billing address missing**
Symptom: Payment create call returns a validation error before reaching the processor. Fix: `billing.address.first_name` and `description` are mandatory for all crypto payments in Hyperswitch. Ensure these fields are present on every `POST /payments` call for crypto.
