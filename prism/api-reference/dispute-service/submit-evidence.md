---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/prism/api-reference/dispute-service/submit-evidence
---

# Submit Evidence

## Overview

The `SubmitEvidence` RPC uploads supporting documentation to contest a chargeback dispute. This evidence is presented to the issuing bank during the dispute resolution process to prove the transaction was valid.

**Business Use Case:** When a customer disputes a charge claiming they didn't receive the product, didn't authorize the transaction, or the product was defective, you need to provide proof to defend against the chargeback. This RPC uploads delivery confirmations, receipts, customer communication, and other supporting documents.

## Purpose

**Why submit evidence for disputes?**

| Scenario                       | Evidence Type                                                    | Expected Outcome                                |
| ------------------------------ | ---------------------------------------------------------------- | ----------------------------------------------- |
| **Product not received**       | Shipping confirmation, tracking records, delivery signature      | Prove delivery occurred                         |
| **Product not as described**   | Product specifications, photos, customer communication           | Show product matched description                |
| **Transaction not authorized** | IP logs, device fingerprints, 3DS authentication data            | Prove customer authorized purchase              |
| **Subscription cancellation**  | Recurring transaction agreement, cancellation policy, usage logs | Show service was provided or properly disclosed |
| **Duplicate charge**           | Order details, refund records, transaction timestamps            | Clarify distinct transactions                   |

**Key outcomes:**

* Evidence attached to dispute record
* Evidence IDs returned for tracking
* Status updated to reflect submission
* Bank reviews evidence during adjudication

## Request Fields

| Field                      | Type                | Required | Description                              |
| -------------------------- | ------------------- | -------- | ---------------------------------------- |
| `merchant_dispute_id`      | string              | Yes      | Your unique dispute reference            |
| `connector_transaction_id` | string              | No       | Original transaction ID                  |
| `dispute_id`               | string              | Yes      | Connector's dispute identifier           |
| `service_date`             | int64               | No       | Unix timestamp when service was provided |
| `shipping_date`            | int64               | No       | Unix timestamp when product was shipped  |
| `evidence_documents`       | EvidenceDocument\[] | No       | Array of evidence documents              |

### EvidenceDocument Fields

| Field              | Type         | Required | Description                                                                                                                                                                                                                                                                                                               |
| ------------------ | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `evidence_type`    | EvidenceType | Yes      | Type of evidence. Values: GOODS\_SERVICES\_RECEIVED, GOODS\_SERVICES\_NOT\_RECEIVED, GOODS\_SERVICES\_NOT\_AS\_DESCRIBED, PROOF\_OF\_DELIVERY, RECEIPT, REFUND\_POLICY, SERVICE\_DOCUMENTATION, SHIPPING\_DOCUMENTATION, INVOICE\_SHOWING\_DISTINCT\_TRANSACTIONS, RECURRING\_TRANSACTION\_AGREEMENT, UNCATEGORIZED\_FILE |
| `file_content`     | bytes        | No       | Binary content of the evidence file                                                                                                                                                                                                                                                                                       |
| `file_mime_type`   | string       | No       | MIME type (e.g., "application/pdf", "image/png")                                                                                                                                                                                                                                                                          |
| `provider_file_id` | string       | No       | External file storage identifier                                                                                                                                                                                                                                                                                          |

## Response Fields

| Field                    | Type                | Description                                                      |
| ------------------------ | ------------------- | ---------------------------------------------------------------- |
| `dispute_id`             | string              | Connector's dispute identifier                                   |
| `submitted_evidence_ids` | string\[]           | IDs of successfully submitted evidence items                     |
| `dispute_status`         | DisputeStatus       | Current status: OPENED, EXPIRED, ACCEPTED, CHALLENGED, WON, LOST |
| `connector_status_code`  | string              | Connector-specific status code                                   |
| `error`                  | ErrorInfo           | Error details if submission failed                               |
| `status_code`            | uint32              | HTTP-style status code                                           |
| `response_headers`       | map\<string,string> | Connector-specific response headers                              |
| `merchant_dispute_id`    | string              | Your dispute reference (echoed back)                             |
| `raw_connector_request`  | SecretString        | Raw API request sent to connector (debugging)                    |

## Example

### Request (grpcurl)

```bash
grpcurl -H "x-connector: stripe" \
  -H "x-connector-config: {\"config\":{\"Stripe\":{\"api_key\":\"$STRIPE_API_KEY\"}}}" \
  -d '{
    "merchant_dispute_id": "dispute_001",
    "dispute_id": "dp_1Oxxx...",
    "connector_transaction_id": "pi_3Oxxx...",
    "shipping_date": 1704067200,
    "service_date": 1704067200,
    "evidence_documents": [
      {
        "evidence_type": "PROOF_OF_DELIVERY",
        "file_content": "base64encodedpdfcontent...",
        "file_mime_type": "application/pdf"
      },
      {
        "evidence_type": "RECEIPT",
        "file_content": "base64encodedreceipt...",
        "file_mime_type": "application/pdf"
      }
    ]
  }' \
  localhost:8080 \
  types.DisputeService/SubmitEvidence
```

### Response

```json
{
  "dispute_id": "dp_1Oxxx...",
  "submitted_evidence_ids": ["file_1Aa...", "file_2Bb..."],
  "dispute_status": "CHALLENGED",
  "status_code": 200
}
```

## Next Steps

* [Defend](defend.md) - Submit formal defense with reason code
* [Get](get.md) - Check dispute status after evidence submission
* [Accept](accept.md) - Concede dispute if evidence is insufficient
