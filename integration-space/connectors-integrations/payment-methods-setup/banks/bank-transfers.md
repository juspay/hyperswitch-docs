---
description: Bank Transfer payment methods
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/banks/bank-transfers
---

# Bank Transfers

{% hint style="info" %}
Bank transfers allow customers to push funds from their bank account to the merchant's.
{% endhint %}

Bank Transfers are a popular way of transmitting money between different bank accounts and they are popular in US, EU and few Asian and LATAM countries. They are primarily used by businesses for accepting large payments from other businesses. Bank transfers are also used by consumers in certain countries as a preferred method for transferring money to others and while transacting online.

### Payment Flow in Bank Transfers

1. Customers select a Bank Transfer method on your checkout page
2. You request Juspay Hyperswitch to initiate a Bank Transfer payment
3. Hyperswitch connects to one of your preferred payment processors for Bank transfers to initiate Bank transfer. Then, Hyperswitch shares the processor's response which contains Virtual bank account details and instructions for the customers to transfer money and complete the payment
4. Customers instruct their bank through in-person visit/phone/website/app to transfer money to the account number mentioned in the instructions in the above step. It takes up to 5 days for the transaction to be settled
5. After the customer's bank transfers the money, the processor notifies Hyperswitch of the transaction's status, following which Hyperswitch notifies your server through Webhooks.

Hyperswitch supports the following Bank Transfers:

* ACH Bank Transfer in US
* SEPA Bank Transfer in EU
* BACS Bank Transfer in UK
* Multibanco in EU (Portugal)
* All Indonesian bank transfers

---

### Connector Capability Matrix

Sourced from each connector's `SupportedPaymentMethods` implementation in `crates/hyperswitch_connectors`.

| Transfer Method | Connectors | Mandates | Refunds | Region / Use Case |
| --- | --- | --- | --- | --- |
| **ACH Bank Transfer** | Stripe | ✗ | ✓ | United States |
| **SEPA Bank Transfer** | Stripe | ✗ | ✓ | EU / EUR-denominated |
| **BACS Bank Transfer** | Stripe | ✗ | ✓ | United Kingdom |
| **Multibanco** | Stripe | ✗ | ✓ | Portugal (EU) |
| **Permata VA** | Adyen | ✗ | ✓ | Indonesia |
| **BCA VA** | Adyen | ✗ | ✓ | Indonesia |
| **BNI VA** | Adyen | ✗ | ✓ | Indonesia |
| **BRI VA** | Adyen | ✗ | ✓ | Indonesia |
| **CIMB VA** | Adyen | ✗ | ✓ | Indonesia |
| **Danamon VA** | Adyen | ✗ | ✓ | Indonesia |
| **Mandiri VA** | Adyen | ✗ | ✓ | Indonesia |
| **Pix** | Adyen | ✗ | ✓ | Brazil |

{% hint style="info" %}
Bank transfers are push-based — the customer must initiate the transfer from their own bank after receiving the virtual account details. Hyperswitch does not pull funds; it provides the transfer instructions and listens for settlement confirmation via webhooks.
{% endhint %}

---

### Payment Flow Detail

**Step 1 — Create payment**
Call `POST /payments` with `payment_method: bank_transfer` and the relevant subtype (e.g., `ach`, `sepa_bank_transfer`, `bni_va`). Hyperswitch creates the payment and returns a virtual account number or reference code.

**Step 2 — Display instructions to customer**
The API response contains the virtual account details (account number, sort code, bank name, or reference). Display these on your confirmation page or email them to the customer. For Indonesian VAs, the customer has a time window (typically 24 hours) to complete the transfer.

**Step 3 — Wait for settlement webhook**
The customer initiates the transfer from their bank. Once the processor receives confirmation from the banking network, Hyperswitch fires a `payment.succeeded` webhook. Settlement can take up to 5 business days depending on the rail.

---

### Common Failure Modes

**Payment expires before customer transfers**
Symptom: Payment status transitions to `payment.failed` with a timeout reason. Fix: Virtual account numbers are time-limited on most processors (especially Indonesian VAs). Display the expiry time prominently and resend reminder instructions if needed. Do not reuse the same virtual account after expiry — create a new payment.

**Payment succeeded webhook not received**
Symptom: Customer completes the transfer but payment status never updates. Fix: Confirm the Hyperswitch webhook endpoint is configured and publicly reachable on the processor dashboard. Bank transfers update exclusively via webhooks — polling the payment status synchronously will not reflect settlement. Check the webhook delivery log in the Hyperswitch control center.

**Wrong transfer details sent to customer**
Symptom: Customer transfers to an incorrect account or uses wrong reference. Fix: Always display the virtual account details returned in the API response for that specific payment. Do not cache or reuse virtual account numbers across payments — they are unique per transaction.
