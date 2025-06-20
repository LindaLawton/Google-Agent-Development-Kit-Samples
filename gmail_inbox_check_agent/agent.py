from google.adk import Agent
from dotenv import load_dotenv
import os

from tools.gmail_tools import get_unread_messages_from_inbox, update_unread_messages_to_read

load_dotenv()
GEMINI_MODEL = os.getenv("TEXT_MODEL_NAME")

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types

APP_NAME="volcano_search_agent"
USER_ID="user1234"
SESSION_ID="1234"


root_agent = Agent(
    name="gmail_inbox_check_agent",
    model="gemini-2.0-flash",
    description="Agent to check email in inbox and summarise them.",
    instruction="You are my email assistant you will find my new unread emails and summarise them for me.",
    tools=[get_unread_messages_from_inbox, update_unread_messages_to_read]
)

# Session and Runner
session_service = InMemorySessionService()
session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)


# Agent Interaction
def call_agent(query):
    """
    Helper function to call the agent with a query.
    """
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

call_agent("what's the latest ai news?")