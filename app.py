from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# Load the model
#llm = OpenAI(temperature=0)

#os.environ["SERPAPI_API_KEY"] = "..."

from langchain.agents import load_tools, initialize_agent, AgentType
#from langchain.llms import OpenAI
import os
from langchain.agents import load_tools
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
#from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent
#import gradio as gr
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate, LLMChain
from langchain import HuggingFaceHub
import requests
from pathlib import Path
from time import sleep
from langchain.agents import AgentType
GOOGLE_API_KEY =os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID =os.getenv("GOOGLE_CSE_ID")
repo_id=os.getenv('repo_id')
search = GoogleSearchAPIWrapper()
llm=HuggingFaceHub(repo_id=repo_id)


tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)


result=agent.run("What is the hight of Obama? And how many cans of coke can you stack to reach that height?")

print(result)
