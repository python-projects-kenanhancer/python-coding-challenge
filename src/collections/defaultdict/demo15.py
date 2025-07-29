def has_duplicates(items: list) -> bool:
    return len(items) != len(set(items))


numbers = [1, 2, 3, 4, 5, 1]

print(has_duplicates(numbers))
