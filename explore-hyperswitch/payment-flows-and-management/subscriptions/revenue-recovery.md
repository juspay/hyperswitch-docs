---
icon: clock-rotate-left
---

# Revenue Recovery

Revenue Recovery module of Hyperswitch is designed to act as a failsafe for recurring payments. It seamlessly integrates with merchants' existing subscription management systems and performs intelligent retries to recover failed transactions. With minimal effort from merchants, Revenue Recovery delivers an uplift in authorization rates, helping businesses reduce churn, recover lost revenue, and maximize customer lifetime value.

### **Why is Revenue Recovery Important?**

For subscription-based businesses, involuntary churn from failed recurring payments can significantly impact revenue. Payment failures may result from insufficient funds, fraud checks, or issuer restrictions. A simple dunning setup is not effective in retrieving these failed payments. Revenue recovery’s Intelligent retry engine analyzes 20+ transaction parameters to find best retry strategy to recover the given payment.

### Benefits for SaaS Businesses

1. **Reduced Passive Churn**: Intelligent retries ensure payments succeed on subsequent attempts, decreasing subscription cancellations.
2. **Seamless Integration**: Easily integrate with existing billing platforms or custom systems without reengineering the payment architecture.
3. **Data-Driven Recovery**: Leverage insights from transaction parameters like decline codes and issuer behaviors to tailor retry strategies.
4. **Enhanced Operational Efficiency**: Automate recovery workflows and record transactions for complete visibility.

### How Does Revenue Recovery Work?

1. **Retry Engine Functionality**:
   1. Intelligent Scheduling: The retry engine analyzes 20+ transaction parameters to determine the best time and acquirer for retries.
   2. Dynamic Routing: Supports multi-PSP setups, allowing retries through the most promising payment gateways.
   3. Compliance Management: Adheres to network-specific retry restrictions, avoiding penalties.
2. **Recovery in Action** (Based on Sequence Diagram):
   1. A failed subscription payment triggers the retry engine.
   2. The engine schedules retries based on failure type, retry limits, and past patterns.
   3. Successful retries update invoice statuses in real time. Failed retries proceed to the next retry schedule until limits are reached.

### Key Features

* **Retry Optimization**:
  * Reduces time between retries, enhancing recovery speed.
* **Error Code Management**:
  * Maps issuer-specific decline codes to identify root causes.
  * Adapts retry strategies based on error categories (e.g., insufficient funds, fraud etc).
* **Integration with Existing Workflows**:
  * Enhances recovery rates without disrupting current dunning setups.
  * Supports integration with billing platforms for automated transaction tracking.

### Enabling Revenue Recovery in Hyperswitch

#### **Step 1: Integration**

* Provide credentials for payment processors and set up our webhook into the payment processors to trigger retry transactions.
* Provide credentials for the billing platform and set up webhooks in your billing platform to monitor failed payments.

#### **Step 2: Configure Retry Rules**:

* Access the Retry Engine Dashboard to define the current dunning setup in the billing platform.
