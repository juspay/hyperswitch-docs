# Node.js/Express Hyperswitch Integration Example

A complete, production-ready example demonstrating how to integrate Hyperswitch payments into a Node.js/Express application.

## Features

- ✅ Create payment intents
- ✅ Collect card details securely
- ✅ Confirm payments
- ✅ Handle 3D Secure authentication
- ✅ Webhook handling
- ✅ Error handling
- ✅ Responsive UI
- ✅ Test card display

## Quick Start

### 1. Get API Credentials

1. Sign up at [app.hyperswitch.io](https://app.hyperswitch.io)
2. Go to **Settings** → **API Keys**
3. Copy your **Publishable Key** and **Secret Key**
4. Connect a payment processor (e.g., Stripe in test mode)

### 2. Install and Run

```bash
# Clone or navigate to this example
cd nodejs-express

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Start the server
npm start
```

### 3. Test the Payment

1. Open [http://localhost:3000](http://localhost:3000)
2. Enter test card details:
   - **Card:** `4242 4242 4242 4242`
   - **Expiry:** Any future date (e.g., `12/25`)
   - **CVC:** Any 3 digits (e.g., `123`)
   - **ZIP:** Any 5 digits (e.g., `12345`)
3. Click **Pay $99.00**
4. Check your Hyperswitch dashboard for the completed payment

## Project Structure

```
nodejs-express/
├── server.js           # Express server with API endpoints
├── package.json        # Dependencies
├── .env.example        # Environment template
├── .env               # Your configuration (not committed)
├── README.md          # This file
└── public/
    └── index.html     # Payment form UI
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve payment page |
| `/api/create-payment` | POST | Create payment intent |
| `/api/confirm-payment` | POST | Confirm payment |
| `/api/payment-status/:id` | GET | Check payment status |
| `/webhooks/hyperswitch` | POST | Receive webhooks |
| `/config` | GET | Get public config |
| `/health` | GET | Health check |

## Configuration

### Required Environment Variables

```bash
HYPERSWITCH_SECRET_KEY=snd_your_secret_key
HYPERSWITCH_PUBLISHABLE_KEY=pk_snd_your_publishable_key
```

### Optional Variables

```bash
HYPERSWITCH_API_URL=https://sandbox.hyperswitch.io  # or production
PORT=3000                                           # Server port
NODE_ENV=development                                # Environment
```

## Payment Flow

```
1. Customer enters card details
   ↓
2. Frontend sends to /api/create-payment
   ↓
3. Server creates payment intent via Hyperswitch API
   ↓
4. Server returns client_secret to frontend
   ↓
5. Frontend collects card details (simulated here)
   ↓
6. Frontend sends to /api/confirm-payment
   ↓
7. Server confirms payment with Hyperswitch
   ↓
8. Payment processor charges card
   ↓
9. Server returns result to frontend
   ↓
10. Customer sees success/error message
```

## Test Cards

Use these for testing different scenarios:

| Card Number | Brand | Result |
|-------------|-------|--------|
| `4242 4242 4242 4242` | Visa | ✅ Success |
| `4000 0000 0000 0002` | Visa | ❌ Declined |
| `4000 0000 0000 3220` | Visa | 🔐 3D Secure |
| `5555 5555 5555 4444` | Mastercard | ✅ Success |
| `3782 822463 10005` | Amex | ✅ Success |

## Webhook Testing

To test webhooks locally, use ngrok:

```bash
# Install ngrok
npm install -g ngrok

# Expose local server
ngrok http 3000

# Copy the HTTPS URL (e.g., https://abc123.ngrok.io)
# Add webhook in Hyperswitch dashboard:
# URL: https://abc123.ngrok.io/webhooks/hyperswitch
# Events: payment_intent.succeeded, payment_intent.failed
```

## Common Issues

### "Missing required environment variables"

Make sure you created the `.env` file:
```bash
cp .env.example .env
# Then edit .env with your real API keys
```

### "Payment creation failed"

Check that:
- API keys are correct
- You've connected a payment processor in the dashboard
- You're using the correct API URL (sandbox vs production)

### "Cannot connect to server"

Ensure the server is running:
```bash
npm start
# Should see: Server running on: http://localhost:3000
```

## Production Checklist

Before deploying to production:

- [ ] Switch to production API keys (`pnd_` prefix)
- [ ] Change `HYPERSWITCH_API_URL` to `https://api.hyperswitch.io`
- [ ] Enable HTTPS (use TLS/SSL certificate)
- [ ] Set `NODE_ENV=production`
- [ ] Configure webhooks with production URL
- [ ] Implement proper error logging
- [ ] Add rate limiting
- [ ] Set up monitoring (e.g., DataDog, New Relic)
- [ ] Implement idempotency for payment creation
- [ ] Add input validation and sanitization
- [ ] Set up automated backups
- [ ] Test disaster recovery procedures

## Next Steps

### Enhancements You Can Add

1. **Use Hyperswitch SDK**
   ```bash
   npm install @hyperswitch/sdk
   ```
   Replace manual card collection with secure SDK elements

2. **Add Database Persistence**
   ```bash
   npm install sequelize pg
   ```
   Store order and payment data locally

3. **Add User Authentication**
   ```bash
   npm install passport jsonwebtoken
   ```
   Track which user made each payment

4. **Implement Retry Logic**
   ```javascript
   const retry = require('async-retry');
   // Add retry logic for failed API calls
   ```

5. **Add Tests**
   ```bash
   npm install --save-dev jest supertest
   npm test
   ```

## Documentation

- [Hyperswitch Docs](https://docs.hyperswitch.io)
- [API Reference](https://api-reference.hyperswitch.io)
- [SDK Documentation](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide)

## Support

- [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite)
- [GitHub Issues](https://github.com/juspay/hyperswitch/issues)
- Email: support@hyperswitch.io

## License

Apache 2.0 - See LICENSE file for details