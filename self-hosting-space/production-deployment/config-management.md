---
description: Configuration Management in Hyperswitch
icon: gear-code
---

# Config Management

Payment configurations in Hyperswitch

A payment is not a single action. It is a sequence of decisions: how to collect the customer's details, whether and how to authenticate, which processor to route the authorisation through, how long to wait for confirmation, what to do when the answer is delayed or ambiguous, and how to reconcile the outcome. Each decision in that sequence is parameterised - and those parameters are configurations.

Configurations are what give a payment journey its shape. They determine which paths are available, how the system behaves at each step, and how it responds when conditions change. Getting them right - and being able to change them quickly when merchant needs, connector behaviour, or regulations shift - is central to operating a payment switch reliably.

Storing these configurations in a generic key-value table worked for global changes, but had some practical limits:

* No native scoping. The table held one value per key. Giving a specific merchant a different value required application code that read the merchant ID and picked the right value.
* No type safety. The table was schemaless. A value expected to be an integer could be stored as a string with no error until something downstream broke.
* Scoping logic lived in code. Every new "this merchant on this connector, except in this region" rule was an engineering change, not a configuration change.

### Introducing Superposition as a Configuration Management Service

Superposition is an open-source, context-aware configuration management platform built by Juspay. It treats configuration as data with structure: every key has a default value validated by a JSON Schema, and values can vary along named dimensions through contextual overrides. At lookup time, the most specific override matching the request context wins - the same resolution model as CSS specificity.

Superposition also includes a built-in experimentation engine, so any configuration change can be rolled out to a percentage of traffic, ramped up, or rolled back in real time without a deployment.

### Superposition in Hyperswitch

As Hyperswitch has grown, so has the need to vary runtime behaviour across the tenant hierarchy, across organisations, merchants, profiles, and connectors — without that variation being expressed as application code. This is a natural extension of how the platform is built: Hyperswitch already models the world in terms of these entities, and it follows that configuration should resolve along the same lines.&#x20;

[ISF merchants](http://hyperswitch.io/ISF) - where a single Hyperswitch instance serves many sub-merchants across regions, payment methods, and connectors - make this need most visible, but the underlying requirement is the same at any scale where merchants operate differently from one another.

Hyperswitch uses Superposition as the resolution layer for the runtime configurations described above. The dimensions wired into the Hyperswitch workspace mirror the existing tenant hierarchy:

Hyperswitch uses Superposition as the resolution layer for the runtime configurations described above. The dimensions wired into the Hyperswitch workspace mirror the existing tenant hierarchy:

Organisation

&#x20;  └── Merchant Account         &#x20;

&#x20;    └── Business Profile

&#x20;      └── Other Payment Parameters (or other dimensions)&#x20;

Configurations registered at a higher level cascade to every entity beneath, unless an override at a lower level wins by specificity. At request time, Hyperswitch builds a context from the entities involved and asks the in-process Superposition client for the resolved value. Resolution happens in memory; the client refreshes its cache asynchronously at timely intervals.

### Learn more about Superposition

Source: [github.com/juspay/superposition](https://github.com/juspay/superposition)

More Details: [https://github.com/juspay/hyperswitch/wiki/Enhanced-configuration-management-&-reliability-in-Hyperswitch](https://github.com/juspay/hyperswitch/wiki/Enhanced-configuration-management-&-reliability-in-Hyperswitch)

Documentation: [juspay.io/superposition/docs](https://juspay.io/superposition/docs)

Hyperswitch ISF reference architecture: [hyperswitch.io/ISF](https://hyperswitch.io/ISF)

<br>
