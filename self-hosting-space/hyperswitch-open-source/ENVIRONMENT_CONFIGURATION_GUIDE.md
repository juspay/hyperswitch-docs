# Environment Variable Configuration Guide

This comprehensive guide explains all environment variables used to configure Hyperswitch, their purposes, and recommended values for different deployment scenarios.

## Quick Start Template

### Minimal Configuration (Local Development)

```bash
# .env file for local Docker setup
HYPERSWITCH_API_URL=http://localhost:8080
HYPERSWITCH_PUBLISHABLE_KEY=pk_snd_your_key_here
HYPERSWITCH_SECRET_KEY=snd_your_key_here
DATABASE_URL=postgresql://hyperswitch:hyperswitch@localhost:5432/hyperswitch
REDIS_URL=redis://localhost:6379
```

### Production Configuration

```bash
# .env file for production (use secrets manager in practice)
HYPERSWITCH_API_URL=https://api.yourdomain.com
HYPERSWITCH_PUBLISHABLE_KEY=pk_pnd_your_production_key
HYPERSWITCH_SECRET_KEY=pnd_your_production_secret
DATABASE_URL=postgresql://hs_user:secure_pass@prod-db:5432/hyperswitch
REDIS_URL=redis://:secure_pass@redis-cluster:6379
LOG_LEVEL=info
METRICS_ENABLED=true
```

---

## Core Application Variables

### API Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `HYPERSWITCH_API_URL` | Yes | `http://localhost:8080` | Base URL for Hyperswitch API |
| `HYPERSWITCH_PUBLISHABLE_KEY` | Yes | - | Client-side API key (starts with pk_) |
| `HYPERSWITCH_SECRET_KEY` | Yes | - | Server-side API key (starts with snd_/pnd_) |
| `API_VERSION` | No | `v1` | API version to use |
| `REQUEST_TIMEOUT` | No | `30000` | Request timeout in milliseconds |

**Example:**
```bash
# Development
HYPERSWITCH_API_URL=https://sandbox.hyperswitch.io
HYPERSWITCH_PUBLISHABLE_KEY=pk_snd_abcdefghijklmnopqrstuv
HYPERSWITCH_SECRET_KEY=snd_abcdefghijklmnopqrstuvwxyz1234

# Production
HYPERSWITCH_API_URL=https://api.hyperswitch.io
HYPERSWITCH_PUBLISHABLE_KEY=pk_pnd_productionkeyhere12345
HYPERSWITCH_SECRET_KEY=pnd_productionsecretkeyhere67890
```

### Server Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SERVER_BIND_ADDRESS` | No | `0.0.0.0` | IP address to bind server |
| `SERVER_PORT` | No | `8080` | HTTP server port |
| `SERVER_WORKERS` | No | `auto` | Number of worker threads |
| `REQUEST_BODY_LIMIT` | No | `1048576` | Max request body size (bytes) |
| `KEEP_ALIVE_DURATION` | No | `5` | Connection keep-alive (seconds) |

**Example:**
```bash
SERVER_BIND_ADDRESS=0.0.0.0
SERVER_PORT=8080
SERVER_WORKERS=4
REQUEST_BODY_LIMIT=2097152  # 2MB
KEEP_ALIVE_DURATION=30
```

---

## Database Configuration

### PostgreSQL Connection

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | - | Full PostgreSQL connection string |
| `DATABASE_POOL_SIZE` | No | `10` | Connection pool size |
| `DATABASE_TIMEOUT` | No | `10000` | Connection timeout (ms) |
| `DATABASE__HOST` | If no URL | `localhost` | Database host |
| `DATABASE__PORT` | If no URL | `5432` | Database port |
| `DATABASE__USERNAME` | If no URL | `hyperswitch` | Database user |
| `DATABASE__PASSWORD` | If no URL | - | Database password |
| `DATABASE__DBNAME` | If no URL | `hyperswitch` | Database name |

**Connection String Format:**
```bash
# Standard format
DATABASE_URL=postgresql://username:password@host:port/database

# With SSL
DATABASE_URL=postgresql://user:pass@host:5432/db?sslmode=require

# With connection pool
DATABASE_URL=postgresql://user:pass@host:5432/db?connection_limit=20
```

**Examples:**

```bash
# Local development
DATABASE_URL=postgresql://hyperswitch:hyperswitch@localhost:5432/hyperswitch
DATABASE_POOL_SIZE=10

# Docker Compose (internal network)
DATABASE_URL=postgresql://hyperswitch:hyperswitch@postgres:5432/hyperswitch

# Production with SSL
DATABASE_URL=postgresql://hs_prod:SecurePass123!@prod-db.cluster-xxx.us-east-1.rds.amazonaws.com:5432/hyperswitch?sslmode=require
DATABASE_POOL_SIZE=50
DATABASE_TIMEOUT=30000
```

### Read Replica Configuration

```bash
# Primary database (writes)
DATABASE_URL=postgresql://primary_user:pass@primary-host:5432/hyperswitch

# Read replica (reads only)
DATABASE_REPLICA_URL=postgresql://replica_user:pass@replica-host:5432/hyperswitch
READ_REPLICA_ENABLED=true
```

---

## Cache Configuration

### Redis Connection

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `REDIS_URL` | Yes | - | Full Redis connection string |
| `REDIS_POOL_SIZE` | No | `10` | Redis connection pool size |
| `REDIS_TIMEOUT` | No | `5000` | Redis timeout (ms) |
| `REDIS_CLUSTER_ENABLED` | No | `false` | Use Redis Cluster |

**Connection String Formats:**

```bash
# Single Redis instance (no auth)
REDIS_URL=redis://localhost:6379

# With password
REDIS_URL=redis://:password@localhost:6379

# With database selection
REDIS_URL=redis://localhost:6379/0

# Redis Cluster
REDIS_URL=redis://node1:6379,redis://node2:6379,redis://node3:6379
REDIS_CLUSTER_ENABLED=true

# TLS/SSL
REDIS_URL=rediss://:password@secure-redis:6380
```

**Examples:**

```bash
# Local development
REDIS_URL=redis://localhost:6379
REDIS_POOL_SIZE=10

# Docker
REDIS_URL=redis://redis:6379

# Production with AUTH
REDIS_URL=redis://:ComplexRedisPass789@prod-redis.cache.amazonaws.com:6379
REDIS_POOL_SIZE=50

# Redis Cluster
REDIS_URL=redis://redis-node-1:6379,redis://redis-node-2:6379
REDIS_CLUSTER_ENABLED=true
```

### Cache TTL Settings

```bash
# How long to cache various data
CACHE_TTL_MERCHANT_CONFIG=3600      # 1 hour
CACHE_TTL_CONNECTOR_CONFIG=300      # 5 minutes
CACHE_TTL_ROUTING_RULES=60          # 1 minute
CACHE_TTL_PAYMENT_METHODS=86400     # 24 hours
```

---

## Security Configuration

### Encryption & Keys

| Variable | Required | Description |
|----------|----------|-------------|
| `MASTER_KEY` | Yes (prod) | Master encryption key for sensitive data |
| `JWT_SECRET` | Yes | Secret for JWT token signing |
| `API_KEY_HASH_SALT` | Yes | Salt for hashing API keys |
| `ENCRYPTION_KEY_ID` | No | Identifier for encryption key version |

**Generating Secure Keys:**

```bash
# Master key (32 bytes hex)
MASTER_KEY=$(openssl rand -hex 32)

# JWT secret
JWT_SECRET=$(openssl rand -base64 48)

# API key salt
API_KEY_HASH_SALT=$(openssl rand -hex 16)
```

**Example:**
```bash
# Development (use strong random values in production)
MASTER_KEY=deadbeefcafebabe1234567890abcdef1234567890abcdef1234567890abcdef
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
API_KEY_HASH_SALT=a1b2c3d4e5f6g7h8
```

### TLS/SSL Configuration

```bash
# Enable TLS
TLS_ENABLED=true

# Certificate paths
TLS_CERT_PATH=/etc/ssl/certs/hyperswitch.crt
TLS_KEY_PATH=/etc/ssl/private/hyperswitch.key

# Minimum TLS version
TLS_MIN_VERSION=1.2

# Cipher suites
TLS_CIPHERS=ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384
```

### CORS Configuration

```bash
# Allowed origins (comma-separated)
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://app.yourdomain.com

# Allowed methods
CORS_ALLOWED_METHODS=GET,POST,PUT,DELETE,OPTIONS

# Allowed headers
CORS_ALLOWED_HEADERS=Content-Type,Authorization,X-Requested-With

# Max age for preflight cache
CORS_MAX_AGE=86400
```

---

## Logging Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `LOG_LEVEL` | No | `info` | Log verbosity (trace/debug/info/warn/error) |
| `LOG_FORMAT` | No | `json` | Log format (json/text/pretty) |
| `LOG_OUTPUT` | No | `stdout` | Log destination (stdout/file/both) |
| `LOG_FILE_PATH` | If file | `/var/log/hyperswitch/app.log` | Log file location |
| `LOG_FILE_ROTATION` | No | `daily` | Rotation frequency |

**Examples:**

```bash
# Development
LOG_LEVEL=debug
LOG_FORMAT=pretty
LOG_OUTPUT=stdout

# Production
LOG_LEVEL=info
LOG_FORMAT=json
LOG_OUTPUT=file
LOG_FILE_PATH=/var/log/hyperswitch/app.log
LOG_FILE_ROTATION=daily
LOG_RETENTION_DAYS=30
```

### Structured Logging Fields

```bash
# Include additional context
LOG_REQUEST_ID=true
LOG_USER_AGENT=true
LOG_REMOTE_ADDR=true
LOG_REQUEST_TIMING=true
```

---

## Monitoring & Observability

### Metrics Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `METRICS_ENABLED` | No | `true` | Enable metrics collection |
| `METRICS_ENDPOINT` | No | `/metrics` | Prometheus metrics endpoint |
| `METRICS_PORT` | No | `9090` | Metrics server port |
| `METRICS_INTERVAL` | No | `15` | Collection interval (seconds) |

**Example:**
```bash
METRICS_ENABLED=true
METRICS_ENDPOINT=/metrics
METRICS_PORT=9090
METRICS_INTERVAL=15
```

### Distributed Tracing

```bash
# OpenTelemetry / Jaeger
TRACING_ENABLED=true
OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4317
OTEL_SERVICE_NAME=hyperswitch-router
OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production

# Sampling rate (0.0 to 1.0)
TRACING_SAMPLING_RATE=0.1
```

### Health Checks

```bash
# Health check endpoint
HEALTH_CHECK_ENDPOINT=/health

# Deep health check (includes DB/cache)
HEALTH_CHECK_DEEP_ENDPOINT=/health/deep

# Health check intervals
HEALTH_CHECK_INTERVAL=10
```

---

## Payment Processing Configuration

### Connector Settings

```bash
# Global connector timeout
CONNECTOR_TIMEOUT=30000

# Retry configuration
CONNECTOR_RETRY_ENABLED=true
CONNECTOR_MAX_RETRIES=3
CONNECTOR_RETRY_BASE_DELAY=1000
CONNECTOR_RETRY_MAX_DELAY=10000

# Circuit breaker
CIRCUIT_BREAKER_ENABLED=true
CIRCUIT_BREAKER_FAILURE_THRESHOLD=5
CIRCUIT_BREAKER_RESET_TIMEOUT=60000
```

### Webhook Configuration

```bash
# Webhook delivery
WEBHOOK_TIMEOUT=5000
WEBHOOK_MAX_RETRIES=5
WEBHOOK_RETRY_BASE_DELAY=1000

# Webhook verification
WEBHOOK_SIGNATURE_ALGORITHM=hmac-sha256
WEBHOOK_SIGNING_SECRET=whsec_your_webhook_secret_here

# Outbound webhook settings
WEBHOOK_OUTBOUND_TIMEOUT=30000
WEBHOOK_OUTBOUND_MAX_REDIRECTS=3
```

### 3D Secure Configuration

```bash
# 3DS settings
THREEDS_ENABLED=true
THREEDS_VERSION=2.2.0
THREEDS_TIMEOUT=300000
THREEDS_CHALLENGE_INDICATOR=no_preference

# 3DS provider (if using external)
THREEDS_PROVIDER=netcetera
THREEDS_PROVIDER_URL=https://3ds-server.example.com
```

---

## Feature Flags

### Experimental Features

```bash
# Enable beta features (use with caution)
FEATURE_SMART_RETRIES_V2=true
FEATURE_INTELLIGENT_ROUTING=true
FEATURE_COST_BASED_ROUTING=false
FEATURE_NEW_CONNECTOR_FRAMEWORK=true
```

### Module Toggles

```bash
# Enable/disable modules
SCHEDULER_ENABLED=true
MONITORING_ENABLED=true
ANALYTICS_ENABLED=true
WEBHOOK_DELIVERY_ENABLED=true
EMAIL_NOTIFICATIONS_ENABLED=false
```

---

## Environment-Specific Configurations

### Development

```bash
# .env.development
HYPERSWITCH_API_URL=http://localhost:8080
HYPERSWITCH_PUBLISHABLE_KEY=pk_snd_dev_key_here
HYPERSWITCH_SECRET_KEY=snd_dev_secret_here

LOG_LEVEL=debug
LOG_FORMAT=pretty
METRICS_ENABLED=false

DATABASE_URL=postgresql://hyperswitch:hyperswitch@localhost:5432/hyperswitch
REDIS_URL=redis://localhost:6379

# Development conveniences
AUTO_MIGRATE=true
SEED_DATA=true
DEBUG_MODE=true
```

### Staging

```bash
# .env.staging
HYPERSWITCH_API_URL=https://api.staging.yourdomain.com
LOG_LEVEL=info
LOG_FORMAT=json

DATABASE_URL=postgresql://hs_staging:secure_pass@staging-db:5432/hyperswitch
REDIS_URL=redis://staging-redis:6379

METRICS_ENABLED=true
TRACING_ENABLED=true

# Test mode
SANDBOX_MODE=true
TEST_PAYMENT_PROCESSORS_ONLY=true
```

### Production

```bash
# .env.production (use secrets manager!)
HYPERSWITCH_API_URL=https://api.yourdomain.com
LOG_LEVEL=warn
METRICS_ENABLED=true

# High availability
DATABASE_URL=postgresql://hs_prod:xxx@prod-db-cluster:5432/hyperswitch?sslmode=require
REDIS_URL=redis://:xxx@prod-redis-cluster:6379
REDIS_CLUSTER_ENABLED=true

# Security
TLS_ENABLED=true
CORS_ALLOWED_ORIGINS=https://yourdomain.com
RATE_LIMITING_ENABLED=true

# Performance
DATABASE_POOL_SIZE=100
REDIS_POOL_SIZE=50
SERVER_WORKERS=auto
```

---

## Configuration Validation

### Startup Validation Script

Create `validate-config.sh`:

```bash
#!/bin/bash
# validate-config.sh - Validate environment configuration

ERRORS=0

# Required variables
declare -a REQUIRED=(
    "HYPERSWITCH_PUBLISHABLE_KEY"
    "HYPERSWITCH_SECRET_KEY"
    "DATABASE_URL"
    "REDIS_URL"
)

echo "🔍 Validating Hyperswitch Configuration..."
echo "=========================================="

# Check required variables
for var in "${REQUIRED[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ ERROR: $var is not set"
        ((ERRORS++))
    else
        echo "✅ $var is set"
    fi
done

# Validate API keys format
if [[ ! "$HYPERSWITCH_PUBLISHABLE_KEY" =~ ^pk_(snd|pnd)_ ]]; then
    echo "❌ ERROR: PUBLISHABLE_KEY format invalid (should start with pk_snd_ or pk_pnd_)"
    ((ERRORS++))
fi

if [[ ! "$HYPERSWITCH_SECRET_KEY" =~ ^(snd|pnd)_ ]]; then
    echo "❌ ERROR: SECRET_KEY format invalid (should start with snd_ or pnd_)"
    ((ERRORS++))
fi

# Check database connection
echo -n "🔌 Testing database connection... "
if psql "$DATABASE_URL" -c "SELECT 1;" > /dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FAILED"
    ((ERRORS++))
fi

# Check Redis connection
echo -n "🔌 Testing Redis connection... "
if redis-cli -u "$REDIS_URL" ping > /dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FAILED"
    ((ERRORS++))
fi

echo "=========================================="
if [ $ERRORS -eq 0 ]; then
    echo "✅ All validations passed!"
    exit 0
else
    echo "❌ Found $ERRORS error(s). Please fix before starting."
    exit 1
fi
```

Usage:
```bash
chmod +x validate-config.sh
./validate-config.sh
```

---

## Best Practices

### Do's ✅

- **Use secrets managers** in production (HashiCorp Vault, AWS Secrets Manager)
- **Separate configs** by environment (dev/staging/prod)
- **Version control** sample configs (.env.example)
- **Never commit** real .env files
- **Rotate credentials** regularly
- **Use strong passwords** (generated, not human-created)
- **Validate on startup** - fail fast if config is wrong
- **Document custom configs** with comments

### Don'ts ❌

- **Hardcode secrets** in code or configs
- **Share production credentials** in Slack/email
- **Use default passwords** in production
- **Mix environment configs** (don't use prod DB in dev)
- **Log sensitive values** (API keys, passwords)
- **Ignore validation errors** - fix them immediately
- **Commit .env files** to version control

---

## Troubleshooting

### "Environment variable not found"

**Check:**
```bash
# Is the variable set?
echo $VARIABLE_NAME

# Is .env file loaded?
source .env
echo $VARIABLE_NAME

# Check for typos
grep VARIABLE_NAME .env
```

### "Invalid database URL format"

**Fix:**
```bash
# Ensure proper format
DATABASE_URL=postgresql://user:pass@host:5432/db

# URL encode special characters
# @ becomes %40
# # becomes %23
```

### "Permission denied" on config files

**Fix:**
```bash
chmod 600 .env
chown app:app .env
```

---

## Environment Variable Reference Table

| Category | Variable | Req | Sensitive | Description |
|----------|----------|-----|-----------|-------------|
| Core | HYPERSWITCH_API_URL | ✅ | ❌ | API base URL |
| Core | HYPERSWITCH_PUBLISHABLE_KEY | ✅ | ⚠️ | Client API key |
| Core | HYPERSWITCH_SECRET_KEY | ✅ | ✅ | Server API key |
| Database | DATABASE_URL | ✅ | ✅ | PostgreSQL connection |
| Cache | REDIS_URL | ✅ | ✅ | Redis connection |
| Security | MASTER_KEY | Prod | ✅ | Encryption key |
| Security | JWT_SECRET | Prod | ✅ | JWT signing key |
| Logging | LOG_LEVEL | ❌ | ❌ | Log verbosity |
| Monitoring | METRICS_ENABLED | ❌ | ❌ | Enable metrics |
| Features | SCHEDULER_ENABLED | ❌ | ❌ | Enable scheduler |

Legend: ✅=Required, ❌=Optional, ⚠️=Semi-sensitive, ✅=Sensitive/Secret

---

**Last Updated:** April 2026  
**Compatibility:** Hyperswitch v1.x  
**Questions?** [Configuration Support](https://docs.hyperswitch.io/support)