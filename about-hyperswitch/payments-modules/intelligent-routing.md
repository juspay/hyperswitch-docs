---
icon: flux-capacitor
---

# Intelligent Routing

Intelligent Routing is a smart payment routing system that helps businesses choose the best way to process payments by adjusting routing rules in real time.&#x20;

Unlike static routing, which follows fixed rules, Intelligent Routing uses up-to-the-minute data—such as success rates, past transaction patterns, and processor issues. By combining past data with real-time insights, it picks the best processor for each payment.

This automation saves businesses from manually updating rules, adapting automatically to current conditions for smoother, more efficient payment processing.

<figure><img src="../../.gitbook/assets/image (156).png" alt=""><figcaption></figcaption></figure>

### Types of Intelligent Routing

Hyperswitch supports three intelligent routing strategies:

* **Success-Based Routing:** Routes payments to processors with the highest historical success rates.
* **Elimination Routing:** Avoids processors experiencing issues or with lower success rates.
* **Contracts-Based Routing:** Distributes payments across processors to meet contractual volume commitments.

### Key Benefits:

* **Boosted Conversion Rates:** Intelligent Routing directs payments to processors with the highest success rates, using real-time data and past patterns. For example, if a particular card type is approved more often with a certain processor, payments with that card are routed there.
* **Regional Optimization:** For global businesses, Intelligent Routing sends payments to processors that perform best in each area. This means using processors with strong connections in Europe for EU payments and ones with strong U.S. connections for payments in the U.S.
* **Meeting Volume Commitments:** Intelligent Routing keeps track of the transaction numbers required by contracts with each processor and distributes payments to meet these targets while maintaining high success rates.
* **Real-Time Outage Handling:** If a processor is down, Intelligent Routing avoids it and reroutes payments to working processors. When the processor is stable again, it gradually resumes use.

### Setting Up Success-Based Routing

To try success-based routing, which routes payments to processors with the highest historical success rates, follow these steps:

1.  **Enable Success-Based Routing for your profile:** There are three options when enabling:

    * **metrics:** Stores entries in the `dynamic_routing_stats` table and provides metrics on how payments would have been routed using success-based routing (analysis only).
    * **dynamic\_connector\_selection:** Actually routes payments through success-based routing.
    * **none:** Disables success-based routing.

    ```bash
    --location --request POST '{{base_url}}/account/{{merchant_id}}/business_profile/{{profile_id}}/dynamic_routing/success_based/toggle?enable=metrics' \
    --header 'api-key: {{api_key}}'
    ```
2.  **Configure the volume of payments sent through intelligent-routing:**

    ```bash
    --location --request POST '{{base_url}}/account/{{merchant_id}}/business_profile/{{profile_id}}/dynamic_routing/set_volume_split?split=100' \
    --header 'api-key: {{api_key}}'
    ```
3. **Monitor performance:** You can check the `dynamic_routing_stats` table for entries to analyze the performance of your intelligent routing configuration. Key fields in the dynamic\_routing\_stats table:
   * **payment\_id**: Unique identifier for the payment transaction
   * **success\_based\_routing\_connector**: The connector suggested by intelligent routing for optimal success
   * **payment\_connector**: The actual connector through which the payment was processed
   * **payment\_status**: Current status of the payment attempt (succeeded, failed, etc.)
   * **conclusive\_classification**: Classification of the routing decision's effectiveness\


{% content-ref url="../../explore-hyperswitch/merchant-controls/" %}
[merchant-controls](../../explore-hyperswitch/merchant-controls/)
{% endcontent-ref %}
