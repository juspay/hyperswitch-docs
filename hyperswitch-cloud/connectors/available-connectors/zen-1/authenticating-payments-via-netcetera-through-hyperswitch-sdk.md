---
description: >-
  How to trigger redirection less external 3DS authentication in HyperSwitch SDK
  ?
---

# Authenticating Payments via Netcetera Through HyperSwitch SDK

Please specify the payment needs to externally authenticated via Netcetera by passing the below field&#x20;

in create payments call. You can read more about it [here](../../../../features/payment-flows-and-management/external-authentication-for-3ds.md#id-1.-create-a-payment-from-your-server-with-request\_external\_three\_ds\_authentication-as-true).

```
"request_external_three_ds_authentication": true
```

Pass your Netcetera SDK API key to HyperSwitch SDK like below.

{% tabs %}
{% tab title="Flutter" %}
```dart
configuration: Configuration(netceteraSDKApiKey: "<YOUR_NETCETERA_API_KEY>")
```
{% endtab %}

{% tab title="Android" %}
<pre class="language-kotlin"><code class="lang-kotlin"><strong>configuration = PaymentSheet.Configuration.Builder("Example, Inc.")
</strong>                .netceteraSDKApiKey("YOUR_NETCETERA_API_KEY")
                .build()
</code></pre>
{% endtab %}

{% tab title="iOS" %}
```swift
configuration.netceteraSDKApiKey="YOUR_NETCETERA_API_KEY"
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
In order to test external authentication on sandbox, a certificate needs to be added. Please follow the below steps.
{% endhint %}

Make the Hyperswitch [Payments - External 3DS Authentication](https://api-reference.hyperswitch.io/api-reference/payments/payments--external-3ds-authentication) request. Take the value of the field `acs_signed_content` , then decrypt it using [JWT.io](https://jwt.io/).  Under the decrypted 'x5c' header you will get your root certificate.

{% hint style="info" %}
This certificate is required is required to decrypt response from Netcetera's Prev (Sandbox) environment Demo ACS Server.
{% endhint %}

{% hint style="success" %}
&#x20;Please note the above step is not required for Production environment.
{% endhint %}

### Providing the root certificate to HyperSwitch SDK

**Android**

Put the obtained certificate in assets directory in your android project.&#x20;

#### iOS

Put the obtained certificate in the root directory in your iOS project.&#x20;

