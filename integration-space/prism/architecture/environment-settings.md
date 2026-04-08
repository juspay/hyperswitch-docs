---
description: >-
  Configure separate environments to isolate test transactions from live payment
  processing
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/prism/architecture/environment-settings
---

# Environment Settings

Your code behaves differently in development, staging, and production. Hyperswitch Prism lets you configure environments explicitly so test transactions don't hit live payment processors and production keys don't leak into debug logs.

## Why Environment Control Matters

Payment integrations have three distinct modes. Typically, most processors support Sandbox and Production. The Development environment will matter when there is a need to mock the payment processor request or response, especially if their sandboxes are flaky for your testing pipeline.

| Environment         | Use Case                                                                                                                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Production**      | Use this to process live customer transactions. Developers monitor real payment flows, handle actual disputes, and optimize conversion based on production data.                                          |
| **Sandbox/Staging** | Use this to validate end-to-end integrations with real payment processors. Developers verify webhook handling, test edge cases with simulated failures, and ensure the full flow works before going live. |
| **Development**     | You may use this to test features locally without network calls. Developers run unit tests against mock responses and iterate on business logic without waiting for external APIs.                        |

## How to Configure Environment?

You may configure environments at the connector level as shown below.

```javascript
const client = new ConnectorServiceClient({
    connectors: {
        stripe: {
            // Use sandbox for development
            apiKey: process.env.STRIPE_TEST_API_KEY,
            environment: 'test'  // or 'live'
        },
        adyen: {
            // Different endpoints for different environments
            apiKey: process.env.ADYEN_TEST_API_KEY,
            merchantAccount: process.env.ADYEN_TEST_MERCHANT,
            environment: 'test'  // or 'live'
        }
    }
});
```
