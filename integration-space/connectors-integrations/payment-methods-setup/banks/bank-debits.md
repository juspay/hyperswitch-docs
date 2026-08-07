---
description: Bank Debits payment method
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/banks/bank-debits
---

# Bank Debits

{% hint style="info" %}
Bank debits pull funds directly from the customer's bank account. Customers provide their bank account information and agree to a mandate to debit their account at specified intervals and amount.
{% endhint %}

Bank Debits enables merchants to directly pull funds from the customers' bank accounts once the customers provide authorization for the same. It is primarily used for recurring transactions/mandates and for large ticket transactions like rent, fees, etc.

Bank debits are delayed notification payment methods (it might take up to 2-7 days for the payment status to be updated).

### Payments Flow

a. Customer selects bank debit on the checkout page

b. They are shown a form to enter their bank details followed by a checkbox to authorize the merchant to debit their bank account later. This authorization from the customer is called mandate

c. The customers are notified about the mandate setup and every time funds are debited from their account

d. The merchant can opt for microdeposits (only on Stripe) or allow the customer to link their bank account in order to verify the authenticity of the bank details.

| **Bank** **Debits** | **Supported Customer Countries** | **Supported Currencies** |
| ------------------- | -------------------------------- | ------------------------ |
| ACH                 | United States                    | USD                      |
| SEPA                | EU                               | EUR                      |
| BACS                | UK                               | GBP                      |
| BECS                | Australia                        | AUD                      |

Juspay Hyperswitch currently supports the following Bank Direct Debits:

### ACH

US based Bank Debit payment method that is extensively used for recurring payments use cases where payments from customers with US bank accounts are debited through the Automated Clearing House (ACH) payments system operated by Nacha.

Since ACH Direct Debit is a delayed notification payment method, it can take up to 4 business days for the payment status to be updated.

### SEPA

SEPA allows direct bank debits payment for EUR denominated bank accounts in the SEPA region (list of countries). The customer accepts a mandate that authorizes the merchant to debit the account.

Since SEPA Direct Debit is a delayed notification payment method, it can take up to 14 business days for the payment status to be updated after initiating a debit from the customer's account.

### BACS

BACS is a popular bank debit payment method for customers with UK bank accounts where the customers authorize a mandate for debit through the Bankers' Automated Clearing Services (BACS).

Since BACS Direct Debit is a delayed notification payment method, it can take up to 6 business days for the payment status to be updated after initiating a debit from the customer's account.

### BECS

BECS is a bank debit that is used for recurring payments for customers with Australian bank accounts who authorize a mandate for debit through the Bulk Electronic Clearing System (BECS).

Since BECS Direct Debit is a delayed notification payment method, it can take up to 3 business days for the payment status to be updated after initiating a debit from the customer's account.

---

### Connector Capability Matrix

Sourced from each connector's `SupportedPaymentMethods` implementation in `crates/hyperswitch_connectors`.

| Debit Rail | Connectors | Mandates | Refunds | Settlement Timeline |
| --- | --- | --- | --- | --- |
| **ACH** | Stripe, Adyen, GoCardless | ✓ (all) | ✓ | Up to 4 business days |
| **SEPA** | Stripe, Adyen, GoCardless, Mollie | Stripe ✓ · Adyen ✓ · GoCardless ✓ · Mollie ✗ | ✓ | Up to 14 business days |
| **BACS** | Stripe, Adyen | ✓ (both) | ✓ | Up to 6 business days |
| **BECS** | Stripe, GoCardless | ✓ (both) | ✓ | Up to 3 business days |

{% hint style="info" %}
Settlement is delayed because bank debit rails (ACH, SEPA, BACS, BECS) operate on batch clearing cycles — they are not real-time rails. The payment status in Hyperswitch reflects the current state on the rail and updates via webhooks as the processor receives confirmation from the clearing house.
{% endhint %}

---

### Mandate Lifecycle

Bank debits in Hyperswitch are mandate-first: every bank debit — including a one-time debit — requires a mandate to be established before funds can be pulled.

**Step 1 — Create mandate (CIT)**

Send `setup_future_usage: off_session` on the initial payment. The customer completes bank account authorization (form + consent checkbox, or Open Banking AIS account linking). A `mandate_id` is returned on success.

```json
{
  "payment_method": "bank_debit",
  "payment_method_data": {
    "bank_debit": {
      "ach_bank_debit": {
        "account_number": "000123456789",
        "routing_number": "110000000",
        "card_holder_name": "John Doe",
        "bank_account_holder_name": "John Doe",
        "bank_name": "ACH",
        "bank_type": "Checking",
        "bank_holder_type": "Personal"
      }
    }
  },
  "setup_future_usage": "off_session",
  "customer_id": "cus_xyz"
}
```

**Step 2 — Subsequent debits (MIT)**

Use the returned `mandate_id` for all future charges. The customer is not involved.

```json
{
  "mandate_id": "man_xyz",
  "off_session": true,
  "customer_id": "cus_xyz",
  "amount": 5000,
  "currency": "USD"
}
```

**Webhook events to expect**

| Event | Meaning |
| --- | --- |
| `payment_processing` | Debit submitted to the clearing house — not yet confirmed |
| `payment_succeeded` | Funds confirmed received |
| `payment_failed` | Debit returned (insufficient funds, account closed, etc.) |
| `mandate_active` | Mandate successfully established |
| `mandate_revoked` | Customer cancelled the mandate at their bank |

---

### Common Failure Modes

**Debit returned (R-code / SEPA return)**
Symptom: Payment shows `payment_processing` then transitions to `payment_failed` after 1–4 days. Fix: The customer's bank returned the debit — check the return reason code (`insufficient_funds`, `account_closed`, `no_mandate`). For recurring mandates, do not retry automatically on `account_closed` or `no_mandate`; contact the customer to re-establish the mandate.

**Mandate not established before MIT charge**
Symptom: MIT charge fails with `mandate_not_found` or `invalid_mandate`. Fix: A mandate must be created via a CIT with `setup_future_usage: off_session` before any MIT charge. Verify `mandate_id` is from the original consent capture and belongs to the same customer.

**Payment remains in `processing` beyond expected window**
Symptom: Payment does not update after the settlement timeline passes. Fix: Bank debits are cleared in batches — status updates arrive via webhooks, not synchronous API polling. Ensure your webhook endpoint is configured and reachable. Contact your connector if the window has passed without a webhook event.
