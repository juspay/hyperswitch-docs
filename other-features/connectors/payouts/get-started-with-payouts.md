---
description: >-
  Learn how to configure payout processors and process payouts via the
  Hyperswitch Dashboard and API.
icon: flag-checkered
metaLinks:
  alternates:
    - get-started-with-payouts.md
---

# Getting Started with Payouts

To begin processing payouts with Juspay Hyperswitch, you must first establish accounts with your [supported payout processors](https://juspay.io/integrations).

The following diagram illustrates the interaction between your application, the Hyperswitch orchestration layer, and the underlying payout processors.

<figure><img src="../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

### Configuration Resources

Implementation requires the Hyperswitch Dashboard for configuration and the API for transaction processing.

* API Endpoint (Sandbox): `https://sandbox.hyperswitch.io`
* Hyperswitch Dashboard: [app.hyperswitch.io](https://app.hyperswitch.io)
* Technical Reference: [Payouts API Reference](https://api-reference.hyperswitch.io/api-reference/payouts/payouts--create)

#### Prerequisites

Before configuring your first payout, ensure you have the following credentials from your Dashboard:

1. A Hyperswitch account.
2. An API Key (located in the Developers section).
3. Your Merchant ID (available on the Home page).

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
