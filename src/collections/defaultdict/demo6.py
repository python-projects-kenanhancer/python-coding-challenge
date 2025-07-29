from collections import Counter

text = "apply banana apple orange banana apple"
text_array = text.split()
word_counts = Counter(text_array)

print(dict(word_counts))
print(word_counts["banana"])
