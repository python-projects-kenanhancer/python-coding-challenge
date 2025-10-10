"""
Python Dictionaries - Comprehensive Examples
============================================

Dictionaries are unordered collections of key-value pairs. They are mutable
and provide fast lookup, insertion, and deletion operations.
"""

# 1. Basic Dictionary Creation and Operations
print("=== BASIC DICTIONARY OPERATIONS ===")

# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
dict_from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])
dict_from_kwargs = dict(name="Bob", age=25, city="Boston")

print(f"Person: {person}")
print(f"Empty dict: {empty_dict}")
print(f"From pairs: {dict_from_pairs}")
print(f"From kwargs: {dict_from_kwargs}")

# Dictionary comprehension
squares = {x: x**2 for x in range(10)}
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# 2. Accessing and Modifying Values
print("\n=== ACCESSING AND MODIFYING VALUES ===")

student = {"name": "Charlie", "grade": "A", "subjects": ["Math", "Science"]}

# Accessing values
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")
print(f"Subjects: {student['subjects']}")

# Using get() method (safer)
print(f"Age (with get): {student.get('age', 'Not specified')}")
print(f"Grade (with get): {student.get('grade', 'Not specified')}")

# Modifying values
student["grade"] = "A+"
student["age"] = 20
print(f"After modifications: {student}")

# Adding new key-value pairs
student["teacher"] = "Dr. Smith"
print(f"After adding teacher: {student}")

# 3. Dictionary Methods
print("\n=== DICTIONARY METHODS ===")

inventory = {"apples": 50, "bananas": 30, "oranges": 40, "grapes": 25}

# keys() - returns view of all keys
print(f"Keys: {list(inventory.keys())}")

# values() - returns view of all values
print(f"Values: {list(inventory.values())}")

# items() - returns view of all key-value pairs
print(f"Items: {list(inventory.items())}")

# len() - number of key-value pairs
print(f"Length: {len(inventory)}")

# in operator - check if key exists
print(f"'apples' in inventory: {'apples' in inventory}")
print(f"'pears' in inventory: {'pears' in inventory}")

# 4. Adding and Removing Elements
print("\n=== ADDING AND REMOVING ELEMENTS ===")

# Adding elements
inventory["pears"] = 35
inventory.update({"mangoes": 20, "kiwis": 15})
print(f"After adding: {inventory}")

# Removing elements
del inventory["kiwis"]
removed_value = inventory.pop("mangoes")
print(f"Removed mangoes: {removed_value}")
print(f"After removing: {inventory}")

# popitem() - removes and returns last inserted item
last_item = inventory.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem(): {inventory}")

# clear() - removes all elements
inventory_copy = inventory.copy()
inventory_copy.clear()
print(f"After clear(): {inventory_copy}")

# 5. Dictionary Comprehensions
print("\n=== DICTIONARY COMPREHENSIONS ===")

# Basic comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(f"Word lengths: {word_lengths}")

# Conditional comprehension
students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 96}
high_achievers = {name: grade for name, grade in students.items() if grade >= 90}
print(f"High achievers: {high_achievers}")

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_dict = {f"pos_{i}_{j}": matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))}
print(f"Flattened matrix: {flattened_dict}")

# 6. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# Phone book
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012",
    "David": "555-3456"
}

print("Phone book:")
for name, phone in phone_book.items():
    print(f"  {name}: {phone}")

# Look up phone number
name_to_find = "Bob"
if name_to_find in phone_book:
    print(f"{name_to_find}'s phone: {phone_book[name_to_find]}")
else:
    print(f"{name_to_find} not found in phone book")

# Student grades with multiple subjects
student_grades = {
    "Alice": {"Math": 95, "Science": 88, "English": 92},
    "Bob": {"Math": 78, "Science": 85, "English": 90},
    "Charlie": {"Math": 92, "Science": 96, "English": 85}
}

print("\nStudent grades:")
for student, grades in student_grades.items():
    avg_grade = sum(grades.values()) / len(grades)
    print(f"  {student}: {grades} (Average: {avg_grade:.1f})")

# 7. Dictionary Views
print("\n=== DICTIONARY VIEWS ===")

data = {"a": 1, "b": 2, "c": 3, "d": 4}

# Views are dynamic - they reflect changes to the dictionary
keys_view = data.keys()
values_view = data.values()
items_view = data.items()

print(f"Keys view: {list(keys_view)}")
print(f"Values view: {list(values_view)}")
print(f"Items view: {list(items_view)}")

# Modify dictionary
data["e"] = 5
print(f"After adding 'e': {list(keys_view)}")  # View updates automatically

# Views support set operations
keys1 = {"a", "b", "c"}.keys()
keys2 = {"b", "c", "d"}.keys()
print(f"Intersection: {keys1 & keys2}")

# 8. Nested Dictionaries
print("\n=== NESTED DICTIONARIES ===")

# Company structure
company = {
    "CEO": {
        "name": "John Smith",
        "department": "Executive",
        "salary": 200000
    },
    "Engineering": {
        "manager": "Alice Johnson",
        "employees": ["Bob", "Charlie", "David"],
        "budget": 500000
    },
    "Marketing": {
        "manager": "Eve Wilson",
        "employees": ["Frank", "Grace"],
        "budget": 200000
    }
}

print("Company structure:")
for dept, info in company.items():
    print(f"  {dept}:")
    for key, value in info.items():
        print(f"    {key}: {value}")

# Accessing nested values
ceo_name = company["CEO"]["name"]
eng_employees = company["Engineering"]["employees"]
print(f"\nCEO: {ceo_name}")
print(f"Engineering employees: {eng_employees}")

# 9. Dictionary Merging
print("\n=== DICTIONARY MERGING ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

# Using update() (modifies original)
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"dict1.update(dict2): {dict1_copy}")

# Using ** operator (Python 3.5+)
merged = {**dict1, **dict2, **dict3}
print(f"Merged with **: {merged}")

# Using | operator (Python 3.9+)
merged_pipe = dict1 | dict2 | dict3
print(f"Merged with |: {merged_pipe}")

# 10. Dictionary Sorting
print("\n=== DICTIONARY SORTING ===")

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 96}

# Sort by keys
sorted_by_keys = dict(sorted(scores.items()))
print(f"Sorted by keys: {sorted_by_keys}")

# Sort by values
sorted_by_values = dict(sorted(scores.items(), key=lambda x: x[1]))
print(f"Sorted by values: {sorted_by_values}")

# Sort by values (descending)
sorted_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted by values (desc): {sorted_desc}")

# 11. Dictionary Performance
print("\n=== DICTIONARY PERFORMANCE ===")

import time

# Large dictionary for performance testing
large_dict = {i: i**2 for i in range(100000)}

# Access time
start_time = time.time()
for i in range(1000):
    _ = large_dict[i % 100000]
access_time = time.time() - start_time

print(f"Access time for 1000 operations: {access_time:.6f}s")

# 12. Common Dictionary Patterns
print("\n=== COMMON DICTIONARY PATTERNS ===")

# Counting occurrences
text = "hello world python programming hello python"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word count: {word_count}")

# Grouping
students_by_grade = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "David": "C",
    "Eve": "B"
}

# Group students by grade
grade_groups = {}
for student, grade in students_by_grade.items():
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(student)

print(f"Students by grade: {grade_groups}")

# Using defaultdict for grouping (more elegant)
from collections import defaultdict
grade_groups_dd = defaultdict(list)
for student, grade in students_by_grade.items():
    grade_groups_dd[grade].append(student)

print(f"Students by grade (defaultdict): {dict(grade_groups_dd)}")

# 13. Dictionary as Switch Statement
print("\n=== DICTIONARY AS SWITCH STATEMENT ===")

def handle_operation(operation, a, b):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    
    if operation in operations:
        return operations[operation](a, b)
    else:
        return "Unknown operation"

print(f"5 + 3 = {handle_operation('add', 5, 3)}")
print(f"10 - 4 = {handle_operation('subtract', 10, 4)}")
print(f"6 * 7 = {handle_operation('multiply', 6, 7)}")
print(f"15 / 3 = {handle_operation('divide', 15, 3)}")
print(f"10 / 0 = {handle_operation('divide', 10, 0)}")
print(f"5 ^ 2 = {handle_operation('power', 5, 2)}")

# 14. Dictionary with Functions
print("\n=== DICTIONARY WITH FUNCTIONS ===")

def greet():
    return "Hello!"

def farewell():
    return "Goodbye!"

def question():
    return "How are you?"

# Dictionary mapping strings to functions
actions = {
    "greet": greet,
    "farewell": farewell,
    "question": question
}

# Execute functions based on string input
user_input = "greet"
if user_input in actions:
    result = actions[user_input]()
    print(f"Action '{user_input}': {result}")

# 15. Dictionary Serialization
print("\n=== DICTIONARY SERIALIZATION ===")

import json

# Dictionary to JSON
person_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}

json_string = json.dumps(person_data, indent=2)
print(f"JSON string:\n{json_string}")

# JSON to dictionary
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")

# 16. Advanced Dictionary Operations
print("\n=== ADVANCED DICTIONARY OPERATIONS ===")

# Dictionary with default values
config = {
    "host": "localhost",
    "port": 8080,
    "timeout": 30
}

# Get with default
debug_mode = config.get("debug", False)
max_connections = config.get("max_connections", 100)
print(f"Debug mode: {debug_mode}")
print(f"Max connections: {max_connections}")

# Dictionary filtering
large_dict = {i: i**2 for i in range(20)}
filtered_dict = {k: v for k, v in large_dict.items() if v % 2 == 0}
print(f"Even values: {filtered_dict}")

# Dictionary transformation
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(f"Doubled values: {doubled}")

# 17. Dictionary Comparison
print("\n=== DICTIONARY COMPARISON ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
dict3 = {"a": 1, "b": 3}

print(f"dict1 == dict2: {dict1 == dict2}")  # True (order doesn't matter)
print(f"dict1 == dict3: {dict1 == dict3}")  # False (values different)

# 18. Dictionary Copying
print("\n=== DICTIONARY COPYING ===")

original = {"a": 1, "b": [1, 2, 3]}

# Shallow copy
shallow_copy = original.copy()
shallow_copy["b"].append(4)

print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Deep copy
import copy
deep_copy = copy.deepcopy(original)
deep_copy["b"].append(5)

print(f"Original after deep copy modification: {original}")
print(f"Deep copy: {deep_copy}")

print("\n" + "="*50)
print("Dictionary examples completed!")
print("="*50)
