import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

os.environ["AZURE_OPENAI_API_KEY"] = os.environ['AZURE_OPENAI_API_KEY']
os.environ["AZURE_OPENAI_ENDPOINT"] = os.environ["AZURE_OPENAI_ENDPOINT"]

chat = AzureChatOpenAI(
    azure_deployment="gpt4",
    openai_api_version="2024-02-15-preview",
    temperature=0
)


def call_llm(message):
    return chat.invoke(message)
