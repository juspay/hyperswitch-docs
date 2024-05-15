---
description: Hyperswitch roadmap (Oct to Dec'23)
---

# 🛣️ Previous roadmap - Q4 2023

🗺️ Our Roadmap typically pans out over a 3-month period and we establish topics we work on upfront.

Before the beginning of every quarter we come together to develop the next roadmap based on our core values, findings over the previous quarter, what we heard from the community as issues and feature requests, in face-to-face discussions and social media.

👂And as always, we listen to your feedback and adapt our plans if needed.

## Core Values

Our core values have pretty much remained the same since the early days and here they are:

* Make payments more `accessible` and `affordable` to every digital business
* Staying `simple` and `super-lightweight`, at the same time `reliable` and `scalable` payment switch
* Being `community-first` in ideation, planning and execution of features

## Themes for Roadmap

There are a lot of problems to be solved in payments, but our majority of our current focus falls under 5 themes below.

* 👨‍💻 **Developer Experience:** Providing a great self-service and self-installation experience for developers who wish to use or contribute back to Hyperswitch.
* 💰 **Reducing Payment Costs:** Payments should be like a free utility for digital businesses. Any business should be able reduce payment processing costs by embracing the diversity in payments.
* 📈 **Improving Authorization Rates:** Ensuring a best-in-class payment experience and access to latest innovations in the payments ecosystem for all businesses.
* 👍 **Reducing Payment Operations:** Managing payments across multiple countries, currencies and processors should not add to the administrative burden on businesses. Hence, Hyperswitch intends to eliminate all such operational burdens so that businesses can focus on the core activities.
* 🌎 **Community Feature Requests:** Most of our community feature requests falls under one of the above themes, but we still keep this as a separate theme, because we intend to actively explore new problem statements and themes from the community before scheduling actual feature work.

<table><thead><tr><th width="148">Legend</th><th>Description</th></tr></thead><tbody><tr><td>🟩</td><td>Work completed</td></tr><tr><td>🟧</td><td>Work in progress</td></tr><tr><td>🟥</td><td>Work not started</td></tr><tr><td>💪</td><td>Stretch target</td></tr><tr><td><span data-gb-custom-inline data-tag="emoji" data-code="1f69b">🚛</span></td><td>Backlogged for next quarter</td></tr></tbody></table>

### Developer Experience

* 🟩 Installation scripts for cloud deployment using EKS (on AWS). [Try the installation from here](https://opensource.hyperswitch.io/deploy-hyperswitch-on-aws/deploy-app-server)
* 🟩 Publish developer docs for self-hosting Hyperswitch. [Checkout the documentation here](https://opensource.hyperswitch.io/)
* 🟩 Hyperswitch Woocommerce plugin for Wordpress users. [Install the Woocommerce plugin](https://hyperswitch.io/docs/sdkIntegrations/wooCommercePlugin/wooCommercePluginOverview)
* 🟩 AWS menu-driven Hyperswitch installation support
* 🟩 Optimizing Hyperswitch application overhead from 30ms to 20ms

### Reducing Payment Costs

* 🟩 Reduce chargebacks by enabling Signifyd and Riskified (FRMs). [Try it out by signing up for hyperswitch](https://app.hyperswitch.io/register)
* 🟩 Support for Gocardless bank direct debits. [Try it out by signing up for Hyperswitch](https://app.hyperswitch.io/register)
* 🟩 Specialized low cost processor integration - Helcim
* 🟩 Open sourcing Smart Routing Framework for self hosting
* 🟧 Support Plaid for ACH account verification
* 🟧 Enabling surcharge for specific payment methods to promote low cost payment methods
* ~~🟥 Direct bank integration - Wells Fargo~~ \[Dropped]

### Improving Authorization Rates

* 🟩 Smart retry with 3DS for fraud declined payments. [Learn more about the feature](https://hyperswitch.io/docs/features/smartRetries)
* :articulated\_lorry: Paypal Vault flows for improving repeat user experience
* :articulated\_lorry:💪 Enhancing 3DS experience with Delegated Authentication and Visa's Digital Authentication Framework (for SCA markets)
* :articulated\_lorry:💪 Improve authorization rates for bank payments through Open banking integration for UK/EU

### Reducing Payment Operations

* 🟩 Support for exporting hyperswitch data to third party data warehouse
* :articulated\_lorry: Audit trail visibility for Payments, Refunds, Disputes on Hyperswitch Control Centre
* :articulated\_lorry:💪 System health metrics monitoring module on Hyperswitch Control Centre

### Community Feature Requests

* 🟩 Open sourcing Hyperswitch Unified Web Checkout for self-hosting. [Try it out here](https://opensource.hyperswitch.io/deploy-hyperswitch-on-aws/deploy-app-server)
* 🟩 Open sourcing Card Vault application code for self-hosting [Try it out here](https://opensource.hyperswitch.io/hyperswitch-open-source/deploy-hyperswitch-on-aws/deploy-card-vault)
* 🟩 Open sourcing Control Centre (Hyperswitch dashboard) for self-hosting [Try it out here](https://opensource.hyperswitch.io/hyperswitch-open-source/deploy-hyperswitch-on-aws/deploy-control-center/standalone-control-center-deployment-for-prototyping)
* 🟩 Direct bank integration - Bank of America
* 🟩💪 Open sourcing Fraud and Risk Management Integrations
* 🟩💪 Open sourcing Payouts module

## **Want to contribute to the roadmap?**

[Submit an idea or feature request here](https://github.com/juspay/hyperswitch/discussions/categories/ideas-feature-requests) with a simple explanation on `What?` and `Why?` included.
