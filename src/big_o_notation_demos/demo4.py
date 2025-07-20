from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)

word_count["orange"] += 5
print(word_count.most_common(3))
