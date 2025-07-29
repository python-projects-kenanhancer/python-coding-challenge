def group_v1(words: list, size: int):
    words_grouped = []

    for i in range(0, len(words), 2):
        words_grouped += [words[i : i + 2]]

    return words_grouped


def group_v2(words: list, size: int):
    index = 0
    words_grouped = []

    while index < len(words):
        words_grouped.append(words[index : index + size])
        index = index + size

    return words_grouped


def group_v3(words: list, size: int):
    index = 0
    words_grouped = []

    while index < len(words):
        words_grouped.append(words[index : index + size])
        index += size

    return words_grouped


def group_v4(words: list, size: int):

    for i in range(0, len(words), size):
        yield words[i : i + size]


def group_v5(words: list, size: int):

    for i in range(0, len(words), size):
        print(f"Before yield: {words[i:i + size]}")
        yield words[i : i + size]
        print(f"After yield: {words[i:i + size]}")

    print("Generator finished execution.")


if __name__ == "__main__":
    words = ["apple", "banana", "orange", "grape", "kiwi", "melon"]

    print("Original words:", words)
    print("Length of words:", len(words))

    print("Group words using group_v1:")
    words_grouped_v1 = group_v1(words, 2)
    print(words_grouped_v1)

    print("Group words using group_v2:")
    words_grouped_v2 = group_v2(words, 2)
    print(words_grouped_v2)

    print("Group words using group_v3:")
    words_grouped_v3 = group_v3(words, 2)
    print(words_grouped_v3)

    print("Group words using group_v4:")
    words_grouped_v4 = group_v4(words, 2)
    print(list(words_grouped_v4))

    for group in group_v4(words, 2):
        print(group)

    print("Group words using group_v5:")
    words_grouped_v5 = group_v5(words, 2)
    for group in words_grouped_v5:
        print(group)
