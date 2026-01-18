# app/memory.py

# In-memory store:
# session_id -> list of messages
conversation_store = {}


def get_memory(session_id: str):
    """
    Returns the message history for a session.
    If the session does not exist, initialize it
    with a system prompt.
    """
    if session_id not in conversation_store:
        conversation_store[session_id] = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]
    return conversation_store[session_id]


def add_message(session_id: str, role: str, content: str):
    """
    Appends a message to the session's conversation history.
    """
    conversation_store[session_id].append(
        {"role": role, "content": content}
    )


#memory trimming phase 3
MAX_MESSAGES = 10  # last 10 messages (excluding system)


def trim_memory(messages):
    system = messages[0]
    recent = messages[-MAX_MESSAGES:]
    return [system] + recent