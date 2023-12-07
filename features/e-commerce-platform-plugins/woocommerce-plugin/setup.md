---
description: WooCommerce Plugin Setup
---

# Setup

{% hint style="info" %}
This section covers the steps to setup woocommerce plugin on your website and managing the orders from the dashboard.
{% endhint %}

### Prerequisites

1. Sign up on the Hyperswitch dashboard and navigate to connectors tab [here](https://app.hyperswitch.io/) to configure connector(s) and enable various Payment Methods.
2. WooCommerce plugin must be installed and enabled on your WordPress website. Visit [here](https://wordpress.org/plugins/woocommerce/) or go to your WordPress Admin dashboard and navigate to "Plugins" section to install and enable the WooCommerce Plugin.

### 1. Setting up the Plugin on your Website

#### 1.1 Download the Plugin

## [Download the Plugin](https://hyperswitch.io/zip/hyperswitch-checkout.zip)

#### 1.2 Installing the Plugin

Head to your WordPress Admin Dashboard, and navigate to Plugins > Add New

<figure><img src="https://hyperswitch.io/img/site/wordpress_plugins.png" alt=""><figcaption></figcaption></figure>

Click on "Upload Plugin". Click on "Choose File" and browse to the directory where you downloaded the plugin file (hyperswitch-checkout.zip) in 1.1, and select it, complete the installation and activate the plugin.

<figure><img src="https://hyperswitch.io/img/site/wordpress_addplugin.png" alt=""><figcaption></figcaption></figure>

#### 1.3 Configuring the Plugin

Navigate to Woocommerce > Settings section in the dashboard. Click on the "Payments" tab and you should be able to find Hyperswitch listed in the Payment Methods table.

<figure><img src="https://hyperswitch.io/img/site/wordpress_settings.png" alt=""><figcaption></figcaption></figure>

Click on "Pay via Hyperswitch" to land on the Hyperswitch Plugin Settings page. Configure your Hyperswitch credentials here, including the Environment, Secret Key, Publishable Key, and Payment Response Hash Key to establish a secure connection between your website and Hyperswitch. You can find these keys in the "Developers" section of your [Hyperswitch dashboard](https://app.hyperswitch.io/developers).

Configure various Payment Controls, such as Capture Method, Webhooks and Saved Customer Payment Methods when Hyperswitch is selected during checkout.

This plugin is built to seamlessly tailor the payment experience to match your website's branding by blending the payment form into your WordPress theme. You can further customize the "Appearance" and "Layout" of the payment form using styles or pre-built themes. Read more about customization [here](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/customization).

<figure><img src="https://hyperswitch.io/img/site/wordpress_hyperswitch_settings.png" alt=""><figcaption></figcaption></figure>

**Note:** To receive webhooks, ensure that you copy the Webhook URL displayed under the "Enable Hyperswitch Webhook" checkbox and paste it onto the "Webhook URL" text field in the Developers > Webhooks section of your [Hyperswitch dashboard](https://app.hyperswitch.io/developers).

### 2. Orders Management on WooCommerce Dashboard

With the Hyperswitch plugin seamlessly integrated into your WooCommerce Dashboard, you gain powerful order management capabilities to enhance your e-commerce operations. This plugin provides access to features that Hyperswitch brings to your WooCommerce order management, enabling you to capture payments manually, create refunds, sync payment status, and update orders via webhooks.

#### 2.1 Manual Payment Capture:

You can choose to capture customer payments automatically or manually, as per your needs. If you wish to exercise the latter option, all you need to do is to update the "Capture Method" in the Hyperswitch Plugin settings to "Manual".

Once a customer authorizes their payment, you can easily capture payments manually through the Woocommerce Dashboard. Navigate to the Order Details page and click on the "Order Actions" dropdown. Select the "Capture Payment with Hyperswitch" option, and click on "Update".

<figure><img src="https://hyperswitch.io/img/site/wordpress_manual_capture.png" alt=""><figcaption></figcaption></figure>

Hyperswitch will process the payment, update the payment status, and provide you with real-time payment details.

#### 2.2 Refunds:

In cases where you need to issue a refund to a customer, the Hyperswitch plugin streamlines the process within your Woocommerce Dashboard. Navigate the Order Details page, click on "Refund" and specify the refund amount, and optionally the reason.

<figure><img src="https://hyperswitch.io/img/site/wordpress_refund.png" alt=""><figcaption></figcaption></figure>

Note: Ensure you click on "Refund via Hyperswitch" and not the "Refund manually". Hyperswitch will handle the refund and update the payment status accordingly, ensuring a seamless refund experience for both you and your customers.

#### 2.3 Payment Sync:

With the Hyperswitch plugin integrated into your Woocommerce Dashboard, you have the flexibility to manually sync payment status whenever necessary. This feature allows you to ensure accurate payment status representation and maintain consistent order management. Navigate to the Order Details page and click on the "Order Actions" dropdown. Select the "Sync Payment with Hyperswitch" option, and click on "Update".

<figure><img src="https://hyperswitch.io/img/site/wordpress_sync.png" alt=""><figcaption></figcaption></figure>

The payment status will be accurately reflected, whether the payment is processing, succeeded, or failed.

#### 2.4 Order Updates via Webhooks:

Hyperswitch facilitates seamless order updates through webhooks, allowing you to automate various order management processes. By setting up webhooks within your Hyperswitch Plugin Settings and configuring the necessary endpoints in your Hyperswitch Dashboard, you can receive real-time notifications about order status changes, payment confirmations, and more. &#x20;

<figure><img src="https://hyperswitch.io/img/site/wordpress_webhook.png" alt=""><figcaption></figcaption></figure>

This enables you to trigger specific actions or update order information in your Woocommerce system, ensuring smooth order processing and fulfillment.
