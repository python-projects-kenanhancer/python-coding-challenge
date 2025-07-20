from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Similar to your Anthropic setup
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # Cheapest option
    temperature=0.7,
    max_tokens=50,  # Limit output
)

# Same prompt structure
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
