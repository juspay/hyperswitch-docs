---
icon: flux-capacitor
---

# Intelligent Routing

The Hyperswitch Intelligent Routing module augments your payment processing by dynamically switching between processors in real-time for every transaction to optimally maximise first attempt auth rates and minimise processing cost.

### Types of Intelligent Routing

Hyperswitch supports four intelligent routing strategies:

* **Auth Rate Based Routing:** Uses real-time success rates and ML-driven optimisation to route transactions to the best-performing gateway.&#x20;
  * The Auth Rates for the payments are tracked at a granular level of payment parameters like payment method, payment method type, amount, currency, authentication type, card network etc.&#x20;
  * **The model** uses a Multi-Armed Bandit (MAB) problem with Delayed Feedback, where each Gateway is an "arm" with fluctuating success rates and varying latency for success and failure. The approach used to solve this problem is driven by **explore-exploit** strategy.
    * **Exploration:** We continuously evaluate all gateways by sending a small percentage of traffic to ensure up-to-date performance data.
    * **Exploitation:** We continuously route most traffic to the best-performing Gateway to maximise the overall success rate.
  * The sensitivity of the system can be tweaked by the merchants by configuring settings such as Bucket Sizes, Parameters to be considered and Hedging Percentage
  * The hedging percentage decides the exploration factor of the model&#x20;
* **Least Cost Routing:** Picks the least cost network for every transaction basis the availability of back-of-the-card network and processor compatibility
* **Elimination Routing:** Tracks acute incidents such as downtimes and technical errors to de-prioritise gateways. This will be used as a final check after other routing logics are applied \[BETA FEATURE]
* **Contracts-Based Routing:** Distributes payments across processors to meet contractual volume commitments. \[BETA FEATURE]

### Self Deploy and integrate it with your existing orchestrator&#x20;

Refer the the setup guide and API reference in this [repository](https://github.com/juspay/decision-engine)&#x20;

### Setting Up Auth Rate Based Routing for Hyperswitch Merchants

1. Enabling your profile with Auth Rate based routing

```
curl --location --request POST 'https://sandbox.hyperswitch.io/account/<merchant_id>/business_profile/<profile-id>/dynamic_routing/success_based/toggle?enable=dynamic_connector_selection' \
--header 'api-key: <api-key>'
```

2. Roll it out to the required split of payment traffic (Merchants can stagger a certain percentage to experiment)

```
curl --location --request POST 'https://sandbox.hyperswitch.io/account/<merchant-id>/business_profile/<profile-id>/dynamic_routing/set_volume_split?split=100' \
--header 'api-key: <api-key>'
```
