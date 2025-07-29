def group(num: int, words: list):
    index = 0
    result = []
    while index < len(words):
        grouped = words[index : index + num]
        result.append(grouped)
        index += num
    return result


words = ["apple", "banana", "orange", "grape", "kiwi", "melon"]
grouped_words = group(2, words)
print(grouped_words)


class Group:
    @staticmethod
    def perform(num: int, words: list):
        index = 0
        result = []
        while index < len(words):
            grouped = words[index : index + num]
            result.append(grouped)
            index += num
        return result


grouped_words_class = Group.perform(5, words)
print(grouped_words_class)
