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

* **Return a 2xx response:** Your server must return a successful 2xx response on successful receipt of webhooks.&#x20;

### Webhook Signature Verification

While creating a business\_profile, `payments_response_hash_key` can be provided, this is used as a key for signature verification, If not specified, a 64-character long randomized key with high entropy is generated. This key will be used to hash both the redirect payment response and webhooks.\
\
**Webhook Signature Generation**:\
Creating a signature for the webhook involves these steps:

* Webhook payload is encoded to JSON string.
* `Hmac-SHA512` signatured is generated using the payload and `payment_response_hash_key`.
* The obtained digest is included as `x-webhook-signature-512` in the headers of the outgoing webhook.

**Webhook Validation**:\
To validate the webhook’s authenticity:

* Retrieve the content of the webhook and encode it as a JSON string.
* Generate a  `Hmac-SHA512` signature using the payload and payment\_response\_hash\_key.
* Compare the obtained digest with the `x-webhook-signature-512` received in the webhook’s header. If the hashes match, the webhook data is untampered and authentic.



### Troubleshooting

If you are sure that the payload is from Hyperswitch but the signature verification fails:

* Make sure you are using the correct header. Hyperswitch recommends that you use the `x-webhook-signature-512` header, which uses the HMAC-SHA512 algorithm. If your machine does't support HMAC-SHA256,  you can use `x-webhook-signature-256` header, which uses the HMAC-SHA256 algorithm&#x20;
* Make sure you are using the correct algorithm. If you are using the `x-webhook-signature-256` header , you should use the HMAC-SHA256 algorithm.

<details>

<summary><strong>Why SHA-512 ?</strong></summary>

SHA-512 is a robust cryptographic hash function designed for security. It generates a fixed-size 512-bit (64-byte) output, making it suitable for tasks such as creating digital signatures, password hashing, and ensuring data integrity.

</details>

