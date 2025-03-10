---
icon: bolt-lightning
---

# Alternate Payment Method Widgets

We support modular, embeddable alternate payment methods (APMs) known as **Hyperwidgets**, which a merchant can use to augment their existing checkout in a low code manner.

<figure><img src="../../../.gitbook/assets/image (4).png" alt="" width="563"><figcaption></figcaption></figure>

Let us understand with an example-

In the below checkout screen the merchant only has Cards and Paypal offered by their current PSP.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-03-10 at 13.27.13.png" alt=""><figcaption></figcaption></figure>

But, if the merchant decides to enable more alternate payment methods (APMs), the problems can be multifold:

1. **Availability** - Current PSP may not support the desired alternate payment method requiring the merchant to do a direct integration or use a different PSP.
2. **Complex to integrate** - In case a PSP supports a desired payment method, integrating it into the existing checkout is tedious and often requires high engineering effort. Hyperwidets offers a low code solution for such a scenario where a merchant can not only choose to have their preferred payment method through a wide range of connectors, but also integrate it with minimal engineering effort.
3. **Complex to enhance** - Traditional PSPs and Middle layers ((Subscription provider’s SDK or Token provider’s SDK or Orchestration provider’s SDK)) offer separate integration for every new APM, requiring ongoing engineering effort for enhancements.&#x20;
   * Hyperwidets offers a way for merchants to extend APMs from just “Apple Pay” to “Apple Pay + Google Pay” to “Apple Pay + Google Pay + Amazon Pay + 10 more” with the same integration and no additional engineering effort.
   * Hyperwidgets also offers merchants the flexibility to surface the right set of APMs in the widget based on the order context - Value, Region and more.
4. **Integration overhead to enable more APMs on the same PSP**: Some PSPs require the merchant to do some additional integration steps to enable an APM. This can be time consuming and require significant tech bandwidth from the merchant. Examples can be when certain APMs are only available on new API versions of the PSP, certification from Apple/ Google is required to go-live for some wallet flows, adding a frontend library/ javascript to add certain APMs, and so on.

in the image below you can find a checkout page with more alternate payment methods via Hyperwidgets.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-03-10 at 13.32.06.png" alt=""><figcaption><p>Checkout page with more alternate payment methods</p></figcaption></figure>

**Additional example:**

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkf7BGdsPkCw9nalhAIlE%2Fuploads%2F5V5WWx1Q4KQglFRvGp13%2FGroup%201000003880.png?alt=media&#x26;token=e34dcdf3-c715-484c-ab81-0a78c5865632" alt="" width="563"><figcaption><p>Example: Checkout page only has Cards and Google Pay offered by their current PSP</p></figcaption></figure>

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkf7BGdsPkCw9nalhAIlE%2Fuploads%2FzFhf33ZBiGwXvInNN3Ma%2FFrame%201321316973.png?alt=media&#x26;token=cd12e266-9e04-4688-8a35-84d8b6813a64" alt="" width="563"><figcaption><p>Example: Checkout page with more alternate payment methods</p></figcaption></figure>

### How is Hyperwidget engineered:&#x20;

Hyperwidgets are engineered to simplify and streamline the integration of alternate payment methods (APMs) for merchants, regardless of their existing payment setup. The design focuses on providing a modular, embeddable, and low-code solution, reducing the engineering effort traditionally required to add or enhance payment options.

#### Single SDK to manage all APMs

Hyperwidgets come packaged in a single SDK that merchants can integrate into their web app and route some of their APM traffic to. The widget is powered through a javascript which resides in the merchant's top level domain. Thus, it acts as an extension of the merchant checkout and powerful enough to offer a range of payment methods from Express Checkout payment options (like Applepay, Paypal, etc.), wallets ( like Wechatpay, Alipay, etc.), BNPLs (like Klarna, Affirm, etc.) to Bank Debits and Transfers (like ACH, BACS, SEPA, etc.)

#### Seamless integration for all tech stacks

The Hyperwidget provides seamless integration for merchants using different frameworks for their web app. This is done using multiple wrappers like React, HTML, Angular, etc. This ensures a low-code, low-effort integration for the merchants.

#### Configuring PSPs is independent from integration

The Hyperwidget integration is a one time effort. To manage the different payment methods across business lines, geographies, etc. the merchant bears no additional overhead. Adding/ removing PSPs and routing the transaction through different PSPs is a dashboard configuration.&#x20;

#### Modular fit with other integrations

Merchants can work with multiple PSPs or middle layers, such as subscription providers or orchestration SDKs, without any conflicts from Hyperwidgets. The Hyperwidgets integration fits seamlessly in their existing checkout flow and business logic. They just need to invoke and handle callbacks at the right triggers in their checkout flow.

#### High customization

The Hyperwidgets UI is highly customizable and can completely blend in with the merchant app. Using a customization object, merchants can very easily control the UI parameters like background color, corner radius of the buttons,font size, etc. to match their branding. Some of the examples to highlight the customization options of the checkout are -&#x20;

#### Unified Analytics and order management

All the transactions that are processed through Hyperwidgets can be seen on a unified dashboard. The merchant can analyse data at a granular level to understand conversion across different payment methods, filter by customer id, transaction type (3DS, no-3DS), get a summary of failure reasons for failed transactions and much more. The unification is done across the PSPs/ Acquirers for each payment method.

#### Future ready design

The engineering ensures support for emerging payment methods and new PSPs without requiring additional engineering work, ensuring a scalable one-time only integration for the merchants.

#### Complete control over UI \[Coming soon]

Merchants can build their own UI for each payment method and call Hyperwidget confirm() function with the relevant payment method data to process a transaction. This way, the merchant retains complete control over the way they want to display the payment methods, handle UI interactions and selectively use Hyperwidgets for certain payment methods. &#x20;

### Supported merchant setups :

* **Setup A** - Merchant is directly integrated with 1 PSP and is looking to enable APMs via same or a different PSP
* **Setup B** - Merchant is indirectly integrated with 1 PSP via a middle layer (Subscription provider’s SDK or Token provider’s SDK or Orchestration provider’s SDK). The merchant is looking to enable APMs via the same or different PSP

<table><thead><tr><th width="374">via PSP or middle layer</th><th>via Hyperwidgets</th></tr></thead><tbody><tr><td><p><mark style="color:blue;">Existing APMs</mark></p><ul><li>Apple Pay - <mark style="color:red;">2-3 weeks of engineering effort</mark></li><li>Klarna - <mark style="color:red;">2-3 weeks of engineering effort</mark></li></ul><p><mark style="color:blue;">New innovations</mark></p><ul><li>Paze - <mark style="color:red;">Not available via most players</mark></li><li>Click2Pay - <mark style="color:red;">Not available via most player</mark></li></ul></td><td><p>⠀</p><p>One time effort of <mark style="color:blue;">2-weeks</mark> to enable all existing APMs and new innovations via the same integration</p></td></tr></tbody></table>

{% content-ref url="hyperwidget-integration-guide.md" %}
[hyperwidget-integration-guide.md](hyperwidget-integration-guide.md)
{% endcontent-ref %}
