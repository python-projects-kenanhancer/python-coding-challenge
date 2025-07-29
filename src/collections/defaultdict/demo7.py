from collections import Counter

text = "apply,banana,apple,orange,banana,apple"
text_array = text.split(",")

words_counts = Counter(text_array)

print(dict(words_counts))
print(words_counts["banana"])
