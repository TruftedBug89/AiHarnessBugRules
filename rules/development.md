# Development Rules

## 1. AI-Driven Development & Agent-Friendly Architecture

All code projects generated or modified during large implementations must be structured for optimal manipulation, reasoning, and navigation by agentic AI models.

### A. File Size Hard Ceiling (< 500 Lines)
- **Hard Limit**: Source code files must never exceed **500 lines of code**.
- **Target Sweet Spot**: Aim for **150–300 lines** per file.
- **Proactive Decomposition**: If a file approaches 400 lines, it must be refactored and split into cohesive sub-modules before adding new functionality.
- **Why**: Large files exhaust model context budgets, trigger truncation in agent file-viewing tools, dramatically increase hallucination rates during replacement diffs, and slow down token generation.

### B. Agent-Friendly Directory Organization
- **Shallow, Predictable Nesting**: Keep folder hierarchy shallow (maximum 3 to 4 directory levels deep). Deeply nested hierarchies cause path errors and excessive navigation tool calls.
- **Domain & Feature First**: Group code by feature or domain boundary (e.g. `src/auth/`, `src/billing/`, `src/notifications/`) rather than technical type dumping grounds (e.g. giant flat folders).
- **Single Responsibility Principle (SRP)**: Each file must serve one well-defined purpose, primary class, or cohesive group of pure functions.
- **Strict Ban on "Grab-Bag" Files**: Never create catch-all junk drawers like `utils.py`, `helpers.ts`, `common.js`, or `misc.py`. Utilities must be narrowly scoped by domain (e.g., `date_parsers.py`, `crypto_hash.ts`, `jwt_codec.py`).
- **Clean Barrel Exports**: Use index files (`index.ts`, `__init__.py`) to declare explicit public APIs so agents can consume symbols without deep private relative imports.
- **Symmetric / Co-located Tests**: Place unit tests directly alongside code or in a strictly mirrored directory structure (e.g., `src/auth/token.ts` -> `tests/auth/test_token.ts`).

### C. Explicit Types, Interfaces, and Contracts Upfront
- Always define explicit data types, interfaces, schemas, and contracts (e.g., TypeScript interfaces, Python Pydantic/dataclasses/type annotations, Go structs).
- Place high-level interfaces in dedicated schema/type files (`types.ts`, `models.py`, `schemas.py`) so agents can read just the contract to understand module behavior without ingesting hundreds of implementation lines.
- Write concise docstrings or type signatures detailing input, output, and potential error states for every public function.

### D. Bite-Sized Pure Functions & Low Coupling
- Keep functions concise (ideally under 40–50 lines).
- Prefer pure functions with explicit inputs and outputs over hidden global state or mutating side effects.
- Small pure functions make atomic edits (`replace_file_content`) fast, deterministic, and free of regression.

### E. Architectural Blueprint (`ARCHITECTURE.md`)
- For multi-file implementations or new codebases, maintain a concise `ARCHITECTURE.md` or dedicated overview section in `README.md`.
- Clearly detail module responsibilities, entry points, data flows, and build/test commands so incoming AI agents can orient immediately in a single read step.

### F. Deterministic Single-Command Verification
- Every project must provide a fast, deterministic single-command test/lint runner (e.g., `pytest`, `npm test`, `cargo test`).
- Test suites must produce targeted, informative error messages that enable agents to isolate regressions and self-correct quickly.
