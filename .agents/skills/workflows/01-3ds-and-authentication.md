---
name: hyperswitch-docs-3ds-authentication
description: Use this skill when the user asks about "3DS decision manager", "3D Secure setup in Hyperswitch", "how to configure 3DS rules", "external 3DS authentication", "authenticate via PSP", "3DS intelligence engine", "native 3DS mobile", "import 3DS results", "SCA configuration", "PSD2 routing", "3DS step-up", or needs to understand how Hyperswitch handles 3DS authentication workflows.
version: 1.0.0
tags: [hyperswitch, docs, 3DS, authentication, SCA, PSD2, decision-manager]
---

# 3DS & Authentication

## Overview

The Hyperswitch 3DS Decision Manager lets you configure when to trigger 3DS, which authentication provider to use, and how to handle the challenge/frictionless flow. This skill covers the docs for all 3DS-related configuration.

**Doc reference:** `explore-hyperswitch/workflows/3ds-decision-manager/README.md`

---

## 3DS Options in Hyperswitch

| Approach | When to Use | Doc |
|----------|-------------|-----|
| **PSP-native 3DS** | Connector handles 3DS transparently | `authenticate-with-3d-secure-via-psp.md` |
| **External 3DS (standard)** | Your own 3DS server (Netcetera, GPay 3DS, etc.) | `external-authentication-for-3ds.md` |
| **3DS Intelligence Engine** | ML-based exemption management | `3ds-intelligence-engine/` |
| **Import 3DS Results** | Pre-authenticated 3DS from external provider | `import-3d-secure-results.md` |
| **Native Mobile 3DS** | In-app 3DS for Android/iOS | `native-3ds-authentication-for-mobile-payments.md` |

---

## Option 1: Authenticate via PSP (Most Common)

The connector's 3DS is triggered by setting `authentication_type: "three_ds"` in the payment request. Hyperswitch delegates the challenge to the connector.

```json
POST /payments
{
  "authentication_type": "three_ds",
  "return_url": "https://yourapp.com/payment/3ds/complete",
  ...
}
```

For SCA compliance: configure your **Business Profile** in the dashboard to set the default `authentication_type` to `three_ds` for the relevant markets.

**Doc reference:** `explore-hyperswitch/workflows/3ds-decision-manager/authenticate-with-3d-secure-via-psp.md`

---

## Option 2: External 3DS Authentication

Use your own 3DS server while Hyperswitch handles payment processing:

1. Authenticate the card externally
2. Submit authentication results to Hyperswitch
3. Hyperswitch authorises the payment using the pre-authenticated data

```json
POST /payments/{payment_id}/3ds/authentication
{
  "client_details": { "ip_address": "...", "user_agent": "..." },
  "sdk_details": {
    "sdk_app_id": "...",
    "sdk_reference_number": "...",
    "sdk_transaction_id": "..."
  }
}
```

**Doc reference:** `explore-hyperswitch/workflows/3ds-decision-manager/external-authentication-for-3ds.md`

---

## Option 3: 3DS Intelligence Engine

The 3DS Intelligence Engine optimises 3DS exemptions — requesting exemptions where risk is low (frictionless), triggering challenges only where required.

Setup:
1. Dashboard → Workflows → 3DS Decision Manager → Enable Intelligence Engine
2. Configure risk thresholds and exemption types (TRA, low-value, secure corporate)
3. The engine evaluates each transaction and sets `authentication_type` automatically

**Doc reference:** `explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine/get-started-with-3ds-decision-manager.md`

---

## Option 4: Import 3DS Results

If the card was already authenticated by an external 3DS server before the payment API call:

```json
POST /payments
{
  "authentication_type": "no_three_ds",
  "external_authentication_details": {
    "eci": "05",
    "cavv": "AAABCSIIAAAAAAACcwgAEMCoNh==",
    "ds_trans_id": "97267598-FAE6-48F2-8083-C23433CFDDA1",
    "authentication_flow": "frictionless",
    "message_version": "2.1.0"
  }
}
```

**Doc reference:** `explore-hyperswitch/workflows/3ds-decision-manager/import-3d-secure-results.md`

---

## Option 5: Native Mobile 3DS

For in-app 3DS on Android/iOS — the challenge is presented in a WebView within your app rather than redirecting to a browser.

**Doc reference:** `explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments.md`

Setup requires:
1. Enabling native 3DS in your Business Profile
2. Passing device fingerprinting data (`browser_info`) in the payment request
3. Handling the in-app WebView challenge via SDK callbacks

---

## Production Tips

- For European/UK merchants: configure 3DS as the default in your Business Profile — regulators require SCA for most card transactions and non-compliance leads to higher dispute rates.
- Use the 3DS Intelligence Engine to maximise frictionless rates — every unnecessary challenge reduces conversion by 15–30%.
- External 3DS is valuable when you have a specific 3DS server that is already certified and you want to reuse it across multiple PSPs.
- Always pass `browser_info` (user-agent, screen dimensions, timezone) when using external 3DS — it significantly improves frictionless approval rates from issuers.
