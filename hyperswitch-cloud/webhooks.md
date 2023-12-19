---
description: Configure outgoing webhooks from Hyperswitch
---

# 🪝 Webhooks

{% hint style="info" %}
This section covers how you can set up your outgoing webhooks from Hyperswitch
{% endhint %}

Webhooks are HTTP-based real-time push notifications that Hyperswitch would use for instant status communication to your server. Webhooks are vital in payments for the following reasons:

* Preventing merchants from losing business due to delayed status communication (say, in case of flight or movie reservations where there is a need for instant payment confirmation).
* Prevent payment reconciliation issues where payments change from “Failed” to “Succeeded”.
* Providing the best payment experience for the end-user by instantly communicating payment status and fulfilling the purchase.

### [​](https://api-reference.hyperswitch.io/essentials/webhooks#configuring-webhooks)Configuring Webhooks <a href="#configuring-webhooks" id="configuring-webhooks"></a>

#### Create an endpoint on your server

You would need to set up a dedicated HTTPS or HTTP endpoint on your server with a URL as a webhook listener that will receive push notifications in the form of a POST request with JSON payload from the Hyperswitch server2

#### Update your webhook endpoint on Hyperswitch Dashboard

Update the above endpoint on your Hyperswitch dashboard under Settings -> Webhooks3

#### Update Hyperswitch’s webhook endpoints on your connector Dashboard

In order for Hyperswitch to receive updates from the connectors you have selected, you would need to update Hyperswitch’s corresponding endpoints on your respective connector dashboard instead of your webhook endpoints

Hyperswitch’s webhook endpoint format is as follows:

| Environment | Webhook Endpoint                                                   |
| ----------- | ------------------------------------------------------------------ |
| Sandbox     | sandbox.hyperswitch.io/webhooks/`{merchant_id}`/`{connector_name}` |
| Production  | api.hyperswitch.io/webhooks/`{merchant_id}`/`{connector_name}`     |

### [​](https://api-reference.hyperswitch.io/essentials/webhooks#handling-webhooks)Handling Webhooks <a href="#handling-webhooks" id="handling-webhooks"></a>

* **Select the events for Webhooks:** On the same page on the dashboard, select the events for which you would like to receive notifications. Currently, Webhooks are available on Hyperswitch for the following events:
  1. payment\_succeeded
  2. payment\_failed
  3. payment\_processing
  4. action\_required
  5. refund\_succeeded
  6. refund\_failed
  7. dispute\_opened
  8. dispute\_expired
  9. dispute\_accepted
  10. dispute\_cancelled
  11. dispute\_challenged
  12. dispute\_won
  13. dispute\_lost

Click [**here**](https://juspay-78.mintlify.app/api-reference/schemas/outgoing--webhook) to see the webhook payload your endpoint would need to parse for each of the above events

* **Return a 2xx response:** Your server must return a successful 2xx response on successful receipt of webhooks.
* **Retries:** In case of 3xx, 4xx, or 5xx response or no response from your endpoint for webhooks, Hyperswitch has a retry mechanism that tries sending the webhooks again up to 3 times before marking the event as failed.
