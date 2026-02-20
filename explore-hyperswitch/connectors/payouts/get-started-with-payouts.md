---
icon: flag-checkered
---

# Getting Started with Payouts

To begin processing payouts with Hyperswitch, you must first establish accounts with your [supported payout processors](https://juspay.io/integrations).

## Overview

The following diagram illustrates the interaction between your application, the Hyperswitch orchestration layer, and the underlying payout processors.

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

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

Navigate to Payout Processors: Select the Payout Processors tab from the sidebar and Select Processor: Choose a processor from the supported list to open the configuration modal.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Payout Processors list</p></figcaption></figure>

Provide Credentials: Enter the authentication keys required by the specific processor to enable communication.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption><p>Configuring auth keys for communicating with the processor</p></figcaption></figure>

Enable Payment Methods: Select the specific payout methods (e.g., Bank Transfer, Cards) you intend to use for this processor.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption><p>Keep preferred payment methods enabled</p></figcaption></figure>

Confirm Configuration: Once saved, the processor will appear as "Active" in your list.

<figure><img src="../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption><p>Successfully configured!</p></figcaption></figure>

#### Processing Payouts via API

For testing and initial integration, you can use the [Hyperswitch Postman Collection](https://www.postman.com/hs-payouts/hyperswitch/collection/u6uep7u/payouts-w-hyperswitch).

Import Collection: Download and import the collection into your Postman workspace.

<figure><img src="../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption><p>Import postman collection</p></figcaption></figure>

Configure Environment Variables: In the Variables tab, set the following parameters:

* `baseUrl`: `https://sandbox.hyperswitch.io`
* `merchant_id`: Your unique merchant identifier.
* `api_key`: Your Hyperswitch API secret key.

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption><p>Updating env variables in postman collection</p></figcaption></figure>

Execute Payout: Navigate to the Process Payouts section of the collection to send a `POST` request to the `/payouts/create` endpoint.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-10-18 at 12.10.26 PM.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="process-payouts-using-saved-payment-methods.md" %}
[process-payouts-using-saved-payment-methods.md](process-payouts-using-saved-payment-methods.md)
{% endcontent-ref %}
