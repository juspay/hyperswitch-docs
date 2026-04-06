---
title: submitEvidence (PHP SDK)
description: Upload evidence to dispute chargebacks and provide documentation to contest fraudulent transaction claims
tags:
  - php
  - disputes
  - evidence
---

# submitEvidence Method

## Overview

The `submitEvidence` method uploads supporting documentation to contest a chargeback.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | string | Yes | The dispute ID |
| `evidenceType` | string | Yes | Type of evidence |
| `files` | array | Yes | File URLs |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `disputeId` | string | The dispute ID |
| `evidenceSubmitted` | bool | Success status |
| `status` | DisputeStatus | Updated status |

## Example

```php
$request = [
    'disputeId' => 'dp_xxx',
    'evidenceType' => 'delivery_proof',
    'files' => ['https://example.com/receipt.pdf']
];
$response = $disputeClient->submitEvidence($request);
```
