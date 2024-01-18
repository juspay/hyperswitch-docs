---
description: Effectively enhance fraud detection across 40+ countries
---

# 🛡 Fraud & risk management

{% hint style="info" %}
With this section you will get a good understanding of FRM, it's need, use cases, architecture and steps to integrate it in your system.
{% endhint %}

The Hyperswitch Fraud and Risk Management (FRM) platform offers a comprehensive Unified API designed to cater to your specific payment validation needs, effectively enhancing fraud protection within your payment ecosystem.

## Benefits

* **Processor-Agnostic Integration:** Single API connect lets you seamlessly connect with an FRM solution of choice.
* **Customized Fraud Strategies:** Enables users to adjust fraud prevention measures by allowing them to select between Pre-Auth and Post-Auth checks based on specific payment methods and connectors.
* **Unified Dashboard:** A consolidated interface that displays all flagged transactions, making decision-making on potential frauds a breeze.
* **Real-Time Alerts:** Immediate notifications are sent when potential fraudulent activity is detected, ensuring quick action and minimal losses.
* **Insightful Analytics:** Detailed reports on fraud patterns help inform decisions and strategy adjustments.

## Use cases

Below are few sample FRM use cases

* **Online Marketplaces:** Secure transactions on e-commerce platforms like Amazon or eBay, regardless of payment methods or processors. Benefit from chargeback guarantees, dispute resolution, account security, real-time fraud alerts, and streamlined fraud investigation tools.
* **High-Value Transactions:** Protect high value orders in luxury retail, or high-end custom services. Ensure payment validity, prevent chargebacks, optimize PSD2 compliance, reduce transaction friction, gain valuable fraud trend insights, and utilize predictive fraud analysis.

## Overview

You can enable the FRM solution of your choice with few clicks and very minimal code changes. Below are the two scenarios in which FRM can be activated through Hyperswitch.

## Prerequisite

* You should possess payment method information
* You will have to signup with an FRM solution provider and get the API keys

## Pre-Authorization Flow

In the PreAuth flow, the FRM solution is invoked before authorizing a payment with your Payment processor. When a customer attempts to make a payment, the transaction details are sent to the FRM solution for analysis. The FRM solution assesses the risk associated with the transaction based on various parameters such as the customer's historical behaviour, transaction patterns, location, device information, and any other relevant data. It then provides a risk score or recommendation. Based on the risk score or recommendation, one can decide whether to proceed with the transaction, decline it, or take additional verification steps to ensure its legitimacy. The goal is to prevent potentially fraudulent transactions from being authorized in the first place.

<figure><img src="../../.gitbook/assets/frm-pre_auth_flow.jpg" alt=""><figcaption></figcaption></figure>

## Post-Authorization Flow

In the PostAuth flow, the FRM solution is called into action after the payment has been processed by the Payment processor. Once the transaction is completed, the details of the transaction are sent to the FRM solution for a second layer of validation. The FRM solution re-evaluates the transaction using the latest data available and cross-references it with historical patterns and known fraud indicators. The PostAuth flow acts as a safety net to catch any suspicious or fraudulent transactions that might have slipped through the PreAuth flow. If the FRM solution identifies a transaction as potentially fraudulent during the PostAuth flow, appropriate actions can be taken, such as issuing a chargeback, notifying the customer, or initiating further investigation.

<figure><img src="../../.gitbook/assets/frm-post_auth_flow.jpg" alt=""><figcaption></figcaption></figure>

## Supported FRM Processors

| Processors | Supported Flows                              | Supported Actions                                                                                | Processor Features                                                                                                 |
| ---------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Signifyd   | <ul><li>Pre-auth</li><li>Post-auth</li></ul> | <ul><li>Cancel or flag for Manual Review</li><li>Auto Refund or flag for Manual Review</li></ul> | <ul><li>Guaranteed Fraud Protection</li><li>Complete Chargeback Protection</li><li>Auth Rate Conversions</li></ul> |

If your FRM processor of choice is not available in the above list, please put a new features request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests).

## How to get started?

**Step 1:** Log in to your [Hyperswitch account](https://app.hyperswitch.io/login).

<figure><img src="../../.gitbook/assets/frm-step1.png" alt=""><figcaption></figcaption></figure>

**Step 2:** Navigate to the 'Fraud & Risk' tab.

<figure><img src="../../.gitbook/assets/frm-step2.png" alt=""><figcaption></figcaption></figure>

**Step 3:** Select the FRM processor(s) you want to use. And provide your processor credentials and configure your preferred payment methods.

<figure><img src="../../.gitbook/assets/frm-step3a.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/frm-step3b.png" alt=""><figcaption></figcaption></figure>

**Step 4:** Once set up, head to the [API Docs](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) to integrate the FRM API and start testing payments with fraud checks.

{% content-ref url="../../hyperswitch-open-source/testing/test-a-payment.md" %}
[test-a-payment.md](../../hyperswitch-open-source/testing/test-a-payment.md)
{% endcontent-ref %}

## FAQs

* **What are the prerequisites for integrating with the Hyperswitch FRM platform?** Depending on the FRM processor of your choice, you may need to pass additional parameters regarding order fullfilment as a webhook to Hyperswitch. Please refer to the section here for more details.
* **Can I adjust my fraud prevention measures based on specific payment methods and connectors?** Yes, the Hyperswitch FRM platform allows you to customize your fraud prevention measures by selecting between pre-authorization and post-authorization checks for each payment method for a processor and the corresponding action to be taken.
