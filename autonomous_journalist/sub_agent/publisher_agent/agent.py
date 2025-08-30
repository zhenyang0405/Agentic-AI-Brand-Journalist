from google.adk.agents import Agent
from . import publishing_tools

publisher_agent = Agent(
    model='gemini-2.5-flash',
    name='publisher_agent',
    description='An AI agent that drafts pitch emails for blog posts.',
    instruction='You are a content manager. Use the provided blog post draft to create a compelling and concise pitch email using the available tool.',
    tools=[publishing_tools.draft_pitch_email],
)