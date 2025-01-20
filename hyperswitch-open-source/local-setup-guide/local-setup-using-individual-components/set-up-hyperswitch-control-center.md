---
icon: laptop
---

# Set up Hyperswitch Control Center

### Prerequisites

1. Node.js and npm installed on your machine.

### Installation Steps

Follow these simple steps to set up Hyperswitch on your local machine.

1.  Clone the repository:

    ```
    git clone https://github.com/juspay/hyperswitch-control-center.git
    ```
2.  Navigate to the project directory:

    ```
     cd hyperswitch-control-center
    ```
3.  Install project dependencies:

    ```
    npm install
    ```
4.  Update the config.toml file

    ```
    api_url = your-backend-url
    sdk_url = your-sdk-url
    # To view Mixpanel events on the Mixpanel dashboard, you must add your Mixpanel token; otherwise, you can ignore this requirement.
    ```
5.  Start the ReScript compiler:

    ```
    npm run re:start
    ```
6.  In another terminal window, start the development server:

    ```
    npm run start
    ```
7. Access the application in your browser at [http://localhost:9000](http://localhost:9000/).

### Running with Docker

1. `docker run -p 9000:9000 -e default__endpoints__api_url=your-backend-url -e default__endpoints__sdk_url=your-sdk-url juspaydotin/hyperswitch-control-center:latest`

### Accessing the Application

Once the containers are up and running, you can access the application by navigating to [http://localhost:9000](http://localhost:9000/) in your web browser.

