---
description: Here's what you'll need to get production ready!
---

# 🚀 Overview

{% hint style="info" %}
This chapter will give you an overview of everything you would need for going live with your cloud setup&#x20;
{% endhint %}

***

## Go live checklist:

### Monitoring

* [ ] Make sure logs are being printed for all components in your setup
* [ ] Aggregate your logs across instances and [setup a logging system](monitoring.md) (e.g. Grafana Loki) for storing and viewing your logs
* [ ] Make sure your metrics pipeline is setup and provides visibility into both application and system performance

### PCI Compliance

* [ ] Make sure your system is meeting the PCI compliance requirements for your business
* [ ] If you are storing card data make sure your [card vault is set up](pci-compliance/card-vault-installation.md) as per our instructions

### Security

* [ ] Keep the system hidden from external access; instead, use a front-end system or a reverse proxy as a protective layer in front of it
* [ ] Make sure to follow our [security guidelines](security.md) for various components in your set up

### Integrate with your app

* [ ] Make sure your API keys are not exposed on the front-end (website/mobile app)
* [ ] Avoid duplication or storage of your API keys in multiple locations
* [ ] Test your integration and make sure all scenarios in the payments lifecycle is handled
* [ ] Make sure your application (Frontend/Backend) is set up to handle all the possible error scenarios
* [ ] Keep track of new releases/bug fixes and make sure to [keep your system updated](updates.md)

### Infra

* [ ] Make sure DB and Redis connections are properly configured
* [ ] Load test your setup and provision resources according to the expected traffic
* [ ] In case you have whitelisting for outgoing request endpoints, make sure to whitelist the required processor endpoints
