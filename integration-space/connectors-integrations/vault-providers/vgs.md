---
description: >-
  Store and retrieve sensitive payment credentials through VGS (Very Good
  Security) integrated via Juspay Hyperswitch as an external vault provider.
---

# VGS (Very Good Security)

VGS connects to Hyperswitch as an external vault provider implementing the `ExternalVault` interface. It provides tokenization and proxy capabilities — card data is stored in VGS and referenced by an alias token. Hyperswitch calls VGS to insert credentials into the vault and to retrieve them for payment processing.

### Authentication

VGS uses `SignatureKey` authentication — three credentials are required.

| Credential | Description |
| --- | --- |
| **Username (API Key)** | VGS client ID (OAuth2 client credentials). Used as the username for Basic Auth to VGS's token endpoint. |
| **Password (Key1)** | VGS client secret. Used as the password for Basic Auth to VGS's token endpoint. |
| **Vault ID (API Secret)** | Your VGS vault identifier (e.g. `tntxxxxxxx`). Determines which vault receives and serves tokenized data. |

### Vault Flows

VGS supports the following Hyperswitch ExternalVault flows:

| Flow | Description |
| --- | --- |
| **ExternalVaultInsert** | Stores sensitive payment credentials (card data) in VGS and returns a VGS alias token |
| **ExternalVaultRetrieve** | Retrieves tokenized credentials from VGS using a stored alias token, for use in payment authorization |

### When to Use VGS

- You already have card data tokenized in VGS and want to use Hyperswitch for payment orchestration without re-collecting card details from customers.
- Your compliance posture requires a specific vault vendor with proxy-based tokenization.
- You need VGS transparent proxy to forward tokenized requests directly to payment processors.

### Common Failure Modes

**OAuth token fetch fails**
Symptom: VGS requests return 401 before reaching the vault. Fix: Verify the Username (client ID) and Password (client secret) stored in Hyperswitch match your VGS credentials. Ensure the OAuth client has the correct scopes for vault read/write.

**Vault ID not found**
Symptom: Insert or Retrieve operations return a 404 or vault not found error. Fix: Verify the Vault ID stored in Hyperswitch matches your VGS vault identifier exactly (e.g. `tntxxxxxxx`). Vault IDs are environment-specific — sandbox vault IDs do not work in production.

**Alias not found on retrieve**
Symptom: ExternalVaultRetrieve returns no data for a stored alias. Fix: Confirm the alias was successfully written during ExternalVaultInsert. Aliases may expire depending on VGS vault retention settings.

---

### Activating VGS via Hyperswitch

#### Prerequisites

1. A registered VGS account with a vault provisioned. Sign up at [verygoodsecurity.com](https://www.verygoodsecurity.com/).
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. VGS client ID, client secret, and vault ID from your VGS dashboard.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/vgs.rs`.
