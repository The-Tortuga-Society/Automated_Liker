#!/bin/bash
export GIT_SSH_COMMAND="ssh -i ~/.ssh/github-deploy-key"

python3 Liker_Feeder.py
git status

git add .
git commit -m "JSON data dump at $(date)"
git push origin main
git status
