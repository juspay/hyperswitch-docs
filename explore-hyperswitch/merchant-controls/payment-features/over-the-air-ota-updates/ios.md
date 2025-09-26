---
icon: apple
---

# iOS

### Configuration

1.  Set the HyperOTA Endpoint

    Edit **`HyperOTA.plist`** to point to your environment-specific endpoint.

    In your **release `config.json`**, ensure the HyperOTA endpoint is correctly defined.
2. Check the **`OTAServices.swift`** file to verify that the release configuration URL is being built correctly.

```swift
let payload = [
                "clientId": getHyperOTAPlist("clientId"),
                "namespace": getHyperOTAPlist("namespace"),
                "forceUpdate": true,
                "localAssets": false,
                "fileName": getHyperOTAPlist("fileName"),
                "releaseConfigURL": getHyperOTAPlist(configKey) + 
                 "/mobile-ota/ios/" + SDKVersion.current + "/config.json",
] as [String: Any]

HyperOTAServices(payload: payload, 
                loggerDelegate: logger, 
                baseBundle: Bundle(for: OTAServices.self))
```

{% hint style="info" %}
Make sure `releaseConfigURL` points to the `config.json` for the correct SDK version and environment.

`Example : $baseURL/mobile-ota/ios/${BuildConfig.VERSION_NAME}/config.json`
{% endhint %}

For more information, [Airborne](https://github.com/juspay/airborne)

