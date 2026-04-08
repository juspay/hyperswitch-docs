# Payout Service Overview

## Overview

The Payout Service enables you to send funds to recipients using the Node.js SDK. Use this for marketplace payouts, refunds to bank accounts, supplier payments, and other fund disbursement needs.

**Business Use Cases:**

* **Marketplace payouts** - Pay sellers/merchants on your platform
* **Supplier payments** - Disburse funds to vendors and suppliers
* **Payroll** - Employee and contractor payments
* **Instant payouts** - Same-day transfers to connected accounts

## Operations

| Operation                                                                            | Description                                                                | Use When                               |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------------------- |
| [`create`](prism/sdks/node/payout-service/create.md)                                 | Create a payout. Initiates fund transfer to recipient.                     | Sending money to a recipient           |
| [`transfer`](prism/sdks/node/payout-service/transfer.md)                             | Create a payout fund transfer. Move funds between accounts.                | Transferring between internal accounts |
| [`get`](prism/sdks/node/payout-service/get.md)                                       | Retrieve payout details. Check status and tracking.                        | Monitoring payout progress             |
| [`void`](prism/sdks/node/payout-service/void.md)                                     | Cancel a pending payout. Stop before processing.                           | Aborting an incorrect payout           |
| [`stage`](prism/sdks/node/payout-service/stage.md)                                   | Stage a payout for later processing. Prepare without sending.              | Delayed payouts, batch processing      |
| [`createLink`](prism/sdks/node/payout-service/create-link.md)                        | Create link between recipient and payout. Associate payout with recipient. | Setting up recipient relationships     |
| [`createRecipient`](prism/sdks/node/payout-service/create-recipient.md)              | Create payout recipient. Store recipient bank/payment details.             | First time paying a new recipient      |
| [`enrollDisburseAccount`](prism/sdks/node/payout-service/enroll-disburse-account.md) | Enroll disburse account. Set up account for payouts.                       | Onboarding new payout accounts         |

## SDK Setup

```javascript
const { PayoutClient } = require('hyperswitch-prism');

const payoutClient = new PayoutClient({
    connector: 'stripe',
    apiKey: 'YOUR_API_KEY',
    environment: 'SANDBOX'
});
```

## Payout Methods

| Method               | Speed             | Typical Use                         |
| -------------------- | ----------------- | ----------------------------------- |
| **Bank transfer**    | 1-3 business days | Standard payouts, large amounts     |
| **Instant transfer** | Minutes           | Same-day needs, existing recipients |
| **Card payout**      | Instant           | Prepaid cards, debit cards          |

## Next Steps

* [createRecipient](prism/sdks/node/payout-service/create-recipient.md) - Set up your first recipient
* [create](prism/sdks/node/payout-service/create.md) - Send your first payout
* [Event Service](event-service-1.md) - Handle payout webhooks
