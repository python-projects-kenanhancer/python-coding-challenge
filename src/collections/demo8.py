def group(size: int, words: list[str]) -> list[list[str]]:
    return [words[i : i + size] for i in range(0, len(words), size)]


words = ["apple", "banana", "orange", "grape", "kiwi", "melon"]
grouped_words = group(2, words)
print(grouped_words)


a1 = range(0, len(words), 2)
print(list(a1))

a2 = [words[0 : 0 + 2], words[2 : 2 + 2], words[4 : 4 + 2]]

aa1 = words[::2]
aa2 = words[1::2]

a3 = list(zip(words[::2], words[1::2]))

print(a2)


a4 = [list(pair) for pair in zip(words[::2], words[1::2])]

print(a4)


# class Group:
#     @staticmethod
#     def perform(size: int, words: list[str]) -> list[list[str]]:
#         return [words[i : i + size] for i in range(0, len(words), size)]


# grouped_words_class = Group.perform(5, words)
# print(grouped_words_class)


# def group_v2(size: int, words: list):
#     int index = 0
#     grouped_words = []
