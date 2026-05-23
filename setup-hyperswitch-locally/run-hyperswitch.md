---
description: Use Docker to set up Hyperswitch app server
---

# 🐳 Run Hyperswitch

{% hint style="info" %}
Let's hit the ground running – in the first fifteen minutes, you’ll see a complete end-to-end example of installing Hyperswitch and making a Payment via a Payment provider of your choice. So, let’s get started!
{% endhint %}

{% embed url="https://www.loom.com/embed/a9b2b42fb72e4691a06e6121b330ebe9?sid=76bf9484-8f0f-462e-95a2-b4f551cd51ed" %}

## **Setting up with Docker**

If you don't already have Docker, you can [download](https://docs.docker.com/get-docker/) it from the official Docker website. Once Docker is installed, launch the Docker app, then use the following commands at the command line to clone the Hyperswitch repository.

```
git clone https://github.com/juspay/hyperswitch
```

Once the repository is cloned, switch to the project directory.

```
cd hyperswitch
```

Now, we'll start all services using Docker Compose. This will compile Hyperswitch and then start the server. Depending on the specifications of your machine, this compilation could take between 10 to 15 minutes.

```
docker compose up -d
```

Congratulations! you've now setup Hyperswitch in your local machine. In order to verify that the server is up and running hit the health endpoint.

```
curl --head --request GET 'http://localhost:8080/health'
```

The expected response here is `200 OK` status code. This indicates that the server and all of its dependent services such as the database and Redis are functioning correctly.

In the next chapter, we'll run payments through your local Hyperswitch setup by setting up the necessary accounts, API credentials and try out payments and refunds.

**Note** : In case you want to set up Hyperswitch from scratch in your local system, please goto this tutorial - [Setup Hyperswitch from scratch](broken-reference)&#x20;

## Run web client

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

**App Server URL -** This is the URL of your app server (for eg., `http://localhost:8080`)



Congratulations! You will now see the playground running on `http://localhost:4242` where you can test your payments.

