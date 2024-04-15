---
description: Configure outgoing webhooks from Hyperswitch
---

# 🪝 Webhooks

{% hint style="info" %}
This section covers how you can set up your outgoing webhooks from Hyperswitch
{% endhint %}

Webhooks are HTTP-based real-time push notifications that Hyperswitch would use for instant status communication to your server. Webhooks are vital in payments for the following reasons:

* Preventing merchants from losing business due to delayed status communication (say, in case of flight or movie reservations where there is a need for instant payment confirmation).
* Prevent payment reconciliation issues where payments change from "Failed" to "Succeeded".
* Providing the best payment experience for the end-user by instantly communicating payment status and fulfilling the purchase.

### Configuring Webhooks

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

### Handling Webhooks

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

Click [**here**](https://api-reference.hyperswitch.io/api-reference/schemas/outgoing--webhook) to see the webhook payload your endpoint would need to parse for each of the above events

### Webhook Signature Verification

While creating a business profile, you can specify a secret key in the `payments_response_hash_key` field, which will be used for signing webhook deliveries. If not specified, a 64-character long randomized key with high entropy will be generated for you. Ensure that you store the secret key in a secure location that your server can access.

#### Webhook Signature Generation

Creating a signature for the webhook involves these steps:

* Webhook payload is encoded to JSON string.
* `Hmac-SHA512` signatured is generated using the payload and `payment_response_hash_key`.
* The obtained digest is included as `x-webhook-signature-512` in the headers of the outgoing webhook.

#### Webhook Validation

To validate the webhook’s authenticity:

* Retrieve the content of the webhook and encode it as a JSON string.
* Generate a  `Hmac-SHA512` signature using the payload and `payment_response_hash_key`.
* Compare the obtained digest with the `x-webhook-signature-512` received in the webhook’s header. If the hashes match, the webhook data is untampered and authentic.

#### Troubleshooting Signature Verification Failures

If you are sure that the payload is from Hyperswitch but the signature verification fails:

* Make sure you are using the correct header. Hyperswitch recommends that you use the `x-webhook-signature-512` header, which uses the HMAC-SHA512 algorithm. If your machine does't support HMAC-SHA256,  you can use `x-webhook-signature-256` header, which uses the HMAC-SHA256 algorithm.
* Make sure you are using the correct algorithm. If you are using the `x-webhook-signature-256` header , you should use the HMAC-SHA256 algorithm.

<details>

<summary><strong>Why SHA-512 ?</strong></summary>

SHA-512 is a robust cryptographic hash function designed for security. It generates a fixed-size 512-bit (64-byte) output, making it suitable for tasks such as creating digital signatures, password hashing, and ensuring data integrity.

</details>

### Webhook Delivery Behavior

To consider a webhook delivery as successful, Hyperswitch expects the HTTP status code to be `2XX` from your server.
If Hyperswitch doesn't receive a `2XX` status code, the delivery of the webhook is retried with an increasing delay over the next 24 hours.

The intervals at which webhooks will be retried are:

| Retry Attempt               | Interval    |
| --------------------------- | ----------- |
| 1st                         |  1 minute   |
| 2nd, 3rd                    |  5 minutes  |
| 4th, 5th, 6th, 7th, 8th     | 10 minutes  |
| 9th, 10th, 11th, 12th, 13th |  1 hour     |
| 14th, 15th, 16th            |  6 hours    |

The interval for the first retry attempt in the above table is the duration since the original webhook delivery attempt, while the intervals for the subsequent retry attempts are the durations since the previous webhook delivery attempt.

#### Handling Duplicates

Due to webhook retries, your application may receive the same webhook more than once.
You can handle duplicate deliveries of webhooks by examining the `event_id` field in the request body, which uniquely identifies a webhook event.

For example, your application could do the following for each webhook received:

1. Obtain the `event_id` from the webhook request body and store it in a persistent store such as a relational database or Redis.
2. Check whether the `event_id` has already been processed.
3. If the webhook has not been processed, then process the webhook; otherwise, it is a duplicate event so can be ignored.
4. Also, since the last retry for a webhook delivery happens at around 24 hours after the original webhook trigger, store the processed `event_id`s for at least 24 hours. In other words, you may purge the stored `event_id`s that are more than 24 hours old.

#### Handling Out-of-order Deliveries

Hyperswitch may deliver webhooks to your application in any order.
This could be due to network delays or webhook delivery failures.
However, you can handle this by examining the `updated` field of the resource sent in the webhook request body.
For every change made to a specific resource, the `updated` field for the resource will be updated with the timestamp at which the update happened, and thus, the time at which the original webhook was triggered.

For example, if you wish to sync resource changes from Hyperswitch to your application, you could:

1. Obtain the value (`timestamp1`) of the `updated` field of the resource in the webhook request body.
2. Obtain the value (`timestamp2`) of the `updated` field of the resource stored on your side.
3. If `timestamp1` > `timestamp2`, process the resource; otherwise, ignore.
