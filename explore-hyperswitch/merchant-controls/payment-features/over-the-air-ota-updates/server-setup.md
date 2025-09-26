---
icon: server
---

# Server setup



​Airborne requires a backend endpoint to serve the **`config.json`** and updated bundles to client apps. This server is responsible for:

* Hosting `config.json` files for each app version and environment (Sandbox, Production).
* Serving updated JS bundles and assets when requested by the app.
* Managing rollout strategies (e.g., staged rollouts, feature flags).
* Ensuring version compatibility between client and bundle.

**For complete server setup instructions and example implementations, see the** [**Airborne**](https://github.com/juspay/airborne/)**.**
