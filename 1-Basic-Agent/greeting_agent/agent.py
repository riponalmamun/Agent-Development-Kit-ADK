from google.adk.agents import Agent



# Define the root agent with its configuration

root_agent = Agent(

    name="greeting_agent",

    # The model defines the capabilities of the agent.

    # We use a fast, capable model here.

    model="gemini-2.5-flash", 

    description="Greeting agent",

    instruction="""

You are a helpful assistant that greets the user. 

Ask for the user's name and greet them by name.

""",

)



# Note: In a full ADK project, you would typically have more logic 

# here, such as functions and tools the agent can use. 

