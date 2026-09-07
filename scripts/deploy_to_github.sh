#!/usr/bin/env bash
# Push to github.com/Adi4545/adityasharma (create repo if missing).
# Requires GH_TOKEN or GITHUB_TOKEN with repo scope for account Adi4545.

set -euo pipefail

GITHUB_USER="${GITHUB_USER:-Adi4545}"
REPO_NAME="${REPO_NAME:-adityasharma}"
REMOTE_NAME="${REMOTE_NAME:-github}"
BRANCH="${BRANCH:-main}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"
if [[ -z "$TOKEN" ]]; then
  echo "Error: set GH_TOKEN or GITHUB_TOKEN (repo scope for ${GITHUB_USER})." >&2
  exit 1
fi

export GH_TOKEN="$TOKEN"
REMOTE_URL="https://${GITHUB_USER}:${TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"

cd "$ROOT"

if ! /exec-daemon/gh repo view "${GITHUB_USER}/${REPO_NAME}" >/dev/null 2>&1; then
  echo "Creating https://github.com/${GITHUB_USER}/${REPO_NAME} ..."
  /exec-daemon/gh repo create "${GITHUB_USER}/${REPO_NAME}" \
    --public \
    --description "AIPEG chapter: When the Algorithm Meets the Absent Facility (India e-waste circular economy)" \
    --source=. \
    --remote="${REMOTE_NAME}" \
    --push
else
  if git remote get-url "$REMOTE_NAME" >/dev/null 2>&1; then
    git remote set-url "$REMOTE_NAME" "$REMOTE_URL"
  else
    git remote add "$REMOTE_NAME" "$REMOTE_URL"
  fi
  git push -u "$REMOTE_NAME" "$BRANCH"
fi

echo ""
echo "Repository: https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo "Enable GitHub Pages: Settings → Pages → Source: GitHub Actions"
echo "Site (after Pages deploy): https://${GITHUB_USER}.github.io/${REPO_NAME}/"
