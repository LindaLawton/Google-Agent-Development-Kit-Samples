# Volcano Search Agent

This script implements a Google ADK (Agent Development Kit) agent designed to answer questions about volcanoes using Google Search to ensure the information is accurate and up-to-date.

## Table of Contents
- [What it Does](#what-it-does)
- [How it Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)

## What it Does

The `volcano_search_agent` is a specialized AI agent that acts as an expert on volcanoes. When you provide it with a query about volcanoes, it utilizes the Google Search tool to find relevant and current information. Its primary goal is to provide accurate and timely responses by leveraging external knowledge from the web.

## How it Works

The agent is built using the Google ADK and operates as follows:

1.  **Agent Definition**: A `root_agent` is defined with a specific `name`, `model` (`gemini-2.0-flash`), `description`, and `instruction`. The instruction "You are an expert on volcano's you will use google search to ensure your information is accurate and up to date" guides the agent's behavior.
2.  **Tool Integration**: The `google_search` tool is integrated into the agent. This allows the agent to perform web searches when it determines that external information is needed to answer a query.
    * For more details on the Google Search tool in ADK, refer to the [Google ADK Documentation](https://developers.google.com/agents/docs/tools/google-search).
3.  **Session Management**: An `InMemorySessionService` is used to manage the conversation session, allowing the agent to maintain context across interactions.
4.  **Runner**: A `Runner` orchestrates the interaction between the user and the agent, processing queries and delivering responses.
5.  **Agent Interaction**: The `call_agent` function sends a user query to the agent. The agent then processes the query, potentially using the `google_search` tool, and returns a final response.

## Installation

To install and run this script, follow these steps:

1.  **Clone the repository (if applicable) or save the `agent.py` file.**
2.  **Create a `.env` file**: In the same directory as `agent.py`, create a file named `.env`.
3.  **Configure your text model name**: Add the following line to your `.env` file, replacing `YOUR_GEMINI_MODEL_NAME` with the actual name of the Gemini model you intend to use (e.g., `gemini-2.0-flash` or `gemini-1.5-pro`).
    ```dotenv
    TEXT_MODEL_NAME=YOUR_GEMINI_MODEL_NAME
    ```
4.  **Install dependencies**: Make sure you have the necessary Python packages installed. You can install them using pip:
    ```bash
    pip install google-generativeai python-dotenv google-adk
    ```

## Usage

To use the agent, simply run the `agent.py` script. The script includes a sample call to the agent.

```bash
adk web