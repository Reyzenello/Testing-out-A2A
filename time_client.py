# Import the requests library to send HTTP GET and POST requests.
# This allows the client to talk to the server over HTTP.
import requests

# Import the uuid module to generate unique task IDs.
# Each A2A task must have a unique ID.
import uuid

# ----------------------------------------------
# Step 1: Discover the Agent
# ----------------------------------------------
print("--- Step 1: Discovering the Agent ---")
# Define the base URL where the server agent is hosted.
# In this case, it runs locally on port 5000.
base_url = "http://127.0.0.1:5000" # Using 127.0.0.1 can sometimes be more reliable than 'localhost'

try:
    # Use HTTP GET to fetch the agent's card from the well-known discovery endpoint.
    agent_card_url = f"{base_url}/.well-known/agent.json"
    print(f"Fetching Agent Card from: {agent_card_url}")
    res = requests.get(agent_card_url)
    res.raise_for_status() # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    # Parse the response JSON into a Python dictionary.
    agent_info = res.json()

    # Display some basic info about the discovered agent.
    print(f"Connected to: {agent_info.get('name', 'Unknown Agent')} – {agent_info.get('description', 'No description')}")
    print(f"Agent URL: {agent_info.get('url')}")
    print(f"Agent Capabilities: {agent_info.get('capabilities')}\n")

except requests.exceptions.RequestException as e:
    print(f"Error during agent discovery: {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred during discovery: {e}")
    exit()


# ----------------------------------------------
# Step 2: Prepare a Task
# ----------------------------------------------
print("--- Step 2: Preparing a Task ---")
# Generate a unique ID for this task using uuid4 (random UUID).
task_id = str(uuid.uuid4())
print(f"Generated Task ID: {task_id}")

# Construct the A2A task payload as a Python dictionary.
# According to A2A spec, we need to include:
# - "id": the unique task ID
# - "message": an object with "role": "user" and a list of "parts" (in this case, text only)
task_payload = {
    "id": task_id,
    "message": {
        "role": "user",  # Indicates that the message is coming from the user
        "parts": [
            {"text": "What time is it?"}  # This is the question the user is asking
        ]
    }
}
print(f"Task Payload: {task_payload}\n")

# ----------------------------------------------
# Step 3: Send the Task to the Agent
# ----------------------------------------------
print("--- Step 3: Sending the Task to the Agent ---")
tasks_send_url = f"{base_url}/tasks/send"
print(f"Sending POST request to: {tasks_send_url}")

try:
    # Send an HTTP POST request to the /tasks/send endpoint of the agent.
    # We use the `json=` parameter so requests will serialize our dictionary as JSON.
    response = requests.post(tasks_send_url, json=task_payload)
    response.raise_for_status() # Check for HTTP errors

    # Parse the agent's JSON response into a Python dictionary.
    response_data = response.json()
    print(f"Received Response Data: {response_data}\n")

except requests.exceptions.RequestException as e:
    print(f"Error sending task: {e}")
    if hasattr(response, 'text'):
        print(f"Server response: {response.text}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while sending task: {e}")
    exit()

# ----------------------------------------------
# Step 4: Display the Agent's Response
# ----------------------------------------------
print("--- Step 4: Displaying Agent's Response ---")
# Extract the list of messages returned in the response.
# This typically includes both the user's message and the agent's reply.
messages = response_data.get("messages", [])

# If there are messages, extract and print the last one (agent's response).
if messages:
    # The last message in the list is typically the agent's most recent reply.
    agent_reply_message = messages[-1]
    if agent_reply_message.get("role") == "agent" and agent_reply_message.get("parts"):
        final_reply_text = agent_reply_message["parts"][0].get("text", "Agent replied with no text.")
        print(f"Agent says: \"{final_reply_text}\"")
    else:
        print("Could not parse agent's reply from messages.")
else:
    # If no messages were received, notify the user.
    print("No response received in mes
