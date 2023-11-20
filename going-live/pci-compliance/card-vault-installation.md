---
description: This section will guide you to set up your own card vault from scratch
---

# 🗄 Card Vault installation

***

The Hyperswitch Card Vault - [Tartarus](https://github.com/juspay/tartarus), is a highly performant and a secure locker to save sensitive data such as payment card details, bank account details etc.&#x20;

It is designed in an polymorphic manner to handle and store any type of sensitive information making it highly scalable with extensive coverage of payment methods and processors.

Tartarus is built with a GDPR compliant personal identifiable information (PII) storage and  secure encryption algorithms to be fully compliant with PCI DSS requirements.

## How does it work?

<figure><img src="../../.gitbook/assets/general-block-diagram.png" alt=""><figcaption><p>Locker usage flow</p></figcaption></figure>

* The Hyperswitch application communicates with Tartarus via a middleware.&#x20;
* All requests and responses to and from the middleware are signed and encrypted with the JWS and JWE algorithms.&#x20;
* The locker supports CRD APIs on the /data and /cards endpoints - [API Reference](https://api-reference.hyperswitch.io/locker-api-reference/)
* Cards are stored against the combination of merchant and customer identifiers.&#x20;
* Internal hashing checks are in place to avoid data duplication.&#x20;

## Key Hierarchy

Master Key - AES generated key to that is encrypted/decrypted by the custodian keys to run the locker and associated configurations.

Custodian Keys - AES generated key that is used to encrypt and decrypt the master key. It broken into two keys (`key 1` and `key 2`) and available with two custodians to enhance security.

<figure><img src="../../.gitbook/assets/locker-key-hierarchy.png" alt=""><figcaption><p>Key Hierarchy of Tartarus</p></figcaption></figure>

## Setting up your Card Locker:

### Pre-requisites

#### Cloning the repository

```
https://github.com/juspay/tartarus.git
```

#### Generating Keys

To generate the `master key` and the `custodian keys` use the following command after cloning the repository.

```
cargo run --bin utils -- master-key
```

`JWE` and `JWS` keys are asymmetric key pairs which should be present with both the locker and the application that is using it (tenant). Here you need to generate 2 key pairs one for the tenant and one for the locker, the below mentioned command can be used to generate the key pairs

```
# Generating the private keys
openssl genrsa -out locker-private-key.pem 2048
openssl genrsa -out tenant-private-key.pem 2048

# Generating the public keys
openssl rsa -in locker-private-key.pem -pubout -out locker-public-key.pem
openssl rsa -in locker-private-key.pem -pubout -out tenant-public-key.pem
```

#### Set up configuration files

The configuration can be updated by replacing the content of `config/development.toml` with the respective configuration values.

```
[server] 
host = "0.0.0.0"
```

#### Setting up the database

You can use the `diesel-cli` to run the database migrations. To install the `diesel-cli`, run the following command.

```
cargo install diesel_cli --no-default-features --features "postgres"
```

Use the following command to create the required database and tables

```
diesel migration --database-url postgres://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME run
```

### Running the locker

You can run the locker either through the docker setup or using cargo. The following sections list the steps for each of these tracks

#### Docker <a href="#user-content-docker" id="user-content-docker"></a>

To build the docker image, run the following command

```
docker build -t locker:latest .
```

After the image is built, you can create an environment file `.env`, which can be passed to the docker container with the required config values.&#x20;

```
LOCKER__SERVER__HOST=0.0.0.0
LOCKER__SERVER__PORT=8080
LOCKER__LOG__CONSOLE__ENABLED=true
LOCKER__LOG__CONSOLE__LEVEL=DEBUG
LOCKER__LOG__CONSOLE__LOG_FORMAT=default

LOCKER__DATABASE__USERNAME=
LOCKER__DATABASE__PASSWORD=
LOCKER__DATABASE__HOST=
LOCKER__DATABASE__PORT=
LOCKER__DATABASE__DBNAME=

LOCKER__SECRETS__TENANT=
LOCKER__SECRETS__MASTER_KEY=
LOCKER__SECRETS__LOCKER_PRIVATE_KEY=
LOCKER__SECRETS__TENANT_PUBLIC_KEY=

LOCKER__KMS__KEY_ID=
LOCKER__KMS__REGION=
```

You can now start the locker by running the following command

```
docker run --env-file .env -d locker:latest
```

#### Cargo <a href="#user-content-cargo" id="user-content-cargo"></a>

If you wish to directly run the executable, the config values to the `config/development.toml` file and run the following command to start the locker

```
cargo run --release --features release
```

### Testing your setup

After starting the locker, run the following command to check health.

```
curl http://localhost:8080/health
```

On a successful set up you should be getting the following output:

```
Health is good
```

Congratulations! You now have the Card Locker up and running. \
\
**To test if you have configured the keys properly, run the following curls**

```
curl -X 'POST' \
  'https://editor.swagger.io/custodian/key1' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": "763bbghs5bd51820acbc8ac20c674254"
}'
```

```
curl -X 'POST' \
  'https://editor.swagger.io/custodian/key2' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": "801bb63c1bd51820acbc8ac20c674675"
}'
```

After this hit the decrypt endpoint to test your configuration

```
curl -X 'POST' \
  'https://editor.swagger.io/custodian/decrypt' \
  -H 'accept: text/plain' \
  -d ''
```

You should be getting the following output after the correct configuration&#x20;

```
Decryption successful
```

### Integrating it with Hyperswitch&#x20;

To start using it with Hyperswitch update the following environment variables while deploying.

```
ROUTER__LOCKER__HOST=
ROUTER__JWEKEY__VAULT_ENCRYPTION_KEY=
```

{% hint style="info" %}
_Note:_ You will have to get your card vault **implementation** audited for PCI Compliance. You can find the list of Qualified Security Assessors - [here](https://listings.pcisecuritystandards.org/assessors\_and\_solutions/qualified\_security\_assessors)
{% endhint %}
