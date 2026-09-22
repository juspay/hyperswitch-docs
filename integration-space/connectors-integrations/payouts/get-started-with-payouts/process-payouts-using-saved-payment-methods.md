---
description: >-
  Store and reuse customer payment methods for payout processing using
  Hyperswitch's secure, PCI-compliant vault and token-based API flows.
icon: repeat
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/connectors/payouts/process-payouts-using-saved-payment-methods
---

<!-- truth manifest; hyperswitch 6fd72e5e6653326acaaf19b5f6aa76a524ff202e; spec api-reference/v1/openapi_spec_v1.json@6fd72e5e6653326acaaf19b5f6aa76a524ff202e
     symbols: recurring true vaults the method after a successful payout, when no payout_method_id was supplied = crates/router/src/core/payouts.rs:3123-3143
     symbols: supplying payout_method_id without confirm true is rejected = crates/router/src/core/payouts/validator.rs:77-92
     symbols: payout_token and payout_method_id are mutually exclusive, and payout_method_id requires customer context whose customer_id must match the stored method = crates/router/src/core/payouts/validator.rs:171-200
     symbols: the create request carries payout_token and payout_method_id, and no payment_token; payment_token is the list response field = crates/api_models/src/payouts.rs:169,209
     absent: recurring schedule interval = checked crates/api_models/src/payouts.rs and crates/router/src/routes/app.rs:1639-1689, not found
     checked: 2026-09-21 -->

# Payouts with Saved Payment Methods

Juspay Hyperswitch allows you to store payment method details in a secure, PCI-compliant card vault for subsequent payout processing. By utilizing stored credentials, you can programmatically list a customer's saved methods and retrieve a `payment_token` to initiate payouts without re-collecting sensitive information.

### Tokenizing Payment Methods

Payment methods are persisted in the [Hyperswitch Vault](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault) through two primary entry points:

* Pre-transaction storage: Create a payment method for a specific customer using the [/payment\_methods API](https://api-reference.hyperswitch.io/v1/payment-methods/paymentmethods--create). This action stores details directly in the secure locker.
* Post-transaction storage: Details are automatically vaulted following a successful transaction if specific flags are set:
  * For payments: Set `"setup_future_usage": "off_session"`.
  * For payouts: set `"recurring": true`. The method is vaulted after the payout succeeds, at [`payouts.rs`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/router/src/core/payouts.rs#L3123-L3143), which saves to the locker when `recurring` is set and no `payout_method_id` was supplied.

Reusing a vaulted method is the other half of this and is covered under [Recurring/Subsequent Payouts](#recurring-subsequent-payouts): pass the stored `payout_method_id` and set `confirm` to `true`. [`validate_create_request`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/router/src/core/payouts/validator.rs#L77-L92) rejects a payout that supplies `payout_method_id` without `confirm: true`.

### Retrieving Saved Methods

To process a payout, fetch the identifiers for a customer's saved methods via the [List Payment Methods API](https://api-reference.hyperswitch.io/v1/payment-methods/payment-method--retrieve#payment-method-retrieve). The response includes a `payment_token`.

### Executing the Payout

The field names differ between the two calls. The list response calls it `payment_token`; [Payouts Create](https://api-reference.hyperswitch.io/v1/payouts/payouts--create#payouts-create) has no `payment_token` field. Send that value as **`payout_token`** instead.

There are two ways to reference a vaulted method, and they are mutually exclusive. [`validate_create_request`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/router/src/core/payouts/validator.rs#L171-L200) rejects a request carrying both.

Either way the request needs customer context. Supplying `payout_token` with no customer or `customer_id` is rejected with a missing-field error naming exactly that ([`validator.rs`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/router/src/core/payouts/validator.rs#L211-L218)), and the `payout_method_id` path additionally checks that the stored method's `customer_id` matches.

* **`payout_token`**, the value the list response returned as `payment_token` ([`PayoutCreateRequest`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/payouts.rs#L169)).
* **`payout_method_id`** ([`PayoutCreateRequest`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/payouts.rs#L209)), which additionally needs `confirm: true`. The validator looks the stored method up and rejects the payout if its `customer_id` does not match the customer on the request.

### Setup and Integration

Utilize the Hyperswitch Dashboard and the specialized Postman collection to test vaulted payout flows.

* Sandbox Endpoint: `https://sandbox.hyperswitch.io`
* Dashboard: [app.hyperswitch.io](https://app.hyperswitch.io)
* Technical Reference: [Payouts API Reference](https://api-reference.hyperswitch.io/v1/payouts/payouts--create)

### Prerequisites

Before implementing saved payment method workflows, ensure the following:

* [Payout processors](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/get-started-with-payouts) are configured and active.
* An API Key is generated in the [Developers section](https://www.google.com/search?q=/docs/dashboard/developers) of the dashboard.
* The Merchant ID is retrieved from your [Dashboard home page](https://app.hyperswitch.io).

### Step-by-Step Implementation

#### Import Testing Collection

Download and import the [Saved Payment Methods Postman Collection](https://www.postman.com/hs-payouts/hyperswitch/collection/us5vnwo/payout-using-saved-payment-methods).

<figure><img src="../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption><p>Import Postman collection</p></figcaption></figure>

#### Configure Environment

In the Variables tab of the collection, define the following global parameters:

* `baseUrl`: `https://sandbox.hyperswitch.io`
* `merchant_id`: Your unique identifier.
* `api_key`: Your secret API key.

<figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption><p>Updating env variables in Postman collection</p></figcaption></figure>

#### Direct Vaulting

Follow the sequence to create a payment method and immediately utilize the resulting token for a payout.

#### Recurring/Subsequent Payouts

Follow the sequence to list existing customer payment methods and process a payout using a previously stored token.

{% content-ref url="route-your-payout-transactions-using-smart-router.md" %}
[route-your-payout-transactions-using-smart-router.md](route-your-payout-transactions-using-smart-router.md)
{% endcontent-ref %}
