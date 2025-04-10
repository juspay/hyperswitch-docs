---
icon: server
---

# Backend

{% hint style="danger" %}
This setup is meant for development. If you want a quick trial of Hyperswitch (without contributing), use [this guide](https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker).
{% endhint %}

## Supported Methods:

<table data-view="cards"><thead><tr><th></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Using docker compose</strong></mark></td></tr><tr><td><mark style="color:blue;"><strong>Rust environment setup along with other dependencies</strong></mark></td></tr></tbody></table>

## Set up a development environment using Docker Compose

1. Install [Docker Compose](https://docs.docker.com/compose/install/).
2.  Clone the repository and switch to the project directory:

    ```bash
    git clone https://github.com/juspay/hyperswitch
    cd hyperswitch
    ```
3. (Optional) Configure the application using the [`config/docker_compose.toml`](https://github.com/juspay/hyperswitch/blob/main/config/docker_compose.toml) file. The provided configuration should work as is. If you do update the `docker_compose.toml` file, ensure to also update the corresponding values in the [`docker-compose.yml`](https://github.com/juspay/hyperswitch/blob/main/docker-compose.yml) file.
4.  Start all the services using Docker Compose:

    ```bash
    docker compose --file docker-compose-development.yml up -d
    ```

    This will compile the payments router, the primary component within hyperswitch and then start it. Depending on the specifications of your machine, compilation can take around 15 minutes.
5. (Optional) You can also choose to [start the scheduler and/or monitoring services](set-up-hyperswitch-backend.md#running-additional-services) in addition to the payments router.
6.  Verify that the server is up and running by hitting the health endpoint:

    ```bash
    curl --head --request GET 'http://localhost:8080/health'
    ```

    If the command returned a `200 OK` status code, proceed with [trying out our APIs](set-up-hyperswitch-backend.md#try-out-our-apis).

## Set up a Rust environment and other dependencies

If you are using `nix`, please skip the setup dependencies step and jump to [Set up the database](set-up-hyperswitch-backend.md#set-up-the-database).

### Set up dependencies on Ubuntu-based systems

This section of the guide provides instructions to install dependencies on Ubuntu-based systems. If you're running another Linux distribution, install the corresponding packages for your distribution and follow along.

1.  Install the stable Rust toolchain using `rustup`:

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    When prompted, proceed with the `default` profile, which installs the stable toolchain.

    Optionally, verify that the Rust compiler and `cargo` are successfully installed:

    ```bash
    rustc --version
    ```

    _Be careful when running shell scripts downloaded from the Internet. We only suggest running this script as there seems to be no `rustup` package available in the Ubuntu package repository._
2.  Install PostgreSQL and start the `postgresql` systemd service:

    ```bash
    sudo apt update
    sudo apt install postgresql postgresql-contrib libpq-dev
    systemctl start postgresql.service
    ```

    If you're running any other distribution than Ubuntu, you can follow the installation instructions on the [PostgreSQL documentation website](https://www.postgresql.org/download/) to set up PostgreSQL on your system.
3.  Install Redis and start the `redis` systemd service:

    ```bash
    sudo apt install redis-server
    systemctl start redis.service
    ```

    If you're running a distribution other than Ubuntu, you can follow the installation instructions on the [Redis website](https://redis.io/docs/getting-started/installation/) to set up Redis on your system.
4.  Install `diesel_cli` using `cargo`:

    ```bash
    cargo install diesel_cli --no-default-features --features postgres
    ```
5.  Make sure your system has the `pkg-config` package and OpenSSL installed

    ```bash
    sudo apt install pkg-config libssl-dev
    ```

Once you're done with setting up the dependencies, proceed with [setting up the database](set-up-hyperswitch-backend.md#set-up-the-database).

### Set up dependencies on Windows (Ubuntu on WSL2)

This section of the guide provides instructions to install dependencies on Ubuntu on WSL2. If you prefer running another Linux distribution, install the corresponding packages for your distribution and follow along.

1.  Install Ubuntu on WSL:

    ```bash
    wsl --install -d Ubuntu
    ```

    Refer to the [official installation docs](https://learn.microsoft.com/en-us/windows/wsl/install) for more information. Launch the WSL instance and set up your username and password. The following steps assume that you are running the commands within the WSL shell environment.

    > Note that a `SIGKILL` error may occur when compiling certain crates if WSL is unable to use sufficient memory. It may be necessary to allow up to 24GB of memory, but your mileage may vary. You may increase the amount of memory WSL can use via a `.wslconfig` file in your Windows user folder, or by creating a swap file in WSL itself. Refer to the [WSL configuration documentation](https://learn.microsoft.com/en-us/windows/wsl/wsl-config/) for more information.
2.  Install the stable Rust toolchain using `rustup`:

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    When prompted, proceed with the `default` profile, which installs the stable toolchain.

    Optionally, verify that the Rust compiler and `cargo` are successfully installed:

    ```
    rustc --version
    ```

    _Be careful when running shell scripts downloaded from the Internet. We only suggest running this script as there seems to be no `rustup` package available in the Ubuntu package repository._
3.  Install PostgreSQL and start the `postgresql` service:

    ```bash
    sudo apt update
    sudo apt install postgresql postgresql-contrib libpq-dev
    sudo service postgresql start
    ```

    For more information, refer to the docs for [installing PostgreSQL on WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-postgresql). If you're running any other distribution than Ubuntu, you can follow the installation instructions on the [PostgreSQL documentation website](https://www.postgresql.org/download/) to set up PostgreSQL on your system.
4.  Install Redis and start the `redis-server` service:

    ```bash
    sudo apt install redis-server
    sudo service redis-server start
    ```

    For more information, refer to the docs for [installing Redis on WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-redis). If you're running a distribution other than Ubuntu, you can follow the installation instructions on the [Redis website](https://redis.io/docs/getting-started/installation/) to set up Redis on your system.
5.  Make sure your system has the packages necessary for compiling Rust code:

    ```bash
    sudo apt install build-essential
    ```
6.  Install `diesel_cli` using `cargo`:

    ```bash
    cargo install diesel_cli --no-default-features --features postgres
    ```
7.  Make sure your system has the `pkg-config` package and OpenSSL installed:

    ```bash
    sudo apt install pkg-config libssl-dev
    ```

Once you're done with setting up the dependencies, proceed with [setting up the database](set-up-hyperswitch-backend.md#set-up-the-database).

### Set up dependencies on Windows

We'll be using [`winget`](https://github.com/microsoft/winget-cli) in this section of the guide, where possible. You can opt to use your favorite package manager instead.

1. Install PostgreSQL database, following the [official installation docs](https://www.postgresql.org/download/windows/).
2. Install Redis, following the [official installation docs](https://redis.io/docs/getting-started/installation/install-redis-on-windows).
3.  Install rust with `winget`:

    ```bash
    winget install -e --id Rustlang.Rust.GNU
    ```
4.  Install `diesel_cli` using `cargo`:

    ```bash
    cargo install diesel_cli --no-default-features --features postgres
    ```
5.  Install OpenSSL with `winget`:

    ```bash
    winget install openssl
    ```

Once you're done with setting up the dependencies, proceed with [setting up the database](set-up-hyperswitch-backend.md#set-up-the-database).

### Set up dependencies on MacOS

We'll be using [Homebrew](https://brew.sh/) in this section of the guide. You can opt to use your favorite package manager instead.

1.  Install the stable Rust toolchain using `rustup`:

    ```bash
    brew install rustup
    rustup default stable
    ```

    Optionally, verify that the Rust compiler and `cargo` are successfully installed:

    ```bash
    rustc --version
    ```
2.  Install PostgreSQL and start the `postgresql` service:

    ```bash
    brew install postgresql@14
    brew services start postgresql@14
    ```

    If a `postgres` database user was not already created, you may have to create one:

    ```bash
    createuser -s postgres
    ```
3.  Install Redis and start the `redis` service:

    ```bash
    brew install redis
    brew services start redis
    ```
4.  Install `diesel_cli` using `cargo`:

    ```bash
    cargo install diesel_cli --no-default-features --features postgres
    ```

    If linking `diesel_cli` fails due to missing `libpq` (if the error message is along the lines of `cannot find -lpq`), you may also have to install `libpq` and reinstall `diesel_cli`:

    ```bash
    brew install libpq
    export PQ_LIB_DIR="$(brew --prefix libpq)/lib"

    cargo install diesel_cli --no-default-features --features postgres
    ```

    You may also choose to persist the value of `PQ_LIB_DIR` in your shell startup file like so:

    ```bash
    echo 'PQ_LIB_DIR="$(brew --prefix libpq)/lib"' >> ~/.zshrc
    ```
5.  Install a command runner called `just`:

    In order to make running migrations easier, you can use a command runner called just

    ```bash
    cargo install just
    ```

Once you're done with setting up the dependencies, proceed with [setting up the database](set-up-hyperswitch-backend.md#set-up-the-database).

### Set up the database

1.  Create the database and database users, modifying the database user credentials and database name as required.

    ```bash
    export DB_USER="db_user"
    export DB_PASS="db_pass"
    export DB_NAME="hyperswitch_db"
    ```

    On Ubuntu-based systems (also applicable for Ubuntu on WSL2):

    ```bash
    sudo -u postgres psql -e -c \
       "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
    sudo -u postgres psql -e -c \
       "CREATE DATABASE $DB_NAME;"
    ```

    On MacOS:

    ```bash
    psql -e -U postgres -c \
       "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
    psql -e -U postgres -c \
       "CREATE DATABASE $DB_NAME"
    ```
2.  Clone the repository and switch to the project directory:

    ```bash
    git clone https://github.com/juspay/hyperswitch
    cd hyperswitch
    ```
3.  Run database migrations:

    Export the `DATABASE_URL` env variable

    ```bash
    export DATABASE_URL=postgres://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME
    ```

    Run the migrations

    * If you have just installed

    ```bash
    just migrate
    ```

    * Using the diesel-cli command

    ```bash
    diesel migration run
    ```

Once you're done with setting up the database, proceed with configuring the application.

{% content-ref url="backend/configuring-and-running-the-application.md" %}
[configuring-and-running-the-application.md](backend/configuring-and-running-the-application.md)
{% endcontent-ref %}
