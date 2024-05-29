---
description: >-
  This guide will walk you through the process of setting up and running the app
  server and control center on your local machine using Docker
---

# 💻 Local Setup

{% hint style="info" %}
Let's hit the ground running – within five minutes, you’ll see a complete end-to-end example of installing Hyperswitch and making a Payment via a Payment provider of your choice. So, let’s get started!
{% endhint %}

{% embed url="https://youtu.be/6yJCvskbc80" %}

## **Setting up with Docker**

If you don't already have Docker, you can [download](https://docs.docker.com/get-docker/) it from the official Docker website. Once Docker is installed, launch the Docker app, then use the following commands at the command line to clone the Hyperswitch repository.

```
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
```

Once the repository is cloned, switch to the project directory.

```
cd hyperswitch
```

Now, we'll start all services using Docker Compose. This will pull Hyperswitch Docker images and then start the server. Wait for the `migration_runner` container to finish running migrations (approximately 2 minutes) before proceeding further.

```
docker compose up -d
```

Congratulations! You've now setup Hyperswitch in your local machine. In order to verify that the server is up and running hit the health endpoint.

```
curl --head --request GET 'http://localhost:8080/health'
```

The expected response here is `200 OK` status code. This indicates that the server and all of its dependent services such as the database and Redis are functioning correctly.

**Access the Control Centre in your browser at** [**http://localhost:9000**](http://localhost:9000/)**.**

In the next chapter, we'll **run payments** through your local Hyperswitch setup by setting up the necessary accounts, API credentials and try out payments and refunds.

If you're **looking to Contribute to Hyperswitch**, try [setting up a **development environment** using Docker Compose](https://github.com/juspay/hyperswitch/blob/main/docs/try\_local\_system.md#set-up-a-development-environment-using-docker-compose).&#x20;

## Next step:

{% content-ref url="account-setup/" %}
[account-setup](account-setup/)
{% endcontent-ref %}
