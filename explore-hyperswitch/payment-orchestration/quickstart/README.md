---
icon: bolt
---

# Accept Payments

We at Hyperswitch simplify accepting one-time payments by offering a seamless integration process that empowers businesses to start accepting payments in just a few minutes.&#x20;

## Get Started

### **1. Get your Hyperswitch API key**

* **Sign up on Hyperswitch Control Centre**: If you haven’t already, create an account on the [Hyperswitch Control Centre](https://app.hyperswitch.io/).&#x20;
* **Locate API key**: Access your API key from the **Settings > Developers** section in the Control Center.

### 2. Configure your payment processor

* **Set up payment processor:** Navigate to the Connectors tab in the Control Center to configure your preferred payment processor. You’ll need API credentials for the processor.

{% hint style="success" %}
**Use the dummy processors:** If credentials are unavailable, you can configure the dummy processors, pre-built into the Control Center.&#x20;

These processors help simulate payment flows during integration and provide a risk-free testing environment.
{% endhint %}

### 3. Integrate Hyperswitch

You will use both a server-side and a client-side component of Hyperswitch to complete the integration. The payment flow begins once your user adds products to a shopping cart and wishes to make a payment.

#### **Steps to Integrate Hyperswitch**

<figure><img src="../../../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

1. **Initiate Payment on Server**:\
   Your server creates a payment request with the Hyperswitch server to obtain a `client_secret`.
2. **Render Payment Widget**:\
   Your website or app initiates the Hyperswitch SDK, which renders a payment widget for the customer. The widget dynamically displays payment methods based on the customer’s currency and country.
3. **Customer Makes Payment**:\
   The customer selects a payment method, provides additional details (e.g., card information), and clicks the **Pay** button.
4. **Secure Payment Processing**:\
   The Hyperswitch SDK securely transmits the payment information to the Hyperswitch server, which processes the payment using the most suitable processor as determined by your smart routing algorithm.
5. **Payment Confirmation**:\
   Upon successful payment, the customer is automatically redirected to your payment status confirmation page.

{% hint style="info" %}
Don’t want to write code? Check out the [Hyperswitch Postman Collection](https://docs.hyperswitch.io) for a no-code way to get started with Hyperswitch's API.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Connectors</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/connectors">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/connectors</a></td></tr><tr><td><mark style="color:blue;"><strong>Setup Payment Methods</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-methods-setup</a></td></tr><tr><td><mark style="color:blue;"><strong>Payment Links</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-links">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-links</a></td></tr><tr><td><mark style="color:blue;"><strong>Save a Payment Method</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/mandates-and-recurring-payments">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/mandates-and-recurring-payments</a></td></tr><tr><td><mark style="color:blue;"><strong>Manual Capture</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/manual-capture">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/manual-capture</a></td></tr><tr><td><mark style="color:blue;"><strong>Incremental Authorization</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/incremental-authorization">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/incremental-authorization</a></td></tr><tr><td><mark style="color:blue;"><strong>Tokenization &#x26; Card Vault</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/tokenization-and-saved-cards">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/tokenization-and-saved-cards</a></td></tr><tr><td><mark style="color:blue;"><strong>Supported Payment Workflows</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-workflows">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/payment-workflows</a></td></tr><tr><td><mark style="color:blue;"><strong>Co-badged Cards</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/co-badged-cards-with-hyperswitch">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/co-badged-cards-with-hyperswitch</a></td></tr><tr><td><mark style="color:blue;"><strong>Webhooks</strong></mark></td><td></td><td></td><td><a href="https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/webhooks">https://docs.hyperswitch.io/explore-hyperswitch/payment-flows-and-management/quickstart/webhooks</a></td></tr></tbody></table>

{% hint style="info" %}
**Have Questions?**\
Join our [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw) to ask questions, share feedback, and collaborate.\
Prefer direct support? Use our [Contact Us](https://hyperswitch.io/contact-us) page to reach out.
{% endhint %}

<details>

<summary>FAQs</summary>

#### What is a connector?

Hyperswitch refers to payment processors, fraud / risk engines and other payment integrations as connectors. Hyperswitch currently supports 50+ global payment processors that you can use to process payments on your application

#### How can I decide the best payment methods for my business?

Hyperswitch supports 100+ payment methods across various payment processors. There is no one size fits all payment methods but you can learn more about how you can decide the best payment methods for you business [here](payment-methods-setup/).

#### What will the completed integration look like?

Hyperswitch offers various customization options but you can try out our demo store [here](https://demo-hyperswitch.netlify.app/checkout) to test the checkout experience

#### Are there any sample integrations for reference?

Here are a few demo integrations for various tech stacks:

* [Hyperswitch React-Node](https://github.com/juspay/hyperswitch-react-node)
* [Hyperswitch HTML-Node](https://github.com/juspay/hyperswitch-html-node)
* [Hyperswitch React-Java](https://github.com/juspay/hyperswitch-react-java)
* [Hyperswitch Next-Node](https://github.com/juspay/hyperswitch-next-node)



</details>
