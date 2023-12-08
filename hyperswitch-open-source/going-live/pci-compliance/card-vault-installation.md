---
description: Introducing the Hyperswitch card vault
---

# 🗄 Hyperswitch Card Vault

{% hint style="info" %}
This section will guide you to set up your own secure card vault from scratch
{% endhint %}

The Hyperswitch Card Vault [(Repo Link)](https://github.com/juspay/tartarus), is a highly performant and a secure locker to save sensitive data such as payment card details, bank account details etc.&#x20;

It is designed in an polymorphic manner to handle and store any type of sensitive information making it highly scalable with extensive coverage of payment methods and processors.

Tartarus is built with a GDPR compliant personal identifiable information (PII) storage and  secure encryption algorithms to be fully compliant with PCI DSS requirements.

## How does it work?

<figure><img src="../../../.gitbook/assets/general-block-diagram.png" alt=""><figcaption><p>Locker usage flow</p></figcaption></figure>

* The Hyperswitch application communicates with Tartarus via a middleware.&#x20;
* All requests and responses to and from the middleware are signed and encrypted with the JWS and JWE algorithms.&#x20;
* The locker supports CRD APIs on the /data and /cards endpoints - [API Reference](https://api-reference.hyperswitch.io/api-reference/cards/add-data-in-locker)
* Cards are stored against the combination of merchant and customer identifiers.&#x20;
* Internal hashing checks are in place to avoid data duplication.&#x20;

## Key Hierarchy

Master Key - AES generated key to that is encrypted/decrypted by the custodian keys to run the locker and associated configurations.

Custodian Keys - AES generated key that is used to encrypt and decrypt the master key. It broken into two keys (`key 1` and `key 2`) and available with two custodians to enhance security.

<figure><img src="../../../.gitbook/assets/locker-key-hierarchy.png" alt=""><figcaption><p>Key Hierarchy of Tartarus</p></figcaption></figure>

## Setting up your Card Vault

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td>Automated Script to Deploy - Standalone</td><td></td><td></td><td><a href="../../deploy-hyperswitch-on-aws/component-wise-deployment/deploy-card-vault.md">deploy-card-vault.md</a></td><td><a href="../../../.gitbook/assets/aws.jpg">aws.jpg</a></td></tr><tr><td>Manual Setup - Cloud (AWS)</td><td></td><td></td><td><a href="../../deploy-hyperswitch-on-aws/component-wise-deployment/deploy-card-vault/manual-setup.md">manual-setup.md</a></td><td><a href="../../../.gitbook/assets/aws.jpg">aws.jpg</a></td></tr><tr><td>Automated Script to Deploy - Fullstack (along with other  components of Hyperswitch)</td><td></td><td></td><td><a href="../../deploy-hyperswitch-on-aws/full-stack-deployment/">full-stack-deployment</a></td><td><a href="../../../.gitbook/assets/aws.jpg">aws.jpg</a></td></tr></tbody></table>

###
