#!/usr/bin/env python3
"""
GitHub-based sync for Claude Shared Memory
Simple, reliable, version-controlled sync
"""

import os
import json
import subprocess
import datetime
from pathlib import Path
from memory_sync import MemorySync

class GitHubSync:
    def __init__(self, repo_url=None, token_path=None):
        self.memory_sync = MemorySync()
        self.repo_path = Path.home() / 'claude-space' / 'shared-memory-repo'
        self.memory_file = 'shared_memory.json'
        
        # Load token
        if not token_path:
            token_path = Path.home() / 'claude-space' / 'config' / 'github_token.txt'
        
        if token_path.exists():
            self.token = token_path.read_text().strip()
        else:
            self.token = None
            print("⚠️  No GitHub token found!")
        
        self.repo_url = repo_url
    
    def setup_repo(self, github_username):
        """Initial repository setup"""
        if not self.token:
            print("✗ No token available")
            return False
        
        # Build authenticated URL
        self.repo_url = f"https://{self.token}@github.com/{github_username}/claude-shared-memory.git"
        
        try:
            if self.repo_path.exists():
                print("✓ Repository already exists locally")
                return True
            
            # Clone repository
            print("📥 Cloning repository...")
            result = subprocess.run(
                ['git', 'clone', self.repo_url, str(self.repo_path)],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✓ Repository cloned successfully")
                
                # Configure git
                os.chdir(self.repo_path)
                subprocess.run(['git', 'config', 'user.name', 'Claude Memory Sync'], check=True)
                subprocess.run(['git', 'config', 'user.email', 'claude@local'], check=True)
                
                return True
            else:
                print(f"✗ Clone failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"✗ Setup failed: {e}")
            return False
    
    def pull_latest(self):
        """Pull latest changes from GitHub"""
        try:
            os.chdir(self.repo_path)
            
            # Fetch and pull
            result = subprocess.run(
                ['git', 'pull', 'origin', 'main'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✓ Pulled latest changes")
                return True
            else:
                print(f"⚠️  Pull had issues: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"✗ Pull failed: {e}")
            return False
    
    def commit_and_push(self, message="Update shared memory"):
        """Commit and push changes"""
        try:
            os.chdir(self.repo_path)
            
            # Add changes
            subprocess.run(['git', 'add', self.memory_file], check=True)
            
            # Check if there are changes
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True
            )
            
            if not result.stdout.strip():
                print("✓ No changes to commit")
                return True
            
            # Commit
            commit_msg = f"{message} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            print("✓ Committed changes")
            
            # Push
            result = subprocess.run(
                ['git', 'push', 'origin', 'main'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✓ Pushed to GitHub")
                return True
            else:
                # Try to create main branch if it doesn't exist
                if "error: src refspec main does not match any" in result.stderr:
                    subprocess.run(['git', 'branch', '-M', 'main'], check=True)
                    subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
                    print("✓ Created main branch and pushed")
                    return True
                else:
                    print(f"✗ Push failed: {result.stderr}")
                    return False
                    
        except Exception as e:
            print(f"✗ Commit/push failed: {e}")
            return False
    
    def sync(self):
        """Perform full sync"""
        try:
            print("\n🔄 Starting GitHub sync...")
            
            # Ensure we're in repo
            if not self.repo_path.exists():
                print("✗ Repository not set up")
                return False
            
            # Pull latest
            self.pull_latest()
            
            # Load local memory
            local_memory = self.memory_sync.load_or_create_memory()
            print("✓ Loaded local memory")
            
            # Load remote memory
            remote_path = self.repo_path / self.memory_file
            if remote_path.exists():
                with open(remote_path, 'r') as f:
                    remote_memory = json.load(f)
                print("✓ Loaded remote memory")
                
                # Merge
                merged_memory = self.memory_sync.merge_memories(local_memory, remote_memory)
                print("✓ Merged memories")
            else:
                merged_memory = local_memory
                print("✓ No remote memory yet, using local")
            
            # Save to both locations
            self.memory_sync.save_memory(merged_memory)
            with open(remote_path, 'w') as f:
                json.dump(merged_memory, f, indent=2)
            print("✓ Saved merged memory")
            
            # Commit and push
            self.commit_and_push("Sync from DevOne laptop")
            
            print("✅ Sync complete!")
            return True
            
        except Exception as e:
            print(f"✗ Sync failed: {e}")
            return False

def main():
    """Interactive setup and sync"""
    print("🧠 Claude Shared Memory - GitHub Sync")
    print("=" * 40)
    
    sync = GitHubSync()
    
    # Check if already set up
    if not sync.repo_path.exists():
        username = input("\n🔧 Enter your GitHub username: ").strip()
        if sync.setup_repo(username):
            print("\n✓ Setup complete!")
        else:
            print("\n✗ Setup failed")
            return
    
    # Run sync
    sync.sync()

if __name__ == "__main__":
    main()