# Security Rules

## 1. Secrets are radioactive — never view them, ever

The rule is **not** "don't print secrets." The rule is: **do not even view them.**

- Never read, `cat`, open, or otherwise pull into context any file that holds secrets: `.env`, `auth.json`, credentials, tokens, API keys, passwords, private keys, or the secret blocks of `config.yaml`.
- Never echo, log, summarize, or return a secret value in any output — not even to the owner.
- Never commit, paste, or write a secret into any file, config, skill, or memory.
- When a task must touch a secret (e.g. move it between stores), operate on the file programmatically so the value never passes through the model's tokens.
- Listing a file's *name / size / existence* is allowed; reading its *contents* is not.

## 2. Never leak via side channels

- Check diffs before committing; a secret or private file must never land in a commit, log, screenshot, paste, or report.
- Redact or omit secret/private material from every artifact the agent produces.
