---
icon: arrows-rotate-reverse
---

# Recurring payments

Recurring payments via Hyperswitch can be setup by passing some additional flags, as highligted below. The recurring payments are not tied to a specific amount or cycle and the merchant can charge the end-user as per their own business requirements.&#x20;

### Programmatic Card-on-File Setup with Immediate Charge (CIT + Save)

When setting up subscription there are two distinct implementation flows. The correct flow depends on whether you intend to charge the customer immediately or simply validate their details for later use.

#### 1. The Setup with Charge Flow

**Use Case:** Use this when you need to collect a payment immediately (e.g., the first month of a subscription or a setup fee) while simultaneously saving the card details for future automatic charges. For this call Payments API with the below configuration parameters.

**Required API Configuration**

Include below parameter and values while calling the [payments](https://api-reference.hyperswitch.io/v1/payments/payments--create) API.

| Parameter            | Value                  |
| -------------------- | ---------------------- |
| `amount`             | >0 (Greater than zero) |
| `setup_future_usage` | `off_session`          |

**Run-Ready API Example (CIT with Charge)**

```json
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": <enter the relevant profile id>,
    "authentication_type": "no_three_ds",
    "setup_future_usage":"off_session", 
    "customer_id": "customer123",
    "description": "Its my first payment request",
    "return_url": "https://example.com", // 
}'
```



#### 2. Zero Dollar Authorization (Mandate-Only Setup)

**Use Case:** Use this for free trials, pay-later models, or delayed billing. This flow validates the payment method details without charging the customer's card.

**Required API Configuration**

Pass below parameters while calling payments API for [Zero Dollar Auth ](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/zero-amount-authorization-1)&#x20;

| Parameter            | Value          |
| -------------------- | -------------- |
| `setup_future_usage` | `off_session`  |
| `amount`             | `0`            |
| `payment_type`       | `payment_type` |

**Run-Ready API Example (Zero Auth Mandate)**

```json
curl --location 'http://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
--data-raw '{
"amount": 0,
"currency": "USD",
"confirm": false,
"customer_id": "zero_auth_test_customer",
"email": "m.arjunkarthik@gmail.com",
"name": "John Doe",
"phone": "999999999",
"phone_country_code": "+1",
"description": "Its my first payment request",
"profile_id": <enter the relevant profile id>,
"setup_future_usage": "off_session"
}'
```

Once the CIT is successful, Hyperswitch returns a `payment_method_id` . This `payment_method_id`  can be used by the merchant for all subsequent MIT recurring payments. Hyperswitch also returns the `network_transction_id`  (NTID) in its response to allow PICI compliant merchants to direct pass card + NTID for processing MIT recurring payments&#x20;

The `payment_method_id` serves as a unique identifier mapped to a specific combination of a Customer ID and a unique Payment Instrument (e.g., a specific credit card, digital wallet, or bank account).  A single customer can have multiple payment methods, each assigned a distinct ID. However, the same payment instrument used by the same customer will always resolve to the same `payment_method_id`.  This uniqueness applies across all payment types, including cards, wallets, and bank details.

For example, you can refer the below table -&#x20;

| **Customer ID** | **Payment Instrument**            | **Payment Method ID** |
| --------------- | --------------------------------- | --------------------- |
| 123             | Visa ending in 4242               | `PM1`                 |
| 123             | Mastercard ending in 1111         | `PM2`                 |
| 456             | Visa ending in 4242               | `PM3`                 |
| 123             | PayPal Account (`user@email.com`) | `PM4`                 |

Internally the payment\_method\_id is mapped to a bunch of credentials -  PSP token, Raw card + NTID, Network token + NTID depending on functionalities enabled for the merchant.



### Customer Consent Capture (Mandate Compliance)

If you are not using Hyperswitch SDK, then `customer_acceptance`  (customer's consent)is required along with the other parameters [confirm](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request to store the card.

```bash
"customer_acceptance": {
        "acceptance_type": "online",
        "accepted_at": "1963-05-03T04:07:52.723Z",
        "online": {
            "ip_address": "in sit",
            "user_agent": "amet irure esse"
        }
    }
```

If you are using the Hyperswitch SDK, the `customer_acceptance` is sent in the [confirm](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request on the basis of customer clicking the save card radio button

**Note:** Ensure to enable this functionality using the [_displaySavedPaymentMethodsCheckbox_](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/web/customization#id-6.-handle-saved-payment-methods) property during SDK integration

***

### Merchant-Initiated Transactions (MIT) – Decoupled Execution

Hyperswitch supports decoupled transaction flows, allowing Merchant-Initiated Transactions (MITs) to be processed independently of the original Customer-Initiated Transaction (CIT), even when the CIT was completed outside the Hyperswitch platform.

MITs are initiated by invoking the [`/payments`](https://api-reference.hyperswitch.io/v1/payments/payments--create) API with `off_session: true` and providing the available reference data in the `recurring_details` object. Depending on the artifacts available in your system, one of the following approaches can be used:

#### [**Payment Method ID**](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#body-recurring-details)

Submit the Hyperswitch generated payment\_method\_id to process the MIT transaction. Depending on the merchant configurations the MIT will be processed with the same PSP or with a different PSP.&#x20;

#### [**Processor Payment Token**](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#option-3)&#x20;

&#x20;Submit a processor-issued token that represents the previously authorized payment instrument.

#### [**Network Transaction ID with Card Data**](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#option-4)&#x20;

&#x20;Provide the original network transaction identifier along with the associated primary card data required for authorization.

{% hint style="info" %}
⚠️ **PSP Configuration Required**

This feature is not enabled by default and must be explicitly enabled by PSP.

You may receive errors such as `Received unknown parameter: payment_method_options[card][mit_exemption]`, follow the steps below to request activation.

Email the PSP Support requesting:

* Access to the `mit_exemption` parameter for MIT (Merchant Initiated Transaction) payments
* Ability to pass `network_transaction_id` in the parameter: `payment_method_options[card][mit_exemption][network_transaction_id]`
* Explain your use case: enabling cross-processor MIT payments using network transaction IDs from card schemes
{% endhint %}

#### [**Network Transaction ID with Network Token**](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#option-5) **:**&#x20;

Submit the network transaction identifier in combination with the corresponding network tokenized card credentials.

#### [**Limited Card Data**](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#option-6) **:**&#x20;

Use a reduced card data set captured at the time of subscription creation to authorize subsequent MITs.

***

### Connector-Agnostic MIT Routing

The CIT used to set up recurring payments via MIT uses the PG token. This introduces a connector stickiness since the recurring payments can only go through the connector which issued the token.

To mitigate this we would be storing the Network Transaction ID which will be a chaining identifier for the CIT in which the payment method was saved for off-session payments.

In the following MIT payments basis the enablement of the feature and the availability of Network Transaction ID Hyperswitch will route your payments to the eligible set of connectors. (This will also be used for retries)

<figure><img src="../../../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

#### Enabling Connector agnostic MITs

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

***

### Routing example - CITs are routed through PSP-1 and all MITs through PSP-2

The [Hyperswitch dashboard](https://app.hyperswitch.io/dashboard/routing/rule) provides UI to configure routing rules for PG Agnostic Recurring Payments. You can choose the profile for which you wish to configure the rule in the Smart Routing Configuration.

Then, you can configure the rule as shown below using the metadata field in the Rule-Based Configuration.

<figure><img src="../../../.gitbook/assets/Routing rule for pg agnostic recurring payments.png" alt=""><figcaption></figcaption></figure>

This rule would be used in conjunction with the other active routing rules that you have configured.

Once the rule is configured, you would need to send the following metadata as per the payment request:

#### **Metadata to be sent in CITs**

```
"metadata": {
    "is_cit": "true"
}
```

#### **Metadata to be sent in MITs**

```
"metadata": {
    "is_mit": "true"
}
```

According to the above configured rule all the CITs for the specific business profile should be routed through Stripe and MITs through Adyen.
