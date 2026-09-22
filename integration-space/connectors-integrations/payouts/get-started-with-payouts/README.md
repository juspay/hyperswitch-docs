---
description: >-
  Learn how to configure payout processors and process payouts via the
  Hyperswitch Dashboard and API.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/connectors/payouts/get-started-with-payouts
---

<!-- truth manifest; hyperswitch 6fd72e5e6653326acaaf19b5f6aa76a524ff202e; spec api-reference/v1/openapi_spec_v1.json@6fd72e5e6653326acaaf19b5f6aa76a524ff202e
     symbols: PayoutCreateRequest.payout_type = crates/api_models/src/payouts.rs:88-94
     symbols: PayoutMethodData = crates/api_models/src/payouts.rs:252-261
     symbols: BankTransfer payout_method_type = crates/api_models/src/payouts.rs:421-434
     symbols: POST /payouts/create = crates/router/src/routes/app.rs:1639-1641
     absent: native payout schedule = checked crates/api_models/src/payouts.rs and crates/router/src/routes/app.rs:1639-1689, not found
     checked: 2026-09-21 -->

# Payout features

To begin processing payouts with Juspay Hyperswitch, you must first establish accounts with your [supported payout processors](https://juspay.io/integrations).

The following diagram illustrates the interaction between your application, the Hyperswitch orchestration layer, and the underlying payout processors.

<figure><img src="../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

### Configuration Resources

Implementation requires the Hyperswitch Dashboard for configuration and the API for transaction processing.

* API Endpoint (Sandbox): `https://sandbox.hyperswitch.io`
* Hyperswitch Dashboard: [app.hyperswitch.io](https://app.hyperswitch.io)
* Technical Reference: [Payouts API Reference](https://api-reference.hyperswitch.io/v1/payouts/payouts--create)

### Prerequisites

Complete these checks before following the walkthrough:

1. Confirm payouts are enabled for your account. If the **Payout Processors** tab is not visible, contact support before continuing.
2. Create or sign in to the payout processor accounts you plan to use.
3. Create an API key in the Dashboard **Developers** section.
4. Copy your Merchant ID from the Dashboard home page.
5. Configure at least one payout processor and enable the payout methods you intend to use.

### Request field guide

The create request uses `payout_type` for the method family and `payout_method_data` for the details:

* `payout_type`: `card`, `bank`, `wallet`, or `bank_redirect`, serialized in `snake_case` by [`PayoutType`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/common_enums/src/enums.rs#L9081-L9090).
* `payout_method_data`: `card`, `bank`, `wallet`, `bank_redirect`, `passthrough`, or `bank_transfer`, serialized in `snake_case` by [`PayoutMethodData`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/payouts.rs#L252-L261). The source marks `bank` deprecated and points new integrations at `bank_transfer`.
* With `bank_transfer`, `payout_method_type` is `ach`, `bacs`, `sepa`, `pix`, `pix_key`, `pix_emv`, `trustly`, `open_banking`, `payshap`, or `payshap_proxy`. These are the tagged wire values on [`BankTransfer`](https://github.com/juspay/hyperswitch/blob/6fd72e5e6653326acaaf19b5f6aa76a524ff202e/crates/api_models/src/payouts.rs#L421-L434).

Crypto assets, including USDT, are not payout method values in these enums.

#### Configuring Payout Processors

Log in to the [Hyperswitch Dashboard](https://app.hyperswitch.io) and follow these steps to connect your processors.

1.  **Navigate to Payout Processors:** Select the **Payout Processors** tab from the sidebar, then choose a processor from the supported list to open the configuration modal.

    <figure><img src="../../../.gitbook/assets/image (37).png" alt=""><figcaption><p>Payout Processors list</p></figcaption></figure>
2.  **Provide Credentials:** Enter the authentication keys required by the specific processor to enable communication.

    <figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption><p>Configuring auth keys for communicating with the processor</p></figcaption></figure>
3.  **Enable Payment Methods:** Select the specific payout methods (e.g., Bank Transfer, Cards) you intend to use for this processor.

    <figure><img src="../../../.gitbook/assets/image (44).png" alt=""><figcaption><p>Keep preferred payment methods enabled</p></figcaption></figure>
4.  **Confirm Configuration:** Once saved, the processor will appear as "Active" in your list.

    <figure><img src="../../../.gitbook/assets/image (66).png" alt=""><figcaption><p>Successfully configured!</p></figcaption></figure>

#### Processing Payouts via API

For testing and initial integration, you can use the [Hyperswitch Postman Collection](https://www.postman.com/hs-payouts/hyperswitch/collection/u6uep7u/payouts-w-hyperswitch).

1.  **Import Collection:** Download and import the collection into your Postman workspace.

    <figure><img src="../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption><p>Import postman collection</p></figcaption></figure>
2.  **Configure Environment Variables:** In the **Variables** tab, set the following parameters:

    * `baseUrl`: `https://sandbox.hyperswitch.io`
    * `merchant_id`: Your unique merchant identifier.
    * `api_key`: Your Hyperswitch API secret key.

    <figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption><p>Updating env variables in postman collection</p></figcaption></figure>
3. **Execute Payout:** Navigate to the **Process Payouts** section of the collection to send a `POST` request to the `/payouts/create` endpoint.

{% content-ref url="process-payouts-using-saved-payment-methods.md" %}
[process-payouts-using-saved-payment-methods.md](process-payouts-using-saved-payment-methods.md)
{% endcontent-ref %}
