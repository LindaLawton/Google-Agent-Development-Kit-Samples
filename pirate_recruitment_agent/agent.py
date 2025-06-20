from google.adk import Agent
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_MODEL = os.getenv("TEXT_MODEL_NAME")


root_agent = Agent(
    name="pirate_recruitment_agent",
    model=GEMINI_MODEL,
    description=(
        "You are a pirate agent."
    ),
    instruction=(
        "You are a pirate agent you will attempt to recruit prospective pirates."
    ),
)