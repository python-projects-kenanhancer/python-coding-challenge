from collections import defaultdict

# Example 1: Grouping items by category
groups = defaultdict(list)

# Adding items to groups - defaultdict automatically creates empty lists for new keys
groups['fruits'].append('apple')
groups['fruits'].append('banana')
groups['vegetables'].append('carrot')
groups['vegetables'].append('broccoli')

print("Grouped items:")
for category, items in groups.items():
    print(f"{category}: {items}")

# Example 2: Counting occurrences
word_count = defaultdict(int)

text = "hello world hello python world python"
for word in text.split():
    word_count[word] += 1  # defaultdict automatically initializes with 0

print("\nWord counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Example 3: Nested defaultdict
nested = defaultdict(lambda: defaultdict(list))

nested['group1']['items'].append('item1')
nested['group1']['items'].append('item2')
nested['group2']['items'].append('item3')

print("\nNested structure:")
for group, data in nested.items():
    print(f"{group}: {dict(data)}")
