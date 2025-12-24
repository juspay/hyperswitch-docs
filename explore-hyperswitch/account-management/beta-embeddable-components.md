---
icon: laptop-code
---

# \[Beta] Embeddable Components

{% hint style="info" %}
**Developer** **Note**:

Active Beta: This feature is currently in active development. While the core architecture is stable, specific API contracts, SDK methods, and implementation details are subject to change as we refine the product
{% endhint %}

#### Introduction

As a SaaS platform or marketplace, your value lies in your core product, not in rebuilding payment setting screens. Yet, to offer financial services to your users ("sub-merchants"), you often face a difficult choice:

1. Redirect them to an external dashboard (breaking the user experience).
2. Build it yourself, spending months on complex forms, credential validation, and security compliance.

HyperSwitch Embeds solves this. We provide a library of pre-built, fully white-labeled UI components  that drop directly into your application. You get the full power of HyperSwitch’s orchestration without ever sending your customers away.

#### How It Works: Architecture

We designed Embeds to be secure, isolated, and incredibly fast to integrate

The integration follows a simple 3-step flow:

1. Server-Side (Secure Handshake): Your backend requests a temporary `access_token` from HyperSwitch using your API key.
2. Client-Side (SDK Initialization): Your frontend initializes the HyperSwitch Embed SDK using this `access_token`.
3. Rendering: The SDK securely loads the component. All business logic (validation, API calls) is handled inside the secure container, isolated from your main application.

#### Coming First: The Connector Component

The most requested feature is now our first embeddable module: The Connector Component

**The Problem**: Allowing sub-merchants to bring their own payment processors (Stripe, Adyen, PayPal, etc.) requires building complex configuration forms for every single processor, handling API key validation, and maintaining those integrations forever.

**The Solution**: Embed the Connector Component. It provides a complete, self-serve interface for your users to select processors and enter credentials.

**Key Features:**

* White-Labeled: No HyperSwitch branding.
* Instant Validation: We validate credentials in real-time before saving.
* Zero Maintenance: When a processor changes their API requirements, we update the component. You don't change a line of code.

<figure><img src="../../.gitbook/assets/Screenshot 2025-12-24 at 10.53.27 AM.png" alt=""><figcaption><p>A seamless, white-labeled configuration experience embedded directly into a demo dashboard.</p></figcaption></figure>

***

#### What’s Next?

We are rolling this out in stages. Following the Connector Component, we will release:

* Native Analytics: charts and reports.
* Operations Center: Refund and Payment management interfaces.
* Support for theme customisation via Control Center.
