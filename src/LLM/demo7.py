# Basic LangChain concept
# from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

template = "Tell me a {adjective} joke about {topic}"
prompt = PromptTemplate(input_variables=["adjective", "topic"], template=template)
