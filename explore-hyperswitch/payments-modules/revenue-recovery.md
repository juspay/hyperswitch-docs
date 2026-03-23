---
icon: clock-rotate-left
description: Configure Juspay Hyperswitch Revenue Recovery to automatically retry failed recurring payments and reduce subscription churn for your SaaS business
---

# Juspay Hyperswitch Revenue Recovery

Revenue Recovery module of Juspay Hyperswitch is designed to act as a failsafe for recurring payments. It seamlessly integrates with merchants' existing subscription management systems and performs intelligent retries to recover failed transactions. With minimal effort from merchants, Revenue Recovery delivers an uplift in authorization rates, helping businesses reduce churn, recover lost revenue, and maximize customer lifetime value.

## Why is Revenue Recovery Important?

For subscription-based businesses, involuntary churn from failed recurring payments can significantly impact revenue. Payment failures may result from insufficient funds, fraud checks, or issuer restrictions. A simple dunning setup is not effective in retrieving these failed payments. Revenue recovery's Intelligent retry engine analyzes 20+ transaction parameters to find best retry strategy to recover the given payment.

## Benefits for SaaS Businesses

1. **Reduced Passive Churn**: Intelligent retries ensure payments succeed on subsequent attempts, decreasing subscription cancellations.
2. **Seamless Integration**: Easily integrate with existing billing platforms or custom systems without reengineering the payment architecture.
3. **Data-Driven Recovery**: Leverage insights from transaction parameters like decline codes and issuer behaviors to tailor retry strategies.

## How Does Revenue Recovery Work?

### Integration

Merchants can configure Revenue Recovery entirely through the dashboard without writing any code. This configuration can be completed using the following three steps.
1. **Step 1:** Provide credentials for payment processors and set up our webhooks with these processors.
2. **Step 2:** Provide credentials for the subscription platform used and set up our webhook within this platform.
3. **Step 3:** Configure the recovery plan (retry budget, start retry after etc.)

### Recovery in action

Once the setup is complete, Revenue Recovery automatically begins monitoring transactions via webhook. When a failed transaction is detected, the system evaluates over 20 parameters to intelligently schedule a retry, aiming to recover the payment. These transactions are then recorded back into the subscription platform to avoid subscription cancellations.

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "background": "#FFFFFF",
    "primaryColor": "#346DDB",
    "primaryTextColor": "#FFFFFF",
    "primaryBorderColor": "#1E4FAA",
    "secondaryColor": "#F6F9FC",
    "secondaryTextColor": "#0A2540",
    "secondaryBorderColor": "#D1D9E0",
    "tertiaryColor": "#F6F9FC",
    "tertiaryTextColor": "#0A2540",
    "tertiaryBorderColor": "#D1D9E0",
    "mainBkg": "#F6F9FC",
    "nodeBorder": "#D1D9E0",
    "clusterBkg": "#F6F9FC",
    "clusterBorder": "#D1D9E0",
    "lineColor": "#346DDB",
    "edgeLabelBackground": "#FFFFFF",
    "titleColor": "#0A2540",
    "textColor": "#0A2540",
    "labelColor": "#0A2540",
    "labelBoxBkgColor": "#F6F9FC",
    "labelBoxBorderColor": "#D1D9E0",
    "loopTextColor": "#0A2540",
    "noteBkgColor": "#F6F9FC",
    "noteBorderColor": "#D1D9E0",
    "noteTextColor": "#0A2540",
    "activationBkgColor": "#EBF1FC",
    "activationBorderColor": "#346DDB",
    "actorBkg": "#F6F9FC",
    "actorBorder": "#D1D9E0",
    "actorTextColor": "#0A2540",
    "actorLineColor": "#D1D9E0",
    "fontFamily": "Inter, sans-serif",
    "fontSize": "14px"
  }
}}%%
sequenceDiagram
    participant Merchant
    participant BillingPlatform as Billing Platform
    participant RRDashboard as RR Dashboard
    participant RetryEngine as Retry Engine
    participant PaymentService as Payment Service
    participant PaymentProcessor as Payment Processor
    
    rect rgb(240, 240, 240)
        Note over Merchant,PaymentProcessor: Onboarding Flow
        Merchant->>RRDashboard: Connect Payment Processor
        RRDashboard-->>Merchant: Get Webhook URL
        Merchant->>PaymentProcessor: Setup Webhook in Payment Processor
        Merchant->>RRDashboard: Connect Billing Platform and provide retry configurations
        RRDashboard-->>Merchant: Get Webhook URL
        Merchant->>BillingPlatform: Setup Webhook in Billing Platform
    end
    
    rect rgb(240, 240, 240)
        Note over Merchant,PaymentProcessor: Recovery in Action
        BillingPlatform->>PaymentService: Trigger subscription payment
        PaymentService->>PaymentProcessor: Process payment
        PaymentProcessor-->>PaymentService: Failed Response
        PaymentService-->>BillingPlatform: Failed Response
        RetryEngine->>PaymentService: Trigger Retry = 1
        PaymentService->>PaymentProcessor: Process payment
        PaymentProcessor-->>PaymentService: Failed Response
        PaymentService-->>RetryEngine: Failed Response
        RetryEngine->>PaymentService: Trigger Retry = x
        PaymentService->>PaymentProcessor: Process payment
        PaymentProcessor-->>PaymentService: Failed Response
        PaymentService-->>RetryEngine: Failed Response
        RetryEngine->>BillingPlatform: Failed Transaction and Invoice
        RetryEngine->>RRDashboard: Schedule Retry = x + 1
        RRDashboard-->>BillingPlatform: Update retry schedule time for the invoice
        RetryEngine->>PaymentService: Trigger Transaction
        PaymentService->>PaymentProcessor: Process payment
        PaymentProcessor-->>PaymentService: Failed Response
        PaymentService-->>RetryEngine: Failed Response
        RetryEngine->>RRDashboard: Record transaction for the invoice
        RRDashboard-->>BillingPlatform: Record transaction for the invoice
        Merchant->>BillingPlatform: Check transaction
        Merchant->>RRDashboard: Check transaction
        RetryEngine->>PaymentService: Schedule Retry if retry count not exhausted or response != terminal error
        RetryEngine->>PaymentService: Trigger Transaction
        PaymentService->>PaymentProcessor: Process payment
        PaymentProcessor-->>PaymentService: Success/Failed Response
        PaymentService-->>RetryEngine: Success/Failed Response
        RetryEngine->>RRDashboard: Record transaction and close the invoice
        RRDashboard-->>BillingPlatform: Record transaction or change the invoice status
    end
```

## Key Features

* **Retry Optimization**:
  * Reduces time between retries, enhancing recovery speed.
* **Error Code Management**:
  * Maps issuer-specific decline codes to identify root causes.
  * Adapts retry strategies based on error categories (e.g., insufficient funds, fraud etc).
* **Integration with Existing Workflows**:
  * Enhances recovery rates without disrupting current dunning setups.
  * Supports integration with billing platforms for automation of payment recovery.
