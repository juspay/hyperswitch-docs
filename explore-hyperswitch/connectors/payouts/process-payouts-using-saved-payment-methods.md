---
icon: repeat
---

# Payouts with Saved Payment Methods

Hyperswitch allows you to store payment method details in a secure, PCI-compliant card vault for subsequent payout processing. By utilizing stored credentials, you can programmatically list a customer’s saved methods and retrieve a `payment_token` to initiate payouts without re-collecting sensitive information.

#### Tokenizing Payment Methods

Payment methods are persisted in the [Hyperswitch Vault](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault) through two primary entry points:

* Pre-transaction storage: Create a payment method for a specific customer using the [/payment\_methods API](https://api-reference.hyperswitch.io/v1/payment-methods/paymentmethods--create). This action stores details directly in the secure locker.
* Post-transaction storage: Details are automatically vaulted following a successful transaction if specific flags are set:
  * For payments: Set `"setup_future_usage": "off_session"`.
  * For payouts: Set `"recurring": true`.

#### Retrieving Saved Methods

To process a payout, fetch the identifiers for a customer’s saved methods via the [List Payment Methods API](https://api-reference.hyperswitch.io/v1/payment-methods/payment-method--retrieve#payment-method-retrieve). The response includes a `payment_token` required for transaction processing.

#### Executing the Payout

The `payment_token` is passed in the [Payouts Create](https://api-reference.hyperswitch.io/v1/payouts/payouts--create#payouts-create) request to trigger the fund transfer using the customer's vaulted credentials.

### Setup and Integration

Utilize the Hyperswitch Dashboard and the specialized Postman collection to test vaulted payout flows.

* Sandbox Endpoint: `https://sandbox.hyperswitch.io`
* Dashboard: [app.hyperswitch.io](https://app.hyperswitch.io)
* Technical Reference: [Payouts API Reference](https://api-reference.hyperswitch.io/api-reference/payouts/payouts--create)

Prerequisites

Before implementing saved payment method workflows, ensure the following:

* [Payout processors](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/get-started-with-payouts) are configured and active.
* An API Key is generated in the [Developers section](https://www.google.com/search?q=/docs/dashboard/developers) of the dashboard.
* The Merchant ID is retrieved from your [Dashboard home page](https://app.hyperswitch.io).

#### Step-by-Step Implementation

Import Testing Collection

Download and import the [Saved Payment Methods Postman Collection](https://www.postman.com/hs-payouts/hyperswitch/collection/us5vnwo/payout-using-saved-payment-methods).

<figure><img src="../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption><p>Import Postman collection</p></figcaption></figure>

Configure Environment

In the Variables tab of the collection, define the following global parameters:

* `baseUrl`: `https://sandbox.hyperswitch.io`
* `merchant_id`: Your unique identifier.
* `api_key`: Your secret API key.

<figure><img src="../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption><p>Updating env variables in Postman collection</p></figcaption></figure>

Direct Vaulting: Follow the sequence to create a payment method and immediately utilize the resulting token for a payout.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-10-18 at 12.14.40 PM.png" alt=""><figcaption></figcaption></figure>

Recurring/Subsequent Payouts: Follow the sequence to list existing customer payment methods and process a payout using a previously stored token.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-10-18 at 12.14.55 PM.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="route-your-payout-transactions-using-smart-router.md" %}
[route-your-payout-transactions-using-smart-router.md](route-your-payout-transactions-using-smart-router.md)
{% endcontent-ref %}
