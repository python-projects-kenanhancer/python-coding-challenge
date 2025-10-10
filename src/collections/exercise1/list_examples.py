"""
Python Lists - Comprehensive Examples
=====================================

Lists are ordered, mutable collections that can contain duplicate elements.
They are one of the most commonly used data structures in Python.
"""

# 1. Basic List Creation and Operations
print("=== BASIC LIST OPERATIONS ===")

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
empty_list = []
list_from_range = list(range(10))

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Empty list: {empty_list}")
print(f"From range: {list_from_range}")

# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# 2. Adding Elements
print("\n=== ADDING ELEMENTS ===")

# append() - adds single element to end
numbers.append(6)
print(f"After append(6): {numbers}")

# extend() - adds multiple elements
numbers.extend([7, 8, 9])
print(f"After extend([7, 8, 9]): {numbers}")

# insert() - inserts at specific position
numbers.insert(0, 0)  # Insert 0 at beginning
print(f"After insert(0, 0): {numbers}")

# 3. Removing Elements
print("\n=== REMOVING ELEMENTS ===")

# remove() - removes first occurrence
numbers.remove(5)
print(f"After remove(5): {numbers}")

# pop() - removes and returns element at index
popped = numbers.pop()  # Removes last element
print(f"Popped element: {popped}")
print(f"After pop(): {numbers}")

popped_at_index = numbers.pop(2)  # Removes element at index 2
print(f"Popped at index 2: {popped_at_index}")
print(f"After pop(2): {numbers}")

# del statement
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# clear() - removes all elements
copy_numbers = numbers.copy()
copy_numbers.clear()
print(f"After clear(): {copy_numbers}")

# 4. Accessing and Modifying Elements
print("\n=== ACCESSING AND MODIFYING ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Indexing
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Second to last: {numbers[-2]}")

# Slicing
print(f"First 3 elements: {numbers[:3]}")
print(f"Last 3 elements: {numbers[-3:]}")
print(f"Middle elements: {numbers[2:6]}")
print(f"Every second element: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

# Modifying elements
numbers[0] = 100
numbers[1:4] = [200, 300, 400]
print(f"After modifications: {numbers}")

# 5. List Methods
print("\n=== LIST METHODS ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# count() - count occurrences
print(f"Count of 1: {numbers.count(1)}")
print(f"Count of 5: {numbers.count(5)}")

# index() - find first occurrence
print(f"Index of 4: {numbers.index(4)}")
print(f"Index of 5: {numbers.index(5)}")

# sort() - sort in place
numbers.sort()
print(f"Sorted: {numbers}")

numbers.sort(reverse=True)
print(f"Reverse sorted: {numbers}")

# sorted() - returns new sorted list
unsorted = [3, 1, 4, 1, 5]
sorted_list = sorted(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted copy: {sorted_list}")

# reverse() - reverse in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed: {numbers}")

# 6. List Comprehensions - Advanced
print("\n=== ADVANCED LIST COMPREHENSIONS ===")

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# Conditional comprehensions
words = ["hello", "world", "python", "programming", "code"]
long_words = [word.upper() for word in words if len(word) > 5]
print(f"Long words (upper): {long_words}")

# Dictionary from list comprehension
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# 7. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# Student grades
grades = [85, 92, 78, 96, 88, 73, 91, 84, 79, 95]

# Calculate statistics
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

print(f"Grades: {grades}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Filter grades above average
above_average = [grade for grade in grades if grade > average]
print(f"Above average: {above_average}")

# Shopping list example
shopping_list = ["apples", "bananas", "milk", "bread", "eggs"]
print(f"Shopping list: {shopping_list}")

# Mark items as bought
bought = ["apples", "milk"]
remaining = [item for item in shopping_list if item not in bought]
print(f"Remaining items: {remaining}")

# 8. Performance Considerations
print("\n=== PERFORMANCE CONSIDERATIONS ===")

import time

# Timing different operations
large_list = list(range(100000))

# Append vs insert
start_time = time.time()
large_list.append(99999)
append_time = time.time() - start_time

start_time = time.time()
large_list.insert(0, 0)  # Much slower for large lists
insert_time = time.time() - start_time

print(f"Append time: {append_time:.6f}s")
print(f"Insert at beginning time: {insert_time:.6f}s")

# 9. Common Pitfalls and Tips
print("\n=== COMMON PITFALLS AND TIPS ===")

# Shallow copy vs deep copy
original = [[1, 2], [3, 4]]
shallow_copy = original.copy()
deep_copy = [row[:] for row in original]

shallow_copy[0].append(3)
deep_copy[1].append(5)

print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Deep copy: {deep_copy}")

# List as default argument (bad practice)
def bad_function(item, my_list=[]):
    my_list.append(item)
    return my_list

def good_function(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(f"Bad function result: {bad_function(1)}")
print(f"Bad function result again: {bad_function(2)}")  # Unexpected!
print(f"Good function result: {good_function(1)}")
print(f"Good function result again: {good_function(2)}")  # Expected!

# 10. List with Different Data Types
print("\n=== WORKING WITH DIFFERENT DATA TYPES ===")

# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
    {"name": "Bob", "age": 22, "grades": [78, 85, 92]},
    {"name": "Charlie", "age": 19, "grades": [92, 88, 95]}
]

# Sort by age
students_by_age = sorted(students, key=lambda x: x["age"])
print("Students by age:")
for student in students_by_age:
    print(f"  {student['name']}: {student['age']} years old")

# Calculate average grades
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    student["average"] = round(avg_grade, 2)

print("\nStudents with averages:")
for student in students:
    print(f"  {student['name']}: {student['average']}")

print("\n" + "="*50)
print("List examples completed!")
print("="*50)
