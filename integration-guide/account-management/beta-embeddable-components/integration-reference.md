---
description: >-
  Learn how to integrate Hyperswitch embeddable components into your React
  application using the SDK provider pattern for secure connector configuration
  management.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/integration-guide/account-management/beta-embeddable-components/integration-reference
---

# Integration Reference

This SDK allows you to embed the Hyperswitch connector configuration directly into your React application. It uses a provider pattern to manage authentication sessions via JWTs, ensuring your API keys never leak to the client.

Repository URL: [https://github.com/juspay/hyperswitch-control-center-embedded](https://github.com/juspay/hyperswitch-control-center-embedded)

Demo URL: [https://embedded-ssr.netlify.app/](https://embedded-ssr.netlify.app/)

## Prerequisites & Compatibility

Before you begin, ensure your environment meets the following requirements:

* Runtime: Node.js (v18+)
* Framework: React (v18.x - 20.x)
* Hyperswitch Credentials:
  * `API-Key` (Can be generated via Control Center)
  * `Profile-ID` (The specific merchant profile you are configuring)
* Support:
  * ✅ Vite
  * ✅ Webpack
  * ✅ Next.js
  * ✅ Create React App

## Step 1: Backend Setup (Server-Side)

Security Warning: Never expose your Hyperswitch API-Key on the frontend. You must create a backend endpoint that acts as a proxy

**Frontend → requests session → Your Backend → requests token (using API Key) → Hyperswitch API**

### Step 1.1: Create the Token Endpoint

Create a route (e.g., /embedded/hyperswitch) in your backend application.

Required Headers for Hyperswitch Call:

* api-key: Your secret API key.
* X-profile-id: The specific profile ID you want the embedded component to access.

{% code title="server.js" %}
```javascript
const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
const port = 4000;

app.use(cors());
app.use(express.json());

const HYPERSWITCH_BASE_URL = 'https://app.hyperswitch.io/api';

app.get('/embedded/hyperswitch', async (req, res) => {
  try {
    const response = await axios.get(
      `${HYPERSWITCH_BASE_URL}/api/embedded/token`,
      {
        headers: {
          'api-key': 'YOUR_ACTUAL_API_KEY_HERE',
          'X-profile-id': 'YOUR_PROFILE_ID_HERE',
          'Content-Type': 'application/json'
        }
      }
    );

    console.log('Hyperswitch Token Generated:', response.data);

    res.json({
      success: true,
      message: 'Token fetched successfully',
      data: response.data
    });

  } catch (error) {
    console.error('Error fetching token:', error.message);

    res.status(500).json({
      error: 'Failed to fetch token from Hyperswitch API',
      details: error.message
    });
  }
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

```
{% endcode %}

## Step 2: Choose Your Integration Method

You must choose one:

* Core (JavaScript Only / HTML)
* React Integration

### 2A: HTML-JS Integration

**2A.1 Install the package:**

```bash
npm install @juspay-tech/hyperswitch-control-center-embed-core
```

**2A.2 Import the SDK in Your Application**

Import (ES Module):

```javascript
import { loadHyperswitch } from "@juspay-tech/hyperswitch-control-center-embed-core";
```

**OR**

Import (CommonJS):

```javascript
const { loadHyperswitch } = require("@juspay-tech/hyperswitch-control-center-embed-core");
```

**2A.3: Example app.js Implementation**

```javascript
import { loadHyperswitch } from "@juspay-tech/hyperswitch-control-center-embed-core";

document.addEventListener("DOMContentLoaded", async function () {

  const fetchToken = async () => {
    try {
      const response = await fetch(
        "http://localhost:4000/embedded/hyperswitch",
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json"
          }
        }
      );

      if (!response.ok) {
        return undefined;
      }

      const responseData = await response.json();
      const token = responseData.data?.token || responseData.token;

      return token;

    } catch (err) {
      return undefined;
    }
  };

  const hyperswitch = loadHyperswitch({
    fetchToken: fetchToken
  });

  const connectorConfig = hyperswitch.create("connectors", {
    url: "https://app.hyperswitch.io/api"
  });

  connectorConfig.mount("#hyperswitch-root");

});

```

### 2B: React Integration

**2B.1 Install the package:**

```bash
npm install @juspay-tech/hyperswitch-control-center-embed-react
```

**2B.2 Import the SDK in Your Application**

```javascript
import React, { useState } from 'react';
import './App.css';
import 'tailwindcss/tailwind.css';
import { loadHyperswitch } from '@juspay-tech/hyperswitch-control-center-embed-core';
import {
  HyperswitchProvider,
  ConnectorConfiguration
} from '@juspay-tech/hyperswitch-control-center-embed-react';
```

**2B.3 Example app.js Implementation**

Key Concept: The fetchToken function is lazy. It is called:

* When the component first mounts.
* Automatically whenever the SDK detects the session has expired (auto-refresh).

```javascript
function App() {
  const [errorMessage, setErrorMessage] = useState(null);

  const [hyperswitchInstance] = useState(() => {

    const fetchToken = async () => {
      try {
        const response = await fetch(
          'http://localhost:4000/embedded/hyperswitch',
          {
            method: "GET",
            headers: {
              'Content-Type': 'application/json'
            }
          }
        );

        if (!response.ok) {
          const errorData = await response.json();
          const errorMsg = errorData.error || 'Network error fetching token';
          setErrorMessage(errorMsg);
          return undefined;
        }

        const responseData = await response.json();
        const token = responseData.data?.token || responseData.token;

        return token;

      } catch (err) {
        setErrorMessage(err.message);
        return undefined;
      }
    };

    return loadHyperswitch({
      fetchToken: fetchToken
    });

  });

  return (
    <div className="h-screen bg-gray-100 p-10 text-gray-700">
      {errorMessage ? (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          <strong>Error: </strong>
          <span>{errorMessage}</span>
        </div>
      ) : (
        <HyperswitchProvider hyperswitchInstance={hyperswitchInstance}>
          <ConnectorConfiguration url="https://app.hyperswitch.io/api" />
        </HyperswitchProvider>
      )}
    </div>
  );
}

export default App;

```

## API Reference

### 1. loadHyperswitch(options)

Initializes the SDK logic.

options.fetchToken () => Promise\<string | undefined>

* Required.
* A function that retrieves a fresh JWT from your backend.
* Should return the JWT string on success.
* Should return undefined on failure.

### 2. HyperswitchProvider

Context provider that holds the authentication state.

* **hyperswitchInstance**: The object returned by loadHyperswitch.

### 3. ConnectorConfiguration

The UI Component that renders the settings form.

* **url (string)**: The base URL for the Hyperswitch Dashboard API.
  * Sandbox:[ https://app.hyperswitch.io](https://app.hyperswitch.io/api)
  * Default:[ http://localhost:9000](http://localhost:9000)
