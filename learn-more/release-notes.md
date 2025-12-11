---
description: >-
  This page is a central archive of Hyperswitch release notes. It summarises
  recent product updates.
---

# Release Notes

Hyperswitch is a fast-moving open source payments orchestration platform. We ship improvements across routing, vaulting, reconciliation, connectors, SDKs, and developer experience.

This page serves as a central place to track what is shipping in Hyperswitch.

These release notes help you:

1. Understand what is new or improved across Hyperswitch.
2. Track connector and SDK updates in one place.
3. Follow product evolution across core orchestration, routing, vault, reconciliation, and customer capabilities.
4. Stay aligned with ongoing improvements in reliability and developer experience.

With these sections:

1. Connector expansions and enhancements
2. Customer and access management
3. Routing and core improvements<br>

<details>

<summary>December 1st - 5th, 2025</summary>

Highlights

1. Expanded Google Pay support across Worldpay and Stripe.
2. Added new voucher, recurring, and webhook capabilities across key connectors.
3. Improved customer sharing and API key authentication foundations for multi merchant setups.
4. Enriched payments data for better tracking, reporting, and operational clarity.

#### Connector expansions and enhancements

1. Worldpay: expanded Google Pay support and added payment and refund webhooks across WPG and XML variants ([#10460](https://github.com/juspay/hyperswitch/pull/10460), [#10496](https://github.com/juspay/hyperswitch/pull/10496))
2. Stripe: added Google Pay support via Stripe Connect and improved metadata handling for cleaner reporting ([#10466](https://github.com/juspay/hyperswitch/pull/10466), [#10537](https://github.com/juspay/hyperswitch/pull/10537))
3. Dlocal: added OXXO voucher support ([#10450](https://github.com/juspay/hyperswitch/pull/10450))
4. Mollie and ACH: expanded recurring and capture support ([#10408](https://github.com/juspay/hyperswitch/pull/10408), [#10412](https://github.com/juspay/hyperswitch/pull/10412))
5. Connector customer experience: introduced a standard Connector Customer Flow with optional billing address support ([#10499](https://github.com/juspay/hyperswitch/pull/10499))
6. Dwolla and Tesouro: improved error and mandate handling for smoother wallet and bank flow reliability ([#10344](https://github.com/juspay/hyperswitch/pull/10344), [#10351](https://github.com/juspay/hyperswitch/pull/10351))
7. Loonio and Gigadat: connector field standardisation for improved consistency across integrations ([#10516](https://github.com/juspay/hyperswitch/pull/10516))

#### Customer and access management

1. Implemented a customer sharing model and refactored API key authentication ([#10387](https://github.com/juspay/hyperswitch/pull/10387))

#### Routing and core improvements

1. Added captured amount in payment attempts and a modified at field in the Payments List response ([#10498](https://github.com/juspay/hyperswitch/pull/10498), [#10492](https://github.com/juspay/hyperswitch/pull/10492))
2. Enabled conditional storage of encrypted payment method data for sensitive additional details ([#10484](https://github.com/juspay/hyperswitch/pull/10484))
3. Added field type support for gift card number and CVC version 2 ([#10433](https://github.com/juspay/hyperswitch/pull/10433))
4. Propagated payment method type and subtype to split payment attempts version 2 ([#10443](https://github.com/juspay/hyperswitch/pull/10443))
5. Updated payout intent handling in webhook scenarios ([#10531](https://github.com/juspay/hyperswitch/pull/10531))
6. Added configuration support to disable pre routing for specific payment methods and types ([#10470](https://github.com/juspay/hyperswitch/pull/10470))
7. Reverted the error reason field change in PaymentsResponse to keep responses consistent with current expectations ([#10455](https://github.com/juspay/hyperswitch/pull/10455))

</details>
