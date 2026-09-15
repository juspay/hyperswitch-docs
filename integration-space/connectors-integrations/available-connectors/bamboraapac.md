---
description: Bambora Asia-Pacific has been decommissioned. The connector no longer processes payments.
metaLinks:
  alternates:
    - bamboraapac.md
---

# Bambora Asia-Pacific

{% hint style="danger" %}
**Decommissioned.** Bambora decommissioned its Asia-Pacific platform in September 2025. The Hyperswitch Bambora Asia-Pacific connector can no longer process payments, and you should not configure it for new or existing traffic.
{% endhint %}

### Status

Bambora announced that the Bambora Asia-Pacific platform would be decommissioned as of September 2025; see the notice on the [Bambora Asia-Pacific developer site](https://dev-apac.bambora.com/support/guides/getting-help/contact-us) and the [Bambora decommissioning FAQs](https://support-apac.bambora.com/hc/en-au/sections/6008611698831-Bambora-decommissioning-FAQs). For questions about the decommissioning, Bambora directs merchants to BamboraAUFAQ@worldline.com.

The connector is still present in Hyperswitch, but the API hosts it is configured to call no longer exist: requests to the [production endpoint](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/production.toml#L48) (`www.bambora.co.nz`) and the [sandbox endpoint](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/sandbox.toml#L48) (`demo.ippayments.com.au`) fail because neither hostname resolves. Payments, captures, refunds, syncs, and mandate setup routed to this connector will fail.

Removing the connector from Hyperswitch is being discussed. This page will be removed when the connector is.

### What to do

- If you have a Bambora Asia-Pacific connector configured, route its traffic to another connector and disable it.
- Do not create new Bambora Asia-Pacific connector accounts.
- The [Bambora](bambora.md) connector is a separate integration that calls a different API ([`api.na.bambora.com`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/production.toml#L47)) and is not covered by this notice.
