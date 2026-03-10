---
icon: hard-drive
---

# Payment Methods Management

## TL;DR

Payment methods management lets customers save cards and other payment instruments for one-click checkout and recurring payments. **Use client-side tokenization (Hyperswitch SDK) to avoid PCI compliance scope.** Tokenized payment methods are reusable across sessions, support 3D Secure authentication, and trigger lifecycle webhooks you can monitor.

| What you need | How to do it |
|---------------|--------------|
| Save a card during checkout | Set `setup_future_usage: on_session` or `off_session` in your payment request |
| Save a card without a payment | Use the `/payment_methods` endpoint with tokenized card data |
| List saved cards | `GET /customers/{customer_id}/payment_methods` |
| Charge a saved card | Pass `payment_method_id` instead of raw card details |
| Handle 3D Secure | Use `on_session` for customer-present flows; expect `requires_customer_action` |

---

## Overview

Payment methods represent stored credentials that can be reused for future transactions without requiring customers to re-enter their details. This includes cards, bank accounts, wallets, and other payment instruments.

### Key Concepts

| Term | Description |
|------|-------------|
| `payment_method_id` | Unique identifier for a stored payment method |
| `customer_id` | Identifier linking payment methods to a customer |
| `payment_method` | Type of payment (card, wallet, bank_transfer) |
| `payment_method_data` | Encrypted sensitive credential data |
| `client_secret` | Temporary token used to confirm payment intent |

---

## Security & PCI Compliance

> ⚠️ **CRITICAL: Never send raw card details from your server**
>
> Sending unencrypted card data from your server requires full PCI DSS compliance certification—a complex and expensive process. **Always use client-side tokenization** to stay out of PCI scope.

### PCI Compliance Options

| Approach | PCI Scope | When to Use |
|----------|-----------|-------------|
| **Hyperswitch SDK (Recommended)** | SAQ A (minimal) | Always prefer this for web/mobile |
| Self-hosted vault with encryption | SAQ D (full) | Only if you have dedicated security teams |

### Client-Side Tokenization Flow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Customer  │────▶│  Your App    │────▶│ Hyperswitch SDK │
│   Browser   │     │   (Frontend) │     │  (Tokenization) │
└─────────────┘     └──────────────┘     └─────────────────┘
                                                │
                                                ▼
                                        ┌─────────────────┐
                                        │  Juspay Vault   │
                                        │ (PCI Compliant) │
                                        └─────────────────┘
                                                │
                                                ▼
                                        ┌─────────────────┐
                                        │  Your Server    │
                                        │ (Token Only)    │
                                        └─────────────────┘
```

**How it works:**
1. Customer enters card details in your payment form
2. Hyperswitch SDK encrypts and tokenizes the card directly in the browser
3. Your server receives only a `payment_token`—never the raw card number
4. You use the token to create payment methods or process payments

---

## setup_future_usage Values

The `setup_future_usage` parameter determines how a saved payment method can be used:

| Value | Description | Use Case |
|-------|-------------|----------|
| `on_session` | Card can be used when customer is present | One-click checkout, customer-initiated payments |
| `off_session` | Card can be used without customer present | Subscription renewals, automated billing |
| `null` | Card is not saved | Single-use payments only |

### When to Use Each

**`on_session`** — Customer is actively using your application:
- Guest checkout with "save card for next time" option
- Logged-in customer making a purchase
- Any flow where customer can complete 3D Secure if required

**`off_session`** — Payment happens without customer interaction:
- Monthly subscription renewals
- Usage-based billing at month end
- Retry of failed subscription payments

> ⚠️ **Note:** `off_session` payments may fail if the issuer requires authentication. Implement retry logic with `on_session` fallback for failed off-session payments.

---

## Save a Payment Method

### Method 1: Client-Side Tokenization (Recommended)

> ⚠️ **PCI Compliance:** Even on the client side, handle raw card data carefully. Always use the official Hyperswitch SDK which encrypts data before transmission. Never log or store card details in your application code.

First, tokenize the card using Hyperswitch SDK:

```javascript
// Using Hyperswitch SDK
const { token } = await hyperswitch.createToken({
  card: {
    number: '4111111111111111',
    card_exp_month: 12,
    card_exp_year: 2027,
    cvc: '123'
  }
});
```

Then create the payment method on your server:

```bash
curl -X POST https://api.hyperswitch.io/v1/payment_methods \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "customer_id": "cust_12345",
    "payment_method": "card",
    "payment_method_data": {
      "card_token": "tok_abcdefghijklmnopqrstuvwxyz"
    }
  }'
```

**Response:**
```json
{
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
  "customer_id": "cust_12345",
  "payment_method": "card",
  "card": {
    "scheme": "visa",
    "last4": "1111",
    "card_exp_month": "12",
    "card_exp_year": "27"
  },
  "created": "2026-03-10T12:00:00Z"
}
```

### Method 2: During Payment (with setup_future_usage)

Save a card automatically when processing a payment:

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
        "card_exp_year": "27",
        "card_holder_name": "John Doe"
      }
    },
    "setup_future_usage": "on_session",
    "confirm": true
  }'
```

**Response includes `payment_method_id`:**
```json
{
  "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
  "status": "succeeded",
  "customer_id": "cust_12345"
}
```

---

## Token Lifecycle

Payment method tokens follow a defined lifecycle:

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  ACTIVE  │───▶│ REQUIRES │───▶│  ACTIVE  │───▶│  DELETED │
│          │    │  ACTION  │    │          │    │          │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │                               ▲              ▲
     │                               │              │
     └───────────────────────────────┘              │
              (authentication                      │
               successful)                   (explicit delete
                                              or expired)
```

### Token States

| State | Description |
|-------|-------------|
| `active` | Token is valid and ready for use |
| `requires_customer_action` | 3D Secure or other authentication needed |
| `inactive` | Temporarily disabled (e.g., suspected fraud) |
| `expired` | Token has reached expiration date |
| `deleted` | Permanently removed |

### Token Expiration

- **Card tokens** expire when the underlying card expires
- You can update expiration dates without re-collecting the full card number
- Expired tokens return `error_type: invalid_request` with `error_code: payment_method_expired`

---

## List Customer Payment Methods

Retrieve all saved payment methods for a customer:

```bash
curl -X GET "https://api.hyperswitch.io/v1/customers/cust_12345/payment_methods" \
  -H "api-key: YOUR_API_KEY"
```

**Response:**
```json
{
  "data": [
    {
      "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
      "customer_id": "cust_12345",
      "payment_method": "card",
      "card": {
        "scheme": "visa",
        "last4": "1111",
        "card_exp_month": "12",
        "card_exp_year": "27"
      },
      "created": "2026-03-10T12:00:00Z"
    }
  ]
}
```

---

## Use Saved Payment Method

Reference a saved payment method when creating a payment:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "confirm": true
  }'
```

---

## 3D Secure for Saved Cards

When using saved cards, 3D Secure may still be required:

### on_session Flow (Customer Present)

```bash
# Initial request
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "setup_future_usage": "on_session",
    "confirm": true,
    "authentication_type": "three_ds",
    "return_url": "https://your-site.com/payment/complete"
  }'
```

**If 3DS is required, response will be:**
```json
{
  "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
  "status": "requires_customer_action",
  "next_action": {
    "type": "three_ds_invoke",
    "three_ds_invoke": {
      "three_ds_url": "https://acs.bank.com/3ds?token=xyz"
    }
  },
  "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyzzy"
}
```

**Redirect the customer to complete authentication, then confirm:**

```bash
curl -X POST https://api.hyperswitch.io/v1/payments/pay_abcdefghijklmnopqrstuvwxyz/confirm \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyzzy"
  }'
```

### off_session Flow (Merchant Initiated)

For recurring payments without customer present:

```bash
curl -X POST https://api.hyperswitch.io/v1/payments \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "customer_id": "cust_12345",
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "setup_future_usage": "off_session",
    "confirm": true,
    "mandate_id": "man_abcdefghijklmnopqrstuvwxyz"
  }'
```

> ℹ️ **Note:** `off_session` payments require a valid mandate. The initial `on_session` payment that saved the card should have `setup_mandate: true` to create this mandate.

---

## Error Handling

### Common Error Scenarios

#### Payment Method Expired
```json
{
  "error_type": "invalid_request",
  "error_code": "payment_method_expired",
  "message": "The payment method has expired. Please update the expiration date or use a different payment method.",
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz"
}
```

#### Payment Method Not Found
```json
{
  "error_type": "invalid_request",
  "error_code": "resource_missing",
  "message": "Payment method 'pm_abcdefghijklmnopqrstuvwxyz' not found or does not belong to this customer"
}
```

#### Insufficient Funds (Off-Session)
```json
{
  "error_type": "processing_error",
  "error_code": "insufficient_funds",
  "message": "The card issuer declined the payment due to insufficient funds.",
  "decline_code": "insufficient_funds",
  "next_action": {
    "type": "retry_with_customer_present",
    "suggested_usage": "on_session"
  }
}
```

#### 3D Secure Required
```json
{
  "error_type": "processing_error",
  "error_code": "three_ds_required",
  "message": "This transaction requires 3D Secure authentication. Please retry with customer present.",
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz"
}
```

### Error Handling Pattern

```javascript
async function processPayment(paymentMethodId) {
  try {
    const response = await createPayment({
      payment_method_id: paymentMethodId,
      setup_future_usage: 'off_session'
    });
    
    if (response.status === 'succeeded') {
      return { success: true, paymentId: response.payment_id };
    }
  } catch (error) {
    if (error.error_code === 'payment_method_expired') {
      // Prompt customer to update card
      return { 
        success: false, 
        requiresUpdate: true,
        paymentMethodId: error.payment_method_id 
      };
    }
    
    if (error.error_code === 'three_ds_required' || 
        error.next_action?.suggested_usage === 'on_session') {
      // Fall back to on_session flow
      return { 
        success: false, 
        requiresCustomerPresent: true,
        paymentMethodId: paymentMethodId
      };
    }
    
    // Log and alert for other errors
    console.error('Payment failed:', error);
    throw error;
  }
}
```

---

## Delete Payment Method

Remove a saved payment method:

```bash
curl -X DELETE https://api.hyperswitch.io/v1/payment_methods/pm_abcdefghijklmnopqrstuvwxyz \
  -H "api-key: YOUR_API_KEY"
```

**Response:**
```json
{
  "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
  "deleted": true
}
```

---

## Update Payment Method

Update details like expiration date:

```bash
curl -X POST https://api.hyperswitch.io/v1/payment_methods/pm_abcdefghijklmnopqrstuvwxyz \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "card": {
      "card_exp_month": "06",
      "card_exp_year": "27"
    }
  }'
```

> ⚠️ **Note:** You cannot update the card number. If the card number changes, create a new payment method and delete the old one.

---

## Webhook Events

Monitor payment method lifecycle through webhooks:

| Event | Description |
|-------|-------------|
| `payment_method.created` | A new payment method was saved |
| `payment_method.updated` | Payment method details were modified |
| `payment_method.authenticated` | 3D Secure authentication completed successfully |
| `payment_method.expiring_soon` | Card expires within 30 days |
| `payment_method.expired` | Card has expired |
| `payment_method.deleted` | Payment method was removed |

### Webhook Payload Example

```json
{
  "event_type": "payment_method.created",
  "event_id": "evt_abcdefghijklmnopqrstuvwxyz",
  "timestamp": "2026-03-10T12:00:00Z",
  "data": {
    "payment_method_id": "pm_abcdefghijklmnopqrstuvwxyz",
    "customer_id": "cust_12345",
    "payment_method": "card",
    "card": {
      "scheme": "visa",
      "last4": "1111",
      "card_exp_month": "12",
      "card_exp_year": "27"
    },
    "setup_future_usage": "on_session"
  }
}
```

### Important Webhook Considerations

1. **Verify signatures** — Always verify webhook signatures to ensure authenticity
2. **Handle idempotency** — Process each event only once using `event_id`
3. **Respond quickly** — Return 200 OK within 5 seconds; defer processing if needed
4. **Retry logic** — Hyperswitch retries failed webhooks with exponential backoff

---

## PCI Compliance Summary

| Scenario | PCI Requirement | Recommendation |
|----------|-----------------|----------------|
| Using Hyperswitch SDK | SAQ A | ✅ Preferred approach |
| Using hosted fields | SAQ A-EP | Acceptable alternative |
| Server-side card handling | SAQ D | ❌ Avoid unless certified |
| Storing CVV | Prohibited | Never store CVV codes |

### Checklist for Compliance

- [ ] Card data never touches your server
- [ ] Use Hyperswitch SDK for tokenization
- [ ] Store only `payment_method_id` tokens
- [ ] Implement webhook signature verification
- [ ] Log and monitor payment method events
- [ ] Have a data retention policy

---

## Next Steps

- [Implement saved card checkout](../../payment-experience/payment/saved-card.md)
- [Set up recurring payments](../recurring-payments.md)
- [Configure vault options](../../../explore-hyperswitch/workflows/vault.md)
- [Handle 3D Secure authentication](../3ds-authentication.md)
