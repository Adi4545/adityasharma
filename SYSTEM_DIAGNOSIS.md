# System Diagnosis — Why Download & GitHub Push Failed

Checked: 2026-09-09. This is factual, not a workaround list.

## What IS working

| Item | Status |
|------|--------|
| PDF files on cloud VM | OK — 45-page course, ZIP, original paper |
| Push to **origin.cursor.com** | OK — branch `cursor/transformer-detailed-course-pdf-fc84` |
| Pull Request on Cursor | OK — PR #6 open |
| Network to github.com | OK |

Files on the remote branch right now:
- `transformer-course/Transformer_Course_All_PDFs.zip`
- `transformer-course/Transformer_Complete_Course_Attention_Is_All_You_Need.pdf`
- `Transformer_Course_Complete.pdf`

## What is NOT working (root causes)

### 1. Download from chat links — BROKEN BY DESIGN

- Links like `/opt/cursor/artifacts/...` point to files on the **remote cloud VM**, not your laptop.
- Cursor desktop chat often shows these as **empty links** or opens a PDF preview whose **Save button does nothing**.
- This is a **Cursor UI limitation**, not a missing file.

**Your files are on a remote machine.** They do not automatically appear in your local Downloads folder.

### 2. Push to github.com — BLOCKED: NO CREDENTIALS

```
GH_TOKEN=MISSING
GITHUB_TOKEN=MISSING
gh auth status=NOT LOGGED IN
git remote 'github'=DOES NOT EXIST
```

- This agent can only `git push` to **origin.cursor.com** (Cursor's git).
- **github.com/Adi4545/adityasharma** is a separate remote with **no token configured**.
- Your public GitHub repo currently only has `My App` and `README.md` — the PDFs were never pushed there because the agent has no GitHub write access.

### 3. Two different git hosts (easy to confuse)

| Host | URL | PDFs pushed? |
|------|-----|--------------|
| Cursor Origin | `origin.cursor.com/git/aditya-sharma-1/originate` | YES |
| GitHub | `github.com/Adi4545/adityasharma` | NO |

## How to fix (pick one)

### Fix A — Push to GitHub (recommended)

1. Create token: https://github.com/settings/tokens → **repo** scope
2. Cursor Dashboard → **Cloud Agents → Secrets** → add **`GH_TOKEN`** (exact name)
3. Reply **"token added"** in chat
4. Agent runs: `bash scripts/push_transformer_to_github.sh`
5. Download from normal GitHub URLs (works in any browser)

### Fix B — Download from Cursor PR (browser)

Open: https://cursor.com/codebase/aditya-sharma-1/originate/pull/6

→ Files changed → click ZIP or PDF → download

### Fix C — Open agent in web

https://cursor.com/agents/bc-28def58d-e86c-4984-9c55-3c7cdac5ee5d

Use the web file browser if desktop Files panel is empty.

## What does NOT fix it

- Clicking Save in PDF preview
- Empty chat artifact links
- Pushing without GH_TOKEN
- Expecting cloud VM files to sync to your laptop automatically
