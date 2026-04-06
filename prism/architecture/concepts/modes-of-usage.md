---
description: Choose between library and microservice deployment modes based on your infrastructure needs
---

# Modes of Usage

Hyperswitch Prism can be used in two modes: **Library (SDK)** or **Microservice (gRPC)**.

## Library Mode (Recommended)

In this scenario, Hyperswitch Prism SDK is directly embedded into your application. This is the recommended mode for most use cases because it is:

- Simple to integrate and deploy within your existing server and cloud resources
- No additional network hops
- Full type safety at compile time

## Microservice Mode

You may deploy Hyperswitch Prism as a standalone service only if you need service isolation due to:

- **Independent deployments** — Being able to update Hyperswitch Prism without redeploying your main application
- **Fast release cycles** — Decoupling the SDK release from your app server releases, and you wish to update Hyperswitch Prism more frequently than your application

Choose this mode only if you need isolation for fast and independent deployments, because this mode comes with additional complexity to handle—such as deployment, provisioning of resources, uptime, and monitoring.