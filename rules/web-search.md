# Web Search Rules

## 1. Always use `infoseek` for web search — never the default/degraded tools

Web research and "look this up" requests run through the user's own `infoseek` tool, **always and first**.

- **Tool**: `infoseek` Python package (installed at `C:\Users\lavvo\.prime\agent\kernel-venv\Lib\site-packages\infoseek`) — keyless, multi-engine (15 engines), async. Call `await infoseek.search(query, n=6, engines='auto', fresh=False)` or `infoseek.ask(query, n=5, extract_top=2, budget=2500)` for an LLM-ready context bundle. CLI: `%kernel-venv%\Scripts\infoseek.exe`.
- **Repo (user's own)**: https://github.com/TruftedBug89/infoseek. Manual/other copy: `C:\Users\lavvo\Documents\infoseek`.
- **Order of fallback** (only drop to the next if the previous fails/rate-limits):
  1. `infoseek`
  2. `web-search-free` (keyless DuckDuckGo/Bing/Brave/Yahoo)
  3. `websearch` (Serper API — requires key; last resort)
- **Do NOT** default to any other search tool, and never silently use the platform's default web-search skill before trying `infoseek`.
