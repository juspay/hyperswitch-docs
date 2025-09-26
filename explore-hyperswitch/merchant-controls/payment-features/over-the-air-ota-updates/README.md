---
description: >-
  Airborne is an open-source project by Juspay designed to help developers
  integrate Over-The-Air (OTA) update capabilities into Android, iOS, and React
  Native applications effortlessly.
icon: arrows-rotate-reverse
---

# Over-the-Air (OTA) Updates



#### **Airborne SDK Overview** <a href="#airborne-sdk-overview-hyperota" id="airborne-sdk-overview-hyperota"></a>

**Purpose**

Airborne enables Hyperswitch SDK to receive live updates without requiring an app store release. This allows you to:

* Push urgent bug fixes instantly.
* Roll out features gradually.
* Control app behavior remotely via feature toggles.

**Real-World Hyperswitch Scenarios**

* **Critical Checkout Fix** – Push a new JS bundle to resolve a bug affecting payments.
* **Feature Rollout** – Show “One-Click Pay” to 5% of users, expand once results are good.
* **Remote Toggles** – Enable/disable “Gift Card Support” instantly for specific merchants.

***

**OTA Flow**

1. App Launch
   * User opens the Hyperswitch-powered app.
2. **Release Config Fetch**
   * Airborne makes an API call to your server to fetch the latest release [configuration](https://github.com/juspay/airborne/) for the app.
3. **Update Check**
   * If the config shows an update is available, Airborne immediately starts downloading the new JavaScript bundle.
4. **Instant Install**
   * Once the critical files are downloaded, Airborne installs the bundle and hands over the latest reference to the app for use in the same launch session.
5. **Fallback Handling**
   * If the update fails or times out, Airborne automatically falls back to:
     * The **previously downloaded working bundle**, or
     * The **default bundle shipped with the app**.
6. **Background Downloads**
   * Non-critical assets (lazy files) continue to download while the app runs, so the user is never blocked.

***

For more information, [Airborne](https://github.com/juspay/airborne)​[\
](https://app.gitbook.com/o/JKqEWJaaVJcFy28N5Z3d/s/kf7BGdsPkCw9nalhAIlE/~/diff/~/revisions/NIN50A3QoITTHFHb4scS/explore-hyperswitch/merchant-controls/integration-guide/server-setup)
