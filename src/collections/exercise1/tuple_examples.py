"""
Python Tuples - Comprehensive Examples
======================================

Tuples are ordered, immutable collections that can contain duplicate elements.
They are similar to lists but cannot be modified after creation.
"""

# 1. Basic Tuple Creation and Operations
print("=== BASIC TUPLE OPERATIONS ===")

# Creating tuples
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True, [1, 2, 3])
empty_tuple = ()
single_element = (42,)  # Note the comma!
single_element_wrong = (42)  # This is just an int, not a tuple

print(f"Numbers tuple: {numbers}")
print(f"Mixed tuple: {mixed}")
print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_element}")
print(f"Type of (42): {type(single_element_wrong)}")
print(f"Type of (42,): {type(single_element)}")

# Tuple from other iterables
list_to_tuple = tuple([1, 2, 3, 4])
string_to_tuple = tuple("hello")
range_to_tuple = tuple(range(5))

print(f"From list: {list_to_tuple}")
print(f"From string: {string_to_tuple}")
print(f"From range: {range_to_tuple}")

# 2. Accessing Elements
print("\n=== ACCESSING ELEMENTS ===")

coordinates = (10, 20, 30)

# Indexing
print(f"First coordinate: {coordinates[0]}")
print(f"Last coordinate: {coordinates[-1]}")
print(f"Middle coordinate: {coordinates[1]}")

# Slicing
print(f"First two: {coordinates[:2]}")
print(f"Last two: {coordinates[-2:]}")
print(f"All elements: {coordinates[:]}")

# 3. Tuple Methods
print("\n=== TUPLE METHODS ===")

numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 5: {numbers.count(5)}")

# index() - find first occurrence
print(f"Index of 3: {numbers.index(3)}")
print(f"Index of 2: {numbers.index(2)}")

# 4. Tuple Unpacking
print("\n=== TUPLE UNPACKING ===")

# Basic unpacking
point = (3, 4)
x, y = point
print(f"Point: {point}")
print(f"x: {x}, y: {y}")

# Multiple assignment
a, b, c = (1, 2, 3)
print(f"a: {a}, b: {b}, c: {c}")

# Extended unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Ignoring values with _
person_info = ("Alice", 25, "Engineer", "New York", "USA")
name, age, *_ = person_info
print(f"Name: {name}, Age: {age}")

# 5. Tuple as Return Values
print("\n=== TUPLES AS RETURN VALUES ===")

def get_stats(numbers):
    """Return multiple statistics as a tuple."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = get_stats(data)
print(f"Data: {data}")
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.2f}")

# 6. Nested Tuples
print("\n=== NESTED TUPLES ===")

# Matrix as tuple of tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Matrix: {matrix}")
print(f"Element at (1,2): {matrix[1][2]}")

# Person records
people = (
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Designer"),
    ("Charlie", 35, "Manager")
)

print("People:")
for name, age, job in people:
    print(f"  {name}: {age} years old, {job}")

# 7. Tuple Comprehensions (Generator Expressions)
print("\n=== TUPLE COMPREHENSIONS ===")

# Using generator expressions
squares_gen = (x**2 for x in range(10))
squares_tuple = tuple(squares_gen)
print(f"Squares: {squares_tuple}")

# Filtering
even_squares = tuple(x**2 for x in range(10) if x % 2 == 0)
print(f"Even squares: {even_squares}")

# 8. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# RGB Colors
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128)
}

print("Color RGB values:")
for color, rgb in colors.items():
    print(f"  {color}: {rgb}")

# Calculate distance between two points
def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

point1 = (0, 0)
point2 = (3, 4)
dist = distance(point1, point2)
print(f"Distance between {point1} and {point2}: {dist}")

# 9. Immutable Nature
print("\n=== IMMUTABLE NATURE ===")

numbers = (1, 2, 3, 4, 5)
print(f"Original tuple: {numbers}")

# These operations will raise TypeError
try:
    numbers[0] = 10
except TypeError as e:
    print(f"Cannot modify tuple: {e}")

try:
    numbers.append(6)
except AttributeError as e:
    print(f"Cannot append to tuple: {e}")

# But we can create new tuples
new_numbers = numbers + (6, 7)
print(f"New tuple with added elements: {new_numbers}")

# 10. Tuple vs List Performance
print("\n=== PERFORMANCE COMPARISON ===")

import time

# Create large collections
size = 100000
list_data = list(range(size))
tuple_data = tuple(range(size))

# Access time comparison
start_time = time.time()
for i in range(1000):
    _ = list_data[i % size]
list_access_time = time.time() - start_time

start_time = time.time()
for i in range(1000):
    _ = tuple_data[i % size]
tuple_access_time = time.time() - start_time

print(f"List access time: {list_access_time:.6f}s")
print(f"Tuple access time: {tuple_access_time:.6f}s")

# 11. Tuple as Dictionary Keys
print("\n=== TUPLES AS DICTIONARY KEYS ===")

# Coordinates as keys
coordinate_map = {
    (0, 0): "origin",
    (1, 0): "east",
    (0, 1): "north",
    (1, 1): "northeast"
}

print("Coordinate map:")
for coord, direction in coordinate_map.items():
    print(f"  {coord} -> {direction}")

# Complex keys
student_grades = {
    ("Alice", "Math"): 95,
    ("Alice", "Science"): 88,
    ("Bob", "Math"): 78,
    ("Bob", "Science"): 92
}

print("\nStudent grades:")
for (student, subject), grade in student_grades.items():
    print(f"  {student} - {subject}: {grade}")

# 12. Named Tuples (using collections.namedtuple)
print("\n=== NAMED TUPLES ===")

from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
p1 = Point(3, 4)
p2 = Point(x=5, y=12)

person1 = Person("Alice", 25, "New York")
person2 = Person(name="Bob", age=30, city="Boston")

print(f"Point 1: {p1} (x={p1.x}, y={p1.y})")
print(f"Point 2: {p2} (x={p2.x}, y={p2.y})")
print(f"Person 1: {person1}")
print(f"Person 1 name: {person1.name}")

# 13. Tuple Methods and Operations
print("\n=== TUPLE METHODS AND OPERATIONS ===")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated 3 times: {repeated}")

# Membership testing
print(f"2 in tuple1: {2 in tuple1}")
print(f"10 in tuple1: {10 in tuple1}")

# Length and iteration
print(f"Length of combined: {len(combined)}")
print("Iterating over tuple:")
for item in combined:
    print(f"  {item}")

# 14. Converting Between Tuples and Lists
print("\n=== CONVERTING BETWEEN TUPLES AND LISTS ===")

# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_tuple}")

# Tuple to list
my_list_from_tuple = list(my_tuple)
print(f"Tuple to list: {my_list_from_tuple}")

# 15. Common Use Cases
print("\n=== COMMON USE CASES ===")

# Function arguments and return values
def process_coordinates(coords):
    """Process a list of coordinate tuples."""
    results = []
    for x, y in coords:
        magnitude = (x**2 + y**2)**0.5
        results.append((x, y, magnitude))
    return results

coordinates = [(3, 4), (5, 12), (1, 1)]
processed = process_coordinates(coordinates)
print("Processed coordinates (x, y, magnitude):")
for x, y, mag in processed:
    print(f"  ({x}, {y}) -> {mag:.2f}")

# Database-like records
employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 45000, "Marketing"),
    ("Charlie", 60000, "Engineering")
]

print("\nEmployees by department:")
engineering = [emp for emp in employees if emp[2] == "Engineering"]
marketing = [emp for emp in employees if emp[2] == "Marketing"]

print("Engineering:")
for name, salary, dept in engineering:
    print(f"  {name}: ${salary:,}")

print("Marketing:")
for name, salary, dept in marketing:
    print(f"  {name}: ${salary:,}")

print("\n" + "="*50)
print("Tuple examples completed!")
print("="*50)
