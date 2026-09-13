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
# Fine-grained PATs require x-access-token as the git username.
REMOTE_URL="https://x-access-token:${TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"

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
  git fetch "$REMOTE_NAME" "$BRANCH" || true
  if ! git push -u "$REMOTE_NAME" "$BRANCH" 2>/tmp/git-push.log; then
    if rg -q 'workflow scope' /tmp/git-push.log 2>/dev/null; then
      echo "PAT lacks workflow scope; pushing without .github/workflows ..."
      tmp_branch="github-push-$(date +%s)"
      git checkout -b "$tmp_branch"
      git rm -r --ignore-unmatch .github/workflows 2>/dev/null || true
      git diff --cached --quiet || git commit -m "Omit GitHub Actions workflow (PAT needs workflow scope)"
      git push -u "$REMOTE_NAME" "$tmp_branch:$BRANCH" --force-with-lease
      git checkout -
      git branch -D "$tmp_branch"
    elif rg -q 'unrelated histories\\|rejected\\|non-fast-forward' /tmp/git-push.log 2>/dev/null; then
      echo "Regular push failed (unrelated history). Retrying with --force-with-lease..."
      git push -u "$REMOTE_NAME" "$BRANCH" --force-with-lease
    else
      cat /tmp/git-push.log >&2
      exit 1
    fi
  fi
fi

echo ""
echo "Repository: https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo "Enable GitHub Pages: Settings → Pages → Source: GitHub Actions"
echo "Site (after Pages deploy): https://${GITHUB_USER}.github.io/${REPO_NAME}/"
