---
title: handle (Java SDK)
description: Process webhook notifications from payment processors to verify signatures and receive normalized event data
tags:
  - java
  - webhooks
  - events
---

# handle Method

## Overview

The `handle` method processes webhook payloads.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantEventId` | String | Yes | Your event reference |
| `payload` | String | Yes | Raw webhook body |
| `headers` | Map | Yes | HTTP headers |
| `webhookSecret` | String | Yes | Signing secret |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `eventType` | String | Event type |
| `sourceVerified` | Boolean | Signature verified |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantEventId", "evt_001");
request.put("payload", payload);
request.put("headers", headers);
request.put("webhookSecret", "whsec_xxx");

Map<String, Object> response = eventClient.handle(request);
```
