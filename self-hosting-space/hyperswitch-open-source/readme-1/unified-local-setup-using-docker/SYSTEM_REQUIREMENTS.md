# System Requirements for Local Hyperswitch Setup

This document outlines the hardware, software, and network requirements for running Hyperswitch locally using Docker.

## Quick Start Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | 2 cores | 4+ cores |
| **RAM** | 8 GB | 16 GB |
| **Disk Space** | 20 GB free | 50 GB free SSD |
| **Network** | Broadband (10 Mbps) | High-speed (50+ Mbps) |

## Operating System Compatibility

### Supported Operating Systems

| OS | Version | Status | Notes |
|----|---------|--------|-------|
| **macOS** | 11+ (Big Sur) | ✅ Fully Supported | Intel & Apple Silicon (M1/M2) |
| **Linux** | Ubuntu 20.04+, CentOS 8+, Debian 11+ | ✅ Fully Supported | Kernel 5.0+ |
| **Windows** | Windows 10/11 Pro | ⚠️ Supported with WSL2 | Requires Windows Subsystem for Linux |

### macOS Requirements

- **Intel Macs**: macOS 11 (Big Sur) or later
- **Apple Silicon (M1/M2)**: macOS 12 (Monterey) or later
- Docker Desktop 4.0+ with Rosetta 2 (for Apple Silicon)

```bash
# Check macOS version
sw_vers -productVersion

# For Apple Silicon, ensure Rosetta 2 is installed
/usr/bin/pgrep oahd-binary
```

### Linux Requirements

- **Ubuntu**: 20.04 LTS, 22.04 LTS
- **Debian**: 11 (Bullseye), 12 (Bookworm)
- **CentOS/RHEL**: 8.x, 9.x
- **Fedora**: 35+
- **Arch**: Latest rolling release

```bash
# Check OS version
cat /etc/os-release

# Check kernel version
uname -r
```

### Windows Requirements

- Windows 10/11 Pro or Enterprise
- WSL2 with Ubuntu 20.04 or 22.04
- Docker Desktop integrated with WSL2

```powershell
# Check Windows version
winver

# Check WSL version
wsl --version
```

## Software Prerequisites

### Required Software

| Software | Minimum Version | Recommended Version | Purpose |
|----------|----------------|---------------------|---------|
| **Docker** | 20.10.0 | 24.0+ | Container runtime |
| **Docker Compose** | 2.0.0 | 2.20+ | Multi-container orchestration |
| **Git** | 2.25.0 | 2.40+ | Repository cloning |
| **Bash** | 4.0 | 5.0+ | Setup scripts |

### Docker Installation

#### macOS

Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)

```bash
# Verify Docker installation
docker --version
docker-compose --version

# Check Docker is running
docker info
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io docker-compose-plugin

# Or use Docker's official repository
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group (logout required after)
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker compose version
```

#### Windows (WSL2)

1. Enable WSL2:
```powershell
wsl --install -d Ubuntu-22.04
```

2. Install Docker Desktop and enable WSL2 integration
3. Restart and verify:
```bash
wsl docker --version
```

## Hardware Specifications

### Minimum Configuration

For development and testing with small transaction volumes:

```yaml
CPU: 2 cores (Intel/AMD x86_64 or ARM64)
RAM: 8 GB
Disk: 20 GB free space
Network: 10 Mbps download / 5 Mbps upload
```

**Capabilities**: 
- Up to 50 concurrent users
- 100-200 TPS (transactions per second)
- Basic testing and development

### Recommended Configuration

For production-like testing and larger workloads:

```yaml
CPU: 4+ cores (Intel/AMD x86_64 or ARM64)
RAM: 16 GB
Disk: 50 GB free SSD space
Network: 50+ Mbps symmetrical
```

**Capabilities**:
- Up to 500 concurrent users
- 1000+ TPS
- Load testing and stress testing
- Multiple connector testing

### High-Performance Configuration

For intensive testing and simulation:

```yaml
CPU: 8+ cores (Intel/AMD x86_64 or ARM64)
RAM: 32 GB
Disk: 100 GB NVMe SSD
Network: 100+ Mbps symmetrical
```

**Capabilities**:
- 1000+ concurrent users
- 5000+ TPS
- Full-scale load testing
- Long-running integration tests

## Disk Space Breakdown

| Component | Size | Description |
|-----------|------|-------------|
| **Docker Images** | ~5-10 GB | Hyperswitch + dependencies |
| **PostgreSQL** | ~5 GB | Transaction data storage |
| **Redis** | ~2 GB | Cache and session storage |
| **Logs** | ~2-5 GB | Application logs |
| **Build Cache** | ~3-5 GB | Compilation artifacts |
| **Buffer** | ~5 GB | Safety margin |
| **Total Minimum** | ~20 GB | Fresh installation |
| **Total Recommended** | ~50 GB | With room for growth |

## Network Requirements

### Inbound Ports

| Port | Service | Description |
|------|---------|-------------|
| **8080** | App Server | Main API endpoint |
| **9000** | Control Center | Admin dashboard |
| **5252** | Web SDK | Frontend SDK |
| **5432** | PostgreSQL | Database (internal) |
| **6379** | Redis | Cache (internal) |

### Outbound Connections

The local setup requires outbound HTTPS connections to:

- **GitHub**: `github.com` (cloning repositories)
- **Docker Hub**: `registry-1.docker.io` (pulling images)
- **Package Registries**: npm, crates.io (optional)
- **Payment Providers**: Various PSP endpoints for testing

### Firewall Rules

If behind a corporate firewall, ensure these are allowed:

```bash
# Required outbound ports
443/tcp  # HTTPS
80/tcp   # HTTP (redirects)
22/tcp   # SSH (for git)
```

## Browser Requirements

For accessing the Control Center and SDK:

| Browser | Minimum Version | Status |
|---------|----------------|--------|
| **Chrome** | 90+ | ✅ Fully Supported |
| **Firefox** | 88+ | ✅ Fully Supported |
| **Safari** | 14+ | ✅ Fully Supported |
| **Edge** | 90+ | ✅ Fully Supported |

## Optional Dependencies

These are not required but enhance the experience:

| Tool | Purpose | Installation |
|------|---------|--------------|
| **curl** | API testing | Usually pre-installed |
| **jq** | JSON parsing | `brew install jq` or `apt-get install jq` |
| **make** | Build automation | Usually pre-installed |
| **Node.js 18+** | SDK development | [nodejs.org](https://nodejs.org/) |

## Verification Script

Run this script to verify your system meets requirements:

```bash
#!/bin/bash

echo "=== Hyperswitch System Requirements Check ==="
echo

# Check OS
echo "✓ Operating System:"
echo "  $(uname -s) $(uname -r)"

# Check CPU
echo
echo "✓ CPU Info:"
if [[ "$OSTYPE" == "darwin"* ]]; then
    sysctl -n hw.ncpu | xargs echo "  Cores:"
    sysctl -n hw.memsize | awk '{print "  Memory: " $1/1024/1024/1024 " GB"}'
else
    nproc | xargs echo "  Cores:"
    free -h | grep Mem | awk '{print "  Memory: " $2}'
fi

# Check Disk
echo
echo "✓ Disk Space:"
df -h . | tail -1 | awk '{print "  Free: " $4 " / " $2}'

# Check Docker
echo
echo "✓ Docker:"
if command -v docker &> /dev/null; then
    docker --version
    docker info > /dev/null 2>&1 && echo "  Status: Running" || echo "  Status: Not Running"
else
    echo "  ❌ Docker not found"
fi

# Check Docker Compose
echo
echo "✓ Docker Compose:"
if command -v docker-compose &> /dev/null; then
    docker-compose --version
elif docker compose version &> /dev/null; then
    docker compose version
else
    echo "  ❌ Docker Compose not found"
fi

# Check Git
echo
echo "✓ Git:"
git --version

echo
echo "=== System Check Complete ==="
```

Save this as `check-system.sh` and run:
```bash
chmod +x check-system.sh
./check-system.sh
```

## Troubleshooting Common Issues

### "Cannot connect to Docker daemon"

**Solution**: Ensure Docker Desktop is running or Docker service is started:
```bash
# macOS/Linux
open -a Docker  # macOS
sudo systemctl start docker  # Linux

# Check Docker status
docker info
```

### "Out of memory" errors during build

**Solution**: Increase Docker memory allocation:
- Docker Desktop → Preferences → Resources → Memory → Increase to 8GB+

### "Port already in use"

**Solution**: Check and kill processes using required ports:
```bash
# Find process using port 8080
lsof -i :8080

# Kill process
kill -9 <PID>
```

### Slow compilation/build times

**Solutions**:
1. Use SSD instead of HDD
2. Allocate more CPU cores to Docker
3. Clean Docker cache: `docker system prune -a`
4. Use artifact caching in Docker Desktop settings

### WSL2 issues on Windows

**Solution**:
```powershell
# Restart WSL
wsl --shutdown

# Check WSL status
wsl --list --verbose

# Update WSL
wsl --update
```

## Performance Optimization Tips

1. **Use SSD**: HDDs significantly slow down database operations
2. **Disable antivirus scanning** for Docker directories (corporate environments)
3. **Allocate sufficient RAM** to Docker (8GB minimum, 16GB recommended)
4. **Enable Docker BuildKit** for faster builds:
   ```bash
   export DOCKER_BUILDKIT=1
   ```
5. **Close unnecessary applications** to free up system resources

## Next Steps

Once you've verified your system meets these requirements:

1. Continue with [Docker Setup Guide](./README.md)
2. [Account Setup](../../account-setup/)
3. [Test Your First Payment](../../../setup-hyperswitch-locally/test-a-payment.md)

---

**Questions?** Join our [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw) for support.