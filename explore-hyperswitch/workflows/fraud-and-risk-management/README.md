---
description: Effectively enhance fraud detection with your preferred FRM engine
icon: shield-check
---

# Fraud & Risk Management

The Hyperswitch Fraud and Risk Management (FRM) workflow offers a comprehensive Unified API designed to cater to your specific payment validation needs, effectively enhancing fraud protection within your payment ecosystem.

#### Key Benefits of FRM workflows

* Processor-Agnostic Integration: Single API connect lets you seamlessly connect with an FRM solution of choice.
* Customized Fraud Strategies: Enables users to adjust fraud prevention measures by allowing them to select between Pre-Auth and Post-Auth checks based on specific payment methods and connectors.
* Unified Dashboard: A consolidated interface that displays all flagged transactions, making decision-making on potential frauds a breeze.
* Real-Time Alerts: Immediate notifications are sent when potential fraudulent activity is detected, ensuring quick action and minimal losses.
* Insightful Analytics: Detailed reports on fraud patterns help inform decisions and strategy adjustments.

#### Use cases for implementing FRM workflows

* Online Marketplaces: Secure transactions on e-commerce platforms, regardless of payment methods or processors. Benefit from chargeback guarantees, dispute resolution, account security, real-time fraud alerts, and streamlined fraud investigation tools.
* High-Value Transactions: Protect high value orders in luxury retail, or high-end custom services. Ensure payment validity, prevent chargebacks, optimize PSD2 compliance, reduce transaction friction, gain valuable fraud trend insights, and utilize predictive fraud analysis.

#### Supported FRM workflows

| Pre-authorization flow                                                                                                                                                                                                                                          | Post-authorization flow                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p></p><p>The Pre-Auth flow is executed before payment authorization.</p><p></p><p>This flow is supported for any payment method </p><p></p><p>Actions supported are:</p><ul><li>Continue on <code>Accept</code></li><li>Halt on <code>Decline</code></li></ul> | <p></p><p>The Post-Auth flow occurs after payment authorization by the processor<br><br>This flow is supported for only cards payment method <br></p><p>Actions supported are:</p><ul><li>Continue to <code>Accept</code></li><li>Halt on <code>Decline</code></li><li>Approve/Decline on <code>Review</code></li></ul> |
