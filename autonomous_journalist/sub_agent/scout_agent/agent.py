from google.adk.agents import Agent
from google.adk.tools import google_search

# The Scout Agent uses Google Search to conduct in-depth research.
scout_agent = Agent(
    model='gemini-2.5-pro', # Upgraded model for better reasoning and synthesis
    name='scout_agent',
    description='An expert research agent that finds trends, research, and competitor news, then creates a research brief.',
    instruction="""You are an expert market researcher. For a given topic, you MUST perform three distinct searches:
    1.  Find the latest **trending news** and top stories.
    2.  Find recent **industry research**, studies, or reports.
    3.  Find news and announcements from key **competitors**.

    Synthesize your findings into a structured Markdown report. The report must have three sections: '### Trending News', '### Industry Research', and '### Competitor Activity'.
    Under each section, provide a bulleted list with a brief 1-2 sentence summary for each finding and include the source URL.
    Your final output is ONLY the Markdown report.
    """,
    tools=[google_search],
)
