# Submit Evidence

## Overview

The `submit_evidence` method uploads supporting documentation to contest a chargeback dispute. Evidence strengthens your defense by proving the transaction was legitimate and the customer received the product or service.

**Business Use Case:** A customer disputed a charge claiming they never received their order. You have delivery confirmation and the customer's signature. Submit this evidence to prove the order was delivered.

## Purpose

**Why submit evidence?**

| Evidence Type              | Use Case                                         |
| -------------------------- | ------------------------------------------------ |
| **Delivery proof**         | Tracking info, receipt signature, GPS logs       |
| **Customer communication** | Email threads showing customer confirmed receipt |
| **Product/service proof**  | Photos, service completion reports               |
| **Terms acceptance**       | Signed contracts, terms of service agreement     |

**Key outcomes:**

* Evidence attached to dispute case
* Stronger position in bank arbitration
* Improved win rate for disputes

## Request Fields

| Field           | Type   | Required | Description                                                                |
| --------------- | ------ | -------- | -------------------------------------------------------------------------- |
| `dispute_id`    | string | Yes      | The connector's dispute ID                                                 |
| `evidence_type` | string | Yes      | Type: delivery\_proof, customer\_communication, product\_description, etc. |
| `files`         | list   | Yes      | List of file URLs or file data                                             |
| `description`   | string | No       | Description of evidence                                                    |

## Response Fields

| Field                | Type          | Description                                 |
| -------------------- | ------------- | ------------------------------------------- |
| `dispute_id`         | string        | Connector's dispute ID                      |
| `evidence_submitted` | bool          | Whether evidence was successfully submitted |
| `status`             | DisputeStatus | Current dispute status                      |
| `status_code`        | int           | HTTP-style status code (200, 422, etc.)     |

## Example

### SDK Setup

```python
from hyperswitch_prism import DisputeClient

dispute_client = DisputeClient(
    connector='stripe',
    api_key='YOUR_API_KEY',
    environment='SANDBOX'
)
```

### Request

```python
request = {
    "dispute_id": "dp_xxx",
    "evidence_type": "delivery_proof",
    "files": [
        "https://storage.example.com/delivery_receipt_001.pdf",
        "https://storage.example.com/tracking_screenshot.png"
    ],
    "description": "Package delivered to customer address on 2024-01-15. Signed by customer."
}

response = await dispute_client.submit_evidence(request)
```

### Response

```python
{
    "dispute_id": "dp_xxx",
    "evidence_submitted": True,
    "status": "NEEDS_RESPONSE",
    "status_code": 200
}
```

## Evidence Types

| Type                     | Description                                | When to Use                                |
| ------------------------ | ------------------------------------------ | ------------------------------------------ |
| `delivery_proof`         | Shipping confirmation, tracking, signature | Physical goods delivered                   |
| `customer_communication` | Emails, chat logs, support tickets         | Customer confirmed receipt or satisfaction |
| `product_description`    | Product details, screenshots, demos        | Service was as described                   |
| `cancellation_policy`    | Terms, refund policy, agreements           | Customer agreed to terms                   |
| `duplicate_charge_doc`   | Proof charges are distinct                 | Multiple legitimate charges                |
| `receipt`                | Transaction receipt, invoice               | Proof of purchase                          |

## Best Practices

* Submit evidence before the deadline (typically 7-21 days)
* Provide clear, high-quality documentation
* Include all relevant communication
* Be concise but comprehensive

## Next Steps

* [defend](defend-2.md) - Submit formal defense after evidence
* [get](get-8.md) - Check dispute status
* [accept](accept-2.md) - Concede if evidence is insufficient
