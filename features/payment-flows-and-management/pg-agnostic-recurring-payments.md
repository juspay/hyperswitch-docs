---
description: Make recurring payments across processors
---

# 🔃 PG Agnostic Recurring Payments

### How does PG agnostic MITs work?

The CIT used to set up recurring payments via MIT uses the PG token. This introduces a connector stickiness since the recurring payments can only go through the connector which issued the token.

To mitigate this we would be storing the Network Transaction ID which will be a chaining identifier for the CIT in which the payment method was saved for off-session payments.

In the following MIT payments basis the enablement of the feature and the availability of Network Transaction ID Hyperswitch will route your payments to the eligible set of connectors. (This will also be used for retries)

<figure><img src="../../.gitbook/assets/Screenshot 2024-02-01 at 3.58.28 AM.png" alt=""><figcaption><p>MIT payment flow</p></figcaption></figure>

## Supported Payment processors

Hyperswitch supports the following processors for PG Agnostic Recurring Payments.

* Stripe
* Adyen
* Cybersource

In case you wish more processors to be covered for PG Agnostic Recurring Payments, please submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests).

### How to enable PG agnostic MITs?

To start routing MIT payments across all supported connectors in addition to the connector through which the recurring payment was set up, use the below API to enable it for a business profile

```bash
curl --location 'http://sandbox.hyperswitch.io/account/:merchant_id/business_profile/:profile_id/toggle_connector_agnostic_mit' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: api_key' \
--data '{
    "enabled": true
}'
```

All the payment methods saved with `setup_future_usage : off_session` after enabling this feature would now be eligible to be routed across the list of supported connectors during the subsequent MIT payments

## FAQs

#### 1. How can I set up connector preferences for the MIT payments?

You can use the payments routing module in the Hyperswitch Control Center to set up volume and rule based routing algorithm. As of now there is no specific keys to set rules only for MIT payments.

#### 2. How are authentication rates affected in PG agnostic MITs?

Network Transaction ID which is provided by the card network itself is a reference to the orginal payment authenticated by the customer and authorized for recurring payments. Hence the MIT exemption is expected to have better auth rates with this. &#x20;

So the internal precedence would be to try the payment with Network Transaction ID if present else the corresponding PG token would be used.
