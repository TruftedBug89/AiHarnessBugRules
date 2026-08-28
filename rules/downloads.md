# Download and System Change Rules

## 1. Ask before substantial downloads or system changes

If a task requires a **substantial download (500 MB or more)** or any **change to the system** (installing software, downloading large model files, modifying system configs, adding services), the agent MUST ask the user for explicit approval before proceeding.

- Never silently download large files, install packages system-wide, pull AI models, or modify system state without the user's green light.
- The user's initial request does NOT imply permission to download or install things. For example, "I want a lip reader AI" does NOT mean "download a 1 GB model and install software to achieve this."
- Only proceed without asking if the user **explicitly specified** the tool, model, or download in their request (e.g. "use my LM Studio model X" or "download Y and set it up").
- When in doubt, describe what you intend to download/install and ask: "This requires downloading X (size). Proceed?"
- Small downloads (< 500 MB) that are clearly implied by the task (e.g. pip installing a listed dependency) are acceptable without asking.
