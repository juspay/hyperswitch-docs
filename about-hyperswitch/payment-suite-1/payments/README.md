---
icon: file-invoice-dollar
---

# Payments Cards

Accept card payments (debit and credit) through Juspay Hyperswitch using any supported card network and payment processor. This guide covers the complete card payment lifecycle including one-time payments, saved cards, recurring payments, and manual capture. **Always use the Hyperswitch SDK for tokenization** to minimize PCI compliance scope—raw card data handling requires SAQ D compliance.

---

## Prerequisites

Before integrating card payments, ensure you have:

### 1. API Keys

- **Publishable Key**: Used in your frontend to initialise the SDK
- **API Key**: Used in your backend for server-to-server API calls

Obtain these from your Hyperswitch Dashboard under **Developers → API Keys**.

### 2. Webhook Endpoint

Configure a webhook endpoint to receive asynchronous payment status updates:

```bash
curl -X POST https://api.hyperswitch.io/v1/webhooks \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "merchant_id": "merchant_12345",
    "webhook_url": "https://your-domain.com/webhooks/hyperswitch",
    "events_enabled": [
      "payment_intent.succeeded",
      "payment_intent.failed",
      "payment_intent.requires_action"
    ]
  }'
```

### 3. SDK Integration

Include the Hyperswitch SDK in your frontend:

```html
<script src="https://checkout.hyperswitch.io/v1/hyper.js"></script>
```

---

## Quick Start

### Step 1: Initialise the SDK

```javascript
const hyper = window.Hyper('pk_test_YOUR_PUBLISHABLE_KEY');
const widgets = hyper.widgets({
  appearance: { theme: 'default' }
});
```

### Step 2: Create a Payment Intent

From your backend, create a payment intent:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345"
  }'
```

**Response:**

```json
{
  "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
  "status": "requires_payment_method",
  "amount": 10000,
  "currency": "USD",
  "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123"
}
```

### Step 3: Mount the Card Element

```javascript
const cardElement = widgets.create('card');
cardElement.mount('#card-element');
```

### Step 4: Confirm the Payment

```javascript
const { error, paymentIntent } = await hyper.confirmPayment({
  clientSecret: clientSecret,
  paymentMethod: {
    card: cardElement,
    billing_details: {
      name: 'John Doe'
    }
  }
});

if (error) {
  console.error('Payment failed:', error.message);
} else if (paymentIntent.status === 'succeeded') {
  console.log('Payment successful!');
}
```

---

## One-Time Payments

For a single, non-recurring payment where the customer enters card details during checkout.

### High-Level Flow

1. Customer enters card details on your checkout page
2. Your frontend securely captures card data using the Hyperswitch SDK
3. SDK tokenizes the card and returns a payment method ID
4. Backend calls `/payments` API with the token
5. Hyperswitch routes to appropriate processor
6. Customer completes 3D Secure authentication if required
7. Payment is authorised and captured

### SDK Tokenization Flow (Recommended)

**⚠️ PCI Compliance Warning:** Always use the SDK tokenization flow to minimise your PCI compliance scope. Handling raw card data requires full SAQ D compliance.

```javascript
// 1. Create payment method using SDK
const { paymentMethod, error } = await hyper.createPaymentMethod({
  type: 'card',
  card: cardElement,
  billing_details: { name: 'John Doe' }
});

// 2. Send payment_method.id to your backend
const response = await fetch('/api/create-payment', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    payment_method_id: paymentMethod.id,
    amount: 10000,
    currency: 'USD'
  })
});
```

Backend:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "confirm": true
  }'
```

**Response:**

```json
{
  "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
  "status": "succeeded",
  "amount": 10000,
  "currency": "USD",
  "payment_method": {
    "type": "card",
    "card": {
      "scheme": "Visa",
      "last4": "1111",
      "exp_month": 12,
      "exp_year": 2025
    }
  },
  "receipt_data": {
    "receipt_number": "RCP_123456789"
  }
}
```

### Raw Card Data Flow (SAQ D Required)

**⚠️ PCI Compliance Warning:** Only use this approach if you have implemented full PCI DSS SAQ D compliance. You are responsible for securely handling sensitive card data.

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_data": {
      "card": {
        "card_number": "4111111111111111",
        "card_exp_month": "12",
        "card_exp_year": "25",
        "card_holder_name": "John Doe",
        "card_cvc": "123"
      }
    },
    "confirm": true
  }'
```

---

## Saved Cards

Use stored card credentials for returning customers without re-entering card details.

### Prerequisites

1. Customer has previously made a payment with card saved (set `setup_future_usage: on_session` or `off_session`)
2. You have the `payment_method_id` from the saved card

### Saving a Card During Payment

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_data": {
      "card": {
        "card_number": "4111111111111111",
        "card_exp_month": "12",
        "card_exp_year": "25",
        "card_holder_name": "John Doe",
        "card_cvc": "123"
      }
    },
    "setup_future_usage": "on_session",
    "confirm": true
  }'
```

**Response:**

```json
{
  "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
  "status": "succeeded",
  "amount": 10000,
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
  "payment_method": {
    "type": "card",
    "card": {
      "scheme": "Visa",
      "last4": "1111",
      "exp_month": 12,
      "exp_year": 2025
    }
  }
}
```

### Paying with a Saved Card

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "payment_method_data": {
      "card": {
        "card_cvc": "123"
      }
    },
    "confirm": true
  }'
```

**Response:**

```json
{
  "payment_id": "pay_bcvwxyabcdefghijklmnopqrstu",
  "status": "succeeded",
  "amount": 10000,
  "currency": "USD",
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz"
}
```

### List Saved Cards for a Customer

```bash
curl -X GET "https://api.hyperswitch.io/v1/payment_methods?customer_id=cust_12345" \
  -H "api-key: YOUR_API_KEY"
```

**Response:**

```json
{
  "data": [
    {
      "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
      "payment_method": "card",
      "card": {
        "scheme": "Visa",
        "last4": "1111",
        "exp_month": 12,
        "exp_year": 2025
      }
    }
  ]
}
```

---

## Recurring Payments

Schedule automatic payments using saved card credentials for subscriptions or instalment payments.

### Setting Up Recurring Payments

1. **Initial Payment with Setup Intent:**

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "setup_future_usage": "off_session",
    "confirm": true
  }'
```

2. **Subsequent Off-Session Payments:**

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -H "X-Idempotency-Key: idem_12345_unique_key" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "off_session": true,
    "confirm": true
  }'
```

**Response:**

```json
{
  "payment_id": "pay_defghijklmnopqrstuvwxyzab",
  "status": "succeeded",
  "amount": 10000,
  "currency": "USD",
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz"
}
```

---

## Manual Capture

For scenarios requiring separate authorisation and capture steps—useful for delayed shipments, pre-orders, or holds.

### Authorisation Only

Creates an authorisation that holds funds but does not capture them:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -H "X-Idempotency-Key: idem_auth_12345" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "capture_method": "manual",
    "confirm": true
  }'
```

**Response:**

```json
{
  "payment_id": "pay_ghijklmnopqrstuvwxyzabcde",
  "status": "requires_capture",
  "amount": 10000,
  "currency": "USD",
  "amount_capturable": 10000,
  "amount_received": 0
}
```

### Capture Later

Captures a previously authorised payment:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments/pay_ghijklmnopqrstuvwxyzabcde/capture \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -H "X-Idempotency-Key: idem_capture_12345" \
  -d '{
    "amount_to_capture": 10000
  }'
```

**Response:**

```json
{
  "payment_id": "pay_ghijklmnopqrstuvwxyzabcde",
  "status": "succeeded",
  "amount": 10000,
  "amount_received": 10000,
  "capture_status": "success"
}
```

### Partial Capture

You can capture less than the authorised amount:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments/pay_ghijklmnopqrstuvwxyzabcde/capture \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount_to_capture": 8000
  }'
```

**Response:**

```json
{
  "payment_id": "pay_ghijklmnopqrstuvwxyzabcde",
  "status": "partially_captured",
  "amount": 10000,
  "amount_capturable": 2000,
  "amount_received": 8000
}
```

---

## 3D Secure (3DS) Handling

3D Secure authentication may be required for certain transactions based on regulatory requirements (e.g., PSD2 Strong Customer Authentication).

### When 3DS is Triggered

- Regulatory requirements (PSD2 in Europe)
- Issuer's risk assessment
- High-value transactions
- Merchant configuration

### Handling 3DS in SDK

The SDK automatically handles 3DS authentication flows:

```javascript
const { error, paymentIntent } = await hyper.confirmPayment({
  clientSecret: clientSecret,
  paymentMethod: { card: cardElement }
});

if (paymentIntent.status === 'requires_action') {
  // SDK automatically presents 3DS challenge
  // Wait for user to complete authentication
}
```

### 3DS Response States

| Status | Description | Action |
|--------|-------------|--------|
| `requires_action` | 3DS challenge pending | SDK handles redirect/challenge |
| `succeeded` | 3DS completed, payment successful | Proceed with order fulfilment |
| `failed` | 3DS failed or abandoned | Prompt customer to retry |

### Server-Side 3DS Handling

If implementing 3DS manually (not recommended):

```bash
curl -X POST https://api.hyperswitch.io/v1/payments/pay_abc123/confirm \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "payment_method": "card",
    "client_secret": "pay_abc123_secret_xyz"
  }'
```

**Response (when 3DS is required):**

```json
{
  "payment_id": "pay_abc123",
  "status": "requires_action",
  "next_action": {
    "type": "three_ds_invoke",
    "three_ds_invoke": {
      "three_ds_authentication_url": "https://acs.bank.com/3ds/challenge"
    }
  }
}
```

---

## Error Handling

### Common Card Errors

| Error Code | Description | Action |
|------------|-------------|--------|
| `card_declined` | Card was declined by issuer | Ask customer to use different card or contact bank |
| `insufficient_funds` | Card has insufficient funds | Ask customer to use different card |
| `expired_card` | Card has expired | Ask customer to check expiry or use different card |
| `incorrect_cvc` | CVC code is incorrect | Ask customer to re-enter CVC |
| `processing_error` | Generic processing error | Retry the payment |
| `authentication_required` | 3DS authentication required | Initiate 3DS flow |
| `issuer_unavailable` | Card issuer temporarily unavailable | Retry after a short delay |

### Error Response Example

```json
{
  "error": {
    "type": "card_error",
    "code": "card_declined",
    "decline_code": "insufficient_funds",
    "message": "Your card was declined.",
    "payment_id": "pay_abcdefghijklmnopqrstuvwxyz"
  }
}
```

### Error Handling Example (JavaScript)

```javascript
try {
  const { error, paymentIntent } = await hyper.confirmPayment({
    clientSecret: clientSecret,
    paymentMethod: { card: cardElement }
  });

  if (error) {
    switch (error.code) {
      case 'card_declined':
        showMessage('Your card was declined. Please try a different card.');
        break;
      case 'insufficient_funds':
        showMessage('Insufficient funds. Please try a different card.');
        break;
      case 'expired_card':
        showMessage('Your card has expired. Please check the expiry date.');
        break;
      case 'incorrect_cvc':
        showMessage('Your CVC is incorrect. Please check and try again.');
        break;
      default:
        showMessage('An error occurred. Please try again.');
    }
  }
} catch (err) {
  console.error('Unexpected error:', err);
  showMessage('Something went wrong. Please contact support.');
}
```

### Error Handling Example (Backend)

```python
import requests

def process_payment(payment_data):
    try:
        response = requests.post(
            'https://api.hyperswitch.io/v1/payments',
            headers={'api-key': API_KEY},
            json=payment_data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_data = response.json()
        error_code = error_data.get('error', {}).get('code')

        if error_code == 'card_declined':
            return {'success': False, 'message': 'Card declined. Please try another card.'}
        elif error_code == 'insufficient_funds':
            return {'success': False, 'message': 'Insufficient funds.'}
        elif error_code == 'expired_card':
            return {'success': False, 'message': 'Card expired.'}
        else:
            return {'success': False, 'message': 'Payment failed. Please try again.'}
```

---

## Webhooks

Configure webhooks to receive asynchronous updates about payment status changes.

### Webhook Events

| Event | Description |
|-------|-------------|
| `payment_intent.succeeded` | Payment completed successfully |
| `payment_intent.failed` | Payment failed |
| `payment_intent.requires_action` | Additional authentication required |
| `payment_intent.canceled` | Payment was cancelled |
| `payment_intent.partially_captured` | Partial capture completed |

### Webhook Payload Example

```json
{
  "type": "payment_intent.succeeded",
  "data": {
    "object": {
      "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
      "status": "succeeded",
      "amount": 10000,
      "currency": "USD",
      "payment_method": "card",
      "customer_id": "cust_12345"
    }
  }
}
```

### Webhook Verification

Verify webhook signatures to ensure authenticity:

```python
import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f'sha256={expected_signature}', signature)
```

---

## Test Card Numbers

Use these test card numbers in your sandbox environment. **Do not use real card numbers in testing.**

### Successful Payments

| Card Number | Brand | CVC | Expiry |
|-------------|-------|-----|--------|
| `4111111111111111` | Visa | Any 3 digits | Any future date |
| `4242424242424242` | Visa | Any 3 digits | Any future date |
| `5555555555554444` | Mastercard | Any 3 digits | Any future date |
| `5105105105105100` | Mastercard | Any 3 digits | Any future date |
| `378282246310005` | American Express | Any 4 digits | Any future date |
| `371449635398431` | American Express | Any 4 digits | Any future date |

### Declined Cards

| Card Number | Decline Reason |
|-------------|----------------|
| `4000000000000002` | Card declined (generic) |
| `4000000000000127` | Incorrect CVC |
| `4000000000000069` | Expired card |
| `4000000000009995` | Insufficient funds |

### 3D Secure Test Cards

| Card Number | 3DS Behaviour |
|-------------|---------------|
| `4000002500003155` | 3DS frictionless flow |
| `4000002760003184` | 3DS challenge flow |
| `4000008260003178` | 3DS challenge with additional friction |

### Manual Capture Test Cards

| Card Number | Behaviour |
|-------------|-----------|
| `4000000000000259` | Requires capture (auto-decline if not captured within 7 days) |

---

## Idempotency Key Guidance

Use idempotency keys to prevent duplicate payments when retrying requests due to network errors or timeouts.

### When to Use Idempotency Keys

- Always for payments (`/payments` endpoint)
- Always for captures (`/payments/{id}/capture` endpoint)
- Always for refunds (`/refunds` endpoint)

### How It Works

Include a unique `X-Idempotency-Key` header with each request:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -H "X-Idempotency-Key: idem_$(date +%s)_$RANDOM" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "confirm": true
  }'
```

### Best Practices

1. **Generate unique keys**: Use UUIDs or combine timestamps with random strings
2. **Reuse keys for retries**: If a request fails, retry with the same key
3. **Keys expire after 24 hours**: After this period, a new request with the same key will be treated as a new transaction
4. **Store keys until you receive a response**: Only clear keys after confirming the request succeeded or definitively failed

### Idempotency Example (with Retry Logic)

```python
import uuid
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_payment_with_retry(payment_data):
    idempotency_key = str(uuid.uuid4())

    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[502, 503, 504]
    )
    session.mount('https://', HTTPAdapter(max_retries=retry))

    try:
        response = session.post(
            'https://api.hyperswitch.io/v1/payments',
            headers={
                'api-key': API_KEY,
                'X-Idempotency-Key': idempotency_key
            },
            json=payment_data,
            timeout=30
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log error and potentially retry with same idempotency key
        logger.error(f"Payment request failed: {e}")
        raise
```

---

## PCI Compliance

### Understanding PCI DSS Scope

| Integration Method | PCI Compliance Level | Effort |
|-------------------|----------------------|--------|
| **Hyperswitch SDK** (tokenization) | SAQ A | Minimal |
| **Raw card data** (direct API) | SAQ D | Extensive |

### SDK Tokenization (SAQ A)

When you use the Hyperswitch SDK:
- Card data never touches your servers
- You handle only tokens (`pm_xxx`)
- Complete SAQ A questionnaire (~20 questions)

### Raw Card Data (SAQ D)

If you must handle raw card data:
- Your systems are in scope for full PCI DSS
- Complete SAQ D questionnaire (~300 questions)
- Annual security audit may be required
- Strict network segmentation and encryption required

### Recommendations

1. **Always use the SDK** for tokenization
2. **Never log card data** (even in test mode)
3. **Use HTTPS** for all API calls
4. **Rotate API keys** regularly
5. **Implement webhook signature verification**

---

## Next Steps

- [Set up saved cards](./saved-card/README.md)
- [Configure recurring payments](./recurring-payments.md)
- [Implement manual capture](./manual-capture/README.md)
- [Handle 3D Secure authentication](../../../explore-hyperswitch/workflows/3ds-decision-manager/README.md)
- [Configure webhooks](../../../explore-hyperswitch/payment-orchestration/quickstart/webhooks.md)
- [Review PCI compliance requirements](../../../explore-hyperswitch/security-and-compliance/pci-compliance.md)
