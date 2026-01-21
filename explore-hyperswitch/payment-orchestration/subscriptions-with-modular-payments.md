---
description: Augment your subscriptions with payments orchestration capabilities
icon: repeat
---

# Subscriptions with Modular Payments

Businesses that run on subscription model powered by providers viz. Chargebee, Recurly, Stripe Billing etc. can now augment it with payments orchestration by decoupling the payments from the subscription provider and using them purely for subscription ledger and scheduling, while owning 100% of the card vaulting, payment attempts, and retry logic (owned in-house, or via an ensemble of specialized payment-focused orchestrator and other focused third parties, modularized to work with each other)

### Benefits

1. Greater control over payments with direct integrations and commercials with a range of Acquirers and Payment Processors
2. Improved reliability with a multi-PSP setup
3. Intelligent Routing capabilities to improve Authorization Rates and minimize Processing costs
4. Greater coverage of PMs, APMs and features offered by the PSPs
5. Centralised tokenisation of payment methods for PSP agnostic payments

### How does it work?

1. Integrate your subscription provider as a billing processor on Hyperswitch
2. Create and maintain plans on the subscription provider's dashboard
3. During the checkout process use Hyperswitch for Payments
4. Hyperswitch completes the payment, securely tokenises and stores the card
5. Subscription is created at Hyperswitch and at the subscription provider's end
6. First invoice is marked as paid and the subscription is activated
7. Subsequent billing cycles are handled independently by Hyperswitch through MIT payments
8. Failed MIT payments can be smartly retries by Hyperswitch ([read more](../payments-modules/revenue-recovery.md)) or by the solution provider of your choice.

### Flow Diagram

#### Initial Subscription create flow (with CIT Payment)

<figure><img src="../../.gitbook/assets/cit flow 13102205.png" alt=""><figcaption></figcaption></figure>

#### MIT payment flow in subsequent billing cycle

<figure><img src="../../.gitbook/assets/mit flow 13102025.png" alt=""><figcaption></figcaption></figure>

### Integration Guide

#### 1. For non-PCI compliant merchants who wants to use Hyperswitch Payments SDK

{% stepper %}
{% step %}
Configure your Subscription Provider with Hyperswitch and set it as billing connector for the desired profile

_Note: Dashboard support for this configuration will be available soon_

{% code overflow="wrap" fullWidth="false" %}
```
curl --location 'http://<base_url>/account/<merchant_id>/connectors' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <api_key>' \
--data '{
    "connector_type": "billing_processor",
    "connector_name": "chargebee",
    "connector_account_details": {
        "auth_type": "HeaderKey",
        "api_key": "<api_key>",
        "site": ""
    },
    "business_country": "US",
    "business_label": "default",
    "connector_webhook_details": {
        "merchant_secret": "hyperswitch", 
        "additional_secret": "hyperswitch" 
    },
    "metadata": {
        "site": "test"
    }
}'

SET AS BILLING CONNECTOR
curl --location 'http://<base_url>/account/<merchant_id>/business_profile/<profile_id' \
--header 'Content-Type: application/json' \
--header 'api-key: <api_key>' \
--data '{
  "billing_processor_id": "<mca_id>"
}'
```
{% endcode %}
{% endstep %}

{% step %}
Configure Hyperswitch Webhook endpoint for invoice events on the subscription provider's dashboard
{% endstep %}

{% step %}
Fetch the plan details (to be setup prior on subscription provider)

```
curl --location 'http://<base_url>/subscriptions/plans' \
--header 'Content-Type: application/json' \
--header 'api-key: <api_key>'

Response:
[
    {
        "plan_id": "cbdemo_enterprise-suite",
        "name": "Enterprise Suite",
        "description": "High-end customer support suite with enterprise-grade solutions."
   	 "price_id": [
        	{
                "id": "cbdemo_enterprise-suite-INR-Daily",
                "name": "Enterprise Suite INR Daily",
                "pricing_model": "flat_fee",
                "price": 10000,
                "period": 1,
                "currency_code": "INR",
                "period_unit": "day",
                "free_quantity": 0,
              }]
       }
]

```
{% endstep %}

{% step %}
Display the retrieved Plan and Price Details to the user to make their selection
{% endstep %}

{% step %}
Once the user selects a particular Plan, create a customer on Hyperswitch ([API Reference](https://api-reference.hyperswitch.io/v1/customers/customers--create)) and create a subscription with the following API

```
curl --location '<baseurl>/subscriptions/create' \
--header 'Content-Type: application/json' \
--header 'X-Profile-Id: <profile_id>' \
--header 'api-key: <api-key>' \
--data '{
    "customer_id": "cus_uBtUJLSVSICr8ctmoL8i",
    "amount": 14100,
    "currency": "USD",
    "payment_details": {
        "authentication_type": "no_three_ds",
        "setup_future_usage": "off_session",
        "capture_method": "automatic",
        "return_url": "https://google.com"
    }
}'
```
{% endstep %}

{% step %}
Initiate the Hyperswitch unified checkout SDK using the `client_secret` returned in the `/subscriptions/create` API response
{% endstep %}

{% step %}
Once the customer selects a payment method and enters the details and confirms the subscription, hit the `/subscriptions/:id/confirm` using a similar [implementation as this](../merchant-controls/integration-guide/web/react-with-rest-api-integration.md)
{% endstep %}

{% step %}
Sync with the subscription status for disbursement of services and future billing cycles
{% endstep %}
{% endstepper %}

#### 2. For PCI Compliant merchants handling the entire checkout experience

{% stepper %}
{% step %}
Follow the same steps as above to create a billing connector, fetch plan details and display the retrieved Plan and Price Details to the user to make their selection
{% endstep %}

{% step %}
Once the user selects a particular Plan, create a customer on Hyperswitch ([API Reference](https://api-reference.hyperswitch.io/v1/customers/customers--create)), initiate checkout and collect payment method details
{% endstep %}

{% step %}
After the user enter card/PM details and confirms the payment, hit the Hyperswitch Subscriptions API

```
curl --location 'http://localhost:8080/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-Profile-Id: pro_2WzEeiNyj8fSCObXqo36' \
--header 'api-key: dev_Ske75Nx2J7qtHsP8cc7pFx5k4dccYBedM6UAExaLOdHCkji3uVWSqfmZ0Qz0Tnyj' \
--data '{
    "item_price_id": "cbdemo_enterprise-suite-INR-Daily",
    "customer_id": "cus_NdHhw4wwWyYXSldO9oYE",
    "billing_address": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "joseph",
            "last_name": "Doe"
        },
        "phone": {
            "number": "8056594427",
            "country_code": "+91"
        }
    },
    "payment_details": {
        "payment_method": "card",
        "payment_method_type": "credit",
        "payment_method_data": {
            "card": {
                "card_number": "4242424242424242",
                "card_exp_month": "10",
                "card_exp_year": "25",
                "card_holder_name": "joseph Doe",
                "card_cvc": "123"
            }
        },
        "setup_future_usage": "off_session",
        "customer_acceptance": {
            "acceptance_type": "online",
            "accepted_at": "1963-05-03T04:07:52.723Z",
            "online": {
                "ip_address": "127.0.0.1",
                "user_agent": "amet irure esse"
            }
        }
    }
}'

```

Response:

```
{
  "id": "subscription_wBV1G9dhh6EBhTOTXRBA",
  "merchant_reference_id": null,
  "status": "active",
  "plan_id": null,
  "price_id": null,
  "coupon": null,
  "profile_id": "profile_id",
  "payment": null,
  "customer_id": "customer_id",
  "invoice": {
    "id": "invoice_0XANlbhMp2V7wUvWRhhJ",
    "subscription_id": "subscription_wBV1G9dhh6EBhTOTXRBA",
    "merchant_id": "merchant_id",
    "profile_id": "profile_id",
    "merchant_connector_id": "mac_id",
    "payment_intent_id": null,
    "payment_method_id": null,
    "customer_id": "cus_id",
    "amount": 14100,
    "currency": "INR",
    "status": "InvoiceCreated"
  }
}
```
{% endstep %}

{% step %}
Sync with the status of the Subscription API to disburse services to subscribed users

{% code overflow="wrap" %}
```
curl --location 'http://localhost:8080/subscriptions/<subscripion_id>' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-Profile-Id: <profile_id>' \
--header 'api-key: <api_key>'

RESPONSE:
{
    "id": "<subcription_id>",
    "merchant_reference_id": "mer_ref_id",
    "status": "active",
    "plan_id": null,
    "profile_id": "<profile_id>",
    "merchant_id": "<merchant_id>",
    "coupon_code": null,
    "customer_id": "<customer_id>"
}
```
{% endcode %}
{% endstep %}

{% step %}
Monitor incoming webhooks for renewal during subsequent cycles
{% endstep %}
{% endstepper %}

### FAQs

#### 1. What are subscriptions providers that are currently supported?

Currently we support Chargebee integration. In the upcoming roadmap we are planning to extend support for Recurly, Stripe Billing and Zuora

#### 2. Can the entire experience from plan display, price estimation to payments be handled by Hyperswitch SDK?

We are planning to release a Hyperswitch Subscriptions SDK that will take care of the end-to-end experience (Tentatively by Q4 2025)
