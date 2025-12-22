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

<details>

<summary>December 6th - 12th, 2025</summary>

Highlights

1. Expanded Worldpay WPG coverage across cards, Apple Pay, 3DS, and payouts.
2. Added mandates, transaction codes, and reliability fixes across Airwallex, Zift, Volt, Peach Payments, Fiserv, Authorize.Net, Gigadat, Payload, and more.
3. Strengthened platform-connected setups with publishable key authentication, shared payment methods, and better tracking for platform-originated payments.
4. Improved payouts, revenue recovery, and routing resilience with new APIs, safer webhooks, and smarter retry behaviour.

#### Connector expansions and enhancements

1. Worldpay WPG: expanded support for card and Apple Pay payout decryption and added 3DS flows for cards, along with improved reference mapping for Worldpay requests ([#10545](https://github.com/juspay/hyperswitch/pull/10545), [#10442](https://github.com/juspay/hyperswitch/pull/10442), [#10482](https://github.com/juspay/hyperswitch/pull/10482), [#10503](https://github.com/juspay/hyperswitch/pull/10503))
2. Airwallex and Zift: added mandate support for Airwallex and introduced transaction\_code support across Zift payment flows, improving traceability and mandate coverage in those integrations ([#10431](https://github.com/juspay/hyperswitch/pull/10431), [#10581](https://github.com/juspay/hyperswitch/pull/10581))
3. Adyen and Peach Payments: made `shopper_reference` optional for on-session Adyen payments and corrected the production base URL for Peach Payments, reducing configuration friction and integration errors ([#10520](https://github.com/juspay/hyperswitch/pull/10520), [#10631](https://github.com/juspay/hyperswitch/pull/10631))
4. Volt, Payload, and VGS vault: refactored the Volt connector to a new API contract, fixed the production URL for Volt refund flows, and improved Payload’s RSync handling so 404s reuse shared utilities. Updated the VGS vault connector configuration for more predictable behaviour ([#9928](https://github.com/juspay/hyperswitch/pull/9928), [#10619](https://github.com/juspay/hyperswitch/pull/10619), [#10542](https://github.com/juspay/hyperswitch/pull/10542), [#10540](https://github.com/juspay/hyperswitch/pull/10540))
5. Fiserv, Authorize.Net, and Gigadat: hardened connector reliability by fixing Fiserv response deserialization, correcting double serialization of `user_fields` and removing an obsolete `authorization_indicator_type` in Authorize.Net, and enforcing stricter typing and masking for Gigadat webhook payloads ([#10124](https://github.com/juspay/hyperswitch/pull/10124), [#10609](https://github.com/juspay/hyperswitch/pull/10609), [#10633](https://github.com/juspay/hyperswitch/pull/10633))
6. Stripe: added direct charges support for Apple Pay, broadening wallet coverage for Stripe integrations ([#10577](https://github.com/juspay/hyperswitch/pull/10577))
7. Metadata handling: ensured metadata values are serialised so that all fields are passed through correctly across connectors ([#10568](https://github.com/juspay/hyperswitch/pull/10568))

#### Customer and access management

1. Platform-connected setups: implemented a platform-connected setup for publishable key authentication and a payment method sharing model for platform-connected environments, plus support for a tracker on platform-originated payment create flows ([#10475](https://github.com/juspay/hyperswitch/pull/10475), [#10458](https://github.com/juspay/hyperswitch/pull/10458), [#10465](https://github.com/juspay/hyperswitch/pull/10465))
2. Payment links governance: added verification for payment method mapping when using custom T\&C in payment links and reverted a previous restriction that disallowed custom T\&C when using Hyperswitch-hosted domains, restoring flexibility while keeping mappings consistent ([#10562](https://github.com/juspay/hyperswitch/pull/10562), [#10616](https://github.com/juspay/hyperswitch/pull/10616))

#### Routing and core improvements

1. Payouts resilience and reporting: implemented a Payouts Aggregate API, fixed a concurrency issue in payout webhooks, and backfilled the payouts table where `organization_id` was null to keep payout data and processing consistent. Also introduced task segregation in the scheduler based on application source for clearer operational boundaries ([#10559](https://github.com/juspay/hyperswitch/pull/10559), [#10523](https://github.com/juspay/hyperswitch/pull/10523), [#10210](https://github.com/juspay/hyperswitch/pull/10210), [#10505](https://github.com/juspay/hyperswitch/pull/10505))
2. Revenue recovery and authorisation: enabled multiple retries for partially charged payments and fixed partial authorisation retries for smart flows, improving recovery rates and reducing manual follow-ups ([#9818](https://github.com/juspay/hyperswitch/pull/9818), [#10564](https://github.com/juspay/hyperswitch/pull/10564))
3. Payment data quality: started consuming cardholder name in payment method batch migrations and converted Merchant Category Code (MCC) handling to a strict struct type, improving downstream categorisation and reporting quality ([#10551](https://github.com/juspay/hyperswitch/pull/10551), [#10423](https://github.com/juspay/hyperswitch/pull/10423))
4. Request and auth flows: added support for passing access tokens across CreateOrder, Capture, and Void calls, and introduced configurable granular preprocessing for connectors that need heavier authentication flows, giving platforms more control over how requests are prepared ([#10582](https://github.com/juspay/hyperswitch/pull/10582), [#10567](https://github.com/juspay/hyperswitch/pull/10567))
5. Customer experience in routing: exposed an `is_guest_customer` flag in the payment method list response to help distinguish guest checkout behaviour in downstream systems ([#10598](https://github.com/juspay/hyperswitch/pull/10598))

</details>
