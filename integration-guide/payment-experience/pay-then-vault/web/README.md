---
description: >-
  Integrate Juspay Hyperswitch unified checkout with your web app for a seamless
  payment experience
icon: globe-pointer
layout:
  width: default
  outline:
    visible: true
---

# Web

## Start integrating

Choose the integration path that matches your web application.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>React with REST API</strong></td><td>Integrate Unified Checkout into a React application.</td><td><a href="react-with-rest-api-integration.md">react-with-rest-api-integration.md</a></td></tr><tr><td><strong>HTML with REST API</strong></td><td>Add Unified Checkout directly to an HTML application.</td><td><a href="html-with-rest-api-integration.md">html-with-rest-api-integration.md</a></td></tr><tr><td><strong>JavaScript with REST API</strong></td><td>Build a Unified Checkout integration using JavaScript.</td><td><a href="js-with-rest-api-integration.md">js-with-rest-api-integration.md</a></td></tr></tbody></table>

## Global Checkout Experience

Juspay Hyperswitch Unified Checkout is an inclusive, consistent and blended payment experience optimized for the best conversion rates.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td><strong>Inclusive</strong></td><td>A variety of global payment methods including cards, buy now pay later and digital wallets are supported by the Unified Checkout, with adaptation to local preferences and ability to local language customization.</td><td><a href="../../../../.gitbook/assets/Payment flow (5) (1).png">Payment flow (5) (1).png</a></td></tr><tr><td><strong>Consistent</strong></td><td>With a diverse set of payment methods supported, the Unified Checkout provides a singular consistent payment experience across platforms (web, android and ios) powered by smart payment forms, minimal redirections and intelligent retries.</td><td><a href="../../../../.gitbook/assets/Payment flow (5) (1).png">Payment flow (5) (1).png</a></td></tr><tr><td><strong>Blended</strong></td><td>The Unified Checkout includes 40+ styling APIs, which could be tweaked to make the payment experience blend with your product. Your users will get a fully native and embedded payment experience within your app or website</td><td><a href="../../../../.gitbook/assets/SME.png">SME.png</a></td></tr></tbody></table>

## Modify and Experiment

While the Unified Checkout is pre-optimized for maximum conversions, Hyperswitch does not restrict you to stick to a one-size-fits-all approach. Using Hyperswitch SDK APIs, you get complete control over modifying the payment experience by,

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td><strong>Prioritizing payment methods</strong><br>You can make an impact on the payment mix or conversion rates by prioritizing/ promoting specific payment methods for your customers.</td><td></td><td></td><td></td><td><a href="../../../../.gitbook/assets/Marketplaces.png">Marketplaces.png</a></td></tr><tr><td><p><strong>Switching themes and layouts of checkout page</strong></p><p>The Unified Checkout comes with a wide range of pre-designed themes and layouts which you can choose from.</p></td><td></td><td></td><td></td><td><a href="../../../../.gitbook/assets/Reconciliation.png">Reconciliation.png</a></td></tr></tbody></table>

## Optimize

You can further optimize Unified Checkout web SDK by preloading all the resources that are needed by the iframe. By the time iframe is to be mounted (checkout button), everything that is required can be fetched from their server and stored in the disk cache.

{% columns %}
{% column width="50%" %}
`<Elements/>` wrapper has to be used in the top-level of the merchants app, say web app has two pages eg: homepage and checkout page, the wrapper must be added in the homepage itself.
{% endcolumn %}

{% column width="50%" %}
`<Elements/>` has the required props to load our Hyperloader (script) which will

1. Preload all the resources that are required by the SDK ie. files, svgs, icons, css, fonts etc.
2. Prefetch the two main API calls and is ready with response
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
**This will significantly decrease the SDK load time from \~10-15s (in slow 3G network) to just \~1-5ms.**
{% endhint %}

## Continue exploring

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Customize checkout</strong></td><td>Adapt the payment experience to your product and brand.</td><td><a href="customization.md">customization.md</a></td></tr><tr><td><strong>Review error codes</strong></td><td>Understand integration errors and how to handle them.</td><td><a href="error-codes.md">error-codes.md</a></td></tr></tbody></table>
