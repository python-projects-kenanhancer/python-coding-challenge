from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


# Create instances
p1 = Point(3.0, 4.0)  # Order matters in NamedTuple
p2 = Point(x=1.0, y=2.0)  # Order doesn't matter with keyword arguments
p3 = Point(y=5.0, x=6.0)  # Order doesn't matter with NamedTuple

# Access values
print(p1.x)  # 3.0
print(p1[0])  # 3.0 (also works with index)

x, y = p1  # Unpack values
