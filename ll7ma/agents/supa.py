from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class Supa(ChatOpenAI):
    def __init__(self):
        super().__init__()