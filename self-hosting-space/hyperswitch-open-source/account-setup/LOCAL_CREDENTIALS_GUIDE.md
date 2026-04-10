# Local Development Credentials Guide

This document provides default credential information for accessing your locally-deployed Hyperswitch instance.

## Default Access Credentials

### After Running `scripts/setup.sh`

When you run the setup script, you'll receive the following credentials displayed in the terminal:

```
================================================
🎉 Hyperswitch Setup Complete!
================================================

📱 Access Points:
   • App Server:    http://localhost:8080
   • Control Center: http://localhost:9000
   • Web SDK:       http://localhost:5252

🔑 API Credentials:
   • Publishable Key: pk_snd_XXXXXXXXXXXXXXXXXXX
   • Secret Key:      snd_XXXXXXXXXXXXXXXXXXXXXX

📝 Default Admin:
   • Email: admin@hyperswitch.io
   • Password: admin123

⚠️  IMPORTANT: Change default password immediately!
================================================
```

## Default Credentials Reference

### API Keys

| Key Type | Format | Example | Usage |
|----------|--------|---------|-------|
| **Publishable Key** | `pk_snd_*` | `pk_snd_abcdefghijklmnopqrstuv` | Client-side SDK initialization |
| **Secret Key** | `snd_*` | `snd_abcdefghijklmnopqrstuvwxyz1234` | Server-side API authentication |

**Location:** These are generated automatically during setup and stored in:
- Environment variables
- Control Center → Settings → API Keys

### Control Center Login

| Field | Default Value | Description |
|-------|---------------|-------------|
| **Email** | `admin@hyperswitch.io` | Default administrator account |
| **Password** | `admin123` | ⚠️ Must be changed immediately |

**URL:** http://localhost:9000 (when using full Docker setup)

### Database Access

#### PostgreSQL (Default Docker Setup)

```yaml
Host: localhost (or postgres container name)
Port: 5432
Database: hyperswitch
Username: hyperswitch
Password: hyperswitch
```

**Connect via psql:**
```bash
docker compose exec postgres psql -U hyperswitch -d hyperswitch
```

**Connection string:**
```
postgresql://hyperswitch:hyperswitch@localhost:5432/hyperswitch
```

#### Redis Cache

```yaml
Host: localhost (or redis container name)
Port: 6379
Password: None (default)
Database: 0
```

**Connect via redis-cli:**
```bash
docker compose exec redis redis-cli
```

## Where Credentials Are Stored

### Environment Variables

During setup, credentials are exported as environment variables:

```bash
# In the running containers
echo $HYPERSWITCH_PUBLISHABLE_KEY
echo $HYPERSWITCH_SECRET_KEY
```

### Configuration Files

#### docker-compose.yml (Runtime Values)
```yaml
environment:
  - HYPERSWITCH_PUBLISHABLE_KEY=${HYPERSWITCH_PUBLISHABLE_KEY}
  - HYPERSWITCH_SECRET_KEY=${HYPERSWITCH_SECRET_KEY}
  - DATABASE_URL=postgresql://hyperswitch:hyperswitch@postgres:5432/hyperswitch
```

#### Environment File (.env)
If using individual components, create `.env`:
```bash
# .env file
HYPERSWITCH_PUBLISHABLE_KEY=pk_snd_your_key_here
HYPERSWITCH_SECRET_KEY=snd_your_key_here
DATABASE_URL=postgresql://hyperswitch:hyperswitch@localhost:5432/hyperswitch
REDIS_URL=redis://localhost:6379
```

### Control Center

View and regenerate credentials:

1. Open http://localhost:9000
2. Login with admin credentials
3. Navigate to **Settings** → **API Keys**
4. Click "Generate New Key" to create additional keys
5. Click "Rotate" to revoke and regenerate existing keys

## Security Best Practices

### ⚠️ CRITICAL: Change Default Credentials

**Immediately after first login:**

1. **Change Admin Password**
   ```
   1. Login to Control Center
   2. Click profile icon (top right)
   3. Select "Change Password"
   4. Enter new secure password
   ```

2. **Rotate API Keys**
   ```
   1. Go to Settings → API Keys
   2. Click "Rotate" on existing keys
   3. Copy new keys
   4. Update your application configuration
   ```

3. **Enable Two-Factor Authentication**
   ```
   1. Go to Settings → Security
   2. Enable 2FA
   3. Scan QR code with authenticator app
   ```

### For Production Deployments

Never use default credentials in production:

```bash
# ❌ WRONG - Using defaults
DATABASE_URL=postgresql://hyperswitch:hyperswitch@prod-db:5432/hyperswitch

# ✅ CORRECT - Use strong passwords
DATABASE_URL=postgresql://hs_prod_user:Xk9#mP2$vL7nQ4@prod-db:5432/hyperswitch
```

**Use a secrets manager:**
- HashiCorp Vault
- AWS Secrets Manager
- Kubernetes Secrets
- Docker Secrets

## Generating New Credentials

### API Keys via Control Center

1. Navigate to **Settings** → **API Keys**
2. Click **"Create New API Key"**
3. Choose key type:
   - **Publishable Key** (client-side, limited permissions)
   - **Secret Key** (server-side, full permissions)
4. Select permissions scope:
   - Payments (read/write)
   - Refunds (read/write)
   - Connectors (read-only)
5. Set expiration (optional)
6. Copy the key immediately (shown only once)

### Programmatic Key Generation

```bash
# Via API (requires admin secret key)
curl -X POST http://localhost:8080/api_keys \
  -H "Content-Type: application/json" \
  -H "api-key: $HYPERSWITCH_ADMIN_KEY" \
  -d '{
    "name": "Production Server",
    "description": "API key for production application server",
    "permissions": ["payments_write", "refunds_write", "connectors_read"]
  }'
```

### Database User Creation

```sql
-- Connect to PostgreSQL
docker compose exec postgres psql -U postgres

-- Create new user
CREATE USER app_server WITH PASSWORD 'secure_password_here';

-- Grant permissions
GRANT CONNECT ON DATABASE hyperswitch TO app_server;
GRANT USAGE ON SCHEMA public TO app_server;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_server;
```

## Credential Rotation

### When to Rotate

- **Quarterly**: Regular security maintenance
- **After employee departure**: Former team members
- **After suspected breach**: Security incidents
- **Before major deployment**: Pre-production updates
- **Every 90 days**: Compliance requirements

### How to Rotate Without Downtime

**API Key Rotation:**
```bash
# 1. Generate new key (keep old key active)
curl -X POST http://localhost:8080/api_keys \
  -H "api-key: $OLD_SECRET_KEY" \
  -d '{"name": "Production v2"}'

# 2. Update application to use new key
export HYPERSWITCH_SECRET_KEY=$NEW_SECRET_KEY

# 3. Deploy application with new key
kubectl rollout restart deployment/app

# 4. Monitor for errors
kubectl logs -f deployment/app

# 5. After 24 hours, revoke old key
curl -X DELETE http://localhost:8080/api_keys/$OLD_KEY_ID \
  -H "api-key: $NEW_SECRET_KEY"
```

**Database Password Rotation:**
```bash
# 1. Create new user with new password
psql -c "CREATE USER hs_new WITH PASSWORD 'new_secure_pass';"

# 2. Grant same permissions as old user
psql -c "GRANT hyperswitch TO hs_new;"

# 3. Update application connection string (gradual rollout)
# Use blue-green or canary deployment

# 4. Revoke old user after 100% migration
psql -c "DROP USER hs_old;"
```

## Troubleshooting Credential Issues

### "Invalid API Key" Error

**Check:**
1. Using correct key format (pk_snd_ vs snd_)
2. No extra spaces or newlines in key
3. Correct API endpoint (sandbox vs production)
4. Key not revoked/expired

**Debug:**
```bash
# Verify key in environment
echo "Key length: ${#HYPERSWITCH_SECRET_KEY}"
echo "Key prefix: ${HYPERSWITCH_SECRET_KEY:0:10}"

# Test API call
curl -H "api-key: $HYPERSWITCH_SECRET_KEY" \
  http://localhost:8080/accounts
```

### "Authentication Failed" in Control Center

**Solutions:**
1. Clear browser cookies/cache
2. Try incognito/private window
3. Verify correct URL (http vs https)
4. Check if session expired
5. Reset password if forgotten

### Database Connection Refused

**Check:**
```bash
# Is database container running?
docker compose ps | grep postgres

# Check connection
docker compose exec postgres pg_isready

# Verify credentials
docker compose exec postgres psql -U hyperswitch -c "SELECT 1;"
```

### Redis Authentication Errors

```bash
# Test Redis connection
docker compose exec redis redis-cli ping

# If password protected
docker compose exec redis redis-cli -a $REDIS_PASSWORD ping
```

## Environment-Specific Credentials

### Development (Local Docker)

```bash
# Weak/simple passwords acceptable
DATABASE_PASSWORD=hyperswitch
REDIS_PASSWORD=""
ADMIN_PASSWORD=admin123
```

### Staging

```bash
# Moderate security
DATABASE_PASSWORD=staging_db_$(openssl rand -hex 8)
REDIS_PASSWORD=staging_redis_$(openssl rand -hex 8)
ADMIN_PASSWORD=$(openssl rand -base64 16)
```

### Production

```bash
# Strong security required
# Use secrets manager, never hardcode
DATABASE_PASSWORD=<from_vault>
REDIS_PASSWORD=<from_vault>
API_KEYS=<rotated_quarterly>
# MFA required for all admin access
```

## Quick Reference

### Default Ports

| Service | Port | Protocol |
|---------|------|----------|
| App Server | 8080 | HTTP |
| Control Center | 9000 | HTTP |
| Web SDK | 5252 | HTTP |
| PostgreSQL | 5432 | TCP |
| Redis | 6379 | TCP |

### Default URLs

```
Control Center:   http://localhost:9000
API Base URL:     http://localhost:8080
Health Check:     http://localhost:8080/health
API Docs:         http://localhost:8080/docs
```

### Password Requirements

**Minimum for production:**
- 12 characters minimum
- Uppercase letter
- Lowercase letter
- Number
- Special character (!@#$%^&*)
- No dictionary words

**Example generator:**
```bash
openssl rand -base64 24 | tr -d "=+/" | cut -c1-20
```

## Getting Help

If you've lost access or credentials aren't working:

1. **Reset Control Center Password:**
   ```bash
   docker compose exec app-server ./reset-admin-password.sh
   ```

2. **Regenerate API Keys:**
   - Via database (emergency only):
   ```sql
   -- This requires database access
   UPDATE api_keys SET status = 'revoked' WHERE key_id = 'old_key';
   INSERT INTO api_keys (key_id, key_value, ...) VALUES (...);
   ```

3. **Complete Reset:**
   ```bash
   # ⚠️ WARNING: This deletes all data
   docker compose down -v
   rm -rf ./data
   ./scripts/setup.sh  # Fresh install
   ```

---

**Security Reminder:** 🔐 Always change default credentials immediately in any non-demo environment!

**Last Updated:** April 2026  
**Security Level:** Internal/Dev Only - Change for Production