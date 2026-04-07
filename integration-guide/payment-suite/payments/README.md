---
description: >-
  Comprehensive guide to card payment processing patterns including one-time
  payments, manual capture, 3DS authentication, and recurring payment flows.
icon: file-invoice-dollar
---

# Pay-Then-Vault

Juspay Hyperswitch provides flexible payment processing with multiple flow patterns to accommodate different business needs. The system supports one-time payments, saved payment methods, and recurring billing through a comprehensive API design.

{% hint style="info" %}
#### Integration Path

**Client-Side SDK Payments (Tokenise Post Payment)**

Refer to Payments (Cards) section if your flow requires the SDK to initiate payments directly. In this model, the SDK handles the payment trigger and communicates downstream to the Hyperswitch server and your chosen Payment Service Providers (PSPs). This path is ideal for supporting dynamic, frontend-driven payment experiences.
{% endhint %}

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#2563EB",
    "lineColor": "#2563EB",
    "secondaryColor": "#EFF6FF",
    "tertiaryColor": "#DBEAFE",
    "fontFamily": "Inter, system-ui, sans-serif",
    "fontSize": "14px",
    "textColor": "#000000",

    "actorBkg": "#346DDB",
    "actorBorder": "#999999",
    "actorTextColor": "#ffffff",

    "signalColor": "#000000",
    "signalTextColor": "#999999",

    "labelBoxBkgColor": "#346DDB",
    "labelBoxBorderColor": "#2563EB"
  }
}}%%

flowchart TD
    A[Payment Request] --> B{Payment Type}

    %% One-time branch
    B -->|One-time| C[One-time Payment Flows]
    C --> C1[Instant Payment]
    C --> C2[Manual Capture]
    C --> C3[Decoupled Flow]

    %% Store card branch
    B -->|Store card| D[Payment Method Storage]
    D --> D1[Long-term storage]
    D --> D2[Short-term storage]
    D --> D3[List Saved Methods]

    %% Recurring branch
    B -->|Recurring| E[Recurring Payment Flows]
    E --> E1["Setup with charge (CIT)"]
    E --> E2["Setup without charge (CIT)"]
    E --> E3["Execute (MIT)"]
```

### One-Time Payment Patterns

#### 1. Instant Payment (Automatic Capture)

**Use Case:** Simple, immediate payment processing

**Endpoint:** `POST /payments`

<pre class="language-mermaid"><code class="lang-mermaid"><strong>%%{init: {
</strong>  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#2563EB",
    "lineColor": "#2563EB",
    "secondaryColor": "#EFF6FF",
    "tertiaryColor": "#DBEAFE",
    "fontFamily": "Inter, system-ui, sans-serif",
    "fontSize": "14px",
    "textColor": "#000000",

    "actorBkg": "#346DDB",
    "actorBorder": "#999999",
    "actorTextColor": "#ffffff",

    "signalColor": "#000000",
    "signalTextColor": "#999999",

    "labelBoxBkgColor": "#346DDB",
    "labelBoxBorderColor": "#2563EB"
  }
}}%%
sequenceDiagram
    participant Client
    participant Hyperswitch
    participant Processor

    Client->>Hyperswitch: POST /payments &#x3C;br> {confirm: true, capture_method: "automatic"}
    Hyperswitch->>Processor: Authorize + Capture
    Processor-->>Hyperswitch: Payment Complete
    Hyperswitch-->>Client: Status: succeeded
</code></pre>

**Required Fields:**

* `confirm: true`
* `capture_method: "automatic"`
* `payment_method`

**Final Status:** `succeeded`

#### 2. Two-Step Manual Capture

**Use Case:** Deferred capture (e.g., ship before charging)

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#2563EB",
    "lineColor": "#2563EB",
    "secondaryColor": "#EFF6FF",
    "tertiaryColor": "#DBEAFE",
    "fontFamily": "Inter, system-ui, sans-serif",
    "fontSize": "14px",
    "textColor": "#000000",

    "actorBkg": "#346DDB",
    "actorBorder": "#999999",
    "actorTextColor": "#ffffff",

    "signalColor": "#000000",
    "signalTextColor": "#696969",

    "labelBoxBkgColor": "#346DDB",
    "labelBoxBorderColor": "#2563EB"
  }
}}%%
sequenceDiagram
    participant Client
    participant Hyperswitch
    participant Processor

    Client->>Hyperswitch: POST /payments\n{confirm: true, capture_method: "manual"}
    Hyperswitch->>Processor: Authorize Only
    Processor-->>Hyperswitch: Authorization Hold
    Hyperswitch-->>Client: Status: requires_capture

    Note over Client: Ship goods, then capture

    Client->>Hyperswitch: POST /payments/{id}/capture
    Hyperswitch->>Processor: Capture Funds
    Processor-->>Hyperswitch: Capture Complete
    Hyperswitch-->>Client: Status: succeeded
```

**Flow:**

1. **Authorize:** `POST /payments` with `capture_method: "manual"`
2. **Status:** `requires_capture`
3. **Capture:** `POST /payments/{payment_id}/capture`
4. **Final Status:** `succeeded`

Read more: [here](https://docs.hyperswitch.io/~/revisions/2M8ySHqN3pH3rctBK2zj/about-hyperswitch/payment-suite-1/payments-cards/manual-capture)

#### 3. Fully Decoupled Flow

**Use Case:** Complex checkout journeys with multiple modification steps. Useful in headless checkout or B2B portals where data is filled progressively.

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#2563EB",
    "lineColor": "#2563EB",
    "secondaryColor": "#EFF6FF",
    "tertiaryColor": "#DBEAFE",
    "fontFamily": "Inter, system-ui, sans-serif",
    "fontSize": "14px",
    "textColor": "#000000",

    "actorBkg": "#346DDB",
    "actorBorder": "#999999",
    "actorTextColor": "#ffffff",

    "signalColor": "#000000",
    "signalTextColor": "#696969",

    "labelBoxBkgColor": "#346DDB",
    "labelBoxBorderColor": "#2563EB"
  }
}}%%
sequenceDiagram
    participant Client
    participant Hyperswitch

    Client->>Hyperswitch: POST /payments\n(Create Intent)
    Hyperswitch-->>Client: payment_id + client_secret

    Client->>Hyperswitch: POST /payments/{id}\n(Update: customer, amount, etc.)
    Hyperswitch-->>Client: Updated Intent

    Client->>Hyperswitch: POST /payments/{id}/confirm\n(Final Confirmation)
    Hyperswitch-->>Client: Status: succeeded / requires_capture

    opt Manual Capture
        Client->>Hyperswitch: POST /payments/{id}/capture
        Hyperswitch-->>Client: Status: succeeded
    end
```

**Endpoints:**

* **Create:** `POST /payments`
* **Update:** `POST /payments/{payment_id}`
* **Confirm:** `POST /payments/{payment_id}/confirm`
* **Capture:** `POST /payments/{payment_id}/capture` (if manual)

#### 4. 3D Secure Authentication Flow

**Use Case:** Enhanced security with customer authentication

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#2563EB",
    "lineColor": "#2563EB",
    "secondaryColor": "#EFF6FF",
    "tertiaryColor": "#DBEAFE",
    "fontFamily": "Inter, system-ui, sans-serif",
    "fontSize": "14px",
    "textColor": "#000000",

    "actorBkg": "#346DDB",
    "actorBorder": "#999999",
    "actorTextColor": "#ffffff",

    "signalColor": "#000000",
    "signalTextColor": "#696969",

    "labelBoxBkgColor": "#346DDB",
    "labelBoxBorderColor": "#2563EB"
  }
}}%%
sequenceDiagram
    participant Client
    participant Hyperswitch
    participant Customer
    participant Bank

    Client->>Hyperswitch: POST /payments<br>{authentication_type: "three_ds"}
    Hyperswitch-->>Client: Status: requires_customer_action <br> + redirect_url

    Client->>Customer: Redirect to 3DS page
    Customer->>Bank: Complete 3DS Challenge
    Bank-->>Hyperswitch: Authentication Result

    Note over Hyperswitch: Resume Payment Processing

    Hyperswitch-->>Client: Status: succeeded
 
```

**Additional Fields:**

* `authentication_type: "three_ds"`

**Status Progression:** `processing` → `requires_customer_action` → `succeeded`

Read more: [here](https://docs.hyperswitch.io/~/revisions/9QlGypixZFcbkq8oGjaF/explore-hyperswitch/workflows/3ds-decision-manager)

### Recurring Payments and Payment Storage

#### 1. Saving Payment Methods

**During Payment Creation:**

* Add `setup_future_usage: "off_session"` or `"on_session"`
* Include `customer_id`
* **Result:** `payment_method_id` returned on success

**Understanding `setup_future_usage`:**

* **`on_session`**: Use when the customer is actively present during the transaction. This is typical for scenarios like saving card details for faster checkouts in subsequent sessions where the customer will still be present to initiate the payment (e.g., card vaulting for e-commerce sites).
* **`off_session`**: Use when you intend to charge the customer later without their active involvement at the time of charge. This is suitable for subscriptions, recurring billing, or merchant-initiated transactions (MITs) where the customer has pre-authorized future charges.

#### 2. Using Saved Payment Methods

<figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

**Steps:**

1. **Initiate:** Create payment with `customer_id`
2. **List:** Get saved cards via `GET /customers/payment_methods`
3. **Confirm:** Use selected `payment_token` in confirm call

#### PCI Compliance and `payment_method_id`

Storing `payment_method_id` (which is a token representing the actual payment instrument, which could be a payment token, network token, or payment processor token) significantly reduces your PCI DSS scope. Hyperswitch securely stores the sensitive card details and provides you with this token. While you still need to ensure your systems handle `payment_method_id` and related customer data securely, you avoid the complexities of storing raw card numbers. Always consult with a PCI QSA to understand your specific compliance obligations.

### Recurring Payment Flows

#### 3. Customer-Initiated Transaction (CIT) Setup

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

Read more: [here](https://docs.hyperswitch.io/~/revisions/j00Urtz9MpwPggJzRCsi/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments)

#### 4. Merchant-Initiated Transaction (MIT) Execution

<figure><img src="../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

Read more: [here](https://docs.hyperswitch.io/~/revisions/j00Urtz9MpwPggJzRCsi/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments)

### Status Flow Summary

<figure><img src="../../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

### Notes

* **Terminal States:** `succeeded`, `failed`, `cancelled`, `partially_captured` are terminal states requiring no further action
* **Capture Methods:** System supports `automatic` (funds captured immediately), `manual` (funds captured in a separate step), `manual_multiple` (funds captured in multiple partial amounts via separate steps), and `scheduled` (funds captured automatically at a future predefined time) capture methods.
* **Authentication:** 3DS authentication automatically resumes payment processing after customer completion
* **MIT Compliance:** Off-session recurring payments follow industry standards for merchant-initiated transactions
