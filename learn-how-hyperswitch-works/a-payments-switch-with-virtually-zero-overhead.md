---
description: Lightning fast with a near-invisible presence
---

# ⚡ A Payments Switch with virtually zero overhead

When it comes to payments, every millisecond counts. The difference between a seamless customer experience and a frustrating one often boils down to the speed and efficiency of payment processing.&#x20;

Merchants who operate in this digital arena understand the importance of **offering multiple payment options to their customers**. The challenge lies in integrating these payment processors seamlessly into their existing systems without wasting dev effort or introducing performance overhead.&#x20;

{% hint style="success" %}
Enter Hyperswitch, a game-changing solution designed to be lightning fast and add **virtually zero overhead** to your payment processing infrastructure!
{% endhint %}

***

**Clarifying latency overhead**

> The latency overhead of Hyperswitch refers specifically to the time taken by the Hyperswitch application itself within the transaction flow.&#x20;

While Hyperswitch optimizes its internal processes to add almost zero overhead, it's important to recognize that the overall transaction latency isn't solely determined by Hyperswitch alone. The entire transaction process involves multiple components, including the payment processor as shown below

| Component                                                                                   | Value                                                     |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Network latency between Client App and your server (starting point)                         | A (BAU)                                                   |
| <mark style="color:blue;">**Hyperswitch Application latency (hosted in your stack)**</mark> | <mark style="color:blue;">**B (negligible)**</mark> :zap: |
| Network latency between your server and payment processor                                   | C (BAU)                                                   |
| Processor Latency                                                                           | D (BAU)                                                   |
| **Total Transaction Latency**                                                               | **A+B+C+D**                                               |

What Hyperswitch does is provide an option to connect to multiple processors at almost zero latency cost

### **How Hyperswitch achieves a near-invisible presence**

At its core, Hyperswitch is a payments switch that effortlessly connects merchants with multiple payment processors. What sets it apart is its extraordinary speed and efficiency. Here's how Hyperswitch manages to be lightning fast and virtually overhead-free:

<details>

<summary><strong>In-Memory Configuration Caching</strong></summary>

* Hyperswitch eliminates the delays associated with fetching configuration data for each transaction by caching all merchant and processor-related configurations in memory
* This ensures that transaction processing remains lightning quick, regardless of the specifics of each transaction

</details>

<details>

<summary><strong>Redis for Transaction Data</strong></summary>

* To further accelerate transaction processing, Hyperswitch stores all transaction-related data reads in Redis, an in-memory key-value store
* This choice of data storage allows for rapid access to transaction details, ensuring that every step of the process is nearly instantaneous.

</details>

<details>

<summary><strong>Asynchronous Data Persistence</strong></summary>

* Hyperswitch optimizes the transaction workflow by making all data writes to Redis and then asynchronously draining this data to the database
* This approach minimizes any potential delays in the critical transaction path, maintaining the rapid pace that customers expect

</details>

<details>

<summary><strong>Parallelization</strong></summary>

* Hyperswitch embraces parallelization wherever possible, ensuring that multiple operations can be executed simultaneously
* This approach further enhances its speed and responsiveness, making it a true powerhouse in payment processing

</details>

{% hint style="info" %}
The latency of the entire Hyperswitch application is just \~25 ms&#x20;
{% endhint %}

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

<div data-full-width="false">

<figure><img src="../.gitbook/assets/Screenshot 2023-10-23 at 12.07.08 AM.png" alt="" width="563"><figcaption></figcaption></figure>

</div>

### **Seamless Integration - Just another microservice in your system**

One of the remarkable features of Hyperswitch is its ability to seamlessly integrate into your existing technology stack. By functioning like a system software, Hyperswitch becomes an integral part of your system, eliminating network latency between your application and the switch. This means there's almost zero overhead introduced into your system.

**Reduced Network Latency**: Hyperswitch's integration into your stack eliminates network latency, leading to quicker transaction processing and improved system performance.

**Streamlined Workflow**: With Hyperswitch seamlessly embedded in your stack, transaction processing becomes an integral part of your system's workflow. This streamlines the management of payment processing and reduces the complexity of maintaining multiple external connections.

**Improved Reliability**: By operating as a tightly integrated component, Hyperswitch can be configured and managed alongside the rest of your stack, allowing for comprehensive monitoring and ensuring high levels of reliability and availability.

### **Bottomline**

By adding almost zero overhead, Hyperswitch ensures that the lion's share of the transaction's latency, as experienced by the end user, is determined by the payment processor's inherent processing time.&#x20;

In essence, Hyperswitch acts as the invisible hand behind the scenes by connecting merchants with multiple payment processors in the blink of an eye without adding any noticeable overhead.

