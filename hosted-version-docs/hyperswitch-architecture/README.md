---
description: A 30,000 feet view of Hyperswitch's architecture
---

# 📐 Hyperswitch architecture

{% hint style="info" %}
This chapter will help you quickly understand the Hyperswitch application's architecture
{% endhint %}

***

At high level, Hyperswitch has two main components,&#x20;

* router, which handles the incoming requests and talks to various connectors.
* a low latency storage layer

<figure><img src="../../.gitbook/assets/HS_architecture (2).png" alt=""><figcaption></figcaption></figure>

## Core API Layer <a href="#core" id="core"></a>

The "Core" is the unifying layer of Hyperswitch, which handles the incoming requests, authenticates, intelligently picks the connector(s) and processes the payments or refunds on behalf of the merchant. &#x20;

The incoming requests could be from merchant servers, the client SDK, or webhooks from the connectors. The core layer also contains other business intelligence like the connector routing logic.

## Connectors <a href="#connectors" id="connectors"></a>

Hyperswitch treats external services as connectors. The connectors could be payment processors like stripe, paypal or fraud/risk prevention services like signifyd, or any other payment services. &#x20;

The "Connector" module is a light weight stateless service, that contains the necessary logic to convert the hyperswitch payments data into a format required by the payment processor, connects to the appropriate endpoints, sends the requests, interprets the response, and provides the final status and message back to the Core.

This module is constructed as a stateless service and hence fully decoupled from the Core. This allows the Core to communicate with the diverse payment processor integrations and helps separate the detail-oriented data transformation layer from the Core.&#x20;

The Core communicates with Connector through a standard interface abstracted to carry the payment use case and respective payment data.

## Storage <a href="#storage" id="storage"></a>

Persistence with consistency is quite crucial for a transactional system like Hyperswitch. However, the storage layer should not become a bottleneck for a high-performance application. The critical path of a payment lifecycle primarily characterizes frequent read and write to a record (lasting for a few minutes), post which the record is frequent read and rarely written (lasting up to 6 months).&#x20;

Hence, to ensure a high-performance system for processing peak transaction volumes, the storage is further divided into three sub-parts:

* **Cache layer** to de-bottleneck the persistent (SQL) storage by exposing data essential for high-frequency read-write operations.&#x20;
* **Persistent (SQL) storage** for ensuring persistence and consistency
* **write-back / drainer** to write back the data to SQL storage layer for persistence and consistency.

The router can still read data from SQL storage as necessary.





