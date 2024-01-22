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

You would need to set up a dedicated HTTPS or HTTP endpoint on your server with a URL as a webhook listener that will receive push notifications in the form of a POST request with JSON payload from the Hyperswitch server.

#### Configure your webhook endpoint on Hyperswitch Dashboard

Configure the above endpoint on your Hyperswitch dashboard under Settings -> Webhooks.

#### Update Hyperswitch’s webhook endpoints on your connector Dashboard

In order for Hyperswitch to receive updates from the connectors you have selected, you would need to update Hyperswitch’s corresponding endpoints on your respective connector dashboard instead of your webhook endpoints.

Hyperswitch's webhook endpoint format is as specified below, or you can obtain the endpoint from the control center under the Processors tab.

| Environment | Webhook Endpoint                                                          |
| ----------- | ------------------------------------------------------------------------- |
| Sandbox     | sandbox.hyperswitch.io/webhooks/`{merchant_id}`/`{merchant_connector_id}` |
| Production  | api.hyperswitch.io/webhooks/`{merchant_id}`/`{merchant_connector_id}`     |

### [​](https://api-reference.hyperswitch.io/essentials/webhooks#handling-webhooks)Handling Webhooks <a href="#handling-webhooks" id="handling-webhooks"></a>

* Below are list of events for which you will receive the webhooks:
  1. `payment_succeeded`
  2. `payment_failed`
  3. `payment_processing`
  4. `payment_cancelled`
  5. `payment_authorized`
  6. `payment_captured`
  7. `action_required`
  8. `refund_succeeded`
  9. `refund_failed`
  10. `dispute_opened`
  11. `dispute_expired`
  12. `dispute_accepted`
  13. `dispute_cancelled`
  14. `dispute_challenged`
  15. `dispute_won`
  16. `dispute_lost`
  17. `mandate_active`
  18. `mandate_revoked`

Click [**here**](https://juspay-78.mintlify.app/api-reference/schemas/outgoing--webhook) to see the webhook payload your endpoint would need to parse for each of the above events

### Webhook Signature Verification

While creating a business\_profile, you can specify a secret key in the `payments_response_hash_key` field, which will be used for signing webhook deliveries. If not specified, a 64-character long randomized key with high entropy will be generated for you. Ensure that you store the secret key in a secure location that your server can access.\
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



* **Return a 2xx response:** Your server must return a successful 2xx response on successful receipt of webhooks.&#x20;
