# Node.js SDK Overview

## 🎯 What is Prism?

Today, integrating multiple payment processors either makes developers running in circles with AI agents to recreate integrations from specs, or developers spending months of engineering effort.

Because every payment processor has diverse APIs, error codes, authentication methods, pdf documents to read, and above all - different behaviour in the actual environment when compared to documented specs. All this rests as tribal or undocumented knowledge making it harder AI agents which are very good at implementing clearly documented specification.

**Prism is a stateless, unified connector library for AI agents and Developers to connect with any payment processor**

**Prism offers hardened transformation through testing on payment processor environment & iterative bug fixing**

**Prism can be embedded in you server application with its wide range of multi-language SDKs, or run as a rRPC microservice**

| ❌ Without Prism                                        | ✅ With Prism                        |
| ------------------------------------------------------ | ----------------------------------- |
| 🗂️ 100+ different API schemas                         | 📋 Single unified schema            |
| ⏳ Never ending agent loops/ months of integration work | ⚡ Hours to integrate, Agent driven  |
| 🔗 Brittle, provider-specific code                     | 🔓 Portable, provider-agnostic code |
| 🚫 Hard to switch providers                            | 🔄 Change providers in 1 line       |

## Installation

```bash
npm install hyperswitch-prism
```

## Quick Start

```javascript
const { PaymentClient } = require('hyperswitch-prism');

const paymentClient = new PaymentClient({
    connector: 'stripe',
    apiKey: 'YOUR_API_KEY',
    environment: 'SANDBOX'
});

// Authorize a payment
const response = await paymentClient.authorize({
    merchantTransactionId: 'txn_order_001',
    amount: {
        minorAmount: 1000,
        currency: 'USD'
    },
    paymentMethod: {
        card: {
            cardNumber: { value: '4242424242424242' },
            cardExpMonth: { value: '12' },
            cardExpYear: { value: '2027' },
            cardCvc: { value: '123' },
            cardHolderName: { value: 'John Doe' }
        }
    },
    authType: 'NO_THREE_DS'
});

console.log(response.status); // AUTHORIZED
```

## Services

| Service                                                                             | Description                                       |
| ----------------------------------------------------------------------------------- | ------------------------------------------------- |
| [Payment Service](payment-service-1.md)                                             | Process payments from authorization to settlement |
| [Recurring Payment Service](recurring-payment-service-1.md)                         | Manage subscriptions and recurring billing        |
| [Refund Service](refund-service-1.md)                                               | Retrieve and track refund statuses                |
| [Dispute Service](dispute-service-1.md)                                             | Handle chargebacks and disputes                   |
| [Event Service](event-service-1.md)                                                 | Process webhook notifications                     |
| [Payment Method Service](payment-method-service-1.md)                               | Store and manage payment methods                  |
| [Customer Service](customer-service-1.md)                                           | Manage customer profiles                          |
| [Merchant Authentication Service](merchant-authentication-service-1.md)             | Generate access tokens                            |
| [Payment Method Authentication Service](payment-method-authentication-service-1.md) | 3D Secure authentication                          |
| [Payout Service](payout-service-1.md)                                               | Send funds to recipients                          |

## Configuration

| Option        | Type   | Required | Description                                  |
| ------------- | ------ | -------- | -------------------------------------------- |
| `connector`   | string | Yes      | Payment connector name (stripe, adyen, etc.) |
| `apiKey`      | string | Yes      | Your API key                                 |
| `environment` | string | Yes      | SANDBOX or PRODUCTION                        |
| `timeout`     | number | No       | Request timeout in ms (default: 30000)       |

## Error Handling

```javascript
try {
    const response = await paymentClient.authorize(request);
} catch (error) {
    if (error.code === 'PAYMENT_DECLINED') {
        // Handle declined payment
    } else if (error.code === 'VALIDATION_ERROR') {
        // Handle validation error
    } else {
        // Handle other errors
    }
}
```

## Support

For support and documentation, visit [https://docs.hyperswitch.io](https://docs.hyperswitch.io)
