# 👨💻 Dev Support

## Dev Support

#### Want to reach out to us

If you have any general queries about of capabilities of hyperswitch, you may reach out to us on [Slack](https://join.slack.com/t/hyperswitch-io/shared\_invite/zt-1k6cz4lee-SAJzhz6bjmpp4jZCDOtOIg) or [Discord](https://discord.gg/wJZ7DVW8mm) or Email us at: [hyperswitch@juspay.in](broken-reference)

## FAQ

### 1. What is Hyperswitch?

Hyperswitch is an open, fast and reliable payment router. With its single unified API, you can connect to any payment processor and offer diverse payment methods to your customers.

### 2. How does Hyperswitch help me?

Hyperswitch helps you to: (a) Improve conversion rates (b) reduce costs (c) simplify payment ops (d) take full control of your payments

It allows you to support multiple payment processors (and all the associated payment methods) with a single API or SDK integration. Hence it saves a lot of Dev efforts to integrate, maintain and manage payment ops. We believe high growth businesses should focus on your core product and customer service rather than managing payment ops.

### 3. Is it free?

Yes, the open-source version of the product is 100% free and you can download and use it under the open-source Apache 2.0 License. We also have a hosted version which is FREE to use for up to 10k transactions per month for 6 months. Beyond 10k transactions, each successful transaction will be charged at a nominal $ 0.04 per transaction. The hosted version comes with a full-stack solution, integration and ongoing support.

### 4. What is the tech stack used?

The back-end is built on Rust with open-source rust-libraries like Diesel & Serde. The DB and data layers are built in PostgreSQL, Redis, Grafana, Loki etc. Front-end is built on React Native, Javascript, Swift, Kotlin etc

### 5. Do you have enterprise support?

Yes, we have 24x7 enterprise support for paid plans. The Enterprise plan comes with dedicated account manager and anytime call support.

### 6. Who is building and backing this product?

Juspay is funding the initiative and the product is built by a strong community of developers. The parent company, Juspay, was founded in 2012 with a mission to make payments reliable and frictionless. As of today, Juspay's tech platform processes 35 million payment transactions per day and its payments SDK is used in more than 1.5 Bn Apps. It has contributed to multiple payment innovations viz. BHIM App, UPI 2FA SDK, BECKN Foundation, OCEN Protocol etc. Juspay has 1000+ employees across 6 offices.

### 7. Which countries does it support?

Currently, we support North America (US and Canada). Support for the 3 more countries in Europe expected in Q2 2023. By the end of 2023, we intend to support 30+ countries across the globe.

### 8. Are you a stripe alternative?

Nope. You can think of HyperSwitch as "Stripe++" - i.e. it allows you to onboard stripe and any of its alternatives with a single integration.

Stripe is a payment processor while hyperSwitch is a payment orchestrator and a unified API/SDK to connect to multiple payment processors like Stripe.

We are wire-compatible with Stripe, making it extremely easy to upgrade from Stripe to Stripe++

### 9. What is a payment orchestrator?

A payment orchestrator allows you to connect to multiple payment processors or gateways or acquirers using a single interface. Some orchestrators allow routing different transactions to different processors based on rules that are defined around factors like payment amount, geography, payment method, issuer, etc.

### 10. How is HyperSwitch different from other payment orchestrators?

HyperSwitch is the only enterprise-grade payment orchestrator which is 100% open sourced. It is fast, reliable and light weight. Due to its modern high-performance architecture and the community contribution, it is offered at the best price compared to other alternatives.

HyperSwitch is also the only orchestrator which comes with a custom native SDK, Checkout Page Studio and an advanced Smart Router.

### 11. What is the HyperSwitch Payments SDK?

Hyperswitch offers multiple SDKs to give your users a seamless and native payment experience. Payment SDK improves developer productivity by offering helper functions for all frequent use cases of payments which can be seamlessly integrated into your app or website.

### 12. What kind of support is available?

HyperSwitch has 3 plans: (1) ## Open-core## with community support (2) ## Pro## plan comes with hosted solution, compliance-in-a-box, white-labeled card-vault and 24x7 email support (3) ## Enterprise## plan includes all features of Pro plan with a dedicated account manager, call support and custom features.

### 13. What payment processors are currently supported?

Our mission is to support all the major payment processors across the globe. To start with, we support all top payment processors for the North American market. We are soon adding the European and Asian processors.

### 14. Can you add / support a new payment processor?

Yes, we do. You can place a request for integration by emailing us @ [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in)

### 15. Where can I find the codebase?

Entire code is hosted as a public repository in GitHub here: [https://github.com/juspay/hyperswitch](https://github.com/juspay/hyperswitch)

### 16. How can I contribute to the Open Source Project?

You are most welcome to contribute to our open source efforts. Login / Signup at GitHub to know more.

Project page here: [https://github.com/juspay/hyperswitch](https://github.com/juspay/hyperswitch). You can find the list of open issues [here](https://github.com/juspay/hyperswitch/issues), contribution guidelines [here](https://github.com/juspay/hyperswitch/blob/main/contrib/CONTRIBUTING.md) and the product roadmap [here](https://github.com/juspay/hyperswitch/projects?query=is%3Aopen).

### 17. Where can I find the documentation?

You can find it here: [https://hyperswitch.io/docs](https://hyperswitch.io/docs) – For any help or support, you can email us at [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in)

### 18. What is the open source license used?

Entire code-base is licensed under [Apache 2.0 License](https://github.com/juspay/hyperswitch/blob/main/LICENSE).

## Resources

### Supported Browsers

Hyperswitch unified checkout is supported on all the recent versions of major browsers. For security reasons and for providing the best payment experience for your customers, we might not be compatible with older versions of browsers.

We support the following desktop browser versions:

* Chrome 65+
* Safari 13.1+
* Firefox 70+
* Edge 80+
* Opera 51+

We support the following mobile browsers:

* iOS Safari 13.1+ and other browsers and web views which use the system-provided WebKit engine
* Android Chrome 65+
* Samsung Browser 7.1+

We do support other browsers that are not explicitly mentioned above (including in-app browsers), given that,

1. TLS 1.2 is supported by the browser
2. The browser is equipped to handle promises in JS
3. The browsers do not have restrictions on iframes.

We passively support these non-mainstream browsers, and respond to bug reports, but do not actively test the unified Checkout compatibility/ performance/ support on these browsers. For issues on any of the browsers or browser support requests, please contact the Hyperswitch team.

As long as the browser requirements are met, Hyperswitch Unified Checkout is compatible and responsive on all the latest desktops, tablets and mobiles.

{% hint style="info" %}
Note: For other browsers, even though the basic functionalities might continue to work, active developer support is not available and compatibility is not guaranteed.
{% endhint %}
