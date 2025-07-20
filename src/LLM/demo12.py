from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama4",
    temperature=0.7,
    max_tokens=50,  # Limit output
)

prompt = ChatPromptTemplate.from_template(
    "Give me 3 company names for a business that makes {product}. Just the names."
)

chain = prompt | llm

# Track costs
result = chain.invoke({"product": "colorful socks"})
print(result.content)

# Check token usage
if hasattr(result, "response_metadata"):
    usage = result.response_metadata.get("usage", {})
    print(f"Tokens used: {usage}")
