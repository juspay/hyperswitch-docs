# Dispute Service Overview

## Overview

The Dispute Service helps you manage chargeback disputes across payment processors using the Python SDK. When customers dispute transactions with their banks, this service enables you to track dispute status, submit evidence, and make informed decisions.

**Business Use Cases:**

* **E-commerce fraud defense** - Submit delivery proof and receipts to contest illegitimate chargebacks
* **Service businesses** - Provide service documentation and customer communication records
* **Subscription disputes** - Submit recurring transaction agreements and cancellation policies
* **Revenue recovery** - Defend valid transactions to minimize chargeback losses

## Operations

| Operation                                 | Description                                                                                                      | Use When                                                         |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`submit_evidence`](submit-evidence-2.md) | Upload evidence to dispute customer chargeback. Provides documentation to contest fraudulent transaction claims. | You have proof of delivery, service, or customer acceptance      |
| [`get`](get-8.md)                         | Retrieve dispute status and evidence submission state. Tracks dispute progress through bank review process.      | Check dispute status, review evidence deadlines                  |
| [`defend`](defend-2.md)                   | Submit defense with reason code for dispute. Presents formal argument against customer's chargeback claim.       | Contesting the dispute with formal defense                       |
| [`accept`](accept-2.md)                   | Concede dispute and accepts chargeback loss. Acknowledges liability when evidence is insufficient.               | Evidence is insufficient, cost of defense exceeds dispute amount |

## SDK Setup

```python
from hyperswitch_prism import DisputeClient

dispute_client = DisputeClient(
    connector='stripe',
    api_key='YOUR_API_KEY',
    environment='SANDBOX'
)
```

## Next Steps

* [Payment Service](payment-service-2.md) - Review original payment details
* [Refund Service](refund-service-2.md) - Process voluntary refunds to avoid disputes
* [Event Service](event-service-2.md) - Handle dispute webhook notifications
