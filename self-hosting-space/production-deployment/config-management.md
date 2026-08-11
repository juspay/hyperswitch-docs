---
description: Configuration Management in Hyperswitch
icon: gear-code
---

# Config Management

Payment configurations in Hyperswitch

A payment is not a single action. It is a sequence of decisions: how to collect the customer's details, whether and how to authenticate, which processor to route the authorisation through, how long to wait for confirmation, what to do when the answer is delayed or ambiguous, and how to reconcile the outcome. Each decision in that sequence is parameterised - and those parameters are configurations.

Configurations are what give a payment journey its shape. They determine which paths are available, how the system behaves at each step, and how it responds when conditions change. Getting them right - and being able to change them quickly when merchant needs, connector behaviour, or regulations shift - is central to operating a payment switch reliably.

Storing these configurations in a generic key-value table worked for global changes, but had some practical limitations:

* No native scoping: The table held one value per key. Giving a specific merchant a different value required application code that read the merchant ID and picked the right value.
* No type safety: The table was schema-less. A value expected to be an integer could be stored as a string with no error until something downstream broke.
* Scoping logic lived in code: Every new "this merchant on this connector, except in this region" rule was an engineering change, not a configuration change.

### 1. Introducing Superposition as a Configuration Management Service

[Superposition](https://github.com/juspay/superposition) is an open-source, context-aware configuration management platform built by Juspay. It treats configuration as data with structure: every key has a default value validated by a JSON Schema, and values can vary along named dimensions through contextual overrides. At lookup time, the most specific override matching the request context wins - the same resolution model as CSS specificity.

Superposition also includes a built-in experimentation engine, so any configuration change can be rolled out to a percentage of traffic, ramped up, or rolled back in real time without a deployment.

### 2. Superposition in Hyperswitch

As Hyperswitch has grown, so has the need to vary runtime behaviour across the tenant hierarchy, across organisations, merchants, profiles, and connectors - without that variation being expressed as application code. This is a natural extension of how the platform is built: Hyperswitch already models the world in terms of these entities, and it follows that configuration should resolve along the same lines.

[ISF merchants](http://hyperswitch.io/ISF) - where a single Hyperswitch instance serves many sub-merchants across regions, payment methods, and connectors - make this need most visible, but the underlying requirement is the same at any scale where merchants operate differently from one another.

Hyperswitch uses Superposition as the resolution layer for the runtime configurations described above. The dimensions wired into the Hyperswitch workspace mirror the existing tenant hierarchy:

Hyperswitch uses Superposition as the resolution layer for the runtime configurations described above. The dimensions wired into the Hyperswitch workspace mirror the existing tenant hierarchy:

Organisation

└── Merchant Account

└── Business Profile

└── Other Payment Parameters (or other dimensions)

Configurations registered at a higher level cascade to every entity beneath, unless an override at a lower level wins by specificity. At request time, Hyperswitch builds a context from the entities involved and asks the in-process Superposition client for the resolved value. Resolution happens in memory; the client refreshes its cache asynchronously at timely intervals.



### 3. Running Superposition with Hyperswitch

**3.1 First Time Self-Hosters**

1. **Deploy Superposition**: Ensure the specific version of Superposition mentioned in the Hyperswitch stable release notes is deployed to your environment. Deployment helm charts will be provided in [hyperswitch-helm](https://github.com/juspay/hyperswitch-helm) along with the stable release.
2. **Execute migration tools**: With every stable release, we provide a migration utility (SQL query and Python script) to transition configurations from hyperswitch\_db into Superposition. To use it, first run the provided SQL queries and migration utilities as provided in the release docs. An example config is as following:

```
SELECT * FROM configs WHERE key LIKE '%poll_config_external_three_ds%';
```

Then, process this file using the provided Python script to automatically create overrides for any non-default configs:

```
python migrate_config.py --input configs.csv --env prod
```

The script processes one Superposition environment at a time, selected using the `--env flag (local, integ, sandbox, or prod)`. You must define connection details - including the host URL, organisation ID, workspace ID, and auth token - in the script's ENVS dictionary before execution. This utility performs two primary functions: it can seed the necessary dimensions into a new workspace using `--seed-dimensions`, and it executes the migration by registering default configuration values and creating dimensional context overrides based on your database dump.



3. **Point Hyperswitch to Superposition**: Configure the new environment variables (SUPERPOSITION\_HOST, workspace identifiers, and polling intervals). Hyperswitch is designed to fail fast on startup if the connection is unreachable. Use the following configuration block:

```
[superposition]
endpoint = "http://localhost:8081"
org_id = "localorg"
workspace_id = "dev"
polling_interval = 300
backup_file_path = "./config/superposition_seed.toml"
```

Configuration Details:

* **endpoint**: The base URL of the running Superposition service.
* **org\_id**: The identifier for your organization within Superposition.
* **workspace\_id**: The identifier for your specific development or production workspace.
* **polling\_interval**: The interval, in seconds, at which the client checks for configuration updates.
* **backup\_file\_path**: The path to a local configuration file used as a fallback if the Superposition service is unreachable, ensuring the application can still function during service disruptions.



**3.2 Maintenance Work (Subsequent Stable Releases)**

1. **Update Superposition and run DB migrations**: For every new release, update Superposition to the corresponding version and execute necessary database migrations before upgrading the superposition application.
2. **Run migration scripts for new configs**: Execute the provided Python migration scripts to move new configuration values from the database into Superposition overrides as required by the release.
3. **Upgrade Hyperswitch**: Once the configuration layer and migrations are finalized, proceed with upgrading the Hyperswitch application to the latest stable version as usual.

### Learn more about Superposition

Source: [github.com/juspay/superposition](https://github.com/juspay/superposition)

More Details: [https://github.com/juspay/hyperswitch/wiki/Enhanced-configuration-management-&-reliability-in-Hyperswitch](https://github.com/juspay/hyperswitch/wiki/Enhanced-configuration-management-&-reliability-in-Hyperswitch)

Documentation: [juspay.io/superposition/docs](https://juspay.io/superposition/docs)

Hyperswitch ISF reference architecture: [hyperswitch.io/ISF](https://hyperswitch.io/ISF)

<br>
