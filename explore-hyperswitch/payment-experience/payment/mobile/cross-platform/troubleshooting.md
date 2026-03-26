---
description: >-
  Troubleshoot common issues to ensure smooth payment integration and operations
---

# Troubleshooting

## Android

1. If you encounter issues related to the **Android browser dependency**, ensure that the required AndroidX Browser version is defined in your project.

&#x20;Add the following versions in your **root `build.gradle`** (or version catalog equivalent):

```
ext {
    androidXBrowser = "1.8.0"
    androidXAnnotation = "1.7.1"
}
```

## IOS

If you are using the **old architecture (Fabric/TurboModules disabled)**, run the pod install with the following command:

```
RCT_NEW_ARCH_ENABLED=0 pod install --verbose
```

This ensures that **React Native installs pods with the old architecture configuration**.
