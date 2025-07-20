from langchain_ollama import ChatOllama

from pydantic import BaseModel, Field


# Pydantic
class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: int = Field(description="How funny the joke is, from 1 to 10")


llm = ChatOllama(
    model="llama4",
    temperature=0.7,
    max_tokens=50,  # Limit output
)

structured_llm = llm.with_structured_output(Joke)

result = structured_llm.invoke("Tell me a joke about cats")

print(result)
