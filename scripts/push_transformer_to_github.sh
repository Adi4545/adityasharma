#!/usr/bin/env bash
# Push ONLY transformer-course PDFs to github.com/Adi4545/adityasharma
# Requires GH_TOKEN or GITHUB_TOKEN in environment (Cursor Secrets tab).

set -euo pipefail

GITHUB_USER="${GITHUB_USER:-Adi4545}"
REPO_NAME="${REPO_NAME:-adityasharma}"
BRANCH="${BRANCH:-transformer-course-download}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"
if [[ -z "$TOKEN" ]]; then
  echo "ERROR: GH_TOKEN is not set." >&2
  echo "" >&2
  echo "This cloud agent can push to origin.cursor.com but NOT github.com without your token." >&2
  echo "" >&2
  echo "Fix:" >&2
  echo "  1. Open https://github.com/settings/tokens" >&2
  echo "  2. Create token with 'repo' scope for Adi4545/adityasharma" >&2
  echo "  3. Cursor Dashboard → Cloud Agents → Secrets → add as GH_TOKEN" >&2
  echo "  4. Start a NEW agent run (or reply 'token added')" >&2
  exit 1
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

# Fine-grained PATs require x-access-token username for git operations
REMOTE_URL="https://x-access-token:${TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo "Cloning github.com/${GITHUB_USER}/${REPO_NAME} ..."
git clone --depth 1 "$REMOTE_URL" "$WORKDIR/repo"
cd "$WORKDIR/repo"

git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"

mkdir -p transformer-course
cp "$ROOT/transformer-course/Transformer_Complete_Course_Attention_Is_All_You_Need.pdf" transformer-course/
cp "$ROOT/transformer-course/Attention_Is_All_You_Need_Vaswani_2017.pdf" transformer-course/
cp "$ROOT/transformer-course/Transformer_Course_All_PDFs.zip" transformer-course/
cp "$ROOT/transformer-course/DOWNLOAD.md" transformer-course/
cp "$ROOT/Transformer_Course_Complete.pdf" .

cat > DOWNLOAD_TRANSFORMER_COURSE.txt <<'EOF'
Download from this GitHub branch:
  transformer-course/Transformer_Course_All_PDFs.zip
  transformer-course/Transformer_Complete_Course_Attention_Is_All_You_Need.pdf
  Transformer_Course_Complete.pdf (workspace root copy)

On GitHub: click the file → click Download (raw) button.
EOF

git add transformer-course/ Transformer_Course_Complete.pdf DOWNLOAD_TRANSFORMER_COURSE.txt
git config user.email "mr.sharmaaditya1999@gmail.com"
git config user.name "Aditya Sharma"

if git diff --cached --quiet; then
  echo "No changes to push."
else
  git commit -m "Add Transformer course PDFs (Parts 0-20) for download"
fi

git push -u origin "$BRANCH"

echo ""
echo "SUCCESS. Download from GitHub:"
echo "  https://github.com/${GITHUB_USER}/${REPO_NAME}/tree/${BRANCH}/transformer-course"
echo ""
echo "Direct ZIP (after push):"
echo "  https://github.com/${GITHUB_USER}/${REPO_NAME}/raw/${BRANCH}/transformer-course/Transformer_Course_All_PDFs.zip"
echo "Direct PDF:"
echo "  https://github.com/${GITHUB_USER}/${REPO_NAME}/raw/${BRANCH}/transformer-course/Transformer_Complete_Course_Attention_Is_All_You_Need.pdf"
