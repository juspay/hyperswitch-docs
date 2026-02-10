---
description: Set up Google pay on your application
---

# Google Pay

Google Pay is a simple and secure way for customers to pay by adding their cards and bank account to their Google wallet. Currently, Google Pay is available through Web and Android devices in [70+ countries](https://support.google.com/googlepay/answer/12429287?hl=en#zippy=%2Cpay-in-store%2Cpay-online-or-in-apps) while iOS devices are supported only in the US and India.

Google Pay has additional layers of security embedded in its payment flow and hence Google Pay integration is bound to be elaborate by nature.

## **Prerequisites**

There are few prerequisites that need to be fulfilled before integrating Google Pay on Hyperswitch -

1. Configure Google Pay on your processor's dashboard
2. In order to test Google Pay integration you will need to add test cards to your google account. You can go to [Google Pay API Test Cards Allowlist](https://groups.google.com/g/googlepay-test-mode-stub-data?pli=1) and click on Join Group to automatically add test cards in your Google Developer Account

## **Configuring Google Pay on Hyperswitch**

To configure Google Pay on Hyperswitch follow the steps given below -

1. Login to [Hyperswitch dashboard](https://app.hyperswitch.io/)
2. In the Connectors tab, select your processor
3. While selecting Payment Methods, click on Google Pay in the Wallet section
4. Use this [link](https://developers.google.com/pay/api/web/guides/tutorial#tokenization) to search for your processor's input parameters. Get those parameters from the processor dashboard and configure them in Google Pay Merchant Key
5. In Google Pay Merchant Name, provide a user-visible merchant name

## **Go-Live Checklist**

Your app requires an approval from Google Pay before you go live. Please follow [Google's instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) and request production access.

1. Choose integration type **Gateway** when prompted.
2. Submit your app screenshots for review.
3. Set the Google Pay Environment to Production.
4. Once the app is reviewed and approved, launch GooglePay from a signed, released build your app.

## **Google Pay Compatibility**

Google Pay is available only in certain countries or regions and on certain devices. Take a look at the [exhaustive list of countries](https://support.google.com/googlepay/answer/12429287?visit_id=638320942600397737-977605919\&rd=1#zippy=%2Cpay-online-or-in-apps) where Google Pay is available. For security reasons, Google Pay is not supported in some browsers. Please check the list below to know the supported browsers:

| Browser                                         | Google Pay Support |
| ----------------------------------------------- | ------------------ |
| `Firefox`                                       | Yes                |
| `Chrome`                                        | Yes                |
| `Safari`                                        | Yes                |
| `Opera`                                         | Yes                |
| `Mobile-web: Firefox`                           | Yes                |
| `Mobile-web: Chrome`                            | Yes                |
| `Mobile-web: Safari`                            | Yes                |
| `iOS in-app browser - Instagram`                | No                 |
| `Android in-app browser - Instagram`            | No                 |
| `iOS in-app browser - X (Formerly Twitter)`     | Yes                |
| `Android in-app browser - X (Formerly Twitter)` | Yes                |
