from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Use your llama4 model
llm = OllamaLLM(model="llama4:latest")

# This creates a reusable prompt template where {product} is a placeholder
prompt = PromptTemplate(
    input_variables=["product"],
    template="Generate ONE creative company name for a business that makes {product}. Reply with only the name.",
)

# Modern approach: Use pipe operator
chain = prompt | llm

# Test with different products
products = ["colorful socks", "eco-friendly bags", "smart water bottles"]

for product in products:
    result = chain.invoke({"product": product})
    print(f"{product} → {result.strip()}")
