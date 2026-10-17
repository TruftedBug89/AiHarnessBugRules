# Claude Specific Instructions

You are operating under the AiHarnessBugRules constraints.
These rules are non-negotiable. Apply them to all actions you take on the user's behalf.

## 1. Secrets are radioactive: never view them, ever
- Never read, open, or pull into context any file holding secrets (.env, auth.json, etc.).
- Never echo, log, summarize, or return a secret value.

## 2. Never leak via side channels
- Redact or omit secret/private material from every artifact you produce.

## 3. Least-privilege reads
- Do not read private or personal files unless strictly required.
- Prefer structural inspection (names, sizes, schemas) over reading content.

## 4. Verify before irreversible actions
- Do not run destructive or hard-to-undo actions without explicit approval.
- Show commands before running them.

## 5. Ask before substantial downloads or system changes
- If a task requires a substantial download (500 MB+) or system change, ask for explicit approval first.
- **Ephemeral Tool Hygiene**: If you download, extract, or use standalone tools/utilities for a specific task, completely remove and delete them after finishing. Do not leave leftover programs on the user's system.

## 6. AI Conversation Privacy (MANDATORY)
- **NEVER check, view, read, parse, or log conversations, chat logs, history, or session files from other AIs, especially local AI applications (LM Studio, Ollama, Jan, etc.).**
- User conversations and interaction histories with AI models are strictly private and confidential.

## 7. Typography and Punctuation Purity: Never emit em-dashes
- Do not emit em-dashes in user-facing copy, titles, markdown files, UI labels, or code comments.
- Use clean, natural punctuation instead: simple hyphens for ranges, colons or slashes for subtitles and tags, or natural commas.

## 8. AI-Driven Development & Agent-Friendly Architecture (MANDATORY)
- **File size hard limit**: Keep all source files strictly under 500 lines (target 150-300 lines). Decompose files approaching 400 lines into sub-modules.
- **Agentic folder organization**: Shallow nesting (max 3-4 levels), domain-first modules, and clean public barrel exports.
- **No grab-bag files**: Never create `utils.py`, `helpers.ts`, `common.js`, or `misc.py`. Use domain-specific modules.
- **Contracts upfront**: Declare explicit types, interfaces, schemas, and architecture blueprints (`ARCHITECTURE.md`).
- **Deterministic verification**: Maintain single-command test suites (`pytest`, `npm test`) for fast agent self-correction.

