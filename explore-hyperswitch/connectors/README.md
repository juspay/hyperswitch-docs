---
description: >-
  Integrate with more than 200+ Connectors enabling 150+ payment methods with
  zero development effort.
icon: plug
---

# Connectors Integration

### Overview

Connectors are integrations that allow Hyperswitch to talk to external payment services such as PSPs, Acquirers, APMs, Card vaults, 3DS authentications, Fraud management, Subscription, Payouts and more. They act as bridges between your Hyperswitch setup and the third-party services that move or manage money for your business.

Every provider has its own APIs, authentication methods, and feature sets. Hyperswitch standardizes these differences through connectors, exposing a single unified **Payments API**. This means you can add, switch, or remove processors without rewriting your code—just plug in credentials and start transacting.

Connectors form the foundation of Hyperswitch's **payment orchestration layer**, enabling you to manage payments, routing, 3DS authentication, fraud checks, and payouts through a single interface.

#### Why Multiple Processors?

As your business grows faster, there would be a need to expand payment offerings with more payment processors. This need might arise due to multiple reasons:

* **Vendor Independence:** Reducing dependency on a single processor and reducing vendor lock-in.
* **Performance Optimization:** Introducing a challenger processor for better cost and auth rates.
* **Global Reach:** Launching a business in new geography with a local payment processor.
* **Localized Experience:** Offering local or new payment methods for your customers.
* **Reliability:** Reducing technical downtimes and improving success rates with a fallback.

Integrating and maintaining multiple payment processors and their different versions is a time and resource intensive process. Hyperswitch can add a new PSP in [**2 weeks**](https://hyperswitch.io/blog/part-1-5-payment-challenges-for-vertical-saas-businesses), allowing you to focus on your core business activities.

#### Adding a Connector

Most connector integrations follow a simple click-and-connect flow on Hyperswitch using your connector credentials. However, some connectors may require additional setup details as required on the control center.

**Standard Setup Steps**

1. **PSP Registration:** You need to be registered with the PSP in order to proceed. In case you aren't, you can quickly setup your account by signing up on their dashboard.
2. **Platform Access:** You should have registered on [Hyperswitch Control center](https://app.hyperswitch.io/).
3. **Credential Mapping:** Add the PSP authentication credentials from their dashboard into the Hyperswitch Control center.

**Authentication Examples**

Authentication credentials vary across different PSPs. Common combinations include:

| Provider          | Required Credentials                             |
| ----------------- | ------------------------------------------------ |
| **Authorize.net** | API Login ID and Transaction Key                 |
| **Adyen**         | API key and Account ID                           |
| **Braintree**     | Merchant ID, Public key and Private key          |
| **Airwallex**     | API key and Client ID                            |
| **Fiserv**        | API Key, API Secret, Merchant ID and Terminal ID |
| **Paypal**        | Client Secret and Client ID                      |

4. **Method Configuration:** Choose the payment methods you want to utilize with the connector (e.g. Authorize.net) by navigating to the next screen on Hyperswitch.
5. **Activation:** Enable the PSP once you're done.

#### Connector Types

Hyperswitch supports a wide variety of connectors to manage your entire financial stack:

* **Core Payments:** Payment Processors, Acquirers & APMs.
* **Platforms:** Payment platforms and Payouts Processors.
* **Recurring Billing:** Subscription Providers.
* **Security & Risk:** &#x20;
  * [Card Vaults](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault)
  * [3DS Authentications](https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager)
  * [Fraud Management](https://docs.hyperswitch.io/explore-hyperswitch/workflows/fraud-and-risk-management)

**Quick Links**

| Resource                                                                                                               | Description                                                           |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [**Activate Connector**](https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch) | A detailed guide on how to configure a connector and payment methods. |
| [**Integrations Directory**](https://juspay.io/integrations)                                                           | Learn more about all the available connectors and payments methods.   |
| [**Request Integration**](https://hyperswitch-io.slack.com/ssb/redirect)                                               | Don't see your processor? Raise an integration request on Slack.      |
