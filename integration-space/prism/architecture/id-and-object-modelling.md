---
description: >-
  Understand Hyperswitch Prism's standardized ID patterns to manage transaction
  references across payment processors
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/prism/architecture/id-and-object-modelling
---

# ID and Object Modelling

The whole complexity in payment integrations exists because all payment processors could not agree on how to name their IDs and how many IDs are needed to process a payment. To add to this complexity:

* Some processors use the ID you pass as the primary reference, whereas other processors generate their own primary IDs
* Some processors also provide upstream IDs (from issuer, acquirer, etc.) to enable merchants with more granular information of the transaction flow

This inconsistency breaks code completion, confuses LLMs, and forces you to maintain different ID handling logic for every connector—whether to send an ID or expect the connector to create its own ID.

Hyperswitch Prism is a stateless service, so it does not create any new IDs. But the important aspect is that Hyperswitch Prism solves the ID problem with a well-solidified grammar in the interface that uses strongly typed, self-describing identifiers regardless of the underlying processor, network, issuer, or any other entity.

## Modelling IDs with clear pattern

The interface of Hyperswitch Prism always uses typed IDs with a consistent format: `entity_domain_id`. So developers using the interface shall have clarity, and all the processor complexity is handled behind the scenes.

### What is Entity?

The stakeholder/system that owns the generation of the ID. Let's see how a transaction ID is spread across multiple entities in a transaction lifecycle.

| Entity        | Prism Field                | Who Generates                     | Purpose                                               |
| ------------- | -------------------------- | --------------------------------- | ----------------------------------------------------- |
| **Merchant**  | `merchant_transaction_id`  | You (the merchant)                | Your internal reference for a particular transaction  |
| **Connector** | `connector_transaction_id` | Payment processor (Stripe, Adyen) | Processor's reference for the transaction             |
| **Acquirer**  | `acquirer_transaction_id`  | Acquiring bank                    | Bank-level reference for settlement                   |
| **Network**   | `network_transaction_id`   | Card network (Visa, Mastercard)   | Network-level trace for disputes and chargebacks      |
| **Issuer**    | `issuer_transaction_id`    | Cardholder's bank                 | Issuing bank's reference for the cardholder statement |

### What is Domain

The domain in which the ID should be interpreted. Below are the reference ID fields from the perspective of a single entity (merchant) but across domains.

| Domain               | Prism Field               | Use Case                                 |
| -------------------- | ------------------------- | ---------------------------------------- |
| **Payment**          | `merchant_transaction_id` | Your reference for a payment transaction |
| **Order**            | `merchant_order_id`       | Your order reference for the payment     |
| **Refund**           | `merchant_refund_id`      | Your reference for a refund              |
| **Recurring Charge** | `merchant_charge_id`      | Your reference for recurring payments    |
| **Event**            | `merchant_event_id`       | Your reference for webhook events        |

Your ID handling becomes simple, safe, and portable across all connectors, if you use and persist the same terminology in your payment system.
