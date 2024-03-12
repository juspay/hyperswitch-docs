---
description: Run the checkout page locally
---

# 💻 Run web client

{% hint style="info" %}
In this section, you will run the Hyperswitch web client SDK on your machine
{% endhint %}

Accept payments from around the globe with a secure, Unified Checkout that gives your customers the best in class payment experience

## Video

***

{% embed url="https://youtu.be/1ZJW6ioxJQM" %}

## Clone the repository <a href="#user-content-clone-the-repository" id="user-content-clone-the-repository"></a>

Clone the repository from Github and save in your folder.

```bash
git clone https://github.com/juspay/hyperswitch-web.git
cd hyperswitch-web
```

Once the repository is cloned, switch to the project directory.

## Setup the repository <a href="#user-content-setup-the-repository" id="user-content-setup-the-repository"></a>

First install all the node modules by running the following command

```bash
npm install
```

Once the installation is successful, you can run the app with the following command -&#x20;

```bash
npm run start:dev
```

This will trigger a build of the project. On a successful build, you should see a message `Compiled successfully` in your terminal.&#x20;

Now you can proceed with launching the playground.&#x20;

{% hint style="info" %}
NOTE: The **playground** is a full stack integrated demo app where you can test your payments. In a separate terminal, run the following command to start the app on your local machine.
{% endhint %}

```bash
npm run start:playground
```

This step will prompt you to enter 3 details that you must have received in the previous step when you set up the app server -&#x20;

| **Publishable Key**                                   |  This is a public key that resides on your client side for authentication                                                                                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Secret Key**                                        | This is the API key which should only be restricted to your app server                                                                                                                      |
| **Self-hosted Hyperswitch Server URL**                |  This is the URL of your self-hosted[ **Hyperswitch app server**](run-app-server.md) (for eg., `http://localhost:8080`)                                                                     |
| **Application Server URL (URL of your node server)**  | This is the URL of your playground server. Please note that this is just a playground setup for quick development and hence contains the server.js file. (for eg., `http://localhost:5252)` |

{% hint style="success" %}
Congratulations! You will now see the web app running on `http://localhost:9060` where you can test your payments.
{% endhint %}

##

<details>

<summary>Troubleshooting/ FAQs</summary>



* **I cannot see the Web app playground running on `http://localhost:9060`**\
  Please recheck the publishable key and secret key that you have provided along with the URLs that you entered during the setup. Make sure that the self-hosted Hyperswitch server URL is your app server URL and the application server URL is the playground server URL\

* **npm commands are throwing errors**\
  Please ensure you have the latest version of npm installed on your system. Once that is done, please reinstall the client application. You can also use `yarn` instead.\

* **I don't know my Self-hosted Hyperswitch Server URL**\
  You should get this as an output when you ran the app server. Running the app server is a pre-requisite for the client playground to run. Please ensure that you have followed steps for[ running the app server](run-app-server.md).\


</details>

## Next step:

{% content-ref url="run-control-center.md" %}
[run-control-center.md](run-control-center.md)
{% endcontent-ref %}
