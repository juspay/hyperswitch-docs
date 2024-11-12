---
description: Make recurring payments across processors
icon: arrows-repeat
---

# PG Agnostic Card Forwarding

### How does PG agnostic MITs work?

The CIT used to set up recurring payments via MIT uses the PG token. This introduces a connector stickiness since the recurring payments can only go through the connector which issued the token.

To mitigate this we would be storing the Network Transaction ID which will be a chaining identifier for the CIT in which the payment method was saved for off-session payments.

In the following MIT payments basis the enablement of the feature and the availability of Network Transaction ID Hyperswitch will route your payments to the eligible set of connectors. (This will also be used for retries)

<figure><img src="../../../.gitbook/assets/Screenshot 2024-02-01 at 3.58.28 AM.png" alt=""><figcaption><p>MIT payment flow</p></figcaption></figure>

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

#### 1. How are authentication rates affected in PG agnostic MITs?

Network Transaction ID which is provided by the card network itself is a reference to the original payment authenticated by the customer and authorized for recurring payments. Hence the MIT exemption is expected to have better auth rates with this.

So the internal precedence would be to try the payment with Network Transaction ID if present else the corresponding PG token would be used.

#### 2. How do I configure a routing rule so that all CITs are routed through one connector and all MITs through another?

The [Hyperswitch dashboard](https://app.hyperswitch.io/dashboard/routing/rule) provides UI to configure routing rules for PG Agnostic Recurring Payments. You can choose the profile for which you wish to configure the rule in the Smart Routing Configuration.

Then, you can configure the rule as shown below using the metadata field in the Rule-Based Configuration.

<figure><img src="../../../.gitbook/assets/Routing rule for pg agnostic recurring payments.png" alt=""><figcaption></figcaption></figure>

This rule would be used in conjunction with the other active routing rules that you have configured.

Once the rule is configured, you would need to send the following metadata as per the payment request:

\-> Metadata to be sent in CITs

```
"metadata": {
    "is_cit": "true"
}
```

\-> Metadata to be sent in MITs

```
"metadata": {
    "is_mit": "true"
}
```

According to the above configured rule all the CITs for the specific business profile should be routed through Stripe and MITs through Adyen.
