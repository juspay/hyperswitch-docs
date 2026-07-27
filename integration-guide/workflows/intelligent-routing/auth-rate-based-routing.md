---
description: Improve successful payments by routing traffic to processors with stronger recent authorization performance
icon: badge-check
metaLinks:
  alternates:
    - auth-rate-based-routing.md
---

# Auth-Rate Routing

Auth-Rate Routing uses recent payment outcomes to choose the processor most likely to authorize the next payment. It is useful when you have multiple processors for the same payment method and want routing to adapt as processor performance changes.

## How It Works

Hyperswitch tracks processor performance across payment attributes such as payment method, payment method type, transaction amount, currency, country, card network, and authentication type. The routing engine then ranks eligible processors by recent success rate.

The model treats each processor as a changing option in a non-stationary multi-armed bandit with delayed feedback. That means it accounts for both fluctuating success rates and the delay between sending a payment and receiving its final outcome.

The strategy balances two behaviors:

* **Exploitation:** Send most traffic to the processor with the best recent performance.
* **Exploration:** Send a smaller share of traffic to other eligible processors so the model keeps fresh performance data.

Hyperswitch uses a sliding window of recent attempts so routing can react to processor behavior without waiting for a manual configuration change. Downtime or repeated technical failures can deprioritize a processor before the final decision is made.

<figure><img src="../../../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

## Merchant Controls

| Control | Why it matters |
| --- | --- |
| Traffic split | Roll out auth-rate routing gradually before using it for all payments. |
| Bucket size | Controls how much recent traffic is used to calculate processor performance. |
| Hedging percentage | Controls the exploration share sent to alternate eligible processors. |
| Elimination threshold | Controls when a poorly performing processor is temporarily deprioritized. |

## Key Configurations

* Bucket size: Number of payments included in a block, limited by count or time period.
* Aggregate pipeline size:
  * Max: Number of buckets used to calculate scores in FIFO order. This determines reaction time.
  * Min: Number of buckets after which scores are used. This acts as the offset for error tolerance.
* Exploration percentage: Share of traffic sent to alternate eligible processors to keep scoring data fresh.

## Dashboard Setup

1. Configure at least two processors that support the same payment method.
2. Go to `Workflow` > `Routing`.
3. Choose `Auth-Rate Routing`.
4. Configure rollout percentage and scoring settings.
5. Save and activate the configuration.
6. Monitor processor share, auth rate, and decision logs.

## API Setup

Enable Auth-Rate Routing for your business profile:

```bash
curl --location --request POST 'https://sandbox.hyperswitch.io/account/<merchant_id>/business_profile/<profile-id>/dynamic_routing/success_based/toggle?enable=dynamic_connector_selection' \
--header 'api-key: <api-key>'
```

Roll it out to the required split of payment traffic:

```bash
curl --location --request POST 'https://sandbox.hyperswitch.io/account/<merchant-id>/business_profile/<profile-id>/dynamic_routing/set_volume_split?split=100' \
--header 'api-key: <api-key>'
```

Update the routing model settings:

```bash
curl --location --request PATCH 'https://sandbox.hyperswitch.io/account/<merchant-id>/business_profile/<profile-id>/dynamic_routing/success_based/config/<routing-id>' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>' \
--data '{
  "config": {
    "min_aggregates_size": 5,
    "max_aggregates_size": 8,
    "current_block_threshold": {
      "max_total_count": 5
    },
    "exploration_percent": 20.0
  }
}'
```

Activate the updated configuration:

```bash
curl --location --request POST 'https://sandbox.hyperswitch.io/routing/<routing-id>/activate' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>'
```

## Test Routing Behavior

Use the routing playground to simulate payment scenarios and review routing choices:

[https://hyperswitch-ten.vercel.app/](https://hyperswitch-ten.vercel.app/)

1. Create a merchant on Juspay Hyperswitch Control Center.
2. Configure at least two payment processors for the merchant profile.
3. Enter the sandbox API key, merchant ID, and profile ID when the simulator prompts for them.
4. Go to the `Routing` tab and toggle Success Based Routing.
5. Select the routing configuration settings.
6. Go to the `General` tab and enter the number of payments to trigger in batches.
7. Click `Start Simulation` to see the results.
8. Use `Test Payment Data` to modify processor auth rates and observe how routing choices change.

For automatic tuning of bucket size and exploration settings, see [Autopilot](autopilot.md).
