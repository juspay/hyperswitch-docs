---
icon: poo-storm
---

# Chaos Testing

This section defines the chaos testing strategy for the critical path of a self-hosted Hyperswitch deployment.&#x20;

It covers three things:&#x20;

(1) What chaos testing is and why it matters specifically for a payments switch,&#x20;

(2) The layered strategy and prioritization used to test the critical path shown below, and&#x20;

(3) The tooling, fault catalog, and metrics used to run and record the experiments.&#x20;

### The Critical Path Under Test

The scope of this exercise is the request path that a payment transaction actually travels through in production, illustrated below. <br>

<figure><img src="../../.gitbook/assets/Screenshot 2026-07-30 at 6.39.46 PM.png" alt=""><figcaption></figcaption></figure>

| **Layer**            | **Component**                   | **Role in Critical Path**                                                                                                                  |
| -------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Ingress / Egress     | Envoy (ingress), Squid (egress) | Envoy terminates inbound merchant/PSP traffic into the cluster; Squid proxies outbound calls from Hyperswitch to external connectors/PSPs. |
| Application          | Hyperswitch (on Amazon EKS)     | Core payments orchestration – request validation, routing, retries, and connector calls. The primary business-logic layer.                 |
| Storage – Cache      | Redis                           | Low-latency state store used for idempotency, locking, session and routing data. Sits in the hot path of every transaction.                |
| Storage – Persistent | Database                        | System of record for transactions, merchant configuration, and reconciliation data.                                                        |
| Compute (underlying) | Amazon EC2                      | Worker nodes underpinning the EKS cluster and, where applicable, self-managed DB/Redis instances.                                          |

## What Is Chaos Testing?

Chaos testing (or chaos engineering) is the discipline of deliberately injecting controlled failures into a system to build confidence in its ability to withstand turbulent, real-world conditions. Rather than only verifying that a system works when everything is healthy, chaos testing verifies what happens when it is not – a node dies, a database fails over, a dependency slows down, or a pod runs out of memory.

### The Four Core Principles

1. Define a steady state – pick a measurable signal of “normal” behavior (e.g., payment success rate, p99 authorization latency, webhook delivery rate).
2. Form a hypothesis – state the expected outcome, e.g., “if one Redis node fails over, payment success rate stays above 99.9% and p99 latency stays under 800ms.”
3. Inject a real-world variable – simulate a fault that could plausibly occur in production: instance termination, AZ failover, CPU/memory exhaustion, network latency or packet loss.
4. Compare and learn – measure whether steady state held. If it didn’t, you’ve found a systemic weakness to fix before it surfaces as a customer-facing incident.

Two further principles apply directly to a production payments system:&#x20;

(1) Always minimize the blast radius (start small – one pod, one AZ, a single non-critical merchant flow – before widening scope), and\
(2 ) Always have an automated abort/rollback mechanism (stop conditions) so an experiment cannot itself cause an outage.

## Why Chaos Testing Matters in Payments

Payments infrastructure has a lower tolerance for failure than almost any other category of software, and the failure modes are unusually unforgiving:

* Direct revenue impact: every second of downtime or degraded latency on the authorization path is a transaction that can be declined, abandoned, or duplicated – directly translating to lost revenue and merchant trust.
* Cascading, hard-to-reproduce failures: a payments switch like Hyperswitch sits between merchants, PSPs/connectors, and the merchant's own database/cache. A slow or failed dependency (Redis lock contention, a DB failover, a connector timeout) can cascade into retry storms, connection-pool exhaustion, or duplicate charges if not handled defensively.
* Consistency and idempotency guarantees: payments must never be double-charged or silently lost. Chaos testing validates that idempotency keys, locking (via Redis) and transactional writes (via the database) hold up when the underlying infrastructure is degraded, not just when it's healthy.
* Regulatory and compliance expectations: PCI DSS and most card-network/PSP agreements expect demonstrable operational resilience and incident-readiness, not just point-in-time security controls.
* Multi-tenant blast radius: a shared Hyperswitch deployment serves many merchants; an infrastructure fault that isn't isolated can turn a single-node failure into a platform-wide incident.<br>

## Chaos Testing Strategy: Layers and Priority

Rather than testing every component simultaneously, the critical path is tested bottom-up in terms of blast radius but top-down in terms of test priority: we start with the layer whose failure has the widest and most silent impact, and work outward. The order used for this program is:

1. Storage layer (Database, Redis) – tested first
2. Application layer (Hyperswitch on EKS) – tested second
3. Compute layer (EC2 – underlying nodes/instances) – tested third

### Why Storage Is Tested First

The database and Redis sit underneath every other component. If the application layer is resilient but the storage layer isn't, that resilience is theoretical: a database failover or Redis eviction event can silently corrupt state, stall locks, or produce inconsistent reads regardless of how well the application pods themselves are engineered.&#x20;

Storage-layer faults also tend to have the longest recovery times (failover, replica promotion) and the least visible symptoms (elevated tail latency before an outright error), so they need the earliest and most thorough validation.

### Why Application (EKS) Is Tested Second

Once the data layer's behavior under stress is understood, the Hyperswitch application layer is tested for how it degrades and recovers – pod evictions, restarts, CPU/memory starvation, and network partition from Redis/the database/PSP connectors.&#x20;

### Why Compute (EC2) Is Tested Third

Compute-layer faults (an EC2 instance/EKS worker node dying, an AZ losing power) are typically the most “visible” and best-understood failure mode, and AWS Auto Scaling already provides a first line of defense (rescheduling, ASG replacement).&#x20;

Testing this layer last validates that the orchestration and auto-recovery mechanisms genuinely restore the steady state established in the two layers above, rather than being tested in isolation.

### Tooling per Layer

Two complementary chaos engineering tools are used, matched to where each layer runs:

1. AWS Fault Ingestion Service (FIS)
2. Chaos Mesh

| <h4>Layer</h4> | <h4>Component(s)</h4>                                   | <h4>Tool</h4> | <h4>Why this tool</h4>                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute        | EC2 (EKS worker nodes / self-managed DB or Redis hosts) | AWS FIS       | Native AWS control-plane actions for instance stop/terminate/reboot and SSM-agent-based stressors; integrates with CloudWatch alarms as automatic stop conditions.                                                                      |
| Storage        | Database (RDS/Aurora), Redis (ElastiCache)              | AWS FIS       | Purpose-built managed-service actions (e.g., failover-db-cluster, failover ElastiCache) that safely trigger the same failover path AWS itself would use, without needing to fake it at the OS level.                                    |
| Application    | Hyperswitch pods on EKS                                 | Chaos Mesh    | Kubernetes-native CRDs (PodChaos, StressChaos, NetworkChaos, IOChaos) that operate at the pod/container level – the right granularity for testing how the application itself degrades and recovers, independent of the underlying node. |

In practice, AWS FIS also has EKS-targeted actions (pod-delete, pod CPU/memory/IO stress, network faults) that overlap with Chaos Mesh. Where a merchant's platform team is already AWS-native, FIS's EKS actions can substitute for Chaos Mesh; this playbook uses Chaos Mesh for the application layer because it requires no extra IAM footprint beyond the cluster, runs identically on non-AWS Kubernetes, and gives finer-grained control over stress workers for reproducible load profiles.

AWS FIS Documentation: [https://docs.aws.amazon.com/fis/latest/userguide/what-is.html<br>](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)ChaosMesh Documentation: [https://chaos-mesh.org/docs/](https://chaos-mesh.org/docs/)

## Fault Injection Catalog by Layer

The tables below list the specific fault types run against each layer, in priority order, along with the tool and action used.

### Storage Layer – Database

| <h4>Fault</h4>                | <h4>Tool / Action</h4>                | <h4>What it validates</h4>                                                                                                             |
| ----------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Forced failover               | AWS FIS – aws:rds:failover-db-cluster | Application reconnects cleanly to the new writer; in-flight transactions are not lost or duplicated; RTO meets target.                 |
| CPU stress on the DB instance | AWS FIS – RDS CPU stress action       | Query latency degradation is bounded; connection pool and timeouts on the application side behave as configured rather than cascading. |
| Elevated replication lag      | AWS FIS – replication delay action    | Read replicas / reporting paths degrade gracefully; no stale-read correctness issues on the payment path.                              |
| Connection storm / throttling | AWS FIS – API throttling faults       | Application-side connection pooling and backoff/retry logic prevent a thundering-herd against the database.                            |

### Storage Layer – Redis

| <h4>Fault</h4>                         | <h4>Tool / Action</h4>                          | <h4>What it validates</h4>                                                                                                                                                                       |
| -------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Forced failover (primary → replica)    | AWS FIS – ElastiCache failover action           | Idempotency-key locking and cached routing/session data survive failover without duplicate charges or stuck locks.                                                                               |
| CPU / memory stress on Redis node      | AWS FIS – EC2/ElastiCache stress actions        | Latency-sensitive operations (locking, idempotency checks) degrade predictably; the application falls back safely (e.g., fails closed on a lock it can't acquire) rather than double-processing. |
| Network latency / packet loss to Redis | AWS FIS – network latency / packet-loss actions | Application timeouts and retries around Redis calls are correctly tuned – no indefinite blocking on the hot path.                                                                                |

### Application Layer – Hyperswitch on EKS

<table data-header-hidden data-search="false"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><h4>Fault</h4></td><td><h4>Chaos Mesh Action</h4></td><td><h4>What it validates</h4></td></tr><tr><td>Pod kill</td><td>PodChaos – pod-kill</td><td>Kubernetes reschedules pods promptly; in-flight requests are not lost; readiness/liveness probes and load balancing route traffic away correctly.</td></tr><tr><td>Pod failure (unready, not deleted)</td><td>PodChaos – pod-failure</td><td>Load balancer / Envoy correctly stops routing to an unready pod without dropping requests.</td></tr><tr><td>Container kill</td><td>PodChaos – container-kill</td><td>Sidecar/init container failure doesn't take down the whole pod unexpectedly.</td></tr><tr><td>CPU stress</td><td>StressChaos – CPU stressors</td><td>Autoscaling (HPA) reacts appropriately; request latency degrades gracefully rather than cliff-dropping under load.</td></tr><tr><td>Memory stress</td><td>StressChaos – memory stressors</td><td>No OOM-kill cascades; memory limits/requests are sized correctly for peak load.</td></tr><tr><td>Network partition / latency to Redis, DB, connectors</td><td>NetworkChaos – delay, loss, partition</td><td>Timeouts, circuit breakers, and retry/backoff logic around each dependency behave as designed; no request pile-ups.</td></tr><tr><td>I/O delay / error</td><td>IOChaos</td><td>Local disk-dependent operations (logging, temp state) don't block the request path.</td></tr></tbody></table>

### Compute Layer – EC2

<table data-header-hidden data-search="false"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><h4>Fault</h4></td><td><h4>Tool / Action</h4></td><td><h4>What it validates</h4></td></tr><tr><td>Instance termination</td><td>AWS FIS – EC2 terminate-instances</td><td>Auto Scaling Group / EKS node group replaces capacity within the target time; workloads reschedule without manual intervention.</td></tr><tr><td>Instance stop/start</td><td>AWS FIS – EC2 stop/start-instances</td><td>Behavior of any workload with local/temporary state on restart is as expected.</td></tr><tr><td>CPU stress</td><td>AWS FIS – EC2 CPU stress (SSM)</td><td>Node-level resource pressure doesn't starve co-located critical pods; validates node-level resource requests/limits and taints.</td></tr><tr><td>Memory stress</td><td>AWS FIS – EC2 memory stress (SSM)</td><td>Same as above for memory; validates kubelet eviction thresholds are tuned correctly.</td></tr><tr><td>Disk I/O stress</td><td>AWS FIS – EC2 IO stress (SSM)</td><td>Disk-bound operations degrade gracefully; no node-level cascading failure.</td></tr><tr><td>AZ-level power/network loss</td><td>AWS FIS – AZ Availability outage scenario</td><td>Multi-AZ failover for EC2/EKS, RDS, and ElastiCache all function together, not just in isolation.</td></tr></tbody></table>

## Test Methodology

### Steady-State Metrics

Before any experiment, capture a baseline for the metrics below over a normal traffic window. Every experiment is judged against this baseline, not against an absolute target.

<table data-header-hidden data-search="false"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><h4>Metric</h4></td><td><h4>Layer it  reflects</h4></td><td><h4>Why it matters</h4></td></tr><tr><td>Payment success rate (authorized / attempted)</td><td>End-to-end</td><td>The single most important business signal – must hold steady through every experiment.</td></tr><tr><td>p50 / p95 / p99 authorization latency</td><td>Application, Storage</td><td>Tail latency exposes lock contention, connection-pool exhaustion, and failover pauses before they become errors.</td></tr><tr><td>Error rate by type (5xx, timeout, connector error)</td><td>Application</td><td>Distinguishes application-level failures from upstream connector issues.</td></tr><tr><td>Redis command latency / connection errors</td><td>Storage – cache</td><td>Detects lock/idempotency-key contention during failover or stress.</td></tr><tr><td>DB replication lag / failover time / connection errors</td><td>Storage – persistent</td><td>Confirms the database recovers within the target RTO and doesn't serve stale reads.</td></tr><tr><td>Pod restart count / readiness-probe failures</td><td>Application</td><td>Confirms Kubernetes correctly detects and routes around unhealthy pods.</td></tr><tr><td>Node/instance recovery time</td><td>Compute</td><td>Confirms ASG/EKS node replacement meets the target time-to-recovery.</td></tr><tr><td>Duplicate or orphaned transaction count</td><td>End-to-end</td><td>Payments-specific correctness check – must remain zero through every experiment.</td></tr></tbody></table>

### Experiment Lifecycle

1. Define hypothesis – name the component, the fault, and the expected steady-state outcome.
2. Set blast radius – start in a staging/pre-production environment or non-critical namespace/AZ; scope to a single pod, node, or replica first.
3. Set stop conditions – attach CloudWatch alarms (FIS) or manual/automated abort criteria (Chaos Mesh) so the experiment halts automatically if error rate or latency breaches a safe threshold.
4. Run the experiment – execute for a fixed, short duration; keep dashboards and alerting open throughout.
5. Observe and record – capture the metrics in section 5.1 before, during, and after the experiment (see the observation template in section 8).
6. Recover and verify – confirm the system returns to steady state without manual intervention beyond what's expected in a real incident.
7. Widen or fix – if steady state held, gradually increase blast radius/duration; if it didn't, treat the finding as a resilience defect and re-test after the fix.

### Safety Guardrails

* Run first in staging with production-like data volume and topology; only promote to production experiments once staging results are clean and stakeholders sign off.
* Always attach a CloudWatch alarm-based stop condition to every AWS FIS experiment template.
* Prefer off-peak windows for early production experiments; schedule and communicate the test window to on-call and support teams in advance.
* Use Chaos Mesh namespace/label selectors to scope pod-level faults – never use cluster-wide selectors in production.
* Verify PodDisruptionBudgets are configured for Hyperswitch deployments before running any pod-kill or node-level experiment.
* Treat every experiment as reversible within minutes; if an action doesn't have a fast, reliable rollback, don't run it against production.

## Suggested Execution Plan for a Production Deployment

Anyone standing up this program for the first time can follow this phased rollout rather than testing everything at once:

1. **Phase 0 – Instrumentation:** confirm dashboards/alerts exist for every metric in section 5.1 before running any experiment. If you can't observe it, don't chaos-test it yet.
2. **Phase 1 – Storage in staging:** run the section 6.1 and 6.2 experiments against a staging environment with production-like data volumes.
3. **Phase 2 – Application in staging:** run the section 6.3 experiments against staging Hyperswitch pods.
4. **Phase 3 – Compute in staging:** run the section 6.4 experiments in staging, including at least one AZ-level scenario.
5. **Phase 4 – Production, single-instance blast radius:** repeat the highest-value experiments from phases 1–3 in production, scoped to a single pod/node/replica, during a low-traffic window.
6. **Phase 5 – Production GameDay:** run a combined scenario (e.g., Redis failover + concurrent pod CPU stress) with cross-functional stakeholders (engineering, SRE, support) observing live, to rehearse the incident-response process itself.
7. **Phase 6 – Recurring cadence:** re-run the full catalog on a fixed cadence (e.g., quarterly) and after any major architecture change (new connector, DB version upgrade, cluster resize).

## Hyperswitch Component & Stack Level RTO/RPO

Below are the RTO and RPO of the database, Redis and overall stack based on chaos and failover tests conducted by the Hyperswitch team on our stack.&#x20;

The RPO in all cases depends on the replication lag between the primary and secondary instances and the values mentioned below are in the ideal case of very low replication lag. It is important to monitor this metric to ensure RPO stays as low as possible.&#x20;

|                                                     |              |              |
| --------------------------------------------------- | ------------ | ------------ |
| <h4>Component</h4>                                  | <h4>RTO</h4> | <h4>RPO</h4> |
| Database (RDS)                                      | 2-4 mins     | \~0          |
| Redis (Elasticache)                                 | <1 min       | \~0          |
| Hyperswitch Stack (Failover from Active to Passive) | 2-5 mins     | \~0          |

