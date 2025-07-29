from collections import Counter

s = "mississippi"

char_counts = Counter(s)

print(dict(char_counts))
print(char_counts["i"])
