---
description: Infinite control over managing your payments
---

# 🛣️ Intelligent Routing

**TL;DR:** Intelligent Routing dynamically directs each payment to the most appropriate processor based on cost, success rates, latency, and your custom business rules. Configure rules via API or Control Centre, apply them to business profiles, and let the system automatically optimise for higher authorization rates (+5-15%), lower costs (10-30% savings), and better user experience.

{% hint style="info" %}
With this section, understand how the Hyperswitch Smart Router works to improve your conversion rates and reduces processing costs by intelligently routing payments across various processors
{% endhint %}

{% embed url="https://hyperswitch.io/video/edit_conf.mp4" %}

## Overview

Intelligent routing is a core capability of Juspay Hyperswitch that optimises payment success rates and reduces costs by dynamically routing transactions to the most appropriate payment processor.

### How It Works

Hyperswitch evaluates each transaction against configured routing rules and selects the optimal processor based on:

- **Cost optimisation**: Route to lowest-cost processor
- **Success rate**: Route to processor with highest authorization rates
- **Latency**: Route to fastest processor
- **Custom rules**: Apply business-specific logic
- **Dynamic retries**: Automatically retry failed payments with alternative processors

## Prerequisites

To get started with Smart Router, ensure to have one or more payment processors integrated. You can integrate the payment processor of your choice on the Control Center by following the [Connector Integration](../hyperswitch-cloud/connectors/) guide.

### Authentication

All API requests require authentication using an API key. Obtain your API key from the Hyperswitch Control Centre under **Developer > API Keys**.

Include your API key in the header of every request:

```
api-key: YOUR_API_KEY
```

### Base URL

All API endpoints use the following base URL:

```
https://api.hyperswitch.io
```

### Required Permissions

To configure and manage routing rules, your API key must have the following permissions:
- `routing:read` — View routing configurations
- `routing:write` — Create and modify routing rules
- `business_profile:write` — Apply routing to business profiles

## Routing Configuration

### Step 1: Define Routing Rules

Create routing rules via API:

**Request:**

```bash
curl -X POST https://api.hyperswitch.io/routing \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "name": "Cost-Optimised Routing",
    "description": "Route to lowest cost processor",
    "algorithm": {
      "type": "cost_based",
      "default_connector": "stripe"
    },
    "rules": [
      {
        "connector": "adyen",
        "conditions": [
          {
            "field": "payment_method",
            "operator": "equals",
            "value": "card"
          },
          {
            "field": "card_network",
            "operator": "equals",
            "value": "visa"
          }
        ]
      }
    ]
  }'
```

**Success Response (201 Created):**

```json
{
  "routing_id": "routing_67890",
  "name": "Cost-Optimised Routing",
  "description": "Route to lowest cost processor",
  "algorithm": {
    "type": "cost_based",
    "default_connector": "stripe"
  },
  "rules": [
    {
      "connector": "adyen",
      "conditions": [
        {
          "field": "payment_method",
          "operator": "equals",
          "value": "card"
        },
        {
          "field": "card_network",
          "operator": "equals",
          "value": "visa"
        }
      ]
    }
  ],
  "created_at": "2024-03-10T10:30:00Z",
  "status": "active"
}
```

### Step 2: Apply Routing Profile

Link the routing configuration to your business profile:

**Request:**

```bash
curl -X POST https://api.hyperswitch.io/account/business_profile \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "profile_id": "pro_12345",
    "routing_algorithm_id": "routing_67890"
  }'
```

**Success Response (200 OK):**

```json
{
  "profile_id": "pro_12345",
  "merchant_id": "merchant_abc123",
  "routing_algorithm_id": "routing_67890",
  "updated_at": "2024-03-10T10:35:00Z"
}
```

## Routing Algorithms

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **Cost-based** | Routes to lowest-cost processor | Cost-sensitive businesses |
| **Success-rate** | Routes to highest-auth-rate processor | Maximising conversions |
| **Latency-based** | Routes to fastest processor | User experience priority |
| **Volume-based** | Distributes volume across processors | Load balancing |
| **Custom** | Apply your own business logic | Complex requirements |

## Rule Evaluation Order

When a payment is processed, Hyperswitch evaluates routing rules in the following order:

1. **Custom Rules First**: Rules with explicit conditions are evaluated in the order they are defined
2. **Algorithm Selection**: If no custom rule matches, the selected algorithm determines the processor
3. **Default Connector**: If the algorithm cannot determine a processor, the `default_connector` is used

### Evaluation Flow

```
Payment Request Received
         ↓
Evaluate Custom Rules (in order)
         ↓
    Match Found? ──Yes──→ Use Specified Connector
         ↓ No
Apply Selected Algorithm
         ↓
Algorithm Returns Processor? ──Yes──→ Use Algorithm Result
         ↓ No
Use Default Connector
```

### Rule Priority Example

```json
{
  "rules": [
    {
      "connector": "adyen",
      "conditions": [
        { "field": "card_network", "operator": "equals", "value": "visa" },
        { "field": "amount", "operator": "less_than", "value": "10000" }
      ]
    },
    {
      "connector": "stripe",
      "conditions": [
        { "field": "card_network", "operator": "equals", "value": "visa" }
      ]
    }
  ],
  "algorithm": {
    "type": "cost_based",
    "default_connector": "checkout"
  }
}
```

In this example:
- A $50 Visa payment matches both rules, so **Adyen** is used (first match)
- A $150 Visa payment matches only the second rule, so **Stripe** is used
- A Mastercard payment matches no rules, so the **cost-based algorithm** selects the processor
- If the algorithm fails, **Checkout** is used as the default

## Fallback Behavior

Hyperswitch provides multiple fallback mechanisms to ensure payments are processed even when primary routing fails:

### 1. Default Connector Fallback

If no rules match and the algorithm cannot determine a processor, the `default_connector` specified in the algorithm configuration is used.

### 2. Smart Retry Fallback

When a payment fails with one processor, Hyperswitch can automatically retry with alternative processors from the retry list.

### 3. Connector Health Fallback

If a connector is marked as unhealthy or unavailable, Hyperswitch automatically skips it and uses the next available option based on the active algorithm.

### Fallback Configuration Example

```json
{
  "algorithm": {
    "type": "success_rate",
    "default_connector": "stripe"
  },
  "rules": [],
  "fallback_config": {
    "skip_unhealthy_connectors": true,
    "health_check_interval_seconds": 60
  }
}
```

## Smart Retries

When a payment fails, Hyperswitch can automatically retry with alternative processors:

**Request:**

```bash
curl -X POST https://api.hyperswitch.io/payments \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "amount": 10000,
    "currency": "USD",
    "routing": {
      "retry": {
        "enabled": true,
        "max_attempts": 3,
        "connectors": ["stripe", "adyen", "checkout"]
      }
    }
  }'
```

**Success Response (200 OK):**

```json
{
  "payment_id": "pay_xyz789",
  "status": "succeeded",
  "amount": 10000,
  "currency": "USD",
  "connector": "adyen",
  "attempts": [
    {
      "attempt_id": "att_001",
      "connector": "stripe",
      "status": "failed",
      "error_code": "card_declined",
      "error_message": "Your card was declined."
    },
    {
      "attempt_id": "att_002",
      "connector": "adyen",
      "status": "succeeded"
    }
  ]
}
```

### Retry Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enable/disable smart retries |
| `max_attempts` | integer | Yes | Maximum number of retry attempts (1-5) |
| `connectors` | array | Yes | Ordered list of connectors to attempt |

## What is smart payment routing?

Selling globally or otherwise invariably brings in a requirement to adopt multiple payment processors to cater to a wide range of payment method needs of the customers and gives you the flexibility to switch between processors to manage down-time and , it could be vital to optimising your payment processing costs as your business can choose the most optimal payment processors for every payment based on the cost, region and customer.

Hence, Hyperswitch's smart router is designed as a no-code tool to provide complete control and transparency in creating and modifying payment routing rules. Hyperswitch supports below formats of Smart Routing.

**Volume Based Configuration:** Define volume distribution among multiple payment processors using percentages.

**Rule Based Configuration:** More granular control which allows to define custom routing logics based on different parameters of payment.

**Default Fallback Routing :** If the active routing rules are not applicable, the priority order of all configured payment processors is used to route payments. This priority order is configurable from the Dashboard.

**Cost Based Configuration** (submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests))**:** Automatically routes transaction to the payment processor charging the least MDR (merchant discount rate) for the opted payment method.

## How does the Smart Router work?

Hyperswitch Smart Router Engine evaluates every payment request against your predefined routing logic and makes a decision on the best payment processor for the payment, and executes the transaction. If the payment fails or if the payment processor is down, the payment is automatically retried through a different processor.

<figure><img src="../.gitbook/assets/Smart Routing Flow.drawio.png" alt=""><figcaption><p>Hyperswitch Smart Router Flow</p></figcaption></figure>

## How to configure the Smart Router?

[Hyperswitch dashboard](https://app.hyperswitch.io/routing) provides a simple, intuitive UI to configure multiple Routing rules on your dashboard under the **Routing** tab. There are three routing rule formats that Hyperswitch currently supports.\


<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Rule Based Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/rule-based-routing.md">rule-based-routing.md</a></td><td><a href="../.gitbook/assets/rule-based.png">rule-based.png</a></td></tr><tr><td><strong>Volume Based Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/volume-based-routing.md">volume-based-routing.md</a></td><td><a href="../.gitbook/assets/volume-based.png">volume-based.png</a></td></tr><tr><td><strong>Default Fallback Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/default-fallback-routing.md">default-fallback-routing.md</a></td><td><a href="../.gitbook/assets/default.png">default.png</a></td></tr></tbody></table>

## Analytics and Optimisation

Monitor routing performance in the Control Centre:

- Authorization rates by processor
- Cost per transaction
- Retry success rates
- Geographic performance

Use these insights to fine-tune your routing rules.

## Use Case Scenarios

### Scenario 1: Cost-Optimised E-commerce

**Business:** Mid-sized online retailer with tight margins  
**Goal:** Minimise payment processing costs

```json
{
  "name": "Cost-Optimised EU Routing",
  "algorithm": {
    "type": "cost_based",
    "default_connector": "stripe"
  },
  "rules": [
    {
      "connector": "checkout",
      "conditions": [
        { "field": "billing_address.country", "operator": "equals", "value": "GB" }
      ]
    }
  ]
}
```

### Scenario 2: Conversion-Focused SaaS

**Business:** Subscription-based SaaS platform  
**Goal:** Maximise payment success rates

```json
{
  "name": "High-Converting Routing",
  "algorithm": {
    "type": "success_rate",
    "default_connector": "adyen"
  },
  "rules": [
    {
      "connector": "stripe",
      "conditions": [
        { "field": "card_network", "operator": "equals", "value": "amex" }
      ]
    }
  ]
}
```

### Scenario 3: Global Marketplace

**Business:** Multi-region marketplace with diverse payment methods  
**Goal:** Optimal routing by region and payment method

```json
{
  "name": "Global Marketplace Routing",
  "algorithm": {
    "type": "latency_based",
    "default_connector": "stripe"
  },
  "rules": [
    {
      "connector": "adyen",
      "conditions": [
        { "field": "billing_address.country", "operator": "in", "value": ["DE", "FR", "NL"] }
      ]
    },
    {
      "connector": "checkout",
      "conditions": [
        { "field": "payment_method", "operator": "equals", "value": "ideal" }
      ]
    }
  ]
}
```

## Error Handling

### Common Error Responses

#### 401 Unauthorized

```json
{
  "error": {
    "type": "authentication_error",
    "code": "invalid_api_key",
    "message": "The provided API key is invalid or expired."
  }
}
```

**Resolution:** Verify your API key is correct and has not expired. Generate a new key in the Control Centre if needed.

#### 400 Bad Request

```json
{
  "error": {
    "type": "invalid_request",
    "code": "validation_error",
    "message": "Invalid routing configuration",
    "details": [
      {
        "field": "algorithm.type",
        "issue": "Unsupported algorithm type 'cost_optimized'"
      }
    ]
  }
}
```

**Resolution:** Check that all field values match the supported options. Refer to the Routing Algorithms section for valid algorithm types.

#### 404 Not Found

```json
{
  "error": {
    "type": "invalid_request",
    "code": "resource_missing",
    "message": "Business profile 'pro_12345' not found"
  }
}
```

**Resolution:** Verify the `profile_id` or `routing_id` exists and belongs to your merchant account.

#### 422 Unprocessable Entity

```json
{
  "error": {
    "type": "invalid_request",
    "code": "invalid_configuration",
    "message": "Connector 'unknown_processor' is not configured for your account"
  }
}
```

**Resolution:** Ensure the connector is enabled and properly configured in your Hyperswitch account before referencing it in routing rules.

## Testing and Validation

### Testing Routing Rules

Before applying routing rules to production traffic, test them using the routing simulation endpoint:

```bash
curl -X POST https://api.hyperswitch.io/routing/simulate \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{
    "routing_id": "routing_67890",
    "payment_context": {
      "amount": 10000,
      "currency": "USD",
      "payment_method": "card",
      "card_network": "visa",
      "billing_address": {
        "country": "US"
      }
    }
  }'
```

**Response:**

```json
{
  "routing_id": "routing_67890",
  "selected_connector": "adyen",
  "matched_rule": {
    "index": 0,
    "connector": "adyen"
  },
  "algorithm_applied": false,
  "fallback_used": false
}
```

### Validation Checklist

Before deploying routing changes:

- [ ] Test routing simulation with various payment scenarios
- [ ] Verify all referenced connectors are active and healthy
- [ ] Confirm default connector is set and operational
- [ ] Validate retry configuration does not exceed rate limits
- [ ] Review error handling for each potential failure mode
- [ ] Monitor routing performance metrics after deployment

## Next step&#20;

To test the Smart Router, after activating one rule, we can make a Test Payment using the [Hyperswitch Dashboard ](https://app.hyperswitch.io/sdk)

{% content-ref url="../hyperswitch-open-source/testing/test-a-payment.md" %}
[test-a-payment.md](../hyperswitch-open-source/testing/test-a-payment.md)
{% endcontent-ref %}

## Benefits

| Benefit | Impact |
|---------|--------|
| **Higher authorization rates** | +5-15% improvement |
| **Lower processing costs** | Save 10-30% on fees |
| **Reduced downtime impact** | Automatic failover |
| **Better user experience** | Faster payments, fewer failures |

## API Reference Summary

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/routing` | POST | Create routing configuration |
| `/routing/{routing_id}` | GET | Retrieve routing configuration |
| `/routing/{routing_id}` | PUT | Update routing configuration |
| `/routing/{routing_id}` | DELETE | Delete routing configuration |
| `/routing/simulate` | POST | Test routing rules |
| `/account/business_profile` | POST | Apply routing to business profile |
| `/payments` | POST | Create payment with routing options |

## Glossary

| Term | Definition |
|------|------------|
| **Connector** | A payment processor integrated with Hyperswitch (e.g., Stripe, Adyen) |
| **Routing Rule** | A condition-based directive that specifies which connector to use |
| **Algorithm** | The logic used to select a processor when no rules match |
| **Default Connector** | The fallback processor used when no rule or algorithm applies |
| **Smart Retry** | Automatic retry of failed payments with alternative processors |

<details>

<summary>FAQs</summary>

### 1. What parameters can I use to configure routing rules?

The rule-based routing supports setting up advanced rule configuration based on all critical /payments parameters such as Payment Method, Payment Method Type, Country, Currency, Amount etc.

### 2. Why did my payment go through 'Y' connector even though I have specified 'X' in my routing configuration? OR Why is it showing me 'Abc' payment method in SDK checkout even though I have not enabled it for the 'X' connector that I'm routing my payments through?

There can be multiple reasons why this happened but all of them can be boiled down to a "connector eligibility failure" for a given payment. We'll walk through a common scenario to examine what this really means.

* Imagine that you configured two connectors for your account. Say `Stripe`, then `Adyen`, in that order. Since you configured them in that order, your default fallback looks like this: `[Stripe, Adyen]` (connectors are appended to the end of your default fallback list when configured for the first time)
* In your connectors dashboard, you enable Cards for Stripe, and ApplePay for Adyen.
* Now you create a new Volume-based routing configuration, and you configure it to route 100% of your traffic through Stripe for now.
* Now you go ahead and open up the Hyperswitch SDK to make a test payment. In the payment method selection area, you can see two buttons, one for `Cards` and one for `ApplePay`.&#20;
  * This is where you run into your first question. "Why is it showing me ApplePay even though I have configured 100% of my payments to go through Stripe, and ApplePay is not enabled for Stripe?"
  * The answer to this is, the payment methods that are shown to the customer in the SDK aren't conscious of your routing configuration. We prioritize giving your customers the complete spread of all enabled payment methods across all of your enabled connectors. Therefore, if you specifically do not wish for ApplePay to appear on your checkout screen, you need to disable it in `Adyen` here, even though your routing configuration makes no mention of Adyen.
* Now you select `ApplePay`, go through the required steps, confirm the payment, and it succeeds. You go to your payments dashboard and see that the payment went through `Adyen`.
  * This is where you run into the second question. "Why is the payment going through `Adyen` even though I have set my routing configuration to route 100% of my payments through `Stripe`?
  * The answer to this carries over from the previous point. Since we displayed `ApplePay` on the checkout screen even though it wasn't enabled for your preferred connector `Stripe`, we need to adhere to your connector payment method configuration and ensure the payment goes through the right connector, here, `Adyen` since `ApplePay` is only enabled for Adyen. To briefly explain how Hyperswitch reaches this conclusion :-
    * Hyperswitch runs your configured routing algorithm. Since this is `100% Stripe`, Hyperswitch receives `Stripe` as the outuput.
    * Hyperswitch then runs an Eligibility Analysis on the output (`Stripe`) to gauge its eligibility for the current payment. The Eligibility Analysis fails once Hyperswitch realizes that the payment is made through `ApplePay` which is not enabled for `Stripe`
    * The application then goes into fallback mode and loads your `default fallback`, which is `[Stripe, Adyen]` as seen earlier.
    * The application looks through the list in order. It ignores `Stripe` since it has already failed the Eligibility Analysis. It instead subjects `Adyen` (the next connector in the list) to the same Eligibility Analysis.
    * This time the analysis passes since `ApplePay` is enabled for `Adyen`.
    * Hyperswitch takes `Adyen` as the final connector to make the payment through even though your configuration says `100% Stripe`.
  * This fallback flow is taken when none of the connectors in the output of routing are eligible for the payment. This is done in an effort to maximize the success rate of the payment even if it means deviating from the currently active routing configuration.

</details>
