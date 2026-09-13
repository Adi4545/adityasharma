#!/usr/bin/env bash
# Push the research-only tree to github.com/Adi4545/adityasharma.
# Requires GH_TOKEN or GITHUB_TOKEN with repo scope for Adi4545.
# If the token lacks "workflow" scope, GitHub Actions files are omitted from the push.

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
REMOTE_URL="https://x-access-token:${TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"

cd "$ROOT"

if ! command -v gh >/dev/null 2>&1 && [[ -x /exec-daemon/gh ]]; then
  GH=/exec-daemon/gh
else
  GH=gh
fi

if ! "$GH" repo view "${GITHUB_USER}/${REPO_NAME}" >/dev/null 2>&1; then
  echo "Creating https://github.com/${GITHUB_USER}/${REPO_NAME} ..."
  "$GH" repo create "${GITHUB_USER}/${REPO_NAME}" \
    --public \
    --description "AIPEG manuscript + reproducible results (India e-waste circular economy)" \
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
  if ! git push -u "$REMOTE_NAME" "HEAD:${BRANCH}" --force-with-lease 2>/tmp/git-push.log; then
    if grep -q 'workflow scope' /tmp/git-push.log 2>/dev/null; then
      echo "PAT lacks workflow scope; pushing without .github/workflows ..."
      tmp_branch="github-research-$(date +%s)"
      git checkout -b "$tmp_branch"
      git rm -r --ignore-unmatch .github/workflows >/dev/null 2>&1 || true
      if ! git diff --cached --quiet; then
        git commit -m "Omit GitHub Actions workflow (PAT needs workflow scope)"
      fi
      git push -u "$REMOTE_NAME" "${tmp_branch}:${BRANCH}" --force-with-lease
      git checkout -
      git branch -D "$tmp_branch"
    else
      cat /tmp/git-push.log >&2
      exit 1
    fi
  fi
fi

echo ""
echo "Research repository: https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo "Update description: AIPEG manuscript + computational results (research showcase)"
