# Hyperswitch Docs — AI Coding Skills

> Context7-compatible skills for navigating [Hyperswitch documentation](https://docs.hyperswitch.io) — helping AI assistants give developers accurate, doc-grounded guidance.

## Quick Install

```bash
npx ctx7 skills install /juspay/hyperswitch-docs
```

## Skills Index

### Integration Guides

| Skill | Description |
|-------|-------------|
| [`integration/00-web-sdk-quickstart`](./integration/00-web-sdk-quickstart.md) | React, vanilla JS, and HTML web checkout — loadHyper → HyperElements → confirmPayment |
| [`integration/01-mobile-sdk`](./integration/01-mobile-sdk.md) | Android (Kotlin), iOS (Swift), React Native, Flutter |

### Workflows

| Skill | Description |
|-------|-------------|
| [`workflows/00-intelligent-routing`](./workflows/00-intelligent-routing.md) | Auth rate, least cost, volume, rule-based, and smart retries |
| [`workflows/01-3ds-and-authentication`](./workflows/01-3ds-and-authentication.md) | 3DS Decision Manager — PSP-native, external, intelligence engine, import results |
| [`workflows/02-vault-and-tokenization`](./workflows/02-vault-and-tokenization.md) | Vault architecture options — Juspay, external, self-hosted, pass-through |

### Connectors

| Skill | Description |
|-------|-------------|
| [`connectors/00-activate-connector`](./connectors/00-activate-connector.md) | Step-by-step connector activation, available connectors reference |

### Operations

| Skill | Description |
|-------|-------------|
| [`operations/00-analytics-and-disputes`](./operations/00-analytics-and-disputes.md) | Analytics dashboard, data export, dispute/chargeback management, fraud blocklist |
| [`operations/01-going-live`](./operations/01-going-live.md) | Pre-launch checklist, live API keys, production deployment options |

---

## How These Skills Differ from the Main Hyperswitch Skills

The [main Hyperswitch skills](https://context7.com/juspay/hyperswitch?tab=skills) (`/juspay/hyperswitch`) cover the **API layer** — request/response formats, field names, status codes.

These skills cover the **documentation layer** — where to find guides, how workflows are configured in the dashboard, doc file paths for deep-linking, and integration patterns as described in the official docs.

Use both together:
```bash
npx ctx7 skills install /juspay/hyperswitch        # API skills
npx ctx7 skills install /juspay/hyperswitch-docs   # Docs navigation skills
```

## Compatible AI Assistants

- Claude Code, Cursor, Windsurf, and any assistant supporting `.agents/skills/`

## Contributing

Skills reference real paths in this repository. Before adding a new skill:
1. Verify all doc paths exist: `find . -path "<doc_path>"`
2. Read the target doc to ensure the skill accurately reflects its content
3. Follow the frontmatter format: `name`, `description` (trigger-rich), `version`, `tags`
