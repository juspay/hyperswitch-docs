# Integration Guide

This SDK allows you to embed the Hyperswitch connector configuration directly into your React application. It uses a provider pattern to manage authentication sessions via JWTs, ensuring your API keys never leak to the client.

Repository URL: [https://github.com/juspay/hyperswitch-control-center-embedded](https://github.com/juspay/hyperswitch-control-center-embedded)

### Prerequisites & Compatibility

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

### Step 1: Client Installation

Since the package is currently hosted on GitHub (not yet on the public npm registry), you must install it by pointing your package.json to the specific repository.

1. Open your package.json file.
2.  Add the following line to your dependencies object:<br>

    ```json
    "dependencies": {
      "hyperswitch-control-center-embedded": "github:juspay/hyperswitch-control-center-embedded"
    }
    ```
3. Run the installation command in your terminal:

```bash
npm install
```

### Step 2: Backend Setup (Server-Side)

Security Warning: Never expose your Hyperswitch API-Key on the frontend. You must create a backend endpoint that acts as a proxy.

The flow is: Frontend → requests session → Your Backend → requests token (using API Key) → Hyperswitch API

#### 2.1. Create the Token Endpoint

Create a route (e.g., /embedded/hyperswitch) in your backend application (Node/Express example below).

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
    // Call Hyperswitch to generate a temporary JWT for the frontend
    const response = await axios.get(`${HYPERSWITCH_BASE_URL}/api/embedded/token`, {
      headers: {
        'api-key': 'YOUR_ACTUAL_API_KEY_HERE', // STORE IN ENV VARIABLES
        'X-profile-id': 'YOUR_PROFILE_ID_HERE',
        'Content-Type': 'application/json'
      }
    });

    console.log('Hyperswitch Token Generated:', response.data);
    
    // Return the token to your frontend
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

### Step 3: Frontend Integration (React)

Now, configure the React application to load the SDK and consume the token from your new backend endpoint.

#### 3.1. Import Components

Import the necessary modules. Note that Tailwind CSS is used for styling in this example.

```javascript
import React, { useState } from 'react';
import './App.css'; 
import 'tailwindcss/tailwind.css'; 
import {
  loadHyperswitch,
  HyperswitchProvider,
  ConnectorConfiguration,
} from 'hyperswitch-control-center-embedded';
```

#### 3.2. Implement the Component

The core logic relies on the loadHyperswitch function. This function takes a fetchToken callback.

Key Concept: The fetchToken function is "lazy." It is called:

1. When the component first mounts.
2. Automatically whenever the SDK detects the session has expired (auto-refresh).

{% code title="app.js" %}
```javascript
function App() {
  const [errorMessage, setErrorMessage] = useState(null);

  // Initialize the SDK instance once
  const [hyperswitchInstance] = useState(() => {
    
    // Define the token fetching logic
    const fetchToken = async () => {
      try {
        // 1. Request token from YOUR backend (created in Step 2)
        const response = await fetch('http://localhost:4000/embedded/hyperswitch', {
          method: "GET",
          headers: {
            'Content-Type': 'application/json'
          }
        });

        if (!response.ok) {
          const errorData = await response.json();
          const errorMsg = errorData.error || 'Network error fetching token';
          console.error('Token fetch failed:', errorMsg);
          setErrorMessage(errorMsg);
          return undefined; // Signals the SDK that auth failed
        }

        const responseData = await response.json();
        
        // 2. Extract the actual JWT string
        // Check both data.token (standard) or root token property depending on your backend response structure
        const token = responseData.data?.token || responseData.token;
        
        console.log('Token received');
        return token;
        
      } catch (err) {
        console.error('Exception during token fetch:', err);
        setErrorMessage(err.message);
        return undefined;
      }
    };

    // Return the initialized loader
    return loadHyperswitch({
      fetchToken: fetchToken,
    });
  });

  return (
    <div className="h-screen bg-gray-100 p-10 text-gray-700">
      
      {/* Error State Handling */}
      {errorMessage ? (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          <strong className="font-bold">Error: </strong>
          <span className="block sm:inline">{errorMessage}</span>
        </div>
      ) : (
        /* Provider wraps the configuration component.
           hyperswitchInstance is passed down here.
        */
        <HyperswitchProvider hyperswitchInstance={hyperswitchInstance}>
          
          {/* Render the actual UI.
             'url' prop points to the Hyperswitch Dashboard API.
             Use "https://app.hyperswitch.io/api" for Sandbox 
          */}
          <ConnectorConfiguration url="https://app.hyperswitch.io/api" />
          
        </HyperswitchProvider>
      )}
    </div>
  );
}

export default App;
```
{% endcode %}

### API Reference

#### loadHyperswitch(options)

Initializes the SDK logic.

* **`options.fetchToken () => Promise<string | undefined>:`**
  * Required. A function that retrieves a fresh JWT from your backend.
  * Should return the JWT string on success.
  * Should return `undefined` on failure.

#### \<HyperswitchProvider>

Context provider that holds the authentication state.

* **hyperswitchInstance**: The object returned by loadHyperswitch.

#### \<ConnectorConfiguration>

The UI Component that renders the settings form.

* url (string): The base URL for the Hyperswitch Dashboard API.
  * Sandbox: `https://app.hyperswitch.io/api`
  * Default: `http://localhost:9000` (Used for local development)
