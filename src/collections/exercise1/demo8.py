from collections import defaultdict

# Create a regular dictionary first
data = {
    'apple': 'fruit',
    'banana': 'fruit', 
    'carrot': 'vegetable',
    'broccoli': 'vegetable',
    'chicken': 'protein',
    'beef': 'protein',
    'orange': 'fruit',
    'spinach': 'vegetable'
}

print("Original dictionary:")
for item, category in data.items():
    print(f"{item}: {category}")

# Group items by category using defaultdict
groups = defaultdict(list)

for item, category in data.items():
    groups[category].append(item)

print("\nGrouped by category:")
for category, items in groups.items():
    print(f"{category}: {items}")

# Another example: Group by first letter
print("\nGrouped by first letter:")
letter_groups = defaultdict(list)

for item in data.keys():
    letter_groups[item[0]].append(item)

for letter, items in sorted(letter_groups.items()):
    print(f"{letter}: {items}")

# Example with numbers: Group by even/odd
numbers = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10
}

print("\nOriginal numbers dict:")
for key, value in numbers.items():
    print(f"{key}: {value}")

# Group by even/odd
even_odd_groups = defaultdict(list)

for key, value in numbers.items():
    if value % 2 == 0:
        even_odd_groups['even'].append(f"{key}({value})")
    else:
        even_odd_groups['odd'].append(f"{key}({value})")

print("\nGrouped by even/odd:")
for group, items in even_odd_groups.items():
    print(f"{group}: {items}")