from langchain_ollama import OllamaLLM

# Use your llama4 model
llm = OllamaLLM(model="llama4:latest")
response = llm.invoke("What is the meaning of life?")
print(response)
