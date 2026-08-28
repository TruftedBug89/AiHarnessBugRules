# Permissions Rules

## 1. Least-privilege reads

- Do not read private or personal files unless the current task strictly requires their contents.
- Prefer structural inspection (names, sizes, schemas, keys-only) over reading content when that answers the question.
- If a file might contain secrets, treat it as a secrets file by default.

## 2. Verify before irreversible actions

- Do not run destructive or hard-to-undo actions (`git push`/reset/force, `rm -rf`, deploys, data deletion) without explicit approval.
- Prefer reversible, inspectable steps, and show the command before running it.
