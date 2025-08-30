from google.adk.agents import SequentialAgent
from .sub_agent.scout_agent.agent import scout_agent
from .sub_agent.writer_agent.agent import writer_agent
from .sub_agent.publisher_agent.agent import publisher_agent

# The Orchestrator defines the end-to-end workflow.
journalist_orchestrator = SequentialAgent(
    name="journalist_orchestrator",
    sub_agents=[scout_agent, writer_agent, publisher_agent],
    description="After gather all the information from coordinator_agent, executes web searches, writing and publishing",

)
