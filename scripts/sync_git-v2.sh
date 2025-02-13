#!/bin/zsh

# Configuration
REPO_PATH="$HOME/Documents/gitnotes/"             # Path to the local repository
REMOTE_REPO="git@github.com:vmbr309/gitnotes.git" # GitHub repository
BRANCH="master"                                   # The branch to sync

# Log file for debugging
LOG_FILE="$HOME/Documents/GitHub/dotfiles/scripts/logs/qownnotes-sync-log.txt"
exec {fd}>>"$LOG_FILE"      # Open file descriptor for logging
tee -a "$LOG_FILE" <&{fd} & # Pipe output to log file and console

# Notification function
notify() {
  local title="$1"
  local message="$2"
  osascript -e "display notification \"$message\" with title \"$title\" sound name 'Sonumi'"
}

# Function to retry a command with exponential backoff
retry_command() {
  local cmd="$1"
  local max_attempts=3
  local delay=2 # Initial delay in seconds

  for ((attempt = 1; attempt <= max_attempts; attempt++)); do
    echo "Attempt $attempt: $cmd"
    eval "$cmd" && return 0 # If command succeeds, return success
    echo "Attempt $attempt failed. Retrying in $delay seconds..."
    sleep $delay
    delay=$((delay * 2)) # Exponential backoff
  done

  echo "Error: Command failed after $max_attempts attempts: $cmd"
  notify "Sync Failed" "Command failed: $cmd"
  exit 1
}

# Timestamp
echo "===================="
echo "Sync started at $(date)"
echo "===================="

# Navigate to the repository
cd "$REPO_PATH" || {
  echo "Repository path not found: $REPO_PATH"
  notify "Sync Failed" "Repository path not found: $REPO_PATH"
  exit 1
}

# Pull the latest changes from the remote repository (with retry)
echo "Pulling the latest changes from $REMOTE_REPO..."
retry_command "git pull origin $BRANCH"

# Stage all changes
echo "Staging all changes..."
git add . || {
  echo "Failed to stage changes."
  notify "Sync Failed" "Failed to stage changes."
  exit 1
}

# Commit changes with a timestamp
echo "Committing changes..."
COMMIT_MESSAGE="Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MESSAGE" || {
  echo "No changes to commit."
}

# Push changes to the remote repository (with retry)
echo "Pushing changes to $REMOTE_REPO..."
retry_command "git push origin $BRANCH"

echo "Sync complete."
notify "Sync Successful" "Your notes have been synced successfully!"
