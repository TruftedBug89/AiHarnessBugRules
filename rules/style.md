# Style & Typography Rules

## 1. Typography and Punctuation Purity: Never emit em-dashes

Do not emit em-dashes (U+2014) in user-facing copy, documentation, titles, markdown files, UI labels, or code comments.

- Em-dashes are one of the most prominent tells of AI-generated text and formulaic prose.
- Use clean, natural punctuation instead:
  - Simple hyphens (`-`) for ranges (e.g. `2023 - 2025` or `1 - 5`).
  - Colons (`:`) or forward slashes (`/`) for subtitles, tags, and category labels.
  - Commas (`, `), periods, or natural sentence phrasing for pauses and clauses.
- When generating code, comments, summaries, or commit messages, maintain an authentic developer aesthetic without decorative typography.
