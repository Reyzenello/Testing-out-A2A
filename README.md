# A2A Protocol: Simple "Tell Time" Agent Example

This project demonstrates a fundamental implementation of Google's Agent-to-Agent (A2A) protocol. It features a simple "Tell Time" agent (server) and a client that discovers this agent and requests the current time.

This example is designed to be beginner-friendly and focuses on core A2A concepts:
1.  **Discovery:** The client discovers the server agent using the `/.well-known/agent.json` endpoint to retrieve the Agent Card.
2.  **Task Handling:** The client sends a task (a request for the current time) to the server's `/tasks/send` endpoint.
3.  **Message and Part Structure:** Tasks and responses are structured with messages, and messages contain parts (in this case, simple text parts).

## Prerequisites

*   **Python 3.12 or higher:** The A2A specification often implies newer Python features.
*   **pip:** Python's package installer.
*   **Required Libraries:**
    *   `Flask`: For creating the server-side agent.
    *   `requests`: For the client to make HTTP requests.

    Install them using:
    ```bash
    pip install flask requests
    ```


