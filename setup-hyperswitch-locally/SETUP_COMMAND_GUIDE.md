# Hyperswitch Local Setup Command Guide

This guide consolidates all local setup commands and provides clear guidance on which to use for your specific needs.

## Quick Decision Chart

```
What do you want to do?
│
├─► Quick test of Hyperswitch (all-in-one)?
│   └─► Use: scripts/setup.sh
│
├─► Just the app server/backend only?
│   └─► Use: docker compose up -d
│
├─► Development/Contribution to Hyperswitch?
│   └─► Use: docker compose -f docker-compose-development.yml up -d
│
└─► Production-like deployment?
│   └─► See: self-hosting-space/production-deployment/
```

## Setup Options Explained

### Option 1: One-Command Setup (Recommended for Testing)

**Use when:** You want to test Hyperswitch quickly with minimal effort  
**Includes:** App server + Control Center + Web SDK  
**Time:** 15-20 minutes (first run)

```bash
# 1. Clone the repository
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
cd hyperswitch

# 2. Run the setup script
./scripts/setup.sh
```

**What this does:**
1. ✅ Checks prerequisites (Docker, Docker Compose)
2. ✅ Downloads required images
3. ✅ Prompts you to select setup type:
   - **Standard** (recommended): App server + Control Center + Web SDK
   - **Full**: Standard + Monitoring + Scheduler
   - **Standalone**: Core app server only
4. ✅ Starts all services
5. ✅ Displays URLs to access:
   - App Server: http://localhost:8080
   - Control Center: http://localhost:9000
   - Web SDK: http://localhost:5252

**Next steps:**
- Access the Control Center at http://localhost:9000
- Create your first merchant account
- Follow the [account setup guide](../self-hosting-space/hyperswitch-open-source/account-setup/)

---

### Option 2: App Server Only (Backend Development)

**Use when:** You only need the payment processing backend  
**Includes:** App server + Database + Redis  
**Excludes:** Control Center, Web SDK  
**Time:** 10-15 minutes

```bash
# 1. Clone the repository
git clone https://github.com/juspay/hyperswitch
cd hyperswitch

# 2. Start services
docker compose up -d

# 3. Verify (should return 200 OK)
curl --head --request GET 'http://localhost:8080/health'
```

**What this does:**
- Starts the core Hyperswitch app server
- Sets up PostgreSQL database
- Sets up Redis cache
- Compiles the Rust application (takes 10-15 min first time)

**Next steps:**
- Use API directly (no UI)
- [Test a payment](../setup-hyperswitch-locally/test-a-payment.md)
- Integrate with your own frontend

---

### Option 3: Development Environment (Contributors)

**Use when:** You're contributing code to Hyperswitch  
**Includes:** App server with hot-reload + all dependencies  
**Time:** 10-15 minutes

```bash
# 1. Clone the repository
git clone https://github.com/juspay/hyperswitch
cd hyperswitch

# 2. Start development environment
docker compose --file docker-compose-development.yml up -d

# 3. Watch logs
docker compose logs -f
```

**Features:**
- Hot-reload on code changes
- Mounted volumes for live editing
- Debug logging enabled
- All Rust compilation tools included

---

## Command Reference

### Common Docker Compose Commands

```bash
# Start all services (detached mode)
docker compose up -d

# Start with specific profile
docker compose --profile scheduler up -d       # Add job scheduler
docker compose --profile monitoring up -d      # Add monitoring stack
docker compose --profile olap up -d            # Add analytics/OLAP

# View running services
docker compose ps

# View logs
docker compose logs -f                    # All services
docker compose logs -f app-server         # Specific service

# Stop services
docker compose stop

# Stop and remove containers
docker compose down

# Stop and remove containers + volumes (⚠️ deletes data)
docker compose down -v

# Restart a service
docker compose restart app-server

# Scale specific service
docker compose up -d --scale app-server=3
```

### Setup Script Commands

```bash
# Run interactive setup
./scripts/setup.sh

# Run setup with defaults (non-interactive)
./scripts/setup.sh --default

# Setup with specific profile
./scripts/setup.sh --profile full

# View help
./scripts/setup.sh --help
```

## Troubleshooting Setup Commands

### Issue: "docker compose" vs "docker-compose"

**Problem:** Some systems have `docker-compose` (v1), others have `docker compose` (v2)

**Solution:**
```bash
# Check which version you have
docker compose version      # Try this first
docker-compose --version    # Try this if above fails

# Create alias if needed (add to ~/.bashrc or ~/.zshrc)
alias docker-compose='docker compose'
```

### Issue: Permission Denied

**Problem:** `scripts/setup.sh: Permission denied`

**Solution:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### Issue: Port Already in Use

**Problem:** `Bind for 0.0.0.0:8080 failed: port is already allocated`

**Solution:**
```bash
# Find what's using the port
lsof -i :8080

# Stop the conflicting service or use different ports
# Edit docker-compose.yml to change ports:
# ports:
#   - "8081:8080"  # Maps host 8081 to container 8080
```

### Issue: Compilation Takes Too Long

**Problem:** First `docker compose up` takes 30+ minutes

**Solutions:**
1. **Increase Docker resources:**
   - Docker Desktop → Settings → Resources
   - CPUs: 4+, Memory: 8GB+, Swap: 2GB+

2. **Use pre-built images (if available):**
   ```bash
   docker pull juspaydotin/hyperswitch-router:latest
   docker compose up -d
   ```

3. **Enable Docker BuildKit:**
   ```bash
   export DOCKER_BUILDKIT=1
   docker compose up -d
   ```

## Environment-Specific Notes

### macOS

```bash
# Use Docker Desktop (recommended)
# OR use OrbStack (faster alternative)
brew install orbstack

# Grant file sharing permissions if using volumes
# Docker Desktop → Settings → Resources → File Sharing
```

### Linux

```bash
# Install Docker and Compose
sudo apt-get update
sudo apt-get install docker.io docker-compose-plugin

# Add user to docker group
sudo usermod -aG docker $USER
# Log out and back in for group changes to take effect
```

### Windows (WSL2)

```bash
# In WSL2 terminal, NOT Windows CMD/PowerShell
# Install Docker Desktop with WSL2 integration enabled

# Clone and setup
git clone https://github.com/juspay/hyperswitch
cd hyperswitch
./scripts/setup.sh
```

## Verification Checklist

After running any setup command, verify:

```bash
# 1. All containers are running
docker compose ps
# Should show: app-server, postgres, redis (and others depending on setup)

# 2. App server health endpoint
curl http://localhost:8080/health
# Expected: {"status":"healthy"}

# 3. Database is accessible
docker compose exec postgres psql -U hyperswitch -c "SELECT 1;"
# Expected: ?column? = 1

# 4. Redis is accessible
docker compose exec redis redis-cli ping
# Expected: PONG
```

## Next Steps After Setup

1. **Account Setup**
   ```bash
   # Open Control Center (if installed)
   open http://localhost:9000
   # OR follow: ../self-hosting-space/hyperswitch-open-source/account-setup/
   ```

2. **Configure Payment Processor**
   - Add Stripe/Adyen/other connector in Control Center
   - Or use API: [Connector Setup Guide](../integration-guide/workflows/connectors/)

3. **Test Payment**
   ```bash
   # Follow: ../setup-hyperswitch-locally/test-a-payment.md
   ```

4. **Web SDK Setup** (if not using setup.sh)
   ```bash
   # Clone and setup separately
   git clone https://github.com/juspay/hyperswitch-web.git
   cd hyperswitch-web
   npm install && npm run start:dev
   ```

## Related Documentation

- [System Requirements](./SYSTEM_REQUIREMENTS.md) - Hardware/software prerequisites
- [Account Setup](../self-hosting-space/hyperswitch-open-source/account-setup/) - After installation
- [Test a Payment](./test-a-payment.md) - Verify your setup
- [Production Deployment](../self-hosting-space/production-deployment/) - For production installs

## Common Mistakes to Avoid

❌ **Don't mix setup methods**
- Using `setup.sh` and then running `docker compose` separately can cause conflicts
- Choose one method and stick with it

❌ **Don't forget prerequisites**
- Docker must be running before executing commands
- Check available ports (8080, 5432, 6379, etc.)

❌ **Don't run in production as-is**
- Default setups are for development/testing
- Use production deployment guides for real deployments

❌ **Don't ignore logs**
- Always check logs if something fails: `docker compose logs -f`
- Look for specific error messages

## Quick Reference Card

Save this for quick access:

```
┌─────────────────────────────────────────────────────────────┐
│  HYPERSWITCH LOCAL SETUP - QUICK REFERENCE                 │
├─────────────────────────────────────────────────────────────┤
│  QUICK TEST (Everything):                                   │
│  git clone --depth 1 --branch latest \                      │
│    https://github.com/juspay/hyperswitch                   │
│  cd hyperswitch && ./scripts/setup.sh                      │
├─────────────────────────────────────────────────────────────┤
│  BACKEND ONLY:                                              │
│  docker compose up -d                                       │
│  curl http://localhost:8080/health                          │
├─────────────────────────────────────────────────────────────┤
│  DEVELOPMENT:                                               │
│  docker compose -f docker-compose-development.yml up -d     │
├─────────────────────────────────────────────────────────────┤
│  COMMON COMMANDS:                                           │
│  docker compose logs -f     # View logs                    │
│  docker compose ps          # List services                │
│  docker compose down        # Stop all                     │
│  docker compose restart     # Restart                      │
└─────────────────────────────────────────────────────────────┘
```

---

**Last Updated:** April 2026  
**Tested with:** Docker 24.x, Docker Compose 2.x  
**Questions?** [Join our Slack](https://join.slack.com/t/hyperswitch-io/shared_invite)