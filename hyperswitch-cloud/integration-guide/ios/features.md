# Features

## Scan Card

<figure><img src="../../../.gitbook/assets/Frame 48095844.png" alt=""><figcaption></figcaption></figure>

#### Key Features of Hyperswitch's Card Scanning Feature

1. Accuracy

Leveraging optical character recognition (OCR) technology, Hyperswitch's card scanning feature accurately extracts credit card details in real-time. This significantly reduces the likelihood of manual entry errors and speeds up the checkout process.

2. Seamless Integration

Hyperswitch offers a developer-friendly SDK that makes it easy to integrate the card scanning feature into various platforms, including native mobile apps ([iOS](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/ios/features) and [Android](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/android/features)), cross-platform frameworks, and even in-browser applications.&#x20;

#### Benefits of Hyperswitch's Card Scanning Feature

1. Improved User Experience

By eliminating the need for manual card data entry, the card scanning feature significantly enhances the user experience, potentially leading to higher conversion rates for businesses.

2. Reduced Error Rates

The scanning technology minimizes the risk of mistyped card information, reducing transaction errors and potential disputes.&#x20;

3. Time-Saving Efficiency

For both customers and merchants, the card scanning feature saves valuable time during the checkout process, potentially leading to increased customer satisfaction and loyalty.

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
