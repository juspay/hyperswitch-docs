# Complete End-to-End Examples

This directory contains fully-functional, production-ready examples demonstrating how to integrate Hyperswitch into your application. Each example includes both backend server code and frontend integration.

## Available Examples

| Example | Stack | Complexity | Time to Run |
|---------|-------|------------|-------------|
| [Node.js/Express](./nodejs-express) | Node.js + Express + HTML | Beginner | 5 minutes |
| [Python/Flask](./python-flask) | Python + Flask + HTML | Beginner | 5 minutes |
| [React](./react-example) | React + Node.js | Intermediate | 10 minutes |
| [Docker Compose](./docker-compose) | Multi-service setup | Beginner | 3 minutes |

## Quick Start

### Option 1: Docker Compose (Fastest)

```bash
cd docker-compose
docker-compose up
```

Then open http://localhost:3000

### Option 2: Node.js Example

```bash
cd nodejs-express
npm install
npm start
```

Then open http://localhost:3000

### Option 3: Python Example

```bash
cd python-flask
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

## Prerequisites

All examples require:
- Hyperswitch account (free at [app.hyperswitch.io](https://app.hyperswitch.io))
- API credentials (Publishable Key and Secret Key)
- At least one payment processor connected (e.g., Stripe test mode)

## What's Included

Each example demonstrates:

1. **Server-side integration**
   - Creating payment intents
   - Handling webhooks
   - Payment confirmation

2. **Client-side integration**
   - Loading Hyperswitch SDK
   - Collecting payment details
   - Handling 3D Secure
   - Error handling

3. **Production-ready features**
   - Environment variable management
   - Error logging
   - Security headers
   - Input validation

## Test Cards

Use these test cards for development:

| Card Number | Type | Result |
|-------------|------|--------|
| `4242 4242 4242 4242` | Visa | Success |
| `4000 0000 0000 0002` | Visa | Declined |
| `4000 0000 0000 3220` | Visa | 3D Secure Required |
| `5555 5555 5555 4444` | Mastercard | Success |

**Any future date for expiry, any 3 digits for CVC**

## Production Checklist

Before going live:

- [ ] Switch to production API keys
- [ ] Enable HTTPS
- [ ] Configure webhooks for production
- [ ] Implement proper error handling
- [ ] Add monitoring and logging
- [ ] Set up retry logic for failed webhooks
- [ ] Test with real payment methods
- [ ] Review PCI compliance requirements

## Getting Help

- [Documentation](https://docs.hyperswitch.io)
- [API Reference](https://api-reference.hyperswitch.io)
- [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite)
- [GitHub Issues](https://github.com/juspay/hyperswitch/issues)

## License

These examples are provided under the Apache 2.0 License.