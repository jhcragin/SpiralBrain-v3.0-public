# GitHub and Cloud Synchronization Setup

This guide explains how to set up automatic synchronization between GitHub commits and your cloud deployment at `34.71.11.103`.

## Quick Setup

### Linux/macOS
```bash
chmod +x setup_cloud_sync.sh
./setup_cloud_sync.sh
```

### Windows (PowerShell)
```powershell
.\setup_cloud_sync.ps1
```

## What Gets Configured

### 1. SSH Key Authentication
- Generates an SSH key pair for secure cloud access
- Tests connection to your cloud VM at `34.71.11.103`

### 2. Git Hooks
- **Post-commit hook**: Automatically syncs commits to cloud
- Only triggers on `main` branch commits
- Can be disabled by removing `.cloud_sync_enabled`

### 3. GitHub Actions
- Enhanced CI/CD workflow with automatic cloud deployment
- Deploys on every push to `main` branch
- Requires GitHub repository secrets (see below)

## GitHub Repository Secrets Required

Add these secrets to your GitHub repository (Settings → Secrets and variables → Actions):

```
CLOUD_VM_HOST=34.71.11.103
CLOUD_VM_USER=spiralbrain
CLOUD_VM_SSH_KEY=<your-private-ssh-key>
CLOUD_VM_PORT=22
```

## Manual Cloud Deployment

If you need to deploy manually:

```bash
# SSH into your VM
ssh -i ~/.ssh/spiralbrain_cloud spiralbrain@34.71.11.103

# Navigate to project and deploy
cd /opt/spiralbrain
git pull origin main
pip install -r requirements.txt
docker-compose down
docker-compose up -d --build
```

## Troubleshooting

### SSH Connection Issues
1. Ensure the public key is added to `~/.ssh/authorized_keys` on the VM
2. Verify the VM is accessible: `ping 34.71.11.103`
3. Check SSH service: `sudo systemctl status ssh` (on Ubuntu/Debian)

### Git Hook Issues
1. Ensure hooks are executable: `chmod +x .git/hooks/post-commit`
2. Check if cloud sync is enabled: `ls -la .cloud_sync_enabled`
3. View hook logs: The hook will output status messages during commits

### Deployment Issues
1. Check Docker logs: `docker-compose logs`
2. Verify requirements: `pip list | grep -f requirements.txt`
3. Check VM resources: `df -h` and `free -h`

## Disabling Auto-Sync

To temporarily disable automatic cloud sync:
```bash
rm .cloud_sync_enabled
```

To re-enable:
```bash
touch .cloud_sync_enabled
git config spiralbrain.cloud-sync true
```