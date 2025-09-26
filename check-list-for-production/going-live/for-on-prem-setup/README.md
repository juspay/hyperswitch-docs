---
icon: clipboard-question
---

# For On-Prem Setup

## Prerequisites

In order to use Hyperswitch for accepting digital payments through a consumer facing website or mobile application there are three main prerequisites

<table data-header-hidden><thead><tr><th width="187"></th><th></th></tr></thead><tbody><tr><td>Resources</td><td><ul><li>Account with cloud service provider (AWS/ GCP/Own Cloud) to host Hyperswitch application</li><li>Contractual relationship and active processing account with payment processor or acquirer (this will be in the form of API keys or merchant identifier)</li></ul></td></tr><tr><td>Technical Know How</td><td><ul><li>For deploying and managing application using Kubernetes</li><li>Handling a Web application written in Rust using Postgres (primary datastore), Redis (distributed key-value store for cached lookups), Prometheus/Grafana (monitoring), S3/CDN (serving static files)</li></ul></td></tr><tr><td>Ensuring Compliance </td><td><p><a href="pci-compliance/its-no-rocket-science.md">Refer here</a> to find out which level of PCI compliance applies to your business.</p><ul><li><strong>Report on Compliance (ROC):</strong> Engage an independent third-party Qualified Security Assessor (QSA) certified by the PCI-SSC to perform the PCI audit and share the findings. The ROC will be prepared by the QSA at the end of the PCI compliance activity. <em>This is required only if your online business processes greater than 1 million card transactions per annum.</em></li></ul><ul><li><strong>Quarterly Network scans:</strong> Engage an <a href="https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors">Approved Scanning Vendor</a> for conducting quarterly network scans and submitting the scan reports to the payment processor/ acquirer</li></ul><ul><li><strong>Self Assessment Questionnaire (SAQ):</strong> This is an assessment which can be self-completed by a business without engaging an Independent PCI Auditor, <em>if your business processes less than 1 million card transactions per annum</em>. A person responsible for the payment infrastructure within your organization fills out the SAQ. This could be the stakeholder who is the closest to your payment infrastructure - your Dev Ops Manager, or Information Security Officer, or CTO.</li></ul></td></tr></tbody></table>

Here's a quick summary of everything you would need for going live with Hyperswitch:

### Security

* [ ] Keep the system hidden from external access; instead, use a front-end system or a reverse proxy as a protective layer in front of it.
* [ ] Make sure to follow our [security guidelines](security.md) for various components in your set up.

### API Keys

* [ ] Change all the default values for all API key fields in the config file ( [Ref](https://github.com/juspay/hyperswitch-helm/tree/main/charts/incubator/hyperswitch-stack#app-server-secrets)). This applies whether you are using Helm charts or not.

### Apple Pay Certificate

* [ ] To enable Apple Pay payments, request the required certificate: `Hyperswitch-app.server.secrets.apple_pay_merchant_cert`. \
  Follow the official setup guide: [Apple Pay Setup](https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup/wallets/apple-pay/ios-application).

### Deploying the Application

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>On Kubernetes</strong></mark></td><td><a href="../../../hyperswitch-open-source/deploy-on-kubernetes-using-helm/">deploy-on-kubernetes-using-helm</a></td></tr><tr><td><mark style="color:blue;"><strong>On AWS</strong></mark></td><td><a href="../../../hyperswitch-open-source/deploy-hyperswitch-on-aws/">deploy-hyperswitch-on-aws</a></td></tr></tbody></table>

{% hint style="info" %}
The above installation guides include vault as well, but you will need to activate the vault by following the steps mentioned in [this guide](https://github.com/juspay/hyperswitch-helm/tree/main/charts/incubator/hyperswitch-stack#-step-1---deploy-card-vault).&#x20;
{% endhint %}

### Outgoing Proxy

* Set up an outgoing proxy outside the Kubernetes cluster for all external communication originating from the Hyperswitch application.
* Direct all outbound traffic through this proxy for monitoring and control purposes.

### Incoming Traffic Management

* Route incoming traffic to the Hyperswitch-server through an incoming proxy.
* This proxy should handle traffic filtering(WAF), rate limiting, request validation, and integration with DDoS protection services before traffic reaches the Kubernetes cluster.

{% hint style="warning" %}
Hyperswitch does not share card BIN data automatically. BIN (Bank Identification Number) data helps identify the card issuer, card type, and country of issuance. This is available as an add-on service. Reach out to us at [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in) to access.
{% endhint %}

### Monitoring

* [ ] Make sure logs are being printed for all components in your setup
* [ ] Aggregate your logs across instances and [setup a logging system](monitoring.md) (e.g. Grafana Loki) for storing and viewing your logs
* [ ] Make sure your metrics pipeline is setup and provides visibility into both application and system performance

### PCI Compliance

* [ ] Make sure your system is meeting the PCI compliance requirements for your business
* [ ] If you are storing card data make sure your [card vault is set up](https://github.com/juspay/hyperswitch-helm/tree/main/charts/incubator/hyperswitch-stack#-step-1---deploy-card-vault) as per our instructions.

### Connector Configurations <a href="#connector-configurations" id="connector-configurations"></a>

* [ ] &#x20;Configure all the required connectors using production credentials on the Hyperswitch production dashboard and enable the required payment methods.
* [ ] &#x20;Ensure that the payment methods are enabled on the connector (payment processor) dashboard.
* [ ] &#x20;Enable raw card processing for each connector. Some connectors offer this as a dashboard toggle feature. Some processors might need you to share a PCI Attestation of Compliance over email to enable this.&#x20;

{% hint style="info" %}
To access the PCI Attestation of Compliance (AOC) document on Hyperswitch, simply navigate to the Compliance section under settings in the Hyperswitch Dashboard. If you need further assistance, you can also email at [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in)
{% endhint %}

### Integrate with your app

* [ ] Make sure your API keys are not exposed on the front-end (website/mobile app)
* [ ] Avoid duplication or storage of your API keys in multiple locations
* [ ] Test your integration and make sure all scenarios in the payments lifecycle is handled
* [ ] Make sure your application (Frontend/Backend) is set up to handle all the [possible error scenarios](https://juspay-78.mintlify.app/essentials/error_codes)
* [ ] Keep track of new releases/bug fixes and make sure to [keep your system updated](updates.md)

### [​](https://api-reference.hyperswitch.io/essentials/go-live#secure-your-api-keys)Secure your api-keys <a href="#secure-your-api-keys" id="secure-your-api-keys"></a>

* [ ] &#x20;Make sure your [secret key](https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles/account-setup#user-content-create-an-api-key-1) (api-key) is not exposed on the front-end (website/mobile app).
* [ ] &#x20;Ensure that your workflow avoids the duplication or storage of your API keys in multiple locations.

### [​](https://api-reference.hyperswitch.io/essentials/go-live#set-up-webhooks)Set up Webhooks <a href="#set-up-webhooks" id="set-up-webhooks"></a>

* [ ] &#x20;[Configure your webhook endpoint](https://juspay-78.mintlify.app/essentials/webhooks#configuring-webhooks) on our dashboard to receive notifications for different events.
* [ ] &#x20;Update Hyperswitch’s webhook endpoints on your connector’s Dashboard. [Refer here](https://juspay-78.mintlify.app/essentials/webhooks#configuring-webhooks) for detailed instructions.
* [ ] &#x20;Update the connector secret key in our dashboard for us to authenticate webhooks sent by your connector.

### [​](https://api-reference.hyperswitch.io/essentials/go-live#secure-your-payments)Secure your Payments <a href="#secure-your-payments" id="secure-your-payments"></a>

* [ ] &#x20;Make sure you decrypt and verify the signed payload sent along with the payment status in your return URL.
* [ ] &#x20;Always verify the payment amount and payment status before fulfilling your customer’s shopping cart/service request.

### [​](https://api-reference.hyperswitch.io/essentials/go-live#error-handling)Error Handling <a href="#error-handling" id="error-handling"></a>

* [ ] &#x20;Make sure your API integration is set up to handle all the possible error scenarios (refer this [link](https://juspay-78.mintlify.app/essentials/error_codes)).
* [ ] &#x20;Ensure your Unified Checkout (SDK) integration is set up to handle all the possible error scenarios (refer this [link](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/errorCodes)).
* [ ] &#x20;Ensure that your integration can handle the entire payments lifecycle and test various scenarios using actual payment details.

{% hint style="warning" %}
For more details, kindly refer to the [state machine diagrams](https://docs.hyperswitch.io/learn-more/payment-flows).&#x20;
{% endhint %}

### [​](https://api-reference.hyperswitch.io/essentials/go-live#customize-and-sanity-check-the-payment-experience)Customize and sanity check the payment experience <a href="#customize-and-sanity-check-the-payment-experience" id="customize-and-sanity-check-the-payment-experience"></a>

* [ ] &#x20;Ensure the pay button is properly highlighted to the customer.
* [ ] &#x20;Ensure a blended look and feel of the payment experience using the [styling APIs](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/customization) of Unified Checkout.

{% hint style="success" %}
You are good to go to run Hyperswitch in production and provide your customers with a safe, reliable, and smooth payment experience.
{% endhint %}
