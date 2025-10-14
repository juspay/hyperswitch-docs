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
* **Elimination Routing:** Tracks acute incidents such as downtimes and technical errors to de-prioritise gateways. This will be used as a final check after other routing logics are applied.
* **Contracts-Based Routing:** Distributes payments across processors to meet contractual volume commitments. \[BETA FEATURE]&#x20;

### Architecture Diagram

<figure><img src="../../../.gitbook/assets/image (157) (1).png" alt=""><figcaption></figcaption></figure>

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Self Deploy the Routing Engine</td><td><a href="../../../.gitbook/assets/image (157).png">image (157).png</a></td><td><a href="self-deployment-guide.md">self-deployment-guide.md</a></td></tr><tr><td>Using Auth Rate based Routing for Hyperswitch</td><td><a href="../../../.gitbook/assets/tryHyperswitch.jpg">tryHyperswitch.jpg</a></td><td><a href="auth-rate-based-routing.md">auth-rate-based-routing.md</a></td></tr></tbody></table>
