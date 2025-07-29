import collections

# --- Basic Collection Types ---

# 1. List: Ordered, mutable, allows duplicate elements.
# Lists are created with square brackets [].
print("--- List Examples ---")
fruits_list = ["apple", "banana", "cherry", "apple"]
print(f"Initial list: {fruits_list}")

# Accessing items by index
print(f"First item: {fruits_list[0]}")
print(f"Last item: {fruits_list[-1]}")

# Modifying an item
fruits_list[1] = "blackberry"
print(f"After modification: {fruits_list}")

# Adding items
fruits_list.append("orange")  # Adds to the end
print(f"After append: {fruits_list}")
fruits_list.insert(1, "apricot")  # Inserts at a specific index
print(f"After insert: {fruits_list}")

# Removing items
fruits_list.remove("cherry")  # Removes the first occurrence of a value
print(f"After removing 'cherry': {fruits_list}")
popped_item = fruits_list.pop()  # Removes and returns the last item
print(f"Popped item: {popped_item}, List now: {fruits_list}")
print("-" * 20)


# 2. Tuple: Ordered, immutable, allows duplicate elements.
# Tuples are created with parentheses (). They cannot be changed after creation.
print("\n--- Tuple Examples ---")
colors_tuple = ("red", "green", "blue", "red")
print(f"Initial tuple: {colors_tuple}")

# Accessing items by index
print(f"Second item: {colors_tuple[1]}")

# Tuples are immutable, so the following lines would cause a TypeError:
# colors_tuple[0] = "yellow"
# colors_tuple.append("cyan")

# You can count items or find their index
print(f"Count of 'red': {colors_tuple.count('red')}")
print(f"Index of 'blue': {colors_tuple.index('blue')}")
print("-" * 20)


# 3. Set: Unordered, mutable, no duplicate elements.
# Sets are created with curly braces {} or the set() function.
# They automatically remove duplicates and do not maintain insertion order.
print("\n--- Set Examples ---")
numbers_set = {1, 2, 3, 4, 3, 2}
print(f"Initial set (duplicates removed): {numbers_set}")

# Adding and removing items
numbers_set.add(5)
print(f"After adding 5: {numbers_set}")
numbers_set.discard(2)  # Use discard to avoid an error if the item doesn't exist
print(f"After discarding 2: {numbers_set}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}, Set B: {set_b}")
print(f"Union (A | B): {set_a.union(set_b)}")
print(f"Intersection (A & B): {set_a.intersection(set_b)}")
print(f"Difference (A - B): {set_a.difference(set_b)}")
print(f"Symmetric Difference (A ^ B): {set_a.symmetric_difference(set_b)}")
print("-" * 20)


# 4. Dictionary: Unordered (in Python < 3.7), ordered (in Python >= 3.7), mutable, key-value pairs.
# Keys must be unique and immutable.
print("\n--- Dictionary Examples ---")
student = {"name": "Alice", "age": 25, "courses": ["Math", "CompSci"]}
print(f"Initial dictionary: {student}")

# Accessing values by key
print(f"Student's name: {student['name']}")
print(f"Student's age: {student.get('age')}")

# Modifying and adding entries
student["age"] = 26
student["major"] = "Computer Science"
print(f"Updated dictionary: {student}")

# Removing entries
del student["courses"]
print(f"After deleting 'courses': {student}")

# Iterating
print("Iterating over keys:", list(student.keys()))
print("Iterating over values:", list(student.values()))
print("Iterating over items:", list(student.items()))
print("-" * 20)


# --- Specialized Collection Types from the `collections` module ---

# 5. collections.namedtuple: Tuple subclasses with named fields
print("\n--- collections.namedtuple Example ---")
Point = collections.namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)
print(f"Named tuple: {p1}")
print(f"Access by name (p1.x): {p1.x}")
print(f"Access by index (p1[1]): {p1[1]}")
print("-" * 20)


# 6. collections.deque: A list-like container with fast appends and pops on either end.
print("\n--- collections.deque Example ---")
tasks = collections.deque(["task1", "task2", "task3"])
print(f"Initial deque: {tasks}")
tasks.appendleft("task0")  # Fast append to the left
print(f"After appendleft: {tasks}")
tasks.popleft()  # Fast pop from the left
print(f"After popleft: {tasks}")
print("-" * 20)


# 7. collections.Counter: A dict subclass for counting hashable objects.
print("\n--- collections.Counter Example ---")
word_counts = collections.Counter("mississippi")
print(f"Counts for 'mississippi': {word_counts}")
print(f"Most common: {word_counts.most_common(2)}")
print("-" * 20)


# 8. collections.defaultdict: A dict subclass that calls a factory function for missing keys.
print("\n--- collections.defaultdict Example ---")
# Creates a list for a key if it doesn't exist
s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(f"Grouped by key: {sorted(d.items())}")
print("-" * 20)
