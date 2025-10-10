numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_every_two_with_enumerate(numbers: list[int]):
    result: list[int] = []
    for i, value in enumerate(numbers):
        if i % 2 == 0:
            result.append(value)
    return result


def print_every_two_with_range(numbers: list[int]):
    result: list[int] = []
    for i in range(0, len(numbers), 2):
        result.append(numbers[i])
    return result


def print_every_two_with_while(numbers: list[int]):
    result: list[int] = []
    i = 0
    while i < len(numbers):
        print(i)
        result.append(numbers[i])
        i += 2
    return result


print(print_every_two_with_enumerate(numbers))
print(print_every_two_with_range(numbers))
print(print_every_two_with_while(numbers))
