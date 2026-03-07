---
description: >-
  Learn how to place authorization holds on customer funds and capture them later—enabling flexible payment flows for pre-orders, hospitality, marketplaces, and more.
icon: transmission
---

# Manual Capture

{% embed url="https://youtu.be/XtOMZVhvLwQ" %}

**What you'll learn:** This video demonstrates how to implement Manual Capture (Auth & Capture) using Hyperswitch, covering the three-step flow from authorization to fund capture.

---

## Overview

**Manual Capture** enables you to authorize funds on a customer's payment method and capture them later—only when you're ready to fulfill the order. Unlike automatic capture where funds are settled immediately, manual capture gives you precise control over when money actually moves.

### Why Use Manual Capture?

| Outcome | Business Impact |
|---------|-----------------|
| **Reduce chargeback risk** | Capture only after delivery confirmation |
| **Improve cash flow** | Hold funds without immediate settlement |
| **Enable flexible fulfillment** | Support split shipments, variable final amounts |
| **Build customer trust** | Charge only when goods/services are ready |

### Common Use Cases

- **Pre-orders**: Authorize at checkout, capture when product ships
- **Hotels & Hospitality**: Hold for incidentals, capture at checkout
- **Marketplaces**: Release funds to sellers upon delivery confirmation
- **Custom Manufacturing**: Capture after production completion
- **Food Delivery**: Capture when order is prepared/dispatched
- **Service appointments**: Capture after service completion

---

## When to Use Manual Capture

Choose the right capture strategy for your business model:

| Scenario | Recommended Capture Type | Rationale |
|----------|-------------------------|-----------|
| Immediate digital goods delivery | [Automatic Capture](../recurring-payments.md) | Funds settle instantly |
| Physical product shipping | **Manual Capture - Full** | Capture when order ships |
| Multi-item orders with split shipping | **Manual Capture - Partial** | Capture as each shipment goes out |
| Variable final amounts (tipping, add-ons) | **Manual Capture - Over Capture** | Capture up to 115% of authorized amount |
| Marketplace with escrow needs | **Manual Capture - Multiple** | Release funds to seller in stages |
| Hotel/lodging with incidentals | **Manual Capture - Over Capture** | Hold for room + potential charges |

### Capture Type Decision Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    Payment Flow Decision                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐                                                │
│  │ Do you need │── NO ──► Automatic Capture (default)          │
│  │ to control  │                                                │
│  │  timing?    │── YES                                          │
│  └─────────────┘         ┌──────────────────────────┐            │
│                          ▼                          │            │
│                ┌─────────────────┐                  │            │
│                │ Will the final  │── NO ──► Full    │            │
│                │  amount vary?   │      Capture     │            │
│                └─────────────────┘                  │            │
│                          │YES                       │            │
│                          ▼                          │            │
│                ┌─────────────────┐                  │            │
│                │ Is final amount │── NO ──► Partial │            │
│                │  HIGHER than    │      Capture     │            │
│                │  authorized?    │                  │            │
│                └─────────────────┘                  │            │
│                          │YES                       │            │
│                          ▼                          │            │
│                   Over Capture ◄────────────────────┘            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Prerequisites

Before implementing Manual Capture, ensure you have:

### 1. API Credentials
- **API Key**: Your secret key for server-side API calls (`snd_...` for sandbox)
- **Publishable Key**: For client-side operations (`pk_...` for sandbox)
- Get these from the [Hyperswitch Dashboard](https://app.hyperswitch.io/)

### 2. Webhook Configuration
Set up webhooks to receive real-time payment status updates:
- Navigate to **Developer → Webhooks** in your Dashboard
- Configure endpoint URL for `payment_authorized` and `payment_captured` events
- Required for production to track authorization hold expirations

### 3. Connector Support
Not all payment processors support Manual Capture. Supported connectors include:

| Connector | Full Capture | Partial Capture | Multiple Captures | Over Capture |
|-----------|-------------|-----------------|-------------------|--------------|
| Stripe | ✅ | ✅ | ✅ | ✅ |
| Adyen | ✅ | ✅ | ✅ | ✅ |
| Checkout.com | ✅ | ✅ | ✅ | ✅ |
| PayPal | ✅ | ✅ | ❌ | ❌ |
| Braintree | ✅ | ✅ | ❌ | ❌ |
| Authorize.net | ✅ | ✅ | ❌ | ❌ |

> **Note:** Check the [Connector Matrix](https://docs.hyperswitch.io/going-live/supported-payment-methods) for the latest support status.

### 4. Authorization Hold Time Limits

Authorization holds expire automatically. Capture before these deadlines:

| Card Network | Hold Duration |
|--------------|---------------|
| Visa | Up to 7 days |
| Mastercard | Up to 7 days |
| American Express | Up to 7 days |
| Discover | Up to 10 days |

> **Important:** After expiration, the hold is automatically released and you cannot capture the funds. You would need to request a new authorization.

---

## How It Works

### Payment State Machine

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Manual Capture Flow                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────┐     Create      ┌───────────┐     Confirm          │
│  │  Created  │◄───────────────►│  Created  │─────────────────┐    │
│  │ (Initial) │  capture_method │ (Manual)  │                 │    │
│  └───────────┘    = "manual"   └───────────┘                 │    │
│                                                                     │
│                                          │                       │    │
│                                          ▼                       │    │
│                                   ┌─────────────┐                │    │
│                                   │   Pending   │                │    │
│                                   │  (3DS/Auth) │                │    │
│                                   └─────────────┘                │    │
│                                          │                       │    │
│                    ┌─────────────────────┼─────────────────────┐ │    │
│                    ▼                     ▼                     ▼ │    │
│              ┌──────────┐         ┌──────────┐         ┌────────┐│    │
│              │  Failed  │         │ Cancelled│         │Requires││    │
│              └──────────┘         └──────────┘         │Capture │├────┤
│                                                        └────────┘│    │
│                              Capture/Void/Expiry                 │    │
│                    ┌─────────────────────┼─────────────────────┐ │    │
│                    ▼                     ▼                     ▼ │    │
│              ┌──────────┐         ┌──────────┐         ┌────────┐│    │
│              │Succeeded │         │Partially │         │ Voided ││    │
│              │(Full Cap)│         │Captured  │         │        ││    │
│              └──────────┘         │(Partial  │         └────────┘│    │
│                                   │ Capture) │                    │    │
│                                   └──────────┘                    │    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Status Transitions

| From Status | Action | To Status | Description |
|-------------|--------|-----------|-------------|
| `requires_confirmation` | Confirm payment | `requires_capture` | Authorized, waiting for capture |
| `requires_capture` | Full capture | `succeeded` | All funds captured |
| `requires_capture` | Partial capture | `partially_captured` | Some funds captured, rest voided |
| `requires_capture` | Partial capture (multi-capture) | `partially_captured_and_capturable` | More captures possible |
| `requires_capture` | Cancel/Void | `cancelled` | Authorization released |
| `requires_capture` | Expiration | `processing` → `failed` | Hold expired, capture failed |

---

## Implementation

### Authentication

All API requests require authentication using your API key:

```bash
# Server-side API calls (Create, Capture, Retrieve)
--header 'api-key: snd_your_secret_key_here'

# Client-side operations (Confirm)
--header 'api-key: pk_your_publishable_key_here'
```

> **Security Tip:** Never expose your secret API key (`snd_...`) in client-side code. Use publishable keys (`pk_...`) for browser/mobile apps.

### Step 1: Create Payment

Create a payment with `capture_method: "manual"` to place an authorization hold.

{% tabs %}
{% tab title="cURL" %}
```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: snd_your_secret_key_here' \
--data '{
    "amount": 6540,
    "currency": "USD",
    "confirm": false,
    "capture_method": "manual",
    "authentication_type": "no_three_ds",
    "return_url": "https://your-website.com/payment-complete",
    "customer_id": "cust_your_customer_id",
    "description": "Order #12345 - Manual capture flow",
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "city": "San Francisco",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "John",
            "last_name": "Doe"
        },
        "email": "john.doe@example.com",
        "phone": {
            "number": "1234567890",
            "country_code": "+1"
        }
    },
    "metadata": {
        "order_id": "order_12345",
        "product_name": "Premium Widget"
    }
}'
```
{% endtab %}

{% tab title="Node.js" %}
```javascript
const hyperswitch = require('@juspay-tech/hyperswitch-node')('snd_your_secret_key_here');

const paymentIntent = await hyperswitch.paymentIntents.create({
    amount: 6540,
    currency: 'USD',
    confirm: false,
    capture_method: 'manual',
    authentication_type: 'no_three_ds',
    return_url: 'https://your-website.com/payment-complete',
    customer_id: 'cust_your_customer_id',
    description: 'Order #12345 - Manual capture flow',
    billing: {
        address: {
            line1: '1467',
            line2: 'Harrison Street',
            city: 'San Francisco',
            state: 'California',
            zip: '94122',
            country: 'US',
            first_name: 'John',
            last_name: 'Doe'
        },
        email: 'john.doe@example.com',
        phone: {
            number: '1234567890',
            country_code: '+1'
        }
    },
    metadata: {
        order_id: 'order_12345',
        product_name: 'Premium Widget'
    }
});

console.log('Payment ID:', paymentIntent.payment_id);
console.log('Client Secret:', paymentIntent.client_secret);
console.log('Status:', paymentIntent.status); // "requires_confirmation"
```
{% endtab %}

{% tab title="Python" %}
```python
import requests

url = "https://sandbox.hyperswitch.io/payments"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "api-key": "snd_your_secret_key_here"
}
payload = {
    "amount": 6540,
    "currency": "USD",
    "confirm": False,
    "capture_method": "manual",
    "authentication_type": "no_three_ds",
    "return_url": "https://your-website.com/payment-complete",
    "customer_id": "cust_your_customer_id",
    "description": "Order #12345 - Manual capture flow",
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "city": "San Francisco",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "John",
            "last_name": "Doe"
        },
        "email": "john.doe@example.com",
        "phone": {
            "number": "1234567890",
            "country_code": "+1"
        }
    },
    "metadata": {
        "order_id": "order_12345",
        "product_name": "Premium Widget"
    }
}

response = requests.post(url, json=payload, headers=headers)
payment_intent = response.json()

print(f"Payment ID: {payment_intent['payment_id']}")
print(f"Client Secret: {payment_intent['client_secret']}")
print(f"Status: {payment_intent['status']}")  # "requires_confirmation"
```
{% endtab %}

{% tab title="Java" %}
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class CreateManualCapturePayment {
    public static void main(String[] args) throws Exception {
        String jsonBody = """
            {
                "amount": 6540,
                "currency": "USD",
                "confirm": false,
                "capture_method": "manual",
                "authentication_type": "no_three_ds",
                "return_url": "https://your-website.com/payment-complete",
                "customer_id": "cust_your_customer_id",
                "description": "Order #12345 - Manual capture flow",
                "billing": {
                    "address": {
                        "line1": "1467",
                        "line2": "Harrison Street",
                        "city": "San Francisco",
                        "state": "California",
                        "zip": "94122",
                        "country": "US",
                        "first_name": "John",
                        "last_name": "Doe"
                    },
                    "email": "john.doe@example.com",
                    "phone": {
                        "number": "1234567890",
                        "country_code": "+1"
                    }
                },
                "metadata": {
                    "order_id": "order_12345",
                    "product_name": "Premium Widget"
                }
            }
            """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://sandbox.hyperswitch.io/payments"))
            .header("Content-Type", "application/json")
            .header("Accept", "application/json")
            .header("api-key", "snd_your_secret_key_here")
            .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
            .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Response: " + response.body());
    }
}
```
{% endtab %}

{% tab title="Go" %}
```go
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
)

func main() {
    payload := map[string]interface{}{
        "amount": 6540,
        "currency": "USD",
        "confirm": false,
        "capture_method": "manual",
        "authentication_type": "no_three_ds",
        "return_url": "https://your-website.com/payment-complete",
        "customer_id": "cust_your_customer_id",
        "description": "Order #12345 - Manual capture flow",
        "billing": map[string]interface{}{
            "address": map[string]interface{}{
                "line1": "1467",
                "line2": "Harrison Street",
                "city": "San Francisco",
                "state": "California",
                "zip": "94122",
                "country": "US",
                "first_name": "John",
                "last_name": "Doe",
            },
            "email": "john.doe@example.com",
            "phone": map[string]interface{}{
                "number": "1234567890",
                "country_code": "+1",
            },
        },
        "metadata": map[string]interface{}{
            "order_id": "order_12345",
            "product_name": "Premium Widget",
        },
    }

    jsonData, _ := json.Marshal(payload)
    req, _ := http.NewRequest("POST", "https://sandbox.hyperswitch.io/payments", bytes.NewBuffer(jsonData))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("Accept", "application/json")
    req.Header.Set("api-key", "snd_your_secret_key_here")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    var result map[string]interface{}
    json.NewDecoder(resp.Body).Decode(&result)
    
    fmt.Printf("Payment ID: %s\n", result["payment_id"])
    fmt.Printf("Status: %s\n", result["status"])
}
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
$url = 'https://sandbox.hyperswitch.io/payments';

$payload = [
    'amount' => 6540,
    'currency' => 'USD',
    'confirm' => false,
    'capture_method' => 'manual',
    'authentication_type' => 'no_three_ds',
    'return_url' => 'https://your-website.com/payment-complete',
    'customer_id' => 'cust_your_customer_id',
    'description' => 'Order #12345 - Manual capture flow',
    'billing' => [
        'address' => [
            'line1' => '1467',
            'line2' => 'Harrison Street',
            'city' => 'San Francisco',
            'state' => 'California',
            'zip' => '94122',
            'country' => 'US',
            'first_name' => 'John',
            'last_name' => 'Doe'
        ],
        'email' => 'john.doe@example.com',
        'phone' => [
            'number' => '1234567890',
            'country_code' => '+1'
        ]
    ],
    'metadata' => [
        'order_id' => 'order_12345',
        'product_name' => 'Premium Widget'
    ]
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Accept: application/json',
    'api-key: snd_your_secret_key_here'
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo "Payment ID: " . $result['payment_id'] . "\n";
echo "Status: " . $result['status'] . "\n";
?>
```
{% endtab %}
{% endtabs %}

**Expected Response:**

```json
{
    "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
    "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123",
    "status": "requires_confirmation",
    "amount": 6540,
    "currency": "USD",
    "capture_method": "manual",
    "created": "2024-03-07T10:30:00.000Z",
    "expires_on": "2024-03-14T10:30:00.000Z"
}
```

Save the `payment_id` and `client_secret` for the next steps.

---

### Step 2: Confirm (Authorize)

Collect payment details from your customer and confirm the authorization. This places a hold on the customer's funds.

{% tabs %}
{% tab title="cURL" %}
```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: pk_your_publishable_key_here' \
--data '{
    "payment_method": "card",
    "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "12",
            "card_exp_year": "2030",
            "card_holder_name": "John Doe",
            "card_cvc": "123"
        }
    }
}'
```
{% endtab %}

{% tab title="Node.js" %}
```javascript
const confirmedPayment = await hyperswitch.paymentIntents.confirm(
    'pay_abcdefghijklmnopqrstuvwxyz',
    {
        payment_method: 'card',
        client_secret: 'pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123',
        payment_method_data: {
            card: {
                card_number: '4242424242424242',
                card_exp_month: '12',
                card_exp_year: '2030',
                card_holder_name: 'John Doe',
                card_cvc: '123'
            }
        }
    }
);

console.log('Status:', confirmedPayment.status); // "requires_capture"
console.log('Amount Capturable:', confirmedPayment.amount_capturable); // 6540
```
{% endtab %}

{% tab title="JavaScript (Frontend)" %}
```javascript
// Using Hyperswitch Unified Checkout
const hyper = Hyper('pk_your_publishable_key_here');
const elements = hyper.elements({ clientSecret: clientSecretFromServer });
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

// When customer submits payment
const { error, paymentIntent } = await hyper.confirmPayment({
    elements,
    confirmParams: {
        return_url: 'https://your-website.com/payment-complete'
    }
});

// On success, paymentIntent.status will be "requires_capture"
```
{% endtab %}

{% tab title="Python" %}
```python
url = "https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/confirm"
payload = {
    "payment_method": "card",
    "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "12",
            "card_exp_year": "2030",
            "card_holder_name": "John Doe",
            "card_cvc": "123"
        }
    }
}

response = requests.post(url, json=payload, headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "api-key": "pk_your_publishable_key_here"
})

confirmed = response.json()
print(f"Status: {confirmed['status']}")  # "requires_capture"
print(f"Amount Capturable: {confirmed['amount_capturable']}")  # 6540
```
{% endtab %}

{% tab title="Java" %}
```java
String jsonBody = """
    {
        "payment_method": "card",
        "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123",
        "payment_method_data": {
            "card": {
                "card_number": "4242424242424242",
                "card_exp_month": "12",
                "card_exp_year": "2030",
                "card_holder_name": "John Doe",
                "card_cvc": "123"
            }
        }
    }
    """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/confirm"))
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .header("api-key", "pk_your_publishable_key_here")
    .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```
{% endtab %}

{% tab title="Go" %}
```go
payload := map[string]interface{}{
    "payment_method": "card",
    "client_secret": "pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123",
    "payment_method_data": map[string]interface{}{
        "card": map[string]interface{}{
            "card_number": "4242424242424242",
            "card_exp_month": "12",
            "card_exp_year": "2030",
            "card_holder_name": "John Doe",
            "card_cvc": "123",
        },
    },
}

jsonData, _ := json.Marshal(payload)
req, _ := http.NewRequest("POST", 
    "https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/confirm",
    bytes.NewBuffer(jsonData))
req.Header.Set("Content-Type", "application/json")
req.Header.Set("Accept", "application/json")
req.Header.Set("api-key", "pk_your_publishable_key_here")

resp, _ := client.Do(req)
defer resp.Body.Close()
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
$url = 'https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/confirm';

$payload = [
    'payment_method' => 'card',
    'client_secret' => 'pay_abcdefghijklmnopqrstuvwxyz_secret_xyz123',
    'payment_method_data' => [
        'card' => [
            'card_number' => '4242424242424242',
            'card_exp_month' => '12',
            'card_exp_year' => '2030',
            'card_holder_name' => 'John Doe',
            'card_cvc' => '123'
        ]
    ]
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Accept: application/json',
    'api-key: pk_your_publishable_key_here'
]);

$response = curl_exec($ch);
curl_close($ch);
?>
```
{% endtab %}
{% endtabs %}

**Expected Response:**

```json
{
    "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
    "status": "requires_capture",
    "amount": 6540,
    "amount_capturable": 6540,
    "amount_captured": 0,
    "currency": "USD",
    "capture_method": "manual",
    "payment_method": "card",
    "connector": "stripe"
}
```

At this point, funds are authorized but not captured. The `amount_capturable` shows how much you can capture.

---

### Step 3: Capture Funds

After delivering goods or services, capture the authorized funds.

#### Full Capture

Capture the entire authorized amount.

{% tabs %}
{% tab title="cURL" %}
```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/capture' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: snd_your_secret_key_here' \
--data '{
    "amount_to_capture": 6540,
    "statement_descriptor_name": "Your Business",
    "statement_descriptor_suffix": "ORDER #12345"
}'
```
{% endtab %}

{% tab title="Node.js" %}
```javascript
const capturedPayment = await hyperswitch.paymentIntents.capture(
    'pay_abcdefghijklmnopqrstuvwxyz',
    {
        amount_to_capture: 6540,
        statement_descriptor_name: 'Your Business',
        statement_descriptor_suffix: 'ORDER #12345'
    }
);

console.log('Status:', capturedPayment.status); // "succeeded"
console.log('Amount Captured:', capturedPayment.amount_captured); // 6540
```
{% endtab %}

{% tab title="Python" %}
```python
url = "https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/capture"
payload = {
    "amount_to_capture": 6540,
    "statement_descriptor_name": "Your Business",
    "statement_descriptor_suffix": "ORDER #12345"
}

response = requests.post(url, json=payload, headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "api-key": "snd_your_secret_key_here"
})

captured = response.json()
print(f"Status: {captured['status']}")  # "succeeded"
print(f"Amount Captured: {captured['amount_captured']}")  # 6540
```
{% endtab %}

{% tab title="Java" %}
```java
String jsonBody = """
    {
        "amount_to_capture": 6540,
        "statement_descriptor_name": "Your Business",
        "statement_descriptor_suffix": "ORDER #12345"
    }
    """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/capture"))
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .header("api-key", "snd_your_secret_key_here")
    .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```
{% endtab %}

{% tab title="Go" %}
```go
payload := map[string]interface{}{
    "amount_to_capture": 6540,
    "statement_descriptor_name": "Your Business",
    "statement_descriptor_suffix": "ORDER #12345",
}

jsonData, _ := json.Marshal(payload)
req, _ := http.NewRequest("POST",
    "https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/capture",
    bytes.NewBuffer(jsonData))
req.Header.Set("Content-Type", "application/json")
req.Header.Set("Accept", "application/json")
req.Header.Set("api-key", "snd_your_secret_key_here")

resp, _ := client.Do(req)
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php
$url = 'https://sandbox.hyperswitch.io/payments/pay_abcdefghijklmnopqrstuvwxyz/capture';

$payload = [
    'amount_to_capture' => 6540,
    'statement_descriptor_name' => 'Your Business',
    'statement_descriptor_suffix' => 'ORDER #12345'
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Accept: application/json',
    'api-key: snd_your_secret_key_here'
]);

$response = curl_exec($ch);
curl_close($ch);
?>
```
{% endtab %}
{% endtabs %}

**Expected Response:**

```json
{
    "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
    "status": "succeeded",
    "amount": 6540,
    "amount_capturable": 0,
    "amount_captured": 6540,
    "currency": "USD",
    "capture_method": "manual"
}
```

---

## Capture Types

### Full Capture

Capture the complete authorized amount in a single API call.

**Use Case:** {% hint style="success" %} **E-commerce shipping** — Capture when order leaves warehouse {% endhint %}

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/{payment_id}/capture' \
--header 'api-key: snd_your_secret_key_here' \
--header 'Content-Type: application/json' \
--data '{
    "amount_to_capture": 6540
}'
```

### Partial Capture

Capture less than the authorized amount. The remaining amount is automatically released.

**Use Case:** {% hint style="info" %} **Split shipments** — Capture $30 now, $20 later when second item ships {% endhint %}

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/{payment_id}/capture' \
--header 'api-key: snd_your_secret_key_here' \
--header 'Content-Type: application/json' \
--data '{
    "amount_to_capture": 3000
}'
```

**Resulting Status:** `partially_captured` or `partially_captured_and_capturable`

| Connector Capability | Resulting Status |
|---------------------|------------------|
| Single capture only | `partially_captured` — remaining amount voided |
| Multiple capture supported | `partially_captured_and_capturable` — more captures possible |

### Over Capture

Capture up to **115%** of the authorized amount to accommodate tips, shipping adjustments, or incidental charges.

**Use Case:** {% hint style="warning" %} **Hotel incidental charges** — Authorize $100 for room, capture $120 including minibar charges {% endhint %}

First, enable Over Capture when creating the payment:

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'api-key: snd_your_secret_key_here' \
--header 'Content-Type: application/json' \
--data '{
    "amount": 10000,
    "currency": "USD",
    "capture_method": "manual",
    "enable_overcapture": true
}'
```

Then capture more than the authorized amount:

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/{payment_id}/capture' \
--header 'api-key: snd_your_secret_key_here' \
--header 'Content-Type: application/json' \
--data '{
    "amount_to_capture": 11500
}'
```

> **Note:** Over Capture is connector-dependent. See [Over Capture Documentation](./overcapture.md) for details.

### Capture Comparison

| Feature | Full | Partial | Over Capture |
|---------|------|---------|--------------|
| **Amount captured** | 100% of authorized | Less than 100% | Up to 115% |
| **Final status** | `succeeded` | `partially_captured` | `succeeded` |
| **Multiple captures** | Single | Depends on connector | Single |
| **Use case** | Standard fulfillment | Split shipments | Variable final amount |

---

## Webhook Events

Configure webhooks to receive real-time updates on payment status changes.

### Required Events

| Event | Trigger | Payload Example |
|-------|---------|-----------------|
| `payment_authorized` | Authorization successful, funds held | See below |
| `payment_captured` | Funds successfully captured | See below |
| `payment.partially_captured` | Partial capture completed | Status: `partially_captured` |
| `payment.cancelled` | Authorization voided or expired | Status: `cancelled` |

### Webhook Payload: payment_authorized

```json
{
    "event_type": "payment_authorized",
    "content": {
        "object": {
            "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
            "status": "requires_capture",
            "amount": 6540,
            "amount_capturable": 6540,
            "amount_captured": 0,
            "currency": "USD",
            "capture_method": "manual",
            "customer_id": "cust_your_customer_id",
            "connector": "stripe",
            "created": "2024-03-07T10:30:00.000Z",
            "expires_on": "2024-03-14T10:30:00.000Z"
        }
    }
}
```

### Webhook Payload: payment_captured

```json
{
    "event_type": "payment_captured",
    "content": {
        "object": {
            "payment_id": "pay_abcdefghijklmnopqrstuvwxyz",
            "status": "succeeded",
            "amount": 6540,
            "amount_capturable": 0,
            "amount_captured": 6540,
            "currency": "USD",
            "capture_method": "manual",
            "captured_at": "2024-03-07T14:22:15.000Z"
        }
    }
}
```

### Idempotency

Use the `x-request-id` header to ensure idempotent capture operations:

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/{payment_id}/capture' \
--header 'api-key: snd_your_secret_key_here' \
--header 'Content-Type: application/json' \
--header 'x-request-id: unique-request-id-12345' \
--data '{
    "amount_to_capture": 6540
}'
```

> **Best Practice:** Generate a unique `x-request-id` for each capture attempt. If a request fails due to network issues, retrying with the same ID prevents duplicate captures.

---

## Error Handling

### Common Errors

| Error Code | HTTP Status | Cause | Resolution |
|------------|-------------|-------|------------|
| `payment_not_found` | 404 | Invalid payment ID | Verify payment ID from create response |
| `payment_not_in_expected_state` | 400 | Payment not in `requires_capture` status | Check payment status before capture |
| `amount_invalid` | 400 | Capture amount exceeds `amount_capturable` | Reduce amount or enable overcapture |
| `authorization_expired` | 400 | Hold period expired | Create new payment, cannot recapture |
| `connector_error` | 502 | Processor declined capture | Check connector dashboard, retry if transient |
| `rate_limit_exceeded` | 429 | Too many requests | Implement exponential backoff |

### Error Response Format

```json
{
    "error": {
        "type": "invalid_request",
        "code": "amount_invalid",
        "message": "The amount_to_capture exceeds the amount_capturable",
        "data": {
            "amount_to_capture": 10000,
            "amount_capturable": 6540,
            "maximum_allowed": 6540
        }
    }
}
```

### Retry Strategy

```javascript
async function captureWithRetry(paymentId, amount, maxRetries = 3) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            return await hyperswitch.paymentIntents.capture(paymentId, {
                amount_to_capture: amount
            });
        } catch (error) {
            // Retry on transient errors only
            if (error.code === 'rate_limit_exceeded' || 
                error.code === 'connector_error') {
                const delay = Math.pow(2, attempt) * 1000; // Exponential backoff
                await new Promise(r => setTimeout(r, delay));
                continue;
            }
            // Don't retry on client errors
            throw error;
        }
    }
    throw new Error('Max retries exceeded');
}
```

---

## Testing

### Sandbox Setup

1. Use sandbox API keys (`snd_...` for secret, `pk_...` for publishable)
2. Set base URL: `https://sandbox.hyperswitch.io`
3. Configure webhooks to a local tunnel (ngrok) or test endpoint

### Test Cards

Use these Stripe test cards for sandbox testing:

| Card Number | Brand | Scenario |
|-------------|-------|----------|
| `4242424242424242` | Visa | Successful authorization |
| `4000000000000002` | Visa | Card declined |
| `4000000000000127` | Visa | Insufficient funds |
| `4000000000000069` | Visa | Expired card |
| `4000000000000119` | Visa | Incorrect CVC |

### Testing Scenarios

| Test | Steps | Expected Result |
|------|-------|-----------------|
| Full capture flow | Create → Confirm → Capture | Status: `succeeded` |
| Partial capture | Create → Confirm → Capture $30 of $50 | Status: `partially_captured` |
| Authorization expiration | Create → Confirm → Wait 8 days → Capture | Error: `authorization_expired` |
| Void before capture | Create → Confirm → Cancel | Status: `cancelled` |

---

## Next Steps

### Related Documentation

- **[Automatic Capture](../recurring-payments.md)** — Learn about immediate fund settlement
- **[Over Capture](./overcapture.md)** — Detailed guide on capturing above authorized amount
- **[Refunds](../saved-card/README.md)** — Process refunds for captured payments
- **[Webhooks Configuration](https://docs.hyperswitch.io/going-live/webhooks)** — Set up event notifications
- **[API Reference](https://api-reference.hyperswitch.io/v1)** — Complete API documentation

### API Reference Links

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/payments` | POST | [Create payment](https://api-reference.hyperswitch.io/v1/payments/payments--create) |
| `/payments/{id}/confirm` | POST | [Confirm payment](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) |
| `/payments/{id}/capture` | POST | [Capture payment](https://api-reference.hyperswitch.io/v1/payments/payments--capture) |
| `/payments/{id}/cancel` | POST | [Cancel authorization](https://api-reference.hyperswitch.io/v1/payments/payments--cancel) |
| `/payments/{id}` | GET | [Retrieve payment](https://api-reference.hyperswitch.io/v1/payments/payments--retrieve) |

---

## Glossary

| Term | Definition |
|------|------------|
| **Authorization Hold** | Temporary hold on customer funds without actual charge |
| **Automatic Capture** | Immediate settlement of funds upon successful authorization |
| **Manual Capture** | Deferred settlement allowing merchant to control capture timing |
| **Capture Method** | Payment parameter: `automatic` (default) or `manual` |
| **Amount Capturable** | Remaining authorized amount available for capture |
| **Over Capture** | Capturing more than the originally authorized amount |
| **Partial Capture** | Capturing only a portion of the authorized amount |
| **Void** | Releasing an authorization hold without capturing funds |

---

## Comparison: Automatic vs Manual Capture

| Aspect | Automatic Capture | Manual Capture |
|--------|------------------|----------------|
| **Settlement timing** | Immediate | Deferred |
| **Chargeback risk** | Higher (customer charged before fulfillment) | Lower (charge only after delivery) |
| **Implementation complexity** | Simple | Requires capture step |
| **Use cases** | Digital goods, subscriptions | Physical goods, services, pre-orders |
| **Cash flow** | Immediate | Delayed until capture |
| **Flexibility** | Fixed amount | Supports partial/over capture |
| **Webhook events** | `payment_succeeded` | `payment_authorized`, `payment_captured` |

---

*Last updated: March 2024*
