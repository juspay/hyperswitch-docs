---
description: This section will guide you to set up your own card vault from scratch
---

# 🗄 Card Vault installation

***

The Hyperswitch Card Vault [(Repo Link)](https://github.com/juspay/tartarus), is a highly performant and a secure locker to save sensitive data such as payment card details, bank account details etc.&#x20;

It is designed in an polymorphic manner to handle and store any type of sensitive information making it highly scalable with extensive coverage of payment methods and processors.

Tartarus is built with a GDPR compliant personal identifiable information (PII) storage and  secure encryption algorithms to be fully compliant with PCI DSS requirements.

## How does it work?

<figure><img src="../../.gitbook/assets/general-block-diagram.png" alt=""><figcaption><p>Locker usage flow</p></figcaption></figure>

* The Hyperswitch application communicates with Tartarus via a middleware.&#x20;
* All requests and responses to and from the middleware are signed and encrypted with the JWS and JWE algorithms.&#x20;
* The locker supports CRD APIs on the /data and /cards endpoints - [API Reference](https://api-reference.hyperswitch.io/api-reference/cards/add-data-in-locker)
* Cards are stored against the combination of merchant and customer identifiers.&#x20;
* Internal hashing checks are in place to avoid data duplication.&#x20;

## Key Hierarchy

Master Key - AES generated key to that is encrypted/decrypted by the custodian keys to run the locker and associated configurations.

Custodian Keys - AES generated key that is used to encrypt and decrypt the master key. It broken into two keys (`key 1` and `key 2`) and available with two custodians to enhance security.

<figure><img src="../../.gitbook/assets/locker-key-hierarchy.png" alt=""><figcaption><p>Key Hierarchy of Tartarus</p></figcaption></figure>

## Setting up your Card Locker:

### Cloud Setup

#### Creating EC2 instance

Log into your AWS account and create a new EC2 instance preferably on a t3.medium machine with an AMI that supports docker like Amazon Linux 2.

<figure><img src="../../.gitbook/assets/Screenshot 2023-11-21 at 5.12.15 PM.png" alt=""><figcaption><p>Create and launch an EC2 Instance</p></figcaption></figure>

{% hint style="danger" %}
Ensure to manage your instances' (EC2 and RDS) security group rules are selectively enabled for the application subnet and not exposed to the internet. (The locker application should not be accessible via internet)
{% endhint %}

#### Install docker on the EC2 instance

Connect to your EC2 instance using the SSH client via a terminal

<figure><img src="../../.gitbook/assets/Screenshot 2023-11-23 at 2.23.35 PM.png" alt=""><figcaption><p>Connecting to your EC2 instance</p></figcaption></figure>

Once you SSH into the EC2 instance, run the following commands on the terminal to install docker

```bash
amazon-linux-extras install docker -y
```

Run the following command to start docker

```bash
systemctl start docker
```

After starting the docker run the following command to pull the `hyperswitch-card-vault` docker image

```bash
docker pull juspaydotin/hyperswitch-card-vault:latest
```

#### Setup Database (AWRDS)

* Create an RDS with the latest `postgres` preferably with `Aurora` and select a storage of `t4g medium`. (Record the master username and password securely for further use in setup)
* Ensure to add the EC2 instance to database's inbound/outbound rules and vice-versa (In the default set up the rules are set to allow all traffic)

<figure><img src="../../.gitbook/assets/Screenshot 2023-11-20 at 5.53.56 PM.png" alt=""><figcaption><p>Creating a database using RDS</p></figcaption></figure>

* To run the migrations install `psql` in the EC2 instance

```bash
sudo yum install postgresql-server postgresql-contrib
```

```bash
sudo amazon-linux-extras install postgresql10
```

* Run the migrations using the following commands

```bash
export DB_USER="<your-database-user>"
export DB_PASS="<your-database-password>" # this is not the master password
export DB_NAME="locker"

sudo psql -h <database-url> -U <master-username> -W -e -c \
 "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
sudo psql -h <database-url> -U <master-username> -W -e -c \
 "CREATE DATABASE $DB_NAME WITH OWNER = $DB_USER;"
```

Now, open sql interactively with the following command

```bash
sudo psql -h <database-url> -U $DB_USER -W locker
```

and paste the contents from the below mentioned migration files

* [FILE - 1](https://github.com/juspay/hyperswitch-card-vault/blob/main/migrations/2023-10-21-104200\_create-tables/up.sql): Creating initial tables
* [FILE - 2](https://github.com/juspay/hyperswitch-card-vault/blob/main/migrations/2023-10-26-072935\_duplication-table/up.sql): Creating duplication tables

#### Setup KMS

Before setting up KMS, create a new IAM role for your EC2 instance to allow connection to KMS. Use `AWS service` as the trusted entity type and add permissions for `AWSKeyManagementServicePowerUser` and create an inline policy allowing `All KMS actions`.

Now, create a KMS key pair on AWS with the key type as `symmetric` and the key usage as Encrypt and Decrypt. Ensure to add the IAM role above in the key administrative permissions and key usage permissions.

<figure><img src="../../.gitbook/assets/Screenshot 2023-11-21 at 2.37.39 PM.png" alt=""><figcaption><p>Setting up KMS</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screenshot 2023-11-21 at 5.08.39 PM.png" alt=""><figcaption><p>Adding IAM roles</p></figcaption></figure>

#### Generating the keys

To generate the `master key` and the `custodian keys` use the following command after cloning the repository.

```bash
cargo run --bin utils -- master-key
```

To generate the `JWE` and `JWS` keys run the following commands

```
# Generating the private keys
openssl genrsa -out locker-private-key.pem 2048
openssl genrsa -out tenant-private-key.pem 2048

# Generating the public keys
openssl rsa -in locker-private-key.pem -pubout -out locker-public-key.pem
openssl rsa -in locker-private-key.pem -pubout -out tenant-public-key.pem
```

{% hint style="info" %}
We recommend generating the Master and JWE/JWS keys as mentioned below in the local setup guide outside of this EC2 machine for better security
{% endhint %}

#### KMS encrypting the keys

After generating your keys and setting up of KMS, run the following command to KMS encrypt the keys.

```bash
function kms_encrypt() {
    xargs -I {} -0 echo -n "{}" | xargs -I {} -0 aws kms encrypt --key-id <your-kms-key-id> --region <your-kms-region> --plaintext "{}"
}
# substitute this in the above mentioned envfile (LOCKER__DATABASE__PASSWORD)
echo -n "<database password>" | kms_encrypt

# substitute this in the above mentioned envfile (LOCKER__SECRETS__MASTER_KEY)
echo -n "<generated master key>" | kms_encrypt

# substitute this in the above mentioned envfile (LOCKER__SECRETS__LOCKER_PRIVATE_KEY)
echo -n '<locker private key>' | kms_encrypt

# substitute this in the above mentioned envfile (LOCKER__SECRETS__TENANT_PUBLIC_KEY)
echo -n '<tenant public key>' | kms_encrypt
 
```

#### Update Config files

* Create an `env-file` in the instance and paste the environment variables mentioned below

```bash
LOCKER__SERVER__HOST=0.0.0.0
LOCKER__SERVER__PORT=8080
LOCKER__LOG__CONSOLE__ENABLED=true
LOCKER__LOG__CONSOLE__LEVEL=DEBUG
LOCKER__LOG__CONSOLE__LOG_FORMAT=default

LOCKER__DATABASE__USERNAME= # add the database user created above
LOCKER__DATABASE__PASSWORD= # add the kms encrypted password here (kms encryption process mentioned below)
LOCKER__DATABASE__HOST= # add the host of the database (database url)
LOCKER__DATABASE__PORT=5432 # if used differently mention here
LOCKER__DATABASE__DBNAME=locker

LOCKER__LIMIT__REQUEST_COUNT=100
LOCKER__LIMIT__DURATION=60

LOCKER__SECRETS__TENANT=hyperswitch
LOCKER__SECRETS__MASTER_KEY= # kms encrypted master key
LOCKER__SECRETS__LOCKER_PRIVATE_KEY= # kms encrypted locker private key
LOCKER__SECRETS__TENANT_PUBLIC_KEY= # kms encrypted locker private key

LOCKER__KMS__KEY_ID= # kms id used to encrypt it below
LOCKER__KMS__REGION= # kms region used

```

#### Running the Locker

After the above changes are done, run the following command to start the locker

```bash
docker run --env-file envfile -d --net=host juspaydotin/hyperswitch-card-vault:latest
```

#### Unlock the locker

Once the locker is up and running, use the 2 key custodian keys generated earlier securely to unlock the locker for use.

The following cURLs are to be used to provide keys

<pre class="language-bash"><code class="lang-bash"># temporary turn of saving to history to run the following commands
unset HISTFILE 

# key 1
<strong> curl -X 'POST' \
</strong>  'localhost:8080/custodian/key1' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": &#x3C;key 1>
}'

# key 2
 curl -X 'POST' \
  'localhost:8080/custodian/key2' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": &#x3C;key 2>
}'

# decrypt
<strong> curl -X 'POST' 'localhost:8080/custodian/decrypt'
</strong></code></pre>

If the last cURL replies with `Decrypted Successfully`, we are ready to use the locker.

#### Integrating it with Hyperswitch&#x20;

To start using it with Hyperswitch application update the following environment variables while deploying the Hyperswitch Server.

```bash
ROUTER__LOCKER__HOST= # add the ip address of the ec2 instance created
ROUTER__JWEKEY__VAULT_ENCRYPTION_KEY= # add the JWE public key of locker generated above
ROUTER__JWEKEY__VAULT_PUBLIC_KEY= # add the JWE private key of tenant generated above
```

### Local Setup

#### Cloning the repository

```bash
https://github.com/juspay/tartarus.git
```

#### Generating Master key

To generate the `master key` and the `custodian keys` use the following command after cloning the repository.

```bash
cargo run --bin utils -- master-key
```

#### Generating JWE and JWS keys

`JWE` and `JWS` keys are asymmetric key pairs which should be present with both the locker and the application that is using it (tenant). Here you need to generate 2 key pairs one for the tenant and one for the locker, the below mentioned command can be used to generate the key pairs

```bash
# Generating the private keys
openssl genrsa -out locker-private-key.pem 2048
openssl genrsa -out tenant-private-key.pem 2048

# Generating the public keys
openssl rsa -in locker-private-key.pem -pubout -out locker-public-key.pem
openssl rsa -in locker-private-key.pem -pubout -out tenant-public-key.pem
```

#### Set up configuration files

The configuration can be updated by replacing the content of `config/development.toml` with the respective configuration values.

```bash
[server] 
host = "0.0.0.0"
```

#### Setting up the database

You can use the `diesel-cli` to run the database migrations. To install the `diesel-cli`, run the following command.

```bash
cargo install diesel_cli --no-default-features --features "postgres"
```

Use the following command to create the required database and tables

```bash
diesel migration --database-url postgres://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME run
```

### Running the locker

You can run the locker either through the docker setup or using cargo. The following sections list the steps for each of these tracks

#### Docker <a href="#user-content-docker" id="user-content-docker"></a>

To build the docker image, run the following command

```bash
docker build -t locker:latest .
```

After the image is built, you can create an environment file `.env`, which can be passed to the docker container with the required config values.&#x20;

```bash
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

```bash
docker run --env-file .env -d locker:latest
```

#### Cargo <a href="#user-content-cargo" id="user-content-cargo"></a>

If you wish to directly run the executable, the config values to the `config/development.toml` file and run the following command to start the locker

```bash
cargo run --release --features release
```

### Testing your setup

After starting the locker, run the following command to check health.

```bash
curl http://localhost:8080/health
```

On a successful set up you should be getting the following output:

```bash
Health is good
```

Congratulations! You now have the Card Locker up and running. \
\
**To test if you have configured the keys properly, run the following curls**

<pre class="language-bash"><code class="lang-bash"><strong>curl -X 'POST' \
</strong>  'https://editor.swagger.io/custodian/key1' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": "763bbghs5bd51820acbc8ac20c674254"
}'
</code></pre>

```bash
curl -X 'POST' \
  'https://editor.swagger.io/custodian/key2' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": "801bb63c1bd51820acbc8ac20c674675"
}'
```

After this hit the decrypt endpoint to test your configuration

<pre class="language-bash"><code class="lang-bash"><strong>curl -X 'POST' \
</strong>  'https://editor.swagger.io/custodian/decrypt' \
  -H 'accept: text/plain' \
  -d ''
</code></pre>

You should be getting the following output after the correct configuration&#x20;

```
Decryption successful
```

### Integrating it with Hyperswitch&#x20;

To start using it with Hyperswitch update the following environment variables while deploying.

```bash
ROUTER__LOCKER__HOST= # add the ip address of the ec2 instance created
ROUTER__JWEKEY__VAULT_ENCRYPTION_KEY= # add the JWE public key of locker generated above
ROUTER__JWEKEY__VAULT_PUBLIC_KEY= # add the JWE private key of tenant generated above
```

{% hint style="info" %}
_Note:_ You will have to get your card vault **implementation** audited for PCI Compliance. You can find the list of Qualified Security Assessors - [here](https://listings.pcisecuritystandards.org/assessors\_and\_solutions/qualified\_security\_assessors)
{% endhint %}
