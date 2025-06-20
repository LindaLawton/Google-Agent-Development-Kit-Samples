# agent.py

This script initializes and configures a conversational agent designed to act as a pirate recruiter. It leverages the Google Agent Development Kit (ADK) to define the agent's behavior, personality, and the underlying language model it uses.

## Core Functionality

- **Environment Configuration**: Loads necessary environment variables, specifically the name of the Gemini model to be used by the agent, from a .env file.
- **Agent Initialization**: Creates an instance of the Agent class from the google.adk library.
- **Agent Definition**:
- - **name**: "pirate_recruitment_agent"  A unique identifier for the agent.
- - **model**: Specifies the Gemini model (e.g., "gemini-1.5-flash-001") that will power the agent's conversational abilities. This is loaded from the TEXT_MODEL_NAME environment variable.
- - **description**: "You are a pirate agent." - A brief description of the agent's persona.
- - **instruction**: "You are a pirate agent you will attempt to recruit prospective pirates." - The primary directive given to the agent, guiding its interactions and objectives.

## Dependencies

To run this script and utilize the agent, you'll need the following Python libraries:
- **google-adk**: The Google Agent Development Kit.
- **python-dotenv**: For managing environment variables.

You can typically install these using pip:

    pip install google-adk python-dotenv


## Configuration

Before running any application that uses this agent, ensure you have a .env file in the root directory of your project with the following variable:

    TEXT_MODEL_NAME="your-gemini-model-name"

Replace "your-gemini-model-name" with the specific Gemini model you intend to use (e.g., gemini-1.5-flash-001).

## Usage

This script defines the root_agent. To use this agent, you would typically import it into another part of your application where you handle interactions, such as a command-line interface, a web service, or an application integrating with the Google ADK framework.

    adk web