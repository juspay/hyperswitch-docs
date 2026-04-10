/**
 * Hyperswitch Node.js/Express Example
 * 
 * This is a complete, production-ready example of integrating Hyperswitch
 * for payment processing. It demonstrates:
 * - Creating payment intents
 * - Serving the payment page
 * - Confirming payments
 * - Handling webhooks
 * 
 * Prerequisites:
 * 1. Node.js 16+ installed
 * 2. Hyperswitch account (sign up at app.hyperswitch.io)
 * 3. API credentials (publishable_key and api_key)
 * 4. At least one payment processor connected (e.g., Stripe in test mode)
 */

require('dotenv').config();
const express = require('express');
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Hyperswitch configuration
const HYPERSWITCH_API_URL = process.env.HYPERSWITCH_API_URL || 'https://api.hyperswitch.io';
const HYPERSWITCH_SECRET_KEY = process.env.HYPERSWITCH_SECRET_KEY;
const HYPERSWITCH_PUBLISHABLE_KEY = process.env.HYPERSWITCH_PUBLISHABLE_KEY;

// Validate required environment variables
if (!HYPERSWITCH_SECRET_KEY || !HYPERSWITCH_PUBLISHABLE_KEY) {
  console.error('❌ Error: Missing required environment variables');
  console.error('Please set HYPERSWITCH_SECRET_KEY and HYPERSWITCH_PUBLISHABLE_KEY');
  console.error('\nCreate a .env file with:\n');
  console.error('HYPERSWITCH_SECRET_KEY=your_secret_key_here');
  console.error('HYPERSWITCH_PUBLISHABLE_KEY=your_publishable_key_here');
  process.exit(1);
}

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Security headers
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  next();
});

// Logging middleware
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`);
  next();
});

/**
 * Route: GET /
 * Serve the payment page
 */
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

/**
 * Route: POST /api/create-payment
 * Create a payment intent
 * 
 * Body: {
 *   amount: number (in cents),
 *   currency: string (e.g., 'USD'),
 *   description: string (optional)
 * }
 */
app.post('/api/create-payment', async (req, res) => {
  try {
    const { amount, currency = 'USD', description = 'Test Payment' } = req.body;

    // Validate input
    if (!amount || amount <= 0) {
      return res.status(400).json({
        error: 'Invalid amount',
        message: 'Amount must be a positive number (in cents)'
      });
    }

    // Create unique identifiers
    const paymentId = uuidv4();
    const customerId = `cust_${uuidv4().slice(0, 8)}`;

    console.log(`💳 Creating payment intent: ${paymentId}`);

    // Create payment intent via Hyperswitch API
    const response = await axios.post(
      `${HYPERSWITCH_API_URL}/payments`,
      {
        amount: amount,
        currency: currency,
        confirm: false, // Don't confirm yet, wait for payment details
        customer_id: customerId,
        description: description,
        metadata: {
          order_id: `order_${Date.now()}`,
          created_by: 'nodejs-example'
        }
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'api-key': HYPERSWITCH_SECRET_KEY
        }
      }
    );

    const paymentData = response.data;

    console.log(`✅ Payment intent created: ${paymentData.payment_id}`);

    // Return client secret and other necessary data
    res.json({
      success: true,
      client_secret: paymentData.client_secret,
      payment_id: paymentData.payment_id,
      publishable_key: HYPERSWITCH_PUBLISHABLE_KEY,
      amount: amount,
      currency: currency
    });

  } catch (error) {
    console.error('❌ Error creating payment:', error.message);
    
    if (error.response) {
      console.error('API Response:', error.response.data);
      return res.status(error.response.status).json({
        error: 'Payment creation failed',
        message: error.response.data.message || 'Unknown error',
        details: error.response.data
      });
    }

    res.status(500).json({
      error: 'Internal server error',
      message: error.message
    });
  }
});

/**
 * Route: POST /api/confirm-payment
 * Confirm a payment (alternative to SDK confirm)
 * Typically called from backend for server-to-server flows
 */
app.post('/api/confirm-payment', async (req, res) => {
  try {
    const { payment_id, payment_method_id } = req.body;

    if (!payment_id || !payment_method_id) {
      return res.status(400).json({
        error: 'Missing required fields',
        message: 'payment_id and payment_method_id are required'
      });
    }

    console.log(`🔐 Confirming payment: ${payment_id}`);

    const response = await axios.post(
      `${HYPERSWITCH_API_URL}/payments/${payment_id}/confirm`,
      {
        payment_method_id: payment_method_id,
        client_secret: req.body.client_secret
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'api-key': HYPERSWITCH_SECRET_KEY
        }
      }
    );

    console.log(`✅ Payment confirmed: ${response.data.status}`);

    res.json({
      success: true,
      status: response.data.status,
      payment_data: response.data
    });

  } catch (error) {
    console.error('❌ Error confirming payment:', error.message);
    res.status(500).json({
      error: 'Confirmation failed',
      message: error.message
    });
  }
});

/**
 * Route: GET /api/payment-status/:paymentId
 * Check payment status
 */
app.get('/api/payment-status/:paymentId', async (req, res) => {
  try {
    const { paymentId } = req.params;

    const response = await axios.get(
      `${HYPERSWITCH_API_URL}/payments/${paymentId}`,
      {
        headers: {
          'api-key': HYPERSWITCH_SECRET_KEY
        }
      }
    );

    res.json({
      success: true,
      status: response.data.status,
      amount: response.data.amount,
      currency: response.data.currency,
      payment_data: response.data
    });

  } catch (error) {
    console.error('❌ Error fetching payment status:', error.message);
    res.status(500).json({
      error: 'Failed to fetch status',
      message: error.message
    });
  }
});

/**
 * Route: POST /webhooks/hyperswitch
 * Handle webhooks from Hyperswitch
 * 
 * IMPORTANT: In production, verify webhook signatures!
 */
app.post('/webhooks/hyperswitch', async (req, res) => {
  try {
    const event = req.body;

    console.log('📬 Webhook received:', event.event_type);
    console.log('Payment ID:', event.content?.object?.payment_id);

    // Handle different event types
    switch (event.event_type) {
      case 'payment_intent.requires_customer_action':
        console.log('⏳ Payment requires customer action (3D Secure)');
        // Could send email notification
        break;

      case 'payment_intent.succeeded':
        console.log('✅ Payment succeeded!');
        // Update order status in your database
        // Send confirmation email
        // Fulfill order
        break;

      case 'payment_intent.failed':
        console.log('❌ Payment failed:', event.content?.object?.error_message);
        // Log failure, notify customer
        break;

      case 'refund.succeeded':
        console.log('↩️ Refund processed');
        break;

      default:
        console.log('ℹ️ Unhandled event type:', event.event_type);
    }

    // Always respond with 200 to acknowledge receipt
    res.status(200).json({ received: true });

  } catch (error) {
    console.error('❌ Webhook processing error:', error.message);
    // Still return 200 to prevent retries
    res.status(200).json({ received: true, error: error.message });
  }
});

/**
 * Route: GET /config
 * Get public configuration for frontend
 */
app.get('/config', (req, res) => {
  res.json({
    publishable_key: HYPERSWITCH_PUBLISHABLE_KEY,
    api_url: HYPERSWITCH_API_URL
  });
});

/**
 * Health check endpoint
 */
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    service: 'hyperswitch-nodejs-example'
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({
    error: 'Internal server error',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong'
  });
});

// Start server
app.listen(PORT, () => {
  console.log('\n🚀 Hyperswitch Node.js Example Server');
  console.log('=' .repeat(50));
  console.log(`Server running on: http://localhost:${PORT}`);
  console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
  console.log(`API Endpoint: ${HYPERSWITCH_API_URL}`);
  console.log('=' .repeat(50));
  console.log('\n📖 Quick Start:');
  console.log('1. Open http://localhost:' + PORT + ' in your browser');
  console.log('2. Enter payment details using test card: 4242 4242 4242 4242');
  console.log('3. Any future date for expiry, any 3 digits for CVC');
  console.log('4. Click Pay to complete the test payment\n');
});