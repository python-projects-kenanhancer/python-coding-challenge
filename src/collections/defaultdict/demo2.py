from collections import defaultdict


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = defaultdict(int)

for word in words:
    counter[word] += 1

print(dict(counter))
