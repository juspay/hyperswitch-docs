---
description: >-
  Setup Taxjar on Hyperswitch to automatically calculate tax in case of Express
  checkout wallets
---

# 💲 Automatic Tax calculation for Express Checkout wallets

Hyperswitch supports configuring [Taxjar](https://www.taxjar.com/) in your dashboard as a tax connector so that tax amount can be calculated automatically whenever your customers change their shipping address on Express Checkout wallets like Apple pay and Paypal

**How to test Taxjar in Apple Pay on Hyperswitch?**

## How to configure Taxjar on Hyperswitch?

You need to enable taxjar from the hyperswitch dashboard. The steps for enabling taxjar are as follows:

* Go to [https://app.hyperswitch.io](https://app.hyperswitch.io)
* Click on Connectors and under Connectors click on Tax Processors.
* To enable Taxjar click on the Connect button.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfw_4V1zufm4H1g4NIRI_PLzz7GsYvDLcLjjqhC_ZvyOPa3fr0RavKs9dPCORPHDh-yDxtiLZ6oPt5aZgFUfb1Eo9uT7RYyuuIvt1KBT4_upYYcG0z6RZuK9WB4hzPKa2NEV9riSN4xpZC70AyiO8tAGMS8?key=60G18knFKBKAyEyzRsD8JA" alt=""><figcaption></figcaption></figure>

* Select the profile id and fill the sandbox token from your Taxjar dashboard. Also add Connector label as well, then click Connect and proceed.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSQL9j8A1VSqoj0J4Lmh3Adws7Zjr_2wrqOygaIeUkCTl8mXTFzs47hhB63GtEYJIqs0Guk-QsCTzctd6zC_dKRO2TPleduk0blC9OS1oLqgESLmxfwhKOU9guxvG1zlJYlGYQUDpCHnu_2k-AMDryR8Q?key=60G18knFKBKAyEyzRsD8JA" alt=""><figcaption></figcaption></figure>

You can now see Taxjar enabled on your acccount

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXecyIrQta6I2HnYLBvOAWlEuuRhjURWL70TgNAN45Ctb83XldY1ylNBpPIrY9Bl66z4-z1bUpJ14ySxwx14SKYwyH92kioaercqUK6On8OR4s-uZESL7NkykM-E1eDtXcSnKiC3kYhSG_Igr-BxtUV9wPp3?key=60G18knFKBKAyEyzRsD8JA" alt=""><figcaption></figcaption></figure>

* To enable collecting shipping details from wallets SDKs you need to enable Collect shipping details from wallets toggle.
* Click on Developers then Payment Settings.
* For the particular profile id check the Collect shipping details from wallets toggle.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfcuPydxmKYpa-4hHwg9X6-SgJNg_2kz-MIiqHjvt8G-qKL-rk7nr1wLE8qP0vmO10xRXaDf3oNvzSR1g9tXXatXHraPB094wUDONI62yAn5sumturz9f6XWduNqScDndCa-ofR-BYtVJpQSjU2O-5Jvh0h?key=60G18knFKBKAyEyzRsD8JA" alt=""><figcaption></figcaption></figure>

### Skipping Tax calculation for a particular payment:

<mark style="color:red;">`skip_external_tax_calculation (boolean)`</mark>

This field is optional for payments create calls and the default value is set to “false”, which means tax will be calculated dynamically. If you explicitly do not want to calculate taxes for a particular order, pass this boolean with value as “true”

\
