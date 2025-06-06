# Exploring AI Agent-to-Agent (A2A) Communication

This repository contains code examples, slide content, and notes from a presentation/exploration of Google's A2A Protocol and related concepts like Model-Context Protocol (MCP). The goal is to understand how AI agents can communicate and collaborate more effectively.

## Overview

The presentation covers:
1.  The challenges of current AI tool integration.
2.  Introduction to Google's A2A Protocol as a standard for agent communication.
3.  The evolution of Large Language Model (LLM) interaction with tools.
4.  A look at the Model-Context Protocol (MCP) for tool and resource connection.
5.  Practical examples using both Google's `a2a-python` library and PraisonAI.
6.  The potential future of an "Agent Economy."

## Repository Structure

*   `slides_content/`: Markdown files containing the textual content from the presentation slides.
*   `google_a2a_python_example/`: Contains the "helloworld" example from the official `google/a2a-python` repository. It's recommended to clone the full repository from [https://github.com/google/a2a-python](https://github.com/google/a2a-python) for complete context and dependencies.
*   `praisonai_examples/`: Python scripts demonstrating MCP server and client interactions using the PraisonAI library.
*   `terminal_outputs/`: Text files capturing the terminal output from running the example scripts.

## Key Concepts

### A2A (Agent-to-Agent) Protocol
An open standard proposed by Google to enable AI agents from different companies and built with different technologies to work together seamlessly. It aims to be like "USB for AI agents."
*   **Core Idea:** Allow one AI agent to "hire" or task other AI agents.
*   **Communication:** Uses JSON-RPC over HTTP. Supports request/response, streaming, and push notifications.
*   **Components:**
    *   **Agent Skill:** Defines what an agent can do (like a tool call).
    *   **Agent Card:** Provides metadata about an agent (name, description, URL, capabilities, skills).
    *   **Agent Executor:** The core logic that uses an LLM or other framework to process requests.
*   **Benefits:** Interoperability, discovery, agent marketplace concept, right-sized models, built-in authentication.
*   **Challenges (as of early state):** Code maturity, limited production tooling, multi-agent complexity, tracing, centralized identity/billing.

### MCP (Model-Context Protocol)
A protocol for connecting agents (or LLMs) to tools, APIs, and resources with structured inputs/outputs. It's a lower-level protocol compared to A2A.
*   **Function:** Provides a standardized way for an LLM to understand what tools are available and how to use them.
*   **Interaction:** Typically involves an MCP Client (part of the agent) and an MCP Server (exposing the tool).

**A2A vs MCP:** They can work together. MCP provides tools, A2A coordinates agents.

## Running the Examples

### 1. Google's `a2a-python` "helloworld" Example

**Prerequisites:**
*   Git
*   Python 3.13+ (as recommended in the video for the `a2a-python` example, though the repo itself might support other versions)
*   Conda (or `venv`) for environment management
*   `uv` (a fast Python package installer and resolver, can be installed with `pip install uv`)

**Setup:**
1.  Clone the official `a2a-python` repository:
    ```bash
    git clone https://github.com/google/a2a-python
    cd a2a-python
    ```
2.  Create and activate a virtual environment:
    ```bash
    conda create -n a2a python=3.13 -y
    conda activate a2a
    ```
3.  Install dependencies (this project uses `pyproject.toml`):
    ```bash
    uv pip install -r pyproject.toml # Or more simply 'uv pip install .' if pyproject.toml is set up for editable install
    ```
    Alternatively, to install dependencies specific to the `helloworld` example if it has its own `pyproject.toml`:
    ```bash
    cd examples/helloworld
    uv pip install -r pyproject.toml # or 'uv pip install .'
    ```

**Running the Server (from within `examples/helloworld` directory):**
```bash
uv run .
