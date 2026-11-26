---
name: hyperswitch-docs-going-live
description: Use this skill when the user asks "how do I go live with Hyperswitch", "production checklist", "switch from sandbox to production", "going live guide", "production deployment Hyperswitch", "live API key", "Hyperswitch production setup", "what do I need before launching payments", or needs to understand the steps to move from sandbox to production.
version: 1.0.0
tags: [hyperswitch, docs, production, go-live, checklist, deployment]
---

# Going Live with Hyperswitch

## Overview

This skill covers the steps documented in the Hyperswitch going-live guide — switching from sandbox to production, configuring live connectors, and verifying your integration is production-ready.

**Doc reference:** `going-live/` directory

---

## Pre-Launch Checklist

Before switching to production:

### Integration
- [ ] All payment flows tested in sandbox: create, confirm, capture, refund, cancel
- [ ] Webhook handler live, signature verification enabled
- [ ] 3DS flows tested (frictionless and challenge)
- [ ] `return_url` is HTTPS and handles all payment statuses (`succeeded`, `failed`, `processing`)
- [ ] Idempotency keys used on all payment creation requests
- [ ] Error states handled gracefully (declined card UI, network failures)

### Connectors
- [ ] Live credentials obtained from your payment processor
- [ ] Connector configured in **Live Mode** (not Test Mode) in the dashboard
- [ ] Live connector tested with a real card for ≤$1.00

### Security
- [ ] Secret API key stored in a secrets manager, not in code or environment files
- [ ] Publishable key is the only Hyperswitch credential in your frontend code
- [ ] Webhook secret stored securely
- [ ] HTTPS enforced on all pages that handle payments

### Compliance
- [ ] Privacy policy mentions payment data handling
- [ ] For subscriptions: terms of service include cancellation policy
- [ ] 3DS/SCA configured for EU/UK markets

---

## Getting a Production API Key

1. Log in to [app.hyperswitch.io](https://app.hyperswitch.io) on your production account (or switch environment)
2. Navigate to **Developers → API Keys**
3. Click **Create API Key** → select **Live**
4. Store the key in your secrets manager immediately

Production keys are prefixed differently from sandbox keys. Never mix them.

---

## Switching Connector to Live Mode

1. Dashboard → Connectors → click your connector
2. Toggle **Test Mode → Live Mode**
3. Enter live credentials (different from test credentials)
4. Run a ≤$1.00 real transaction to verify

---

## Hyperswitch Cloud vs Self-Hosted

| Deployment | Guide |
|------------|-------|
| Hyperswitch Cloud | `hyperswitch-cloud/` directory — managed SaaS |
| AWS Self-Hosted | `deploy-hyperswitch-on-aws/` directory |
| Local Development | `setup-hyperswitch-locally/` directory |
| Production Self-Hosted | `production-deployment/` directory |

---

## E-Commerce Platform Plugins

If you use a platform rather than a custom integration:

| Platform | Doc |
|----------|-----|
| WooCommerce | `explore-hyperswitch/e-commerce-platform-plugins/woocommerce-plugin/` |
| Saleor | `explore-hyperswitch/e-commerce-platform-plugins/saleor-app/` |

---

## MCP Server Setup (AI Development)

For teams using AI coding assistants with the Hyperswitch MCP server:

**Doc reference:** `about-hyperswitch/ai-resources/setup-mcp-server.md`

```json
// Claude Desktop / Claude Code MCP config
{
  "mcpServers": {
    "hyperswitch": {
      "command": "npx",
      "args": ["-y", "@juspay/hyperswitch-mcp"],
      "env": { "HYPERSWITCH_API_KEY": "YOUR_KEY" }
    }
  }
}
```

---

## Production Tips

- Run load tests (using `loadtest/` scripts in the main repo) before launch to identify bottlenecks.
- Set up monitoring alerts for: payment success rate drops below 90%, webhook delivery failures, connector error spikes.
- Keep sandbox credentials active after going live — you'll need them for testing new features and debugging reported issues.
- For high-traffic launches (e.g., a sale event), contact your connector's support in advance — some have transaction rate limits that require manual lifting.
