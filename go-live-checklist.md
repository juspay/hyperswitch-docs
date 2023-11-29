# Go-live Checklist

> The connecotor configurations set up in sandbox, needs to be replicated on hyperswitch production account.

## Signing of Hyperswitch services agreement

* [ ] Ensure that Hyperswitch services agreement is signed and share with Hyperswitch team. In case you need any help, please drop an email to <mark style="color:blue;">biz@hyperswitch.io</mark>

> The hyperswitch team will share you production hyperswitch credentials once the above process is completed

## Connector Configurations

* [ ] Configure all the required connectors using production credentials on hyperswitch production dashboard and enable the required payment methods
* [ ] Ensure that the payment methods are enabled on connector (payment processor) dashboard
* [ ] Enable raw card processing for each connector. Some connectors offer this as a dashboard toggle feature. Some processors might need you share a PCI Attestation of Compliance over email to enable this. Drop an email to biz@hyperswitch.io if you need any support with PCI AOC

## Secure your api-keys

* [ ] Make sure your secret key (api-key) is not exposed on the front-end (website/mobile app)
* [ ] Ensure that your workflow avoids the duplication or storage of your API keys in multiple locations

## Set up Webhooks

* [ ] [Configure your webhook endpoint](https://api-reference.hyperswitch.io/essentials/webhooks) on our dashboard to receive notifications for different events
* [ ] Update Hyperswitch's webhook endpoints on your connector's Dashboard. [Refer here](https://api-reference.hyperswitch.io/essentials/webhooks) for detailed instructions
* [ ] Update the connector secret key in our dashboard for us to authenticate webhooks sent by your connector

## Secure your Payments

* [ ] Make sure you decrypt and verify the signed payload sent along with the payment status in your return url
* [ ] Always verify the payment amount and payment status before fulfilling your customer's shopping cart/ service request

## Error Handling

* [ ] Make sure your API integration is set up to handle all the possible error scenarios (refer this [link](https://api-reference.hyperswitch.io/essentials/error\_codes))
* [ ] Ensure your Unified Checkout (SDK) integration is set up to handle all the possible error scenarios (refer this [link](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/errorCodes))
* [ ] Ensure that your integration can handle the entire payments lifecycle and test various scenarios using actual payment details

## Customise and sanity check the payment experience

* [ ] Ensure the pay button is properly highlighted to the customer
* [ ] Ensure a blended look and feel of the payment experience using the [styling APIs](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/customization) of Unified Checkout
