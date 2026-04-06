---
title: createAccessToken (PHP SDK)
description: Generate short-lived API access tokens for secure temporary access to payment processor APIs
tags:
  - php
  - tokens
  - authentication
---

# createAccessToken Method

## Overview

The `createAccessToken` method generates a short-lived authentication token.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `scope` | string | No | Token scope |
| `expiresIn` | int | No | Lifetime in seconds |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `accessToken` | string | Token string |
| `tokenType` | string | Bearer |
| `expiresIn` | int | Seconds until expiry |

## Example

```php
$request = ['scope' => 'payment:write', 'expiresIn' => 3600];
$response = $authClient->createAccessToken($request);
```
