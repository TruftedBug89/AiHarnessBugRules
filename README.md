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


## 5. Always use `infoseek` for web search — never the default/degraded tools

Web research and "look this up" requests run through the user's own `infoseek`
tool, **always and first**.

- **Tool**: `infoseek` Python package (installed at
  `C:\Users\lavvo\.prime\agent\kernel-venv\Lib\site-packages\infoseek`)
  — keyless, multi-engine (15 engines), async. Call
  `await infoseek.search(query, n=6, engines='auto', fresh=False)` or
  `infoseek.ask(query, n=5, extract_top=2, budget=2500)` for an LLM-ready
  context bundle. CLI: `%kernel-venv%\Scripts\infoseek.exe`.
- **Repo (user's own)**: https://github.com/TruftedBug89/infoseek
  Manual/other copy: `C:\Users\lavvo\Documents\infoseek`.
- **Order of fallback** (only drop to the next if the previous fails/rate-limits):
  1. `infoseek`
  2. `web-search-free` (keyless DuckDuckGo/Bing/Brave/Yahoo)
  3. `websearch` (Serper API — requires key; last resort)
- **Do NOT** default to any other search tool, and never silently use the
  platform's default web-search skill before trying `infoseek`.

## 6. Ask before substantial downloads or system changes

If a task requires a **substantial download (500 MB or more)** or any **change to the system** (installing software, downloading large model files, modifying system configs, adding services), the agent MUST ask the user for explicit approval before proceeding.

- Never silently download large files, install packages system-wide, pull AI models, or modify system state without the user's green light.
- The user's initial request does NOT imply permission to download or install things. For example, "I want a lip reader AI" does NOT mean "download a 1 GB model and install software to achieve this."
- Only proceed without asking if the user **explicitly specified** the tool, model, or download in their request (e.g. "use my LM Studio model X" or "download Y and set it up").
- When in doubt, describe what you intend to download/install and ask: "This requires downloading X (size). Proceed?"
- Small downloads (< 500 MB) that are clearly implied by the task (e.g. pip installing a listed dependency) are acceptable without asking.

## 7. AI Conversation Privacy — NEVER inspect conversations with other AIs

Conversations and interactions with AI assistants (especially local AI applications like LM Studio, Ollama, Jan, Text-Gen-WebUI, or cloud transcripts/chat history) are **strictly private and confidential**.

- **NEVER** check, view, read, search, parse, or log past conversation files, transcripts, chat history directories, or session databases of other AI tools.
- Do NOT inspect conversation history files even for debugging, inferring configuration parameters, or checking user preferences.
- If runtime configurations, model parameters, or presets are needed, ask the user directly or use documented CLI/configuration settings.

---

This file is the canonical source of truth for the rules. Mirror it into the
memory of each harness (Hermes `MEMORY.md`, etc.) and re-apply whenever it changes.

