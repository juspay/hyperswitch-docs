---
icon: gift
---

# For SaaS Setup

Refer to this checklist for a seamless transition as you prepare to go live with your integration.

{% hint style="warning" %}
The connector configurations set up in the sandbox need to be replicated on the Hyperswitch production account.
{% endhint %}

### [​](https://api-reference.hyperswitch.io/essentials/go-live#signing-of-hyperswitch-services-agreement)Signing of Hyperswitch services agreement <a href="#signing-of-hyperswitch-services-agreement" id="signing-of-hyperswitch-services-agreement"></a>

* [ ] &#x20;Ensure that the Hyperswitch services agreement is signed and shared with the Hyperswitch team. In case you need any help, please drop an email to [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in)

{% hint style="warning" %}
The Hyperswitch team will share your production Hyperswitch credentials once the above process is completed.
{% endhint %}

{% hint style="success" %}
If you are using our SDK, pci compliance is automatically taken care of.
{% endhint %}

### [​](https://api-reference.hyperswitch.io/essentials/go-live#connector-configurations)Connector Configurations <a href="#connector-configurations" id="connector-configurations"></a>

* [ ] &#x20;Configure all the required connectors using production credentials on the Hyperswitch production dashboard and enable the required payment methods.
* [ ] &#x20;Ensure that the payment methods are enabled on the connector (payment processor) dashboard.
* [ ] &#x20;Enable raw card processing for each connector. Some connectors offer this as a dashboard toggle feature. Some processors might need you to share a PCI Attestation of Compliance over email to enable this.&#x20;

{% hint style="info" %}
To access the PCI Attestation of Compliance (AOC) document on Hyperswitch, simply navigate to the Compliance section under settings in the Hyperswitch Dashboard. If you need further assistance, you can also email at [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in)
{% endhint %}

### [​](https://api-reference.hyperswitch.io/essentials/go-live#secure-your-api-keys)Secure your api-keys <a href="#secure-your-api-keys" id="secure-your-api-keys"></a>

* [ ] &#x20;Make sure your secret key (api-key) is not exposed on the front-end (website/mobile app).
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
