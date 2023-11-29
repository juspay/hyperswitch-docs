---
description: Deploy web client on AWS
---

# Production ready deployment

{% hint style="info" %}
In this section, you will be deploying the web client on your AWS account
{% endhint %}

We use webpack to generate a build file and recommend the same to be used but you may use your own bundler. In the `webpack.common.js` you can change your backend endpoints and the URL of where you host your SDK.

```javascript
let backendEndPoint ="YOUR_HOSTED_APP_SERVER_URL"
```

\
After running `npm run build`, you will get a **`dist`** folder, which you can then deploy to the service of your choice.

In our case, we use AWS , a combination of S3 and Cloudfront, as our CDN, for our deployment and hosting. We would recommend the same for everybody, but feel free to use any other Cloud services for hosting.\


**End goal**

* Hyperswitch Web SDK deployed and active on your AWS account.
* The script to be accessible to anybody who tries to fetch it and be able to open the SDK using that.

**What do you need to get started**

* An AWS account (you can create an account [here](https://portal.aws.amazon.com/billing/signup?refid=em\_127222\&redirect\_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email) if you do not have one)

**Let’s begin!**

**Step 1**

Open up your AWS console and click on S3 in Services section or search for the same.

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

**Step 2**

Select Buckets on the left sidebar.

<figure><img src="../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

**Step 3**

Click on create bucket and configure your bucket according to your needs.

<figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

**Step 4**

Click on your newly created bucket name.

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

**Step 5**

Click on upload, and upload your **`dist`** folder.

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

**Step 6**\
\
After uploading, click on the path where HyperLoader.js is. You will be taken to a page with object “Properties”. There you will find Object URL which will look something like this.\
`https://{domain}.s3.amazonaws.com/{path}/HyperLoader.js`

<figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

**Great!**\
Your Web Client is hosted and can be accessed by this URL.

Now that the web client is hosted, you can integrate it with your app and go live. The detailed steps are given below.

##
