"""
Python Counter - Comprehensive Examples
=======================================

Counter is a subclass of dict that is designed for counting hashable objects.
It's part of the collections module and provides convenient methods for counting.
"""

from collections import Counter
import re

import random
from datetime import datetime, timedelta

# 1. Basic Counter Creation and Operations
print("=== BASIC COUNTER OPERATIONS ===")

# Creating counters
counter1 = Counter()
counter2 = Counter(["a", "b", "c", "a", "b", "a"])
counter3 = Counter({"a": 3, "b": 2, "c": 1})
counter4 = Counter(a=3, b=2, c=1)

print(f"Empty counter: {counter1}")
print(f"From list: {counter2}")
print(f"From dict: {counter3}")
print(f"From kwargs: {counter4}")

# Counter from string
text = "hello world"
char_counter = Counter(text)
print(f"Character counter: {char_counter}")

# Counter from word list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counter = Counter(words)
print(f"Word counter: {word_counter}")

# 2. Accessing and Modifying Counts
print("\n=== ACCESSING AND MODIFYING COUNTS ===")

counter = Counter(["a", "b", "c", "a", "b", "a"])

# Accessing counts
print(f"Count of 'a': {counter['a']}")
print(f"Count of 'b': {counter['b']}")
print(f"Count of 'x': {counter['x']}")  # Returns 0 for missing keys

# Modifying counts
counter["a"] += 1
counter["d"] = 5
print(f"After modifications: {counter}")

# Update counter
counter.update(["a", "b", "c", "d"])
print(f"After update: {counter}")

counter.update({"a": 2, "e": 3})
print(f"After dict update: {counter}")

# 3. Counter Methods
print("\n=== COUNTER METHODS ===")

counter = Counter(["a", "b", "c", "a", "b", "a", "c", "a"])

# most_common() - returns most common elements
print(f"Most common: {counter.most_common()}")
print(f"Top 3 most common: {counter.most_common(3)}")
print(f"Most common element: {counter.most_common(1)}")

# subtract() - subtract counts
counter.subtract(["a", "b"])
print(f"After subtract: {counter}")

counter.subtract({"a": 2})
print(f"After dict subtract: {counter}")

# elements() - returns elements repeated according to count
print(f"Elements: {list(counter.elements())}")

# 4. Counter Arithmetic Operations
print("\n=== COUNTER ARITHMETIC OPERATIONS ===")

counter1 = Counter(["a", "b", "c", "a", "b"])
counter2 = Counter(["b", "c", "d", "b", "c"])

print(f"Counter 1: {counter1}")
print(f"Counter 2: {counter2}")

# Addition
sum_counter = counter1 + counter2
print(f"Addition (+): {sum_counter}")

# Subtraction
diff_counter = counter1 - counter2
print(f"Subtraction (-): {diff_counter}")

# Union (max of each element)
union_counter = counter1 | counter2
print(f"Union (|): {union_counter}")

# Intersection (min of each element)
intersection_counter = counter1 & counter2
print(f"Intersection (&): {intersection_counter}")

# 5. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# Text analysis
text = "Python is great. Python is powerful. Python is versatile."
words = re.findall(r"\w+", text.lower())
word_count = Counter(words)

print(f"Text: {text}")
print(f"Word count: {word_count}")
print(f"Most common words: {word_count.most_common(3)}")

# Voting results
votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "David", "Alice"]
vote_counter = Counter(votes)

print(f"\nVotes: {votes}")
print(f"Vote count: {vote_counter}")
print(f"Winner: {vote_counter.most_common(1)[0]}")

# Dice rolling simulation
import random


def simulate_dice_rolls(n_rolls):
    rolls = [random.randint(1, 6) for _ in range(n_rolls)]
    return Counter(rolls)


dice_results = simulate_dice_rolls(1000)
print(f"\nDice rolls (1000 times): {dice_results}")
print(f"Most common roll: {dice_results.most_common(1)}")

# 6. Counter with Different Data Types
print("\n=== COUNTER WITH DIFFERENT DATA TYPES ===")

# Numbers
numbers = [1, 2, 3, 2, 1, 3, 1, 2, 3, 1]
number_counter = Counter(numbers)
print(f"Number counter: {number_counter}")

# Tuples (hashable)
coordinates = [(1, 2), (3, 4), (1, 2), (5, 6), (1, 2), (3, 4)]
coord_counter = Counter(coordinates)
print(f"Coordinate counter: {coord_counter}")

# Mixed types
mixed = [1, "a", 1, "b", "a", 2, "b", 1]
mixed_counter = Counter(mixed)
print(f"Mixed counter: {mixed_counter}")

# 7. Advanced Counter Operations
print("\n=== ADVANCED COUNTER OPERATIONS ===")

# Shopping cart
cart = Counter({"apple": 5, "banana": 3, "orange": 2, "grape": 1})

print(f"Shopping cart: {cart}")

# Add more items
cart.update({"apple": 2, "mango": 3})
print(f"After adding more: {cart}")

# Remove some items
cart.subtract({"banana": 1, "orange": 1})
print(f"After removing some: {cart}")

# Get total items
total_items = sum(cart.values())
print(f"Total items: {total_items}")

# Get unique item types
unique_items = len(cart)
print(f"Unique item types: {unique_items}")

# 8. Counter for Data Analysis
print("\n=== COUNTER FOR DATA ANALYSIS ===")

# Student grades
grades = [85, 92, 78, 96, 88, 73, 91, 84, 79, 95, 85, 92, 88, 91, 85]
grade_counter = Counter(grades)

print(f"Grade distribution: {grade_counter}")


# Grade ranges
def get_grade_range(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


grade_ranges = Counter(get_grade_range(grade) for grade in grades)
print(f"Grade ranges: {grade_ranges}")

# 9. Counter with File Analysis
print("\n=== COUNTER WITH FILE ANALYSIS ===")

# Simulate file content
file_content = """
Python is a programming language.
Python is easy to learn.
Python is powerful.
Python programming is fun.
"""

# Count words
words = re.findall(r"\b\w+\b", file_content.lower())
word_freq = Counter(words)

print(f"File content: {file_content.strip()}")
print(f"Word frequency: {word_freq}")
print(f"Most common words: {word_freq.most_common(5)}")

# Count characters (excluding whitespace)
chars = [c for c in file_content.lower() if c.isalpha()]
char_freq = Counter(chars)
print(f"Character frequency: {char_freq.most_common(5)}")

# 10. Counter Performance and Memory
print("\n=== COUNTER PERFORMANCE ===")

import time

# Large dataset
large_data = [random.randint(1, 100) for _ in range(100000)]

# Time Counter creation
start_time = time.time()
counter = Counter(large_data)
counter_time = time.time() - start_time

# Time manual counting
start_time = time.time()
manual_count = {}
for item in large_data:
    manual_count[item] = manual_count.get(item, 0) + 1
manual_time = time.time() - start_time

print(f"Counter creation time: {counter_time:.6f}s")
print(f"Manual counting time: {manual_time:.6f}s")
print(f"Counter is {manual_time / counter_time:.1f}x faster")

# 11. Counter with Custom Objects
print("\n=== COUNTER WITH CUSTOM OBJECTS ===")

# Using Counter with tuples (representing coordinates)
coordinates = [(1, 1), (2, 2), (1, 1), (3, 3), (2, 2), (1, 1)]
coord_counter = Counter(coordinates)

print(f"Coordinate frequency: {coord_counter}")
print(f"Most visited coordinate: {coord_counter.most_common(1)}")

# Using Counter with strings (representing categories)
categories = ["fruit", "vegetable", "fruit", "meat", "vegetable", "fruit", "dairy"]
category_counter = Counter(categories)

print(f"Category frequency: {category_counter}")

# 12. Counter for Anagrams
print("\n=== COUNTER FOR ANAGRAMS ===")


def is_anagram(word1, word2):
    """Check if two words are anagrams using Counter."""
    return Counter(word1.lower()) == Counter(word2.lower())


def find_anagrams(word_list):
    """Group words by their character counts."""
    groups = {}
    for word in word_list:
        # Use sorted tuple of characters as key
        key = tuple(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups


words = ["listen", "silent", "enlist", "hello", "world", "drawn", "ward"]
anagram_groups = find_anagrams(words)

print(f"Words: {words}")
print("Anagram groups:")
for group in anagram_groups.values():
    if len(group) > 1:
        print(f"  {group}")

# 13. Counter for Network Analysis
print("\n=== COUNTER FOR NETWORK ANALYSIS ===")

# Simulate network connections
connections = [
    ("A", "B"),
    ("B", "C"),
    ("A", "C"),
    ("D", "E"),
    ("B", "D"),
    ("C", "E"),
    ("A", "D"),
    ("B", "E"),
]

# Count connections per node
node_connections = Counter()
for source, target in connections:
    node_connections[source] += 1
    node_connections[target] += 1

print(f"Connections: {connections}")
print(f"Node connection counts: {node_connections}")
print(f"Most connected node: {node_connections.most_common(1)}")

# 14. Counter with Mathematical Operations
print("\n=== COUNTER WITH MATHEMATICAL OPERATIONS ===")

# Set operations with counters
counter1 = Counter({"a": 3, "b": 2, "c": 1})
counter2 = Counter({"a": 1, "b": 3, "d": 2})

print(f"Counter 1: {counter1}")
print(f"Counter 2: {counter2}")

# Addition (combines counts)
combined = counter1 + counter2
print(f"Combined (+): {combined}")

# Subtraction (subtracts counts, removes zero/negative)
subtracted = counter1 - counter2
print(f"Subtracted (-): {subtracted}")

# Union (takes maximum of each)
union = counter1 | counter2
print(f"Union (max): {union}")

# Intersection (takes minimum of each)
intersection = counter1 & counter2
print(f"Intersection (min): {intersection}")

# 15. Counter for Time Series Analysis
print("\n=== COUNTER FOR TIME SERIES ANALYSIS ===")

# Simulate daily sales data

# Generate 30 days of sales data
start_date = datetime.now() - timedelta(days=30)
daily_sales = {}

for i in range(30):
    date = start_date + timedelta(days=i)
    # Simulate sales of different products
    products = ["laptop", "mouse", "keyboard", "monitor", "headphones"]
    sales = random.choices(products, k=random.randint(10, 50))
    daily_sales[date.strftime("%Y-%m-%d")] = Counter(sales)

# Analyze total sales across all days
total_sales = Counter()
for day_sales in daily_sales.values():
    total_sales += day_sales

print(f"Total sales over 30 days: {total_sales}")
print(f"Best selling product: {total_sales.most_common(1)}")

# 16. Counter Methods Deep Dive
print("\n=== COUNTER METHODS DEEP DIVE ===")

counter = Counter(["a", "b", "c", "a", "b", "a", "c"])

# elements() - returns iterator
elements = list(counter.elements())
print(f"Elements iterator: {elements}")

# most_common() variations
print(f"All elements (most common): {counter.most_common()}")
print(f"Top 2: {counter.most_common(2)}")
print(f"Least common: {counter.most_common()[-1]}")

# subtract() with negative results
counter.subtract(["a", "a", "a", "a"])  # More than available
print(f"After excessive subtract: {counter}")
print(f"Elements after negative count: {list(counter.elements())}")

# 17. Counter for Configuration Analysis
print("\n=== COUNTER FOR CONFIGURATION ANALYSIS ===")

# Analyze configuration settings
configs = [
    {"debug": True, "port": 8080, "host": "localhost"},
    {"debug": False, "port": 8080, "host": "production"},
    {"debug": True, "port": 3000, "host": "localhost"},
    {"debug": False, "port": 8080, "host": "staging"},
]

# Count occurrences of each configuration value
debug_count = Counter(config["debug"] for config in configs)
port_count = Counter(config["port"] for config in configs)
host_count = Counter(config["host"] for config in configs)

print(f"Debug settings: {debug_count}")
print(f"Port settings: {port_count}")
print(f"Host settings: {host_count}")

print("\n" + "=" * 50)
print("Counter examples completed!")
print("=" * 50)
