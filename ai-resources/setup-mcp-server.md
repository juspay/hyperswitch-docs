---
icon: user-robot-xmarks
---

# Setup MCP Server

**Prerequisites**: Ensure you have an MCP client installed (Cursor, Claude Desktop, Cline, etc.)

### Step 1: Install the MCP Server

```bash
npx mint-mcp add api-reference.hyperswitch.io
```

### Step 2: Configure your MCP Server

*   Enter your Hyperswitch API key (You can generate one from the developer section in [Hyperswitch Control Center](https://app.hyperswitch.io/dashboard/developer-api-keys))



    <figure><img src="../.gitbook/assets/Screenshot 2025-07-07 at 6.59.56 AM (1).png" alt=""><figcaption></figcaption></figure>
*   Select your preferred MCP client from the prompt.

    <figure><img src="../.gitbook/assets/Screenshot 2025-07-07 at 7.00.02 AM (1).png" alt=""><figcaption></figcaption></figure>

### Step 3: Run the Server

On completing step 2, you will get an output similar to&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2025-07-07 at 7.02.01 AM.png" alt=""><figcaption></figcaption></figure>

You can then just copy the command and run it:

```
node <path to your local folder>/.mcp/api-reference.hyperswitch.io/src/index.js
```

Once done, you will see this as output:

<figure><img src="../.gitbook/assets/Screenshot 2025-07-07 at 7.07.18 AM.png" alt=""><figcaption></figcaption></figure>

### Step 4: Enable in your MCP Client

* Go to integrations (or MCP tools) section in your MCP client
* Look for the locally available MCP tool: `api.reference.hyperswitch.io`

### Step 5: Make your First Payment

Paste this prompt in your MCP Client:

```
Make a payment of 100 USD via Hyperswitch.
```

#### **Output:**&#x20;

You can head on to payment section in [Hyperswitch Control Center](https://app.hyperswitch.io/dashboard/payments) and verify the payment with the time stamp and status as `REQUIRES_PAYMENT_METHOD` .

{% hint style="warning" %}
This MCP server is only meant for product exploration while using sandbox environment.\
**DO NOT USE Hyperswitch API Key from the PRODUCTION ENVIRONMENT.**
{% endhint %}
