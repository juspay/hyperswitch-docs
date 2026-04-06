---
title: submitEvidence (Java SDK)
description: Upload evidence to dispute chargebacks and provide documentation to contest fraudulent transaction claims
tags:
  - java
  - disputes
  - evidence
---

# submitEvidence Method

## Overview

The `submitEvidence` method uploads evidence to contest a chargeback.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | String | Yes | Dispute ID |
| `evidenceType` | String | Yes | Type of evidence |
| `files` | List | Yes | File URLs |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("disputeId", "dp_xxx");
request.put("evidenceType", "delivery_proof");
request.put("files", List.of("https://example.com/receipt.pdf"));

Map<String, Object> response = disputeClient.submitEvidence(request);
```
