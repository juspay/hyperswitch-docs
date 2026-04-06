---
title: createAccessToken (Java SDK)
description: Generate short-lived API access tokens for secure temporary access to payment processor APIs
tags:
  - java
  - tokens
  - authentication
---

# createAccessToken Method

## Overview

The `createAccessToken` method generates a short-lived authentication token.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `scope` | String | No | Token scope |
| `expiresIn` | Integer | No | Lifetime in seconds |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `accessToken` | String | Token string |
| `tokenType` | String | Bearer |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("scope", "payment:write");
request.put("expiresIn", 3600);

Map<String, Object> response = authClient.createAccessToken(request);
```
