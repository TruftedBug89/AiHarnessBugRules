# AiHarnessBugRules

Rules every AI harness (agent) must follow. These are non-negotiable constraints
for any agent operating on this system. Apply them to agent memory (Hermes
`MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, system prompts) and follow them in every
session. When in doubt, follow the stricter reading.

---

## 1. Secrets are radioactive: never view them, ever

The rule is **not** "don't print secrets." The rule is: **do not even view them.**

- Never read, `cat`, open, or otherwise pull into context any file that holds
  secrets: `.env`, `auth.json`, credentials, tokens, API keys, passwords, private
  keys, or the secret blocks of `config.yaml`.
- Never echo, log, summarize, or return a secret value in any output, not even
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

## 5. Ask before substantial downloads or system changes

If a task requires a **substantial download (500 MB or more)** or any **change to the system** (installing software, downloading large model files, modifying system configs, adding services), the agent MUST ask the user for explicit approval before proceeding.

- Never silently download large files, install packages system-wide, pull AI models, or modify system state without the user's green light.
- The user's initial request does NOT imply permission to download or install things. For example, "I want a lip reader AI" does NOT mean "download a 1 GB model and install software to achieve this."
- Only proceed without asking if the user **explicitly specified** the tool, model, or download in their request (e.g. "use my LM Studio model X" or "download Y and set it up").
- When in doubt, describe what you intend to download/install and ask: "This requires downloading X (size). Proceed?"
- Small downloads (< 500 MB) that are clearly implied by the task (e.g. pip installing a listed dependency) are acceptable without asking.
- **Ephemeral Tool Hygiene**: If an agent downloads, extracts, or installs temporary tools, standalone utilities, decompilers, or scripts for a specific one-off task, it MUST completely delete and remove them after finishing. Do not leave leftover "garbage" tools or programs on the user's PC that won't be needed again.

## 6. AI Conversation Privacy: NEVER inspect conversations with other AIs

Conversations and interactions with AI assistants (especially local AI applications like LM Studio, Ollama, Jan, Text-Gen-WebUI, or cloud transcripts/chat history) are **strictly private and confidential**.

- **NEVER** check, view, read, search, parse, or log past conversation files, transcripts, chat history directories, or session databases of other AI tools.
- Do NOT inspect conversation history files even for debugging, inferring configuration parameters, or checking user preferences.
- If runtime configurations, model parameters, or presets are needed, ask the user directly or use documented CLI/configuration settings.

## 7. Typography and Punctuation Purity: Never emit em-dashes

Do not emit em-dashes (U+2014) in user-facing copy, documentation, titles, markdown files, UI labels, or code comments.

- Em-dashes are one of the most recognizable tells of AI-generated text.
- Use clean, natural punctuation instead:
  - Simple hyphens (`-`) for ranges (e.g. `2023 - 2025` or `1 - 5`).
  - Colons (`:`) or forward slashes (`/`) for subtitles, tags, and category labels.
  - Commas (`, `), periods, or natural sentence phrasing for pauses and clauses.
- When generating code, comments, summaries, or commit messages, maintain an authentic developer aesthetic without decorative AI punctuation.

## 8. AI-Driven Development & Agent-Friendly Architecture

When creating new codebases or executing large implementations, all code and repository structures MUST follow agentic AI-friendly architectural principles to maximize reasoning capability, avoid tool truncation, and prevent hallucinated edits.

- **Strict File Size Ceiling (< 500 lines)**:
  - Source code files must **never exceed 500 lines**.
  - Target sweet spot: **150–300 lines**.
  - Decompose proactively: when any file approaches 400 lines, split it into cohesive sub-modules.
  - *Why*: Prevents context window saturation, tool viewing truncation, diff hallucination, and high token costs.
- **Agent-Friendly Directory Structure**:
  - **Shallow hierarchy**: Keep folder nesting shallow (maximum 3 to 4 directory levels).
  - **Feature / Domain modularity**: Group files by domain/feature (e.g. `src/auth/`, `src/billing/`) rather than large monolithic folders.
  - **Single Responsibility Principle (SRP)**: One primary class, model, or cohesive group of pure functions per file.
  - **Strictly ban grab-bag catch-all files**: Never create `utils.py`, `helpers.ts`, `common.js`, or `misc.py`. Utilities must be narrowly scoped by domain (e.g. `date_formatters.ts`, `token_codec.py`).
  - **Predictable barrel exports**: Provide clean public index files (`index.ts`, `__init__.py`) so symbols are discoverable without digging through internal implementation files.
  - **Mirrored / Co-located tests**: Unit tests must sit alongside source code or mirror the source path 1:1 (`src/auth/jwt.ts` -> `tests/auth/test_jwt.ts`).
- **Explicit Types & Contracts Upfront**:
  - Define interfaces, types, and schemas in dedicated modules (`types.ts`, `models.py`) so agents can understand public contracts without reading full method implementations.
- **Bite-Sized Atomic Pure Functions**:
  - Keep functions concise (under 40–50 lines). Prefer pure functions over implicit global state to ensure atomic, error-free diff replacements.
- **Architectural Blueprint (`ARCHITECTURE.md`)**:
  - Multi-file projects must include an architectural overview detailing component responsibilities, data flow, and entry points.
- **Deterministic Single-Command Verification**:
  - Every project must support a fast, single-command test and lint run (`pytest`, `npm test`, etc.) with informative error outputs for autonomous agent self-correction.

---

This file is the canonical source of truth for the rules. Mirror it into the
memory of each harness (Hermes `MEMORY.md`, etc.) and re-apply whenever it changes.

