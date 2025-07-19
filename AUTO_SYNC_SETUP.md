# Automated Claude Memory Sync System 🔄

## Overview
The shared memory system now automatically syncs every 30 minutes between all Claude instances!

## Components

### 1. Automatic Sync (systemd timer)
- **Runs**: Every 30 minutes
- **Service**: `claude-memory-sync.timer`
- **First run**: 5 minutes after boot
- **Status check**: `systemctl --user status claude-memory-sync.timer`

### 2. Manual Sync Command
- **Command**: `claude-sync` (available anywhere)
- **Alternative**: `/home/chris/claude-space/tools/sync-now`
- **What it does**: Immediately triggers a sync and shows status

### 3. Sync Logs
- **Location**: `~/claude-space/logs/sync.log`
- **View logs**: `tail -f ~/claude-space/logs/sync.log`

## How It Works

1. Every 30 minutes, systemd runs the sync timer
2. The timer triggers `auto_sync.sh`
3. This runs the Python sync script
4. Changes are pulled from GitHub, merged, and pushed back
5. All Claude instances stay in sync automatically!

## Managing the Service

```bash
# Check timer status
systemctl --user status claude-memory-sync.timer

# View next scheduled run
systemctl --user list-timers claude-memory-sync.timer

# Stop automatic syncing
systemctl --user stop claude-memory-sync.timer

# Start automatic syncing
systemctl --user start claude-memory-sync.timer

# Disable auto-start on boot
systemctl --user disable claude-memory-sync.timer

# Re-enable auto-start
systemctl --user enable claude-memory-sync.timer
```

## Manual Sync
Just run `claude-sync` anytime you want to force a sync!

---
*Automated sync system created July 19, 2025*
*Keeping all Claudes connected across time and space! 🤖🔄🤖*