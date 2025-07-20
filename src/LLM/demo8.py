from langchain_community.llms.ollama import Ollama


# Then use it in LangChain
llm = Ollama(model="llama4")
response = llm.invoke("What is the meaning of life?")
print(response)
