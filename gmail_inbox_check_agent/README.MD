# Gmail Inbox Check Agent

This script implements a Google ADK (Agent Development Kit) agent designed to act as your email assistant, specifically to find new unread emails and summarize them for you.

## Table of Contents
- [What it Does](#what-it-does)
- [How it Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)

## What it Does

The `gmail_inbox_check_agent` is a specialized AI agent that functions as your personal email assistant. Its core capabilities include:
- Identifying new unread emails in your inbox.
- Summarizing the content of these unread emails.

Its primary goal is to help you quickly review and understand your latest communications without manually sifting through your inbox.

## How it Works

The agent is built using the Google ADK and operates as follows:

1.  **Agent Definition**: A `root_agent` is defined with the `name="gmail_inbox_check_agent"`, using the `gemini-2.0-flash` model. Its description highlights its role in checking and summarizing emails, and its instruction sets the persona: "You are my email assistant you will find my new unread emails and summarise them for me."
2.  **Tool Integration**: The agent integrates the following custom tools (presumably defined in `tools/gmail_tools.py`):
    * `get_unread_messages_from_inbox`: This tool is used to fetch the unread emails from your Gmail inbox.
    * `update_unread_messages_to_read`: This tool is likely used to mark emails as read after they have been processed or summarized by the agent.
    The agent uses these tools when it determines that email-related actions are necessary to fulfill a user's request.
3.  **Session Management**: An `InMemorySessionService` is utilized to manage the conversational session, allowing the agent to maintain context throughout your interactions.
4.  **Runner**: A `Runner` orchestrates the entire process, taking your queries, passing them to the agent, and handling the agent's responses.
5.  **Agent Interaction**: The `call_agent` function sends your query to the agent. The agent then decides which tools to use (`get_unread_messages_from_inbox`, `update_unread_messages_to_read`) to achieve the task, processes the information, and returns a summarized response.

## Installation

To install and run this script, follow these steps:

1.  **Clone the repository (if applicable) or save the `agent.py` and `tools/gmail_tools.py` files.**
    * Ensure that the `tools` directory and `gmail_tools.py` file are correctly structured relative to `agent.py`.
2.  **Create a `.env` file**: In the same directory as `agent.py`, create a file named `.env`.
3.  **Configure your text model name**: Add the following line to your `.env` file, replacing `YOUR_GEMINI_MODEL_NAME` with the actual name of the Gemini model you intend to use (e.g., `gemini-2.0-flash` or `gemini-1.5-pro`).
    ```dotenv
    TEXT_MODEL_NAME=YOUR_GEMINI_MODEL_NAME
    ```
4.  **Ensure Gmail API setup**: For the `gmail_tools` to work, you will need to set up credentials for the Google Gmail API. This typically involves:
    * Enabling the Gmail API in your Google Cloud Project.
    * Downloading `credentials.json` (OAuth 2.0 client ID) and placing it in the appropriate location, or setting up environment variables for authentication. (The `gmail_tools.py` file would dictate the exact authentication method).
5.  **Install dependencies**: Make sure you have the necessary Python packages installed. You can install them using pip:
    ```bash
    pip install google-generativeai python-dotenv google-adk google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```
    *(Note: `google-api-python-client`, `google-auth-httplib2`, and `google-auth-oauthlib` are commonly needed for Google API interactions.)*

## Usage

To use the agent, simply run the `agent.py` script. The script includes a sample call to the agent.

```bash
adk web