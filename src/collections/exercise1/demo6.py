numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))


def get_min_with_for(numbers: list[int]):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value


def get_min_with_while(numbers: list[int]):
    min_value = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1
    return min_value


def get_min_with_range(numbers: list[int]):
    min_value = numbers[0]
    for i in range(0, len(numbers), 1):
        if numbers[i] < min_value:
            min_value = numbers[i]

    return min_value


def get_min_with_enumerate(numbers: list[int]):
    min_value = numbers[0]
    for i, value in enumerate(numbers):
        if value < min_value:
            min_value = value
    return min_value


print(get_min_with_for(numbers))
print(get_min_with_while(numbers))
print(get_min_with_range(numbers))
print(get_min_with_enumerate(numbers))


def get_max_with_for(numbers: list[int]):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value


def get_max_with_while(numbers: list[int]):
    max_value = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i += 1


def get_max_with_range(numbers: list[int]):
    max_value = numbers[0]
    for i in range(0, len(numbers), 1):
        if numbers[i] > max_value:
            max_value = numbers[i]
    return max_value


def get_max_with_enumerate(numbers: list[int]):
    max_value = numbers[0]
    for i, value in enumerate(numbers):
        if value > max_value:
            max_value = value
    return max_value


def get_sum_with_for(numbers: list[int]):
    sum_value = 0
    for number in numbers:
        sum_value += number
    return sum_value


def get_sum_with_for_range(numbers: list[int]):
    sum_value = 0
    for i in range(0, len(numbers), 1):
        sum_value += numbers[i]
    return sum_value


def get_sum_with_enumerate(numbers: list[int]):
    sum_value = 0
    for i, value in enumerate(numbers):
        sum_value += value
    return sum_value


def get_sum_with_while(numbers: list[int]):
    sum_value = 0
    i = 0
    while i < len(numbers):
        sum_value += numbers[i]
        i += 1
    return sum_value


def get_average_with_for(numbers: list[int]):
    sum_value = 0
    for number in numbers:
        sum_value += number
    average_value = sum_value / len(numbers)
    return average_value

