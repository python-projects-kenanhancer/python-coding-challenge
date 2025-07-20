from typing import TypedDict, Literal

# from typing_extensions import TypedDict, Literal


class Status(TypedDict):
    code: Literal[200, 404, 500]
    message: Literal["OK", "Not Found", "Error"]


status: Status = {"code": 200, "message": "Created"}
