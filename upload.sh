#!/bin/bash
export GIT_SSH_COMMAND="ssh -i ~/.ssh/github-deploy-key"

git pull origin main
git add Liker_Data.json
git commit -m "JSON data dump at $(date)"
git push origin main
