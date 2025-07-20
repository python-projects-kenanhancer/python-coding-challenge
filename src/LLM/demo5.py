from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Use your llama4 model
llm = OllamaLLM(model="llama4:latest")

# This creates a reusable prompt template where {product} is a placeholder
prompt = PromptTemplate(
    input_variables=["product"],
    template="""What is a good name for a company that makes {product}?

Important: Provide only two names. Do not explain or give multiple options. Just the company name.""",
)

# Modern approach: Use pipe operator
chain = prompt | llm

# Use invoke instead of run
result = chain.invoke({"product": "colorful socks"})

print(result)
