---
description: Integrate unified checkout with your web app
---

# 🌐 Web

{% hint style="info" %}
In this section, you will get an overview of the Hyperswitch Unified Checkout for your Web App
{% endhint %}

## Global Checkout Experience

Hyperswitch Unified Checkout is an inclusive, consistent and blended payment experience optimized for the best conversion rates.

| <img src="../../../../.gitbook/assets/image (137).png" alt="" data-size="original"> | <p><strong>Inclusive</strong><br>A variety of global payment methods including cards, buy now pay later and digital wallets are supported by the Unified Checkout, with adaptation to local preferences and ability to local language customization.</p>                            |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="../../../../.gitbook/assets/image (134).png" alt="" data-size="original"> | <p><strong>Consistent</strong><br>With a diverse set of payment methods supported, the Unified Checkout provides a singular consistent payment experience across platforms (web, android and ios) powered by smart payment forms, minimal redirections and intelligent retries.</p> |
| <img src="../../../../.gitbook/assets/image (136).png" alt="" data-size="original"> | <p><strong>Blended</strong><br>The Unified Checkout includes 40+ styling APIs, which could be tweaked to make the payment experience blend with your product. Your users will get a fully native and embedded payment experience within your app or website</p>                     |

## Modify and Experiment

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-10-12 at 11.57.45 AM.png" alt="" width="563"><figcaption></figcaption></figure>

##

While the Unified Checkout is pre-optimized for maximum conversions, Hyperswitch does not restrict you to stick to a one-size-fits-all approach. Using Hyperswitch SDK APIs, you get complete control over modifying the payment experience by,

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Prioritizing payment methods</strong> <br>You can make an impact on the payment mix or conversion rates by prioritizing/ promoting specific payment methods for your customers.</td><td></td><td></td><td><a href="../../../../learn-more/sdk-reference/js.md">js.md</a></td><td><a href="../../../../.gitbook/assets/22 (2).jpg">22 (2).jpg</a></td></tr><tr><td><p><strong>Switching themes and layouts of checkout page</strong></p><p>The Unified Checkout comes with a wide range of pre-designed themes and layouts which you can choose from.</p></td><td></td><td></td><td><a href="../../../../learn-more/sdk-reference/js.md">js.md</a></td><td><a href="../../../../.gitbook/assets/18 (1).jpg">18 (1).jpg</a></td></tr></tbody></table>

## Optimize

You can further optimize Unified Checkout web SDK by preloading all the resources that are needed by the iframe. By the time iframe is to be mounted (checkout button), everything that is required can be fetched from their server and stored in the disk cache.

* `<Elements/>` wrapper has to be used in the top-level of the merchants app , say web app has two pages eg: homepage and checkout page, the wrapper must be added in the homepage itself.
* `<Elements/>` has the required props to load our Hyperloader (script) which will
  1. Preload the all the resources that are required by the SDK ie. files, svgs, icons, css, fonts etc.
  2. Prefetch the two main API calls and is ready with response

{% hint style="success" %}
**This will significantly decrease the SDK load time from \~10-15s (in slow 3G network) to just \~1-5ms.**
{% endhint %}
