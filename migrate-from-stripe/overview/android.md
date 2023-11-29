# Android

If you are already integrated with Stripe as your payment processor, we have made migrating to Hyperswitch much simpler for you. And we will be adding quick migration support for more leading payment processors in the near future. And once you migrate, get immediate access to 40+ payment processors and features such as Smart Router, Digital Payments Manager and many more.

### Android - Node Backend and Kotlin Frontend

The code from your Stripe integration to be removed and replaced is explained below in a step by step manner.

**Step 1:** Install Hyperswitch’s SDK and server side dependencies from npm

```js
 $ npm install @juspay-tech/hyperswitch-node
```

**Step 2:** Change the API key on the server side and modify the paymentIntent endpoint from your server side. You can get the API key from [Developers](https://app.hyperswitch.io/developers) page on the dashboard.

```js
// from
const stripe = require("stripe")(your_stripe_api_key);
// to
const stripe = require("@juspay-tech/hyperswitch-node")(
  "your_hyperswitch_api_key"
);
```

**Step 3:** Configure your android with Hyperswitch dependency Add the following maven repository to the settings.gradle file

```java
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven {
            url "https://maven.hyperswitch.io/release/production/android/maven/1.0.1"
        }
    }
}
```

**Step 4:** Replace the dependencies block of your app build.gradle file

```java
// from
implementation 'com.stripe:stripe-android:20.27.3'
// to
implementation 'io.hyperswitch:hyperswitch-android:1.0.1'
```

**Step 5:** Change these imports in your project

```java
// from
import com.stripe.android.PaymentConfiguration;
import com.stripe.android.paymentsheet.PaymentSheet;
import com.stripe.android.paymentsheet.PaymentSheetResult;

// to
import io.hyperswitch.PaymentConfiguration;
import io.hyperswitch.paymentsheet.PaymentSheet;
import io.hyperswitch.paymentsheet.PaymentSheetResult;

```

**Step 6:** Add an extra import for HyperSwitch and implement HyperInterface

```java
import io.hyperswitch.HyperInterface

class CheckoutActivity : AppCompatActivity(), HyperInterface {

```

**Step 7:** Run your application to make a test payment. And verify the status of the transaction on Hyperswitch Dashboard and Stripe Dashboard. Congratulations ! You have successfully integrated Hyperswitch to your payments stack and you now have access to a suite of 40+ payment processors and acquirers.
