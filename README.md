# Agent 48

```
      .---.
     /     \\
    | () () |
     \\  ^  /
      |||||
      |||||
```

**Agent 48** is a specialized, Docker-only CLI coding agent inspired by Claude Code and the *Hitman* series. It provides a surgical approach to coding tasks by interfacing with local LLMs via Ollama.

## Features

- **Tactical Upgrades**:
    - **Streaming Responses**: Real-time generation for a faster feel.
    - **Persistent Memory**: Saves history in `.agent48_history.json` so you can resume missions.
    - **Surgical Search**: New `search_files` tool for finding code patterns instantly.
    - **Manual Confirmation**: Agent 48 will ask for your permission before executing any terminal command.
- **Agentic Persona**: A professional, concise system prompt designed for mission focus.
- **Ollama Integration**: Uses locally hosted models (defaults to `granite4:3b`).
- **Rich TUI**: A beautiful terminal interface with a Hitman ASCII art icon.

## Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose.
- [Ollama](https://ollama.com/) running on your host machine.

## Getting Started

1. **Verify Ollama is running**:
   Ensure `ollama serve` is active and you have the `granite4:3b` model downloaded (`ollama pull granite4:3b`).

2. **Clone and Build**:
   ```powershell
   docker-compose build
   ```

3. **Deploy the Agent**:
   ```powershell
   docker-compose run agent48
   ```

## Usage

Once active, use the `MISSION >` prompt to give instructions.

- **Filesystem**: "List the files in the src folder" or "Read main.py".
- **Creation**: "Create a new Python script that calculates fibonacci numbers".
- **Execution**: "Run the tests" or "Check the python version".

## Mission Control

You can specify a different model at runtime:
```powershell
docker-compose run agent48 --model llama3.2:3b
```

---
*Precision is the only thing that matters.*
