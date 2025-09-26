# Storage

Storage layer is built with caching layer and persistent storage. The goal is to provide low latency persistent storage at lower cost.

## Cache Layer

Redis cluster is used as the cache.&#x20;

Any data that is accessed frequently but doesn't change often, is already cached in the router's memory. Payment related data is cached in the cache layer. Cache allows very low latency payments through hyperswitch.

## Persistent Storage

Since Payment data should never be lost, the data is persisted in normal databases like Postgres. This allows hyperswitch to provide data related to payments, refunds, etc to the users on their dashboards.

## Drainer

The Payment related events are written to a queue (like kafka) and the drainer takes the events and populate/update the persistent storage in near realtime. This allows hyperswitch to handle traffic at scale and not bottleneck the database.

\
