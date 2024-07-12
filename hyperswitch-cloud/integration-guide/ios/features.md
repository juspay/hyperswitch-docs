# Features

## 1. Scan Card

### 1.0 Configure pods to support Scan Card feature&#x20;

Scan Card Setup

Add these lines to your Podfile:

```ruby
#use_frameworks!
#target 'YourAPP' do
  pod 'hyperswitch-sdk-ios/scancard'
#end
```

Note: Above subspec installs both Hyperswitch SDK and Scan Card dependencies to your app

Run the following command:

```
pod install
```

To update to the latest version of the SDK, run:

```
pod install --repo-update
```

### 1.1 Enable scan card support for iOS app&#x20;

To enable scan card support, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the Info.plist of your application, and provide a reason for accessing the camera (for example, “camera access required to scan cards”). Devices with iOS 13 or higher support card scanning.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-04-26 at 2.28.47 PM.png" alt=""><figcaption></figcaption></figure>
