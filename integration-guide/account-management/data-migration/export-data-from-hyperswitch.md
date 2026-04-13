---
description: >-
  Learn how to safely export your payment data from Hyperswitch to a PCI-DSS
  compliant payment processor.
icon: left-from-bracket
metaLinks:
  alternates:
    - export-data-from-hyperswitch.md
---

# Data Migration From Hyperswitch

We believe customers fully own their data. If you decide to export data from Hyperswitch, we will work with your new payment service provider to safely export your data.

{% hint style="info" %}
To meet PCI compliance requirements, Hyperswitch can export data only to a PCI-DSS compliant payment processor. Kindly request your new payment processor's PCI Attestation of Compliance (AoC) certificate, and share it to [support.global@juspay.io](mailto:support.global@juspay.io) while requesting your data export.
{% endhint %}

## Performing the Export Process

1. Merchant requests a data export by sharing the PCI-AoC certificate of their new payment service provider.
2. Once approved by our security team, we will request the new payment service provider's PGP public encryption key.
3. We will use the public key to encrypt the sensitive data for export.
4. The PGP-encrypted CSV file will be transferred via SFTP to your new payment service provider.

It is the responsibility of your new payment service provider to protect their private key file in accordance with PCI DSS compliance.
