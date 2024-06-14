import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

from llm_helper import chat as llm

# Create a pandas dataframe
df = pd.read_csv("sample.csv")

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# Now you can use the agent to interact with the dataframe
result = agent.invoke('What is max and min value of NAV?')

print("RESULT:- ", result)