---
description: >-
  Distribute funds programmatically to bank accounts, cards, and wallets via
  Hyperswitch's unified payout infrastructure, with smart routing, bulk
  operations, and independent tokenization.
icon: file-invoice-dollar
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/connectors/payouts
---

<!-- truth manifest; hyperswitch 6fd72e5e6653326acaaf19b5f6aa76a524ff202e; spec api-reference/v1/openapi_spec_v1.json@6fd72e5e6653326acaaf19b5f6aa76a524ff202e
     symbols: PayoutConnectors = crates/api_models/src/enums.rs:46-70
     symbols: PayoutType = crates/common_enums/src/enums.rs:9081-9090
     symbols: PayoutMethodData = crates/api_models/src/payouts.rs:252-261
     symbols: BankTransfer payout_method_type = crates/api_models/src/payouts.rs:421-434
     symbols: recurring saved-method validation = crates/router/src/core/payouts/validator.rs:77-92
     absent: native payout schedule = checked crates/api_models/src/payouts.rs, crates/router/src/routes/app.rs:1639-1689, and crates/router/src/core/payouts; not found outside payout sync scheduling
     derived: 21 payout connectors = variants in PayoutConnectors, source crates/api_models/src/enums.rs:48-70
     checked: 2026-09-21 -->

# Payout Processors

### Overview

The Juspay Hyperswitch Payouts infrastructure allows you to programmatically distribute funds to third parties, including affiliates, contractors, and merchants, across a variety of payment methods. By integrating with global processors, Hyperswitch helps you manage the entire payout lifecycle from a single point of control.

* **Automate at scale:** Orchestrate high-volume bulk payouts. Schedule when each payout is created from your application.
* **Optimize reliability:** Use [smart retries](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/smart-retries-in-payout) and routing to minimize failed transfers.
* **Maintain compliance:** Reduce your PCI burden with secure, [processor-agnostic tokenization](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation).
* **Unified visibility:** Track every payout across different regions and connectors in one dashboard.

<figure><img src="../../.gitbook/assets/payouts.png" alt=""><figcaption></figcaption></figure>

### Key Features

#### High-velocity distribution

Move funds to bank accounts, cards, or digital wallets through your preferred connectors. Whether you are using funds collected through Hyperswitch or external sources, our API ensures a seamless transfer experience.

#### Intelligence and routing

Maximize payout success with [Smart Retries](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/smart-retries-in-payout). If a payout fails due to a temporary connector error, Hyperswitch automatically retries the transaction through the most viable path, ensuring your partners get paid on time without manual intervention.

#### Flexible data handling

* **Independent Tokenization:** Securely store card and bank data using our processor-independent vault. This gives you the flexibility to switch payout partners without losing your users' payment credentials.
* **Bulk Operations:** Effortlessly manage large-scale disbursements by uploading `.xlsx` or `.csv` files directly via the dashboard.
* **Account Verification:** Ensure the validity of recipient bank accounts through Stripe or other supported verification providers.

### Supported payout connectors

The payout connector enum defines **21** wire values: `adyen`, `adyenplatform`, `cybersource`, `deutschebank`, `ebanx`, `gigadat`, `gotyme_sanlam`, `loonio`, `nomupay`, `nuvei`, `payone`, `paypal`, `stripe`, `truelayer`, `trustly`, `wise`, `worldpay`, `worldpayxml`, `envoy`, `itaubank`, and `santander`. See the [`PayoutConnectors` enum and its `snake_case` serialization](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/enums.rs#L46-L70).

Helcim is not a payout processor in this list. Connector-specific payment methods can differ, so check the relevant payout processor page before integration.

### Payout fields and wire values

Use these request values when you create or update a payout:

* `payout_type`: `card`, `bank`, `wallet`, or `bank_redirect`. These values come from [`PayoutType` with `snake_case` serialization](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/common_enums/src/enums.rs#L9081-L9090).
* `payout_method_data`: `card`, `bank`, `wallet`, `bank_redirect`, `passthrough`, or `bank_transfer`. These values come from [`PayoutMethodData` with `snake_case` serialization](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/payouts.rs#L252-L261).
* For `bank_transfer`, `payout_method_type`: `ach`, `bacs`, `sepa`, `pix`, `pix_key`, `pix_emv`, `trustly`, `open_banking`, `payshap`, or `payshap_proxy`. The field is the tagged discriminator on [`BankTransfer`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/payouts.rs#L421-L434).

Crypto assets are not modeled as payout methods. This includes USDT. The payout method enums have no crypto or USDT wire value.

### FAQ

**Can I use Hyperswitch solely for payouts without payments?**

Yes. Hyperswitch is modular. You can use our infrastructure to handle payouts independently of your payment collection. You can initiate payouts via direct payment info or by using an existing Token ID.


**Can Hyperswitch schedule recurring payouts?**

The payout service can reuse a saved payout method for a later payout, but your application must decide when to create each payout. The create validator treats a request with `payout_method_id` as a recurring payout and requires `confirm: true`; it does not define a schedule or recurrence interval. See the [`validate_create_request` check](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/router/src/core/payouts/validator.rs#L77-L92). Follow [Payouts with Saved Payment Methods](get-started-with-payouts/process-payouts-using-saved-payment-methods.md) for method reuse.

**What is the benefit of independent tokenization?**

It prevents vendor lock-in. By tokenizing sensitive data independently of the underlying processor, you retain ownership of your data and can route payouts to any supported connector without asking your users to re-enter their information.
