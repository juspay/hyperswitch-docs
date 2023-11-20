---
description: >-
  Accept payments from around the globe with a secure, Unified Checkout that
  gives your customers the best in class payment experience
---

# 💻 Run web client

{% hint style="info" %}
In this section, you will run the Hyperswitch web client SDK on your machine.&#x20;
{% endhint %}

#### [Clone the repository](https://github.com/juspay/hyperswitch-web/tree/main#clone-the-repository) <a href="#user-content-clone-the-repository" id="user-content-clone-the-repository"></a>

Clone the repository from Bitbucket and save in your folder.

```bash
git clone https://github.com/juspay/hyperswitch-web.git
cd hyperswitch-web
```

Once the repository is cloned, switch to the project directory.

#### [Setup the repository](https://github.com/juspay/hyperswitch-web/tree/main#setup-the-repository) <a href="#user-content-setup-the-repository" id="user-content-setup-the-repository"></a>

First install all the node modules by running the following command

```bash
npm install
```

Once the installation is successful, you can run the app with the following command -&#x20;

```bash
npm run start:dev
```

This will trigger a build of the project. On a successful build, you should see a message `Compiled successfully` in your terminal.&#x20;

Now you can proceed with launching the playground. The playground is a demo app where you can test your payments. In a separate terminal, run the following command to start the app on your local machine.

```bash
npm run start:playground
```

This step will prompt you to enter 3 details that you must have received in the previous step when you set up the app server -&#x20;

**Publishable Key -** This is a public key that resides on your client side for authentication

**Secret Key -** This is the API key which should only be restricted to your app server

**Server URL -** This is the URL of your app server (for eg., `http://localhost:8080`)



Congratulations! You will now see the web app running on `http://localhost:4242` where you can test your payments.

