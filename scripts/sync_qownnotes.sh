#!/bin/bash

# Configuration
REPO_PATH="$HOME/Documents/GitHub/qownnotes"  # Path to the local repository
REMOTE_REPO="git@github.com:vmbr309/qownnotes.git"  # GitHub repository
BRANCH="main"  # The branch to sync

# Log file for debugging
LOG_FILE="$HOME/Documents/GitHub/dotfiles/scripts/logs/qownnotes-sync-log.txt"
exec > >(tee -a "$LOG_FILE") 2>&1

# Notification function
notify() {
    local title="$1"
    local message="$2"
    osascript -e "display notification \"$message\" with title \"$title\" sound name 'Sonumi'"
}


# Timestamp
echo "===================="
echo "Sync started at $(date)"
echo "===================="

# Navigate to the repository
cd "$REPO_PATH" || {
  echo "Repository path not found: $REPO_PATH"
  exit 1
}

# Pull the latest changes from the remote repository
echo "Pulling the latest changes from $REMOTE_REPO..."
git pull origin "$BRANCH" || {
  echo "Failed to pull changes. Check your internet connection and repository access."
  exit 1
}

# Stage all changes
echo "Staging all changes..."
git add . || {
  echo "Failed to stage changes."
  exit 1
}

# Commit changes with a timestamp
echo "Committing changes..."
COMMIT_MESSAGE="Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MESSAGE" || {
  echo "No changes to commit."
}

# Push changes to the remote repository
echo "Pushing changes to $REMOTE_REPO..."
git push origin "$BRANCH" || {
  echo "Failed to push changes. Check your internet connection and repository access."
  exit 1
}

echo "Sync complete."