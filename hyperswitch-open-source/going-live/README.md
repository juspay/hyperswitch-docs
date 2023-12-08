---
description: Overview of everything you would need for going live
---

# 🚀 Going live

{% hint style="info" %}
This chapter will give you an overview of everything you would need for going live with your cloud setup&#x20;
{% endhint %}

***

## Prerequisites

In order to user Hyperswitch for accepting digital payments through a consumer facing website or mobile application there are three main prerequisites

<table data-header-hidden><thead><tr><th width="187"></th><th></th></tr></thead><tbody><tr><td>Resources</td><td><ul><li>Account with cloud service provider (AWS/ GCP) to host Hyperswitch application</li><li>Contractual relationship and active processing account with payment processor or acquirer (this will be in the form of API keys or merchant identifier)</li></ul></td></tr><tr><td>Technical Know How</td><td><ul><li>For deploying and managing application using Kubernetes</li><li>Handling a Web application written in Rust using Postgres (primary datastore), Redis (distributed key-value store for cached lookups), Prometheus/Grafana (monitoring), S3/CDN (serving static files)</li></ul></td></tr><tr><td>Ensuring Compliance </td><td><p><a href="pci-compliance/its-no-rocket-science.md">Refer here</a> to find out which level of PCI compliance applies to your business.</p><ul><li><strong>Report on Compliance (ROC):</strong> Engage an independent third-party Qualified Security Assessor (QSA) certified by the PCI-SSC to perform the PCI audit and share the findings. The ROC will be prepared by the QSA at the end of the PCI compliance activity. <em>This is required only if your online business processes greater than 1 million card transactions per annum.</em></li></ul><ul><li><strong>Quarterly Network scans:</strong> Engage an <a href="https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors">Approved Scanning Vendor</a> for conducting quarterly network scans and submitting the scan reports to the payment processor/ acquirer</li></ul><ul><li><strong>Self Assessment Questionnaire (SAQ):</strong> This is an assessment which can be self-completed by a business without engaging an Independent PCI Auditor, <em>if your business processes less than 1 million card transactions per annum</em>. A person responsible for the payment infrastructure within your organization fills out the SAQ. This could be the stakeholder who is the closest to your payment infrastructure - your Dev Ops Manager, or Information Security Officer, or CTO.</li></ul></td></tr></tbody></table>

## Go live checklist:

Here's a quick summary of everything you would need for going live with Hyperswitch:

### Monitoring

* [ ] Make sure logs are being printed for all components in your setup
* [ ] Aggregate your logs across instances and [setup a logging system](monitoring.md) (e.g. Grafana Loki) for storing and viewing your logs
* [ ] Make sure your metrics pipeline is setup and provides visibility into both application and system performance

### PCI Compliance

* [ ] Make sure your system is meeting the PCI compliance requirements for your business
* [ ] If you are storing card data make sure your [card vault is set up](pci-compliance/hyperswitch-card-vault.md) as per our instructions

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
