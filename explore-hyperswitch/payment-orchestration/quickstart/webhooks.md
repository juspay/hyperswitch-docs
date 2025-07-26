---
icon: anchor
description: Configure outgoing webhooks from Hyperswitch
---

# Webhooks

Webhooks are HTTP-based real-time push notifications that **Hyperswitch** uses to communicate instant status updates to your server. They are essential in payment processing for several reasons:

- **Prevent transaction delays** – Ensuring real-time status updates helps avoid lost revenue in time-sensitive transactions like flight or movie reservations.
- **Ensure accurate payment reconciliation** – Handling cases where a payment status changes from "Failed" to "Succeeded."
- **Enhance user experience** – Real-time updates enable seamless order fulfillment and improve customer satisfaction.

## Configuring Webhooks

### 1. Create a Webhook Listener on Your Server
To receive webhook events from Hyperswitch, you must create an **HTTP or HTTPS endpoint** that listens for incoming `POST` requests containing JSON payloads.

#### Example: Basic Webhook Listener in Node.js (Express)
```javascript
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
    console.log('Received webhook:', req.body);
    res.sendStatus(200);
});

app.listen(3000, () => console.log('Webhook listener running on port 3000'));
```
This endpoint will receive JSON payloads from Hyperswitch and log them for processing.

### 2. Configure Webhooks on the Hyperswitch Dashboard

Go to **Developer → Payment Settings** in the Hyperswitch Dashboard, select your business profile, and configure the webhook settings by providing your endpoint URL.

### 3. Add Custom HTTP Headers (Optional)
If your webhook endpoint requires custom HTTP headers for authentication, you can specify them in the **Webhook Setup** section.

<figure><img src="../../../../.gitbook/assets/Webhook-custom-HTTP-headers.png" alt="Webhook Custom Headers"></figure>

### 4. Register Hyperswitch Webhooks in Your Connector Dashboard
For Hyperswitch to receive updates from payment connectors, you must update the webhook endpoint in the respective connector dashboard.

**Webhook Endpoint Format:**

| Environment | Webhook Endpoint |
|------------|----------------|
| Sandbox | `https://sandbox.hyperswitch.io/webhooks/{merchant_id}/{merchant_connector_id}` |
| Production | `https://api.hyperswitch.io/webhooks/{merchant_id}/{merchant_connector_id}` |

## Handling Webhooks

### Webhook Events
You will receive webhooks for the following events:

| Event Name | Description |
|------------|-------------|
| `payment_succeeded` | Payment was successful. |
| `payment_failed` | Payment attempt failed. |
| `payment_processing` | Payment is in progress. |
| `payment_cancelled` | Payment was canceled. |
| `payment_authorized` | Payment was authorized but not captured. |
| `payment_captured` | Payment was successfully captured. |
| `action_required` | Additional user action is needed. |
| `refund_succeeded` | Refund was processed successfully. |
| `refund_failed` | Refund attempt failed. |
| `dispute_opened` | A dispute was opened. |
| `dispute_won` | Dispute was won. |
| `dispute_lost` | Dispute was lost. |
| `mandate_active` | Payment mandate is active. |
| `mandate_revoked` | Payment mandate was revoked. |

Refer to the [API reference](https://api-reference.hyperswitch.io/api-reference/schemas/outgoing--webhook) for webhook payload details.

## Webhook Signature Verification
To ensure webhook security, Hyperswitch signs each payload with a **HMAC-SHA512** signature using your `payment_response_hash_key`.

### Signature Generation Process
1. Encode the JSON webhook payload.
2. Generate an **HMAC-SHA512** signature using the payload and your secret key.
3. The signature is included in the `x-webhook-signature-512` header.

#### Example: Verifying Webhook Signature in Python
```python
import hmac
import hashlib
import json

def verify_webhook_signature(payload, secret_key, received_signature):
    computed_signature = hmac.new(secret_key.encode(), json.dumps(payload).encode(), hashlib.sha512).hexdigest()
    return computed_signature == received_signature
```

### Troubleshooting Signature Verification
- Use the `x-webhook-signature-512` header for HMAC-SHA512 verification.
- If your system doesn't support SHA512, use the `x-webhook-signature-256` header for HMAC-SHA256 verification.

## Webhook Delivery Behavior
Hyperswitch expects a **2XX** HTTP response for successful webhook processing. If no `2XX` response is received, it retries webhook delivery for up to **24 hours** with exponential backoff.

| Retry Attempt | Interval |
|--------------|----------|
| 1st         | 1 min    |
| 2nd, 3rd    | 5 min    |
| 4th–8th     | 10 min   |
| 9th–13th    | 1 hour   |
| 14th–16th   | 6 hours  |

### Handling Duplicates
Since webhook retries can result in duplicate events, you should track the `event_id` in your system to prevent duplicate processing.

#### Example: Deduplicating Webhooks in Python
```python
import redis

db = redis.Redis()

def process_webhook(event_id, data):
    if db.get(event_id):
        print("Duplicate event. Skipping...")
        return
    db.set(event_id, 1, ex=86400)  # Store for 24 hours
    print("Processing webhook:", data)
```

### Handling Out-of-order Webhooks

Hyperswitch may deliver webhooks to your application in any order. This could be due to network delays or webhook delivery failures. However, you can handle this by examining the `updated` field of the resource sent in the webhook request body. For every change made to a specific resource, the `updated` field for the resource will be updated with the timestamp at which the update happened, and thus, the time at which the original webhook was triggered.

For example, if you wish to sync resource changes from Hyperswitch to your application, you could:

1. Obtain the value (`timestamp1`) of the `updated` field of the resource in the webhook request body.
2. Obtain the value (`timestamp2`) of the `updated` field of the resource stored on your side.
3. If `timestamp1` > `timestamp2`, process the resource; otherwise, ignore.

## Testing Webhooks

Before going live, test your webhooks using tools like below. They provide you with a public HTTP endpoint for receiving event payloads, inspecting and routing them to the localhost/development box.

| Tool | Description |
|------|-------------|
| [Beeceptor](https://beeceptor.com/) | You can receive payloads for discovery and routing to the localhost service in real-time. Free to use. |
| [RequestBin by Pipedream](https://pipedream.com/requestbin) | You can receive and inspect HTTP requests in real-time. Free to use. |

You can configure Hyperswitch to send test webhooks to these services and inspect the payloads before deploying them to production.
