---
description: >-
  Connect Stripe to Juspay Hyperswitch to accept payments, manage webhooks, and
  enable multiple payment methods through a unified API integration.
metaLinks:
  alternates:
    - stripe.md
---

# Stripe

![Stripe Logo](https://hyperswitch.io/icons/homePageIcons/logos/stripeLogo.svg)

Stripe connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — a single secret key passed as `Authorization: Bearer {secret_key}` on every request. All requests to Stripe are sent as `application/x-www-form-urlencoded` (not JSON), and Hyperswitch pins a specific Stripe API version in the `Stripe-Version` header to ensure consistent behaviour across your integration. Hyperswitch translates its own unified payment intent model into Stripe's PaymentIntent and Charge objects, mapping status transitions bidirectionally on every sync and webhook event.

Stripe is the only connector in Hyperswitch that supports incremental authorization natively alongside a full dispute evidence upload flow — both are part of the same connector implementation and operate independently.

---

### Payment Method Support

The table below reflects what is implemented in the Hyperswitch–Stripe connector. Enable only the methods that are also active in your Stripe dashboard under **Settings → Payment methods** — a mismatch between the two is the most common source of payment failures.

| Payment Method | Type | Mandates | Refunds | Capture Methods |
|---|---|---|---|---|
| Credit Card | Card | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| Debit Card | Card | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| Apple Pay | Wallet | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| Google Pay | Wallet | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| Cash App Pay | Wallet | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| Revolut Pay | Wallet | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| Amazon Pay | Wallet | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| WeChat Pay | Wallet | ✗ | ✓ | Automatic only |
| AliPay | Wallet | ✗ | ✓ | Automatic, Manual, SequentialAutomatic |
| Klarna | Pay Later | ✗ | ✓ | Automatic, Manual, SequentialAutomatic |
| Affirm | Pay Later | ✗ | ✓ | Automatic, Manual, SequentialAutomatic |
| Afterpay / Clearpay | Pay Later | ✗ | ✓ | Automatic, Manual, SequentialAutomatic |
| ACH Direct Debit | Bank Debit | ✓ | ✓ | Automatic only |
| SEPA Direct Debit | Bank Debit | ✓ | ✓ | Automatic only |
| BACS Direct Debit | Bank Debit | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| BECS Direct Debit | Bank Debit | ✓ | ✓ | Automatic, Manual, SequentialAutomatic |
| iDEAL | Bank Redirect | ✓ | ✓ | Automatic only |
| Bancontact | Bank Redirect | ✓ | ✓ | Automatic only |
| Sofort | Bank Redirect | ✓ | ✓ | Automatic only |
| BLIK | Bank Redirect | ✗ | ✓ | Automatic only |
| Giropay | Bank Redirect | ✗ | ✗ | Automatic only |
| Przelewy24 | Bank Redirect | ✗ | ✓ | Automatic only |
| EPS | Bank Redirect | ✗ | ✓ | Automatic only |
| FPX Online Banking | Bank Redirect | ✗ | ✓ | Automatic only |
| ACH Bank Transfer | Bank Transfer | ✗ | ✓ | Automatic only |
| SEPA Bank Transfer | Bank Transfer | ✗ | ✓ | Automatic only |
| BACS Bank Transfer | Bank Transfer | ✗ | ✓ | Automatic only |

Supported card networks: Visa, Mastercard, American Express, Discover, JCB, Diners Club, UnionPay.

`ManualMultiple` and `Scheduled` capture methods are not supported by the Stripe connector.

---

### Advanced Capabilities

**Incremental Authorization**
Stripe supports incremental authorization for card payments. Hyperswitch passes the additional amount via a separate capture call against the original PaymentIntent. This only works when `capture_method` is set to `manual` — incremental authorization against an automatically-captured payment will fail at the Stripe API level.

**Setup Mandate and Recurring Payments**
Stripe stores payment methods as Stripe Customer + PaymentMethod objects. When Hyperswitch sets up a mandate (via `SetupIntent` on Stripe's side), Stripe returns a `payment_method` ID that Hyperswitch stores against the mandate record. Subsequent merchant-initiated transactions (MIT) pass this stored `payment_method` ID directly to Stripe, bypassing any cardholder interaction. Mandate support is available for cards, Apple Pay, Google Pay, ACH, BACS, BECS, SEPA Direct Debit, iDEAL, Bancontact, and Sofort.

**Dispute Evidence Upload**
Hyperswitch supports the full Stripe dispute flow: file upload (multipart, via Stripe's Files API) followed by evidence submission against the dispute ID. Both steps are part of the Hyperswitch unified disputes interface — you do not call Stripe's API directly for dispute management.

**Payouts (Stripe Connect)**
When configured for Stripe Connect, the connector passes the `Stripe-Account` header to route requests to a connected account. Payout operations supported: Create, Fulfill, Cancel, Recipient setup, and Recipient Account setup.

**Webhook Events**
Hyperswitch processes the following Stripe webhook event types: `payment_intent.payment_failed`, `payment_intent.succeeded`, `payment_intent.canceled`, `payment_intent.amount_capturable_updated`, `charge.succeeded`, `charge.refund.updated`, `source.chargeable`, `dispute.created`, and `dispute.closed`. Events outside this list are received but not acted on.

---

### Activating Stripe via Hyperswitch

#### Prerequisites

1. You need to be registered with Stripe. Sign up at [dashboard.stripe.com/register](https://dashboard.stripe.com/register).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Request Stripe support to enable raw card data handling for your Stripe account (see [PCI compliance details](https://docs.hyperswitch.io/security-and-compliance/pci-compliance#docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715-1)). Without this, Hyperswitch cannot pass card data to Stripe directly — all card payments will be declined at the Stripe API level.
4. Enter your Country, Business Label, and Stripe Secret Key in the Hyperswitch control center. The secret key is found in your Stripe dashboard under **Developers → API keys**. Use the **Secret Key**, which starts with `sk_`. Do not use the publishable key (`pk_`) — it does not have the permissions required for server-side payment operations.
5. Select the payment methods you want to use with Stripe. These must match the methods enabled in your Stripe dashboard under **Settings → Payments → Payment methods**.
6. Navigate to **Developers → Webhooks** in your Stripe dashboard and create a new webhook endpoint.

[Steps to activate Stripe on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Configuring Webhooks

Webhook delivery works as a two-hop chain: Stripe delivers events to Hyperswitch, and Hyperswitch forwards them to your endpoint.

**Step 1:** Set up your webhook endpoint on the Hyperswitch dashboard under **Settings → Payment settings → Click on the profile**.

<figure><img src="../../.gitbook/assets/webhook1.png" alt=""><figcaption></figcaption></figure>

**Step 2:** Configure Hyperswitch's webhook endpoint on your Stripe dashboard. You can find Hyperswitch's endpoint for your Stripe account by clicking **Processors → Stripe**.

<figure><img src="../../.gitbook/assets/webhook2.png" alt=""><figcaption></figcaption></figure>

Hyperswitch verifies every incoming Stripe webhook using HMAC-SHA256 against the `Stripe-Signature` header. The signature value is extracted from the `v1` field in that header (format: `t={timestamp},v1={signature}`), and the verification message is constructed as `{timestamp}.{raw_request_body}`. The webhook signing secret used for this verification is the one Stripe shows in **Developers → Webhooks → your endpoint → Signing secret** — this must be stored in Hyperswitch, not the API key.

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, mandate record storage, retry scheduling, webhook fan-out to your endpoint, and unified error code mapping across connectors. **Stripe owns:** charge execution, fraud evaluation (Radar), payment method storage as Customer + PaymentMethod objects, and webhook delivery to Hyperswitch's endpoint. These are independent systems — Stripe does not know about Hyperswitch's routing layer, and Hyperswitch does not participate in Stripe's fraud scoring.

**Hyperswitch owns:** webhook forwarding to your configured endpoint. **Stripe owns:** webhook delivery to Hyperswitch's registered endpoint. If Stripe's webhook does not reach Hyperswitch (network failure, wrong endpoint configured), Hyperswitch has no record of the event and cannot forward it. Payment status will not update automatically in this case — use the sync API to reconcile.

---

### Common Failure Modes

**Raw card data not enabled on Stripe account**
Symptom: Card payments return an error at Stripe before authorization. Stripe declines the request because your account is not permitted to receive raw card numbers. Fix: Contact Stripe support and request that raw card data be enabled for your account before going live.

**Publishable key used instead of secret key**
Symptom: All API calls return HTTP 401 from Stripe. Fix: Replace the key in the Hyperswitch control center with the secret key (`sk_live_...` or `sk_test_...`). The publishable key (`pk_...`) cannot authorize server-side payment operations.

**Webhook signing secret mismatch**
Symptom: Stripe webhooks arrive at Hyperswitch but are rejected — payment and refund statuses do not update asynchronously. Fix: The signing secret in Hyperswitch must match the value shown in Stripe under **Developers → Webhooks → your endpoint → Signing secret**. This is different from the API key and rotates independently.

**Payment method enabled in Hyperswitch but not in Stripe**
Symptom: Payments fail with Stripe error `payment_method_not_available` or similar. Fix: Cross-check the methods selected in the Hyperswitch connector configuration against **Settings → Payments → Payment methods** in your Stripe dashboard.

**Incremental authorization attempted with automatic capture**
Symptom: Incremental authorization call fails. Fix: Incremental authorization requires `capture_method: manual` on the original payment. Automatic capture payments cannot be incrementally authorized — Stripe does not support this combination.

---

The Stripe connector implementation is at `crates/hyperswitch_connectors/src/connectors/stripe.rs`. The webhook signature verification logic, payment method matrix, and Stripe Connect header handling are all defined in the same file and its `transformers/` submodule.
