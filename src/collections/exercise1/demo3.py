numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])


def print_every_two(numbers: list[int]):
    result: list[int] = []
    for i in range(0, len(numbers), 2):
        result.append(numbers[i])

    return result


def every_two_with_enumerate(numbers: list[int]):
    result: list[int] = []
    for i, value in enumerate(numbers):
        if i % 2 == 0:
            result.append(value)
    return result


def every_two_with_while(numbers: list[int]):
    result: list[int] = []
    i = 0
    while i < len(numbers):
        result.append(numbers[i])
        i += 2
    return result


print(numbers[::2])

