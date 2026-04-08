---
description: Deploy the Hyperswitch web client on the cloud for production use
icon: globe-wifi
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/hyperswitch-open-source/deploy-hyperswitch-on-aws/component-wise-deployment/deploy-web-client
---

# Deploy web client

{% hint style="info" %}
This section is aimed at helping you deploy the Web client on the cloud and access it over the internet
{% endhint %}

Deploying web client consists of two main steps:

1. Deploy HyperLoader.js - this is the core logic of the web client
2. Integrate the web client SDK on your app and deploy the app

For quick prototyping, you can also try out deploying the full stack integrated demo app playground.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Production ready deployment</strong></td><td>Host the web client SDK (<strong>HyperLoader.js</strong>) on the cloud to serve your customers.</td><td></td><td><a href="../../../../.gitbook/assets/Payment flow.jpg">Payment flow.jpg</a></td></tr><tr><td><strong>Integrate on your app and deploy[REGULAR]</strong></td><td>Once HyperLoader.js is deployed on cloud, integrate the SDK in your web app.</td><td></td><td><a href="../../../../.gitbook/assets/production.jpg">production.jpg</a></td></tr><tr><td><strong>Deploy the playground (OPTIONAL)</strong></td><td>The web client comes with a full stack playground for quick prototyping. Test the deployment with a single script and get a feel of the product before you integrate it on your app.</td><td></td><td><a href="../../../../.gitbook/assets/Playground.jpg">Playground.jpg</a></td></tr></tbody></table>
