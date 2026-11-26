---
name: hyperswitch-docs-web-sdk-quickstart
description: Use this skill when the user asks "how do I integrate Hyperswitch on the web", "web SDK quickstart", "Hyperswitch React integration steps", "loadHyper setup", "HyperElements setup", "how to embed a payment form", "where do I find my publishable key", "server setup for Hyperswitch", "create-payment endpoint", "client_secret flow", or needs a step-by-step guide to get the Hyperswitch checkout working in a browser.
version: 1.0.0
tags: [hyperswitch, docs, web, sdk, integration, quickstart]
---

# Web SDK Integration Quickstart

## Overview

This skill guides you through the complete web checkout integration: server-side payment creation, client-side SDK initialisation, and the payment confirmation flow. Covers React, vanilla JS, and HTML integrations.

## Prerequisites

- Hyperswitch account with at least one connector configured ([app.hyperswitch.io](https://app.hyperswitch.io))
- Your **publishable key** from Dashboard → Developers → API Keys
- Your **secret key** (server-side only — never expose in the browser)

---

## Architecture

```
Browser (your frontend)
   └─ loadHyper(publishableKey) → HyperElements → PaymentElement
                                                         ↓
                                               confirmPayment()
                                                         ↓
Server (your backend)                    POST /payments/confirm
   └─ POST /payments → client_secret ──────────────────→ Hyperswitch API
```

---

## Step 1: Server — Create a Payment

Create a server endpoint that calls Hyperswitch and returns the `client_secret`:

```javascript
// Node.js / Express
app.post('/create-payment', async (req, res) => {
  const response = await fetch('https://sandbox.hyperswitch.io/payments', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'api-key': process.env.HYPERSWITCH_SECRET_KEY,
    },
    body: JSON.stringify({
      amount: req.body.amount,       // smallest currency unit
      currency: req.body.currency,
      confirm: false,                // SDK confirms client-side
      customer_id: req.user?.id,
      return_url: `${process.env.APP_URL}/payment/complete`,
    }),
  });
  const payment = await response.json();
  res.json({ clientSecret: payment.client_secret });
});
```

**Doc reference:** `explore-hyperswitch/payment-experience/payment/web/` → Server Setup

---

## Step 2: Install the SDK

```bash
npm install @juspay-tech/hyper-js @juspay-tech/react-hyper-js
```

---

## Step 3: React Integration

```jsx
// App.jsx — fetch client_secret and wrap with HyperElements
import { useState, useEffect } from 'react';
import { loadHyper } from '@juspay-tech/hyper-js';
import { Elements } from '@juspay-tech/react-hyper-js';
import CheckoutForm from './CheckoutForm';

const hyperPromise = loadHyper('YOUR_PUBLISHABLE_KEY', {
  customBackendUrl: 'https://sandbox.hyperswitch.io',
});

export default function App() {
  const [clientSecret, setClientSecret] = useState(null);

  useEffect(() => {
    fetch('/create-payment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: 1000, currency: 'USD' }),
    })
      .then(r => r.json())
      .then(({ clientSecret }) => setClientSecret(clientSecret));
  }, []);

  return clientSecret ? (
    <Elements hyper={hyperPromise} options={{ clientSecret }}>
      <CheckoutForm />
    </Elements>
  ) : <p>Loading...</p>;
}
```

```jsx
// CheckoutForm.jsx — render PaymentElement and handle submission
import { useHyper, useElements, PaymentElement } from '@juspay-tech/react-hyper-js';

export default function CheckoutForm() {
  const hyper = useHyper();
  const elements = useElements();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await elements.submit();
    const { error } = await hyper.confirmPayment({
      elements,
      confirmParams: { return_url: window.location.origin + '/payment/complete' },
    });
    if (error) alert(error.message);
    // On success: SDK redirects to return_url
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit">Pay</button>
    </form>
  );
}
```

**Doc reference:** `explore-hyperswitch/payment-experience/payment/web/react-with-rest-api-integration.md`

---

## Step 4: Handle the Return URL

```javascript
// /payment/complete — verify payment status server-side
app.get('/payment/complete', async (req, res) => {
  const { payment_id } = req.query;
  const resp = await fetch(`https://sandbox.hyperswitch.io/payments/${payment_id}`, {
    headers: { 'api-key': process.env.HYPERSWITCH_SECRET_KEY },
  });
  const payment = await resp.json();
  if (payment.status === 'succeeded') {
    // fulfill order
  }
  res.redirect(payment.status === 'succeeded' ? '/success' : '/failed');
});
```

---

## Vanilla JS / HTML Alternative

**Doc reference:** `explore-hyperswitch/payment-experience/payment/web/html-with-rest-api-integration.md` and `vanilla-js-and-rest-api-integration.md`

```html
<script src="https://hyperswitch.io/v1/HyperLoader.js"></script>
<div id="payment-element"></div>

<script>
const hyper = Hyper('YOUR_PUBLISHABLE_KEY', {
  customBackendUrl: 'https://sandbox.hyperswitch.io'
});

fetch('/create-payment', { method: 'POST', ... })
  .then(r => r.json())
  .then(({ clientSecret }) => {
    const elements = hyper.elements({ clientSecret });
    const paymentElement = elements.create('payment');
    paymentElement.mount('#payment-element');

    document.querySelector('#pay-btn').addEventListener('click', async () => {
      await hyper.confirmPayment({ elements, confirmParams: { return_url: '...' } });
    });
  });
</script>
```

---

## Customising Appearance

```javascript
const elements = hyper.elements({
  clientSecret,
  appearance: {
    theme: 'midnight',  // 'default' | 'midnight' | 'charcoal' | 'brutalist'
    variables: {
      colorPrimary: '#6366F1',
      fontFamily: 'Inter, sans-serif',
      borderRadius: '8px',
    },
  },
});
```

**Doc reference:** `explore-hyperswitch/payment-experience/payment/web/customization.md`

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Invalid publishable key` | Using secret key instead of publishable key | Use `pk_...` key from Dashboard, not `snd_...` |
| SDK not rendering | `client_secret` null/undefined | Ensure server returns `client_secret` before rendering `Elements` |
| Payment loops on return_url | Re-creating payment on every page load | Only create payment once; check `payment_id` in URL on return |

**Doc reference for errors:** `explore-hyperswitch/payment-experience/payment/web/error-codes.md`

---

## Production Tips

- Your `return_url` must be HTTPS in production — HTTP will cause redirect failures with most connectors.
- Pass `customer_id` in `POST /payments` so returning customers see their saved cards.
- Never log or store `client_secret` — it grants write access to the payment object.
- Test with the Headless SDK (`explore-hyperswitch/payment-experience/payment/web/headless.md`) if you need full control over the UI.
