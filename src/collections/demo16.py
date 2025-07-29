from dataclasses import dataclass, field
from typing import NamedTuple


@dataclass(frozen=True)
class Color:
    r: int = field(default=0)
    g: int = field(default=0)
    b: int = field(default=0)


class Point(NamedTuple):
    x: int
    y: int


p1 = Point(3, 4)

c1 = Color(255, 0, 0)

print(f"Point coordinates: {p1}")
print(f"Color values: {c1}")
