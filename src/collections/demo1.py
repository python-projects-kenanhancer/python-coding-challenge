from typing import TypedDict, Literal, Annotated, Optional


class Status(TypedDict):
    code: Annotated[Literal[200, 404, 500], ..., "HTTP status code"]
    message: Annotated[Literal["OK", "Not Found", "Error"], ..., "HTTP status message"]


class Joke(TypedDict):
    setup: Annotated[str, ..., "The setup of the joke"]
    punchline: Annotated[str, ..., "The punchline of the joke"]
    rating: Annotated[Optional[int], None, "How funny"]


class Person(TypedDict):
    name: str
    age: int


status: Status = {"code": 200, "message": "OK"}

p1 = Person(name="Alice", age=30)
p2: Person = {"name": "Bob", "age": 25}

j1 = Joke(
    setup="Why did the chicken cross the road?",
    punchline="To get to the other side!",
    rating=5,
)

j2: Joke = {
    "setup": "What do you call a bear with no teeth?",
    "punchline": "A gummy bear!",
    "rating": None,
}
