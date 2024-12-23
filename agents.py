import os
from google import genai
from decouple import config
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI  

load_dotenv()

api_key = config('GEMINI_API_KEY')
os.environ["GEMINI_API_KEY"] = api_key

class CustomAgents:
    def __init__(self):
        self.client = genai.Client(
            vertexai=False,
            api_key=api_key
        )

    def financial_data_collector(self):
        llm = ChatGoogleGenerativeAI(
            model='gemini-1.5-flash',  
            verbose=True,
            temperature=0.5,
            google_api_key=os.getenv('GEMINI_API_KEY') 
        )
        return llm

    def budget_calculator(self):
        llm = ChatGoogleGenerativeAI(
            model='gemini-1.5-flash',
            verbose=True,
            temperature=0.5,
            google_api_key=os.getenv('GEMINI_API_KEY')
        )
        return llm

    def savings_advisor(self):
        llm = ChatGoogleGenerativeAI(
            model='gemini-1.5-flash', 
            verbose=True,
            temperature=0.5,
            google_api_key=os.getenv('GEMINI_API_KEY')
        )
        return llm
