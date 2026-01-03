from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime   # ✅ Missing import added


def get_search_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS 
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# Define the root agent with its configuration
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.5-flash",  # model name OK
    description="Tool agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
