---
description: Process one-time and recurring payments with multiple flow patterns
icon: vault
---

# Pay-Then-Vault

Juspay Hyperswitch provides flexible payment processing with multiple flow patterns to accommodate different business needs. The system supports one-time payments, saved payment methods, and recurring billing through a comprehensive API design.

{% hint style="info" %}
**Integration Path**

**Client-Side SDK Payments**

Refer to Payments (Cards) section if your flow requires the SDK to initiate payments directly. In this model, the SDK handles the payment trigger and communicates downstream to the Hyperswitch server and your chosen Payment Service Providers (PSPs). This path is ideal for supporting dynamic, frontend-driven payment experiences.
{% endhint %}

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-5488973c66c60d28c0d7cde47c7a479455933c64%252Fimage%2520%28167%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=913fa83b\&sv=2)

#### One-Time Payment Patterns <a href="#one-time-payment-patterns" id="one-time-payment-patterns"></a>

**1. Instant Payment (Automatic Capture)**

**Use Case:** Simple, immediate payment processing

**Endpoint:** `POST /payments`

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-e61ebf7b2846582278b74f9f2ab31ce1f21d3195%252Fimage%2520%28168%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=269ebedf\&sv=2)

**Required Fields:**

* `confirm: true`
* `capture_method: "automatic"`
* `payment_method`

**Final Status:** `succeeded`

**2. Two-Step Manual Capture**

**Use Case:** Deferred capture (e.g., ship before charging)

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-67e537f14bfd445467c8f272b90655f5dd9698fb%252Fimage%2520%28170%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=8f9f7e07\&sv=2)

**Flow:**

1. **Authorize:** `POST /payments` with `capture_method: "manual"`
2. **Status:** `requires_capture`
3. **Capture:** `POST /payments/{payment_id}/capture`
4. **Final Status:** `succeeded`

Read more - [here](https://docs.hyperswitch.io/~/revisions/2M8ySHqN3pH3rctBK2zj/about-hyperswitch/payment-suite-1/payments-cards/manual-capture)

**3. Fully Decoupled Flow**

**Use Case:** Complex checkout journeys with multiple modification steps. Useful in headless checkout or B2B portals where data is filled progressively.

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-a6c4453837660d02246bd75a346253e5c312c546%252Fimage%2520%28171%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=c1396971\&sv=2)

**Endpoints:**

* **Create:** `POST /payments`
* **Update:** `POST /payments/{payment_id}`
* **Confirm:** `POST /payments/{payment_id}/confirm`
* **Capture:** `POST /payments/{payment_id}/capture` (if manual)

**4. 3D Secure Authentication Flow**

**Use Case:** Enhanced security with customer authentication

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-c7fa93ddd123c9c4b969bb39f439f14df454a190%252Fimage%2520%28172%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=8b16bef6\&sv=2)

**Additional Fields:**

* `authentication_type: "three_ds"`

**Status Progression:** `processing` → `requires_customer_action` → `succeeded`

Read more - [link](https://docs.hyperswitch.io/~/revisions/9QlGypixZFcbkq8oGjaF/explore-hyperswitch/workflows/3ds-decision-manager)

#### Recurring payments and Payment storage <a href="#recurring-payments-and-payment-storage" id="recurring-payments-and-payment-storage"></a>

**1. Saving Payment Methods**

**During Payment Creation:**

* Add `setup_future_usage: "off_session"` or `"on_session"`
* Include `customer_id`
* **Result:** `payment_method_id` returned on success

**Understanding `setup_future_usage`:**

* **`on_session`**: Use when the customer is actively present during the transaction. This is typical for scenarios like saving card details for faster checkouts in subsequent sessions where the customer will still be present to initiate the payment (e.g., card vaulting for e-commerce sites).
* **`off_session`**: Use when you intend to charge the customer later without their active involvement at the time of charge. This is suitable for subscriptions, recurring billing, or merchant-initiated transactions (MITs) where the customer has pre-authorized future charges.

**2. Using Saved Payment Methods**

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-d82f0cc65ff2e569bb82711ec5ce86123a78542d%252Fimage%2520%28173%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=6698b515\&sv=2)

**Steps:**

1. **Initiate:** Create payment with `customer_id`
2. **List:** Get saved cards via `GET /customers/payment_methods`
3. **Confirm:** Use selected `payment_token` in confirm call

**PCI Compliance and `payment_method_id`**

Storing `payment_method_id` (which is a token representing the actual payment instrument, which could be a payment token, network token, or payment processor token) significantly reduces your PCI DSS scope. Hyperswitch securely stores the sensitive card details and provides you with this token. While you still need to ensure your systems handle `payment_method_id` and related customer data securely, you avoid the complexities of storing raw card numbers. Always consult with a PCI QSA to understand your specific compliance obligations.

#### Recurring Payment Flows <a href="#recurring-payment-flows" id="recurring-payment-flows"></a>

**3. Customer-Initiated Transaction (CIT) Setup**

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-abd9b3e7c0c1d24d61e4a99cd7586670841e1f3c%252Fimage%2520%28174%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=b6b295b\&sv=2)

Read more - [link](https://docs.hyperswitch.io/~/revisions/j00Urtz9MpwPggJzRCsi/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments)

**4. Merchant-Initiated Transaction (MIT) Execution**

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-cc0a650c7ce3f037c769bf94776a7c9dac0a08c9%252Fimage%2520%28175%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=844c48d4\&sv=2)

Read more - [link](https://docs.hyperswitch.io/~/revisions/j00Urtz9MpwPggJzRCsi/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments)

#### Status Flow Summary <a href="#status-flow-summary" id="status-flow-summary"></a>

![](https://sites.gitbook.com/preview/site_gbSsq/~gitbook/image?url=https%3A%2F%2F1943537505-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fkf7BGdsPkCw9nalhAIlE%252Fuploads%252Fgit-blob-d5398451bd689564978c796db3690c4dd3aae69a%252Fimage%2520%28179%29.png%3Falt%3Dmedia\&width=768\&dpr=3\&quality=100\&sign=e3226751\&sv=2)

#### Notes <a href="#notes" id="notes"></a>

* **Terminal States:** `succeeded`, `failed`, `cancelled`, `partially_captured` are terminal states requiring no further action
* **Capture Methods:** System supports `automatic` (funds captured immediately), `manual` (funds captured in a separate step), `manual_multiple` (funds captured in multiple partial amounts via separate steps), and `scheduled` (funds captured automatically at a future predefined time) capture methods.
* **Authentication:** 3DS authentication automatically resumes payment processing after customer completion
* **MIT Compliance:** Off-session recurring payments follow industry standards for merchant-initiated transactions

<br>
