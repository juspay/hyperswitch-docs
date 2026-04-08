---
description: Troubleshoot common issues with React Native and Flutter SDKs
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/integration-guide/payment-experience/payment/mobile/cross-platform/troubleshooting
---

# Troubleshooting

This guide helps you resolve common issues encountered when integrating Juspay Hyperswitch React Native and Flutter SDKs.

### Android

1. If you encounter issues related to the **Android browser dependency**, ensure that the required AndroidX Browser version is defined in your project.

Add the following versions in your **root `build.gradle`** (or version catalog equivalent):

```
ext {
    androidXBrowser = "1.8.0"
    androidXAnnotation = "1.7.1"
}
```

### iOS

If you are using the **old architecture (Fabric/TurboModules disabled)**, run the pod install with the following command:

```
RCT_NEW_ARCH_ENABLED=0 pod install --verbose
```

This ensures that **React Native installs pods with the old architecture configuration**.
