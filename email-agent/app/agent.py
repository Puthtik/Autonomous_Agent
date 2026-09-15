from idlelib import config

from ollama import chat
from config import MODEL,SYSTEM

def create_email_agent(user_request: str):
    messages = [
        {
            "role": "system",
            "content": "SYSTEM"
        },
        {
            "role": "user",
            "content": user_request,
        },
    ]

    return messages

SEND_EMAIL_TOOL = {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "Send email to recipient",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "Recipient email address",
                },
                "subject": {
                    "type": "string",
                    "description": "Email subject",
                },
                "body": {
                    "type": "string",
                    "description": "Email body",
                },
            },
            "required": [
                "to",
                "subject",
                "body",
            ],
        }
    }
}

def run_agent(user_request: str):
    messages = [
        {
            "role": "system",
            "content": "SYSTEM"
        },
        {
            "role": "user",
            "content": user_request,
        }
    ]

    response = chat(
        model=MODEL,
        messages=messages,
        tools=[SEND_EMAIL_TOOL], # This tell ollama "the agent has access to this tool"
    )

    return response