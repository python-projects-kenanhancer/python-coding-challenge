from typing import Callable
from functools import reduce


add_10: Callable[[int], [int]] = lambda x: x + 10
multiply: Callable[[int, int], int] = lambda x, y: x * y
print(add_10(5))
print(multiply(5, 10))


def add_10_func(x: int) -> int:
    return x + 10


print(add_10_func(5))

numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers)

squared = map(lambda x: x**2, numbers)
print(list(squared))

squared2 = reduce(lambda acc, item: acc + [item**2], numbers, [])
print(squared2)

print([1, 4] + [3, 2])
