from collections import Counter

cart = ["apple", "banana", "apple", "apple", "orange", "banana", "banana"]

item_counts = Counter(cart)

for item, count in item_counts.items():
    print(f"{item}: {count}")

print(item_counts["banana"])
