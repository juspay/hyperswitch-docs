---
title: handle (PHP SDK)
description: Process webhook notifications from payment processors to verify signatures and receive normalized event data
tags:
  - php
  - webhooks
  - events
---

# handle Method

## Overview

The `handle` method processes webhook payloads from payment processors.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantEventId` | string | Yes | Your event reference |
| `payload` | string | Yes | Raw webhook body |
| `headers` | array | Yes | HTTP headers |
| `webhookSecret` | string | Yes | Signing secret |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `eventType` | string | Event type |
| `sourceVerified` | bool | Signature verified |

## Example

```php
$request = [
    'merchantEventId' => 'evt_001',
    'payload' => file_get_contents('php://input'),
    'headers' => getallheaders(),
    'webhookSecret' => 'whsec_xxx'
];
$response = $eventClient->handle($request);
```
