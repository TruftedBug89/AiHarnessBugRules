# AiHarnessBugRules

Rules every AI harness (agent) must follow. These are non-negotiable constraints
for any agent operating on this system. Apply them to agent memory (Hermes
`MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, system prompts) and follow them in every
session. When in doubt, follow the stricter reading.

---

## 1. Secrets are radioactive — never view them, ever

The rule is **not** "don't print secrets." The rule is: **do not even view them.**

- Never read, `cat`, open, or otherwise pull into context any file that holds
  secrets: `.env`, `auth.json`, credentials, tokens, API keys, passwords, private
  keys, or the secret blocks of `config.yaml`.
- Never echo, log, summarize, or return a secret value in any output — not even
  to the owner.
- Never commit, paste, or write a secret into any file, config, skill, or memory.
- When a task must touch a secret (e.g. move it between stores), operate on the
  file programmatically so the value never passes through the model's tokens.
- Listing a file's *name / size / existence* is allowed; reading its *contents*
  is not.

## 2. Least-privilege reads

- Do not read private or personal files unless the current task strictly requires
  their contents.
- Prefer structural inspection (names, sizes, schemas, keys-only) over reading
  content when that answers the question.
- If a file might contain secrets, treat it as a secrets file by default.

## 3. Never leak via side channels

- Check diffs before committing; a secret or private file must never land in a
  commit, log, screenshot, paste, or report.
- Redact or omit secret/private material from every artifact the agent produces.

## 4. Verify before irreversible actions

- Do not run destructive or hard-to-undo actions (`git push`/reset/force,
  `rm -rf`, deploys, data deletion) without explicit approval.
- Prefer reversible, inspectable steps, and show the command before running it.

---

This file is the canonical source of truth for the rules. Mirror it into the
memory of each harness (Hermes `MEMORY.md`, etc.) and re-apply whenever it changes.
