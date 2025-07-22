---
icon: badge-check
---

# Auth Rate Based Routing

### How does it work?

**Auth Rate Based Routing** is a smart, adaptive approach to optimize transaction success across multiple gateways.&#x20;

At its core, the system treats each Gateway as a dynamic option in a decision-making model known as a **Non-stationary Multi-Armed Bandit (MAB)** with **Delayed Feedback**. This allows the routing logic to account for both fluctuating success rates and variable response times.

The routing strategy follows a two-part approach:

* **Exploration**: A small share of traffic is continuously routed to all Gateways to gather current performance data.
* **Exploitation**: The majority of traffic is directed to the top-performing Gateway to maximize success rates.

To keep decisions current and responsive, the system uses a **sliding window** to track recent performance, enabling fast adaptation to changing conditions—without requiring any manual intervention or downtime.

By intelligently balancing experimentation with optimization, Auth Rate Based Routing helps ensure higher authorization success, improved customer experience, and better utilization of Gateway infrastructure.

<figure><img src="../../../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

Key Configurations

* Bucket size : No. of payments included in a block limited by count or time period
* Aggregate pipeline size :&#x20;
  * Max: No. of buckets used to calculate scores (FIFO manner). It determines the reaction time&#x20;
  * Min: No. of buckets after which the scores will be used. It is equivalent to the zero error/offset for error tolerance

### How to setup Auth Rate Based Routing for your Hyperswitch Merchant?

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

3. To update the setting of the routing model use the below API:

```
curl --location --request PATCH 'https://sandbox.hyperswitch.io/account/<merchant-id>/business_profile/<profile-id>/dynamic_routing/success_based/config/<routing-id>' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>' \
--data '{
        "min_aggregates_size": 5, // Min. no. of buckets used to caluclate score
        "max_aggregates_size": 8, // Max. no. of buckets used to calculate score
        "current_block_threshold": {
            "max_total_count": 5, // Number of payments in a Bucket 
            "exploration_percent": 20.0 
        }
}'
```

4. Activating the updating configuration

```
curl --location --request POST 'https://sandbox.hyperswitch.io/routing/<routing-id>/activate' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>'
```

### How to test the routing behaviour?

You can use the routing playground tool to simulate different payment scenarios to test the routing behaviour

Access the tool using this URL - [https://hyperswitch-ten.vercel.app/](https://hyperswitch-ten.vercel.app/)

1. Create a merchant on Hyperswitch Control Center
2. Ensure to configure atleast two payment processors for the merhcant profile
3. Enter the sandbox API key, merchant id and profile id in the modal that pops-up once you click the 'Start Simulation' button on the top-right corner
4. Head to the 'routing' tab on the left nav bar and toggle the Success Based Routing button
5. Select the desired routing configuration settings
6. Head to the 'general' tab on the left nav bar and enter the no. of payments you want to trigger in batches
7. Hit Start Simulation to see the results
8. You can use the Test Payment Data tab on the left nav bar to modify the processor auth rates to see how it will impact the routing choices
