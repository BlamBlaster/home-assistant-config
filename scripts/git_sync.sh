#!/bin/bash

cd /config

# Add all changes
git add .

# Commit with timestamp (only if there are changes)
if ! git diff --cached --quiet; then
  git commit -m "Auto backup: $(date '+%Y-%m-%d %H:%M:%S')"
  git push origin main
else
  echo "No changes to commit"
fi
