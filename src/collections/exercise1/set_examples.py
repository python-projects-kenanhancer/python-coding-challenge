"""
Python Sets - Comprehensive Examples
====================================

Sets are unordered collections of unique elements. They are mutable and
support mathematical set operations like union, intersection, and difference.
"""

# 1. Basic Set Creation and Operations
print("=== BASIC SET OPERATIONS ===")

# Creating sets
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}
empty_set = set()  # Note: {} creates an empty dict, not set!
empty_set_wrong = {}  # This is a dictionary!

print(f"Numbers set: {numbers}")
print(f"Mixed set: {mixed}")
print(f"Empty set: {empty_set}")
print(f"Type of {{}}: {type(empty_set_wrong)}")

# Set from other iterables
list_to_set = set([1, 2, 3, 3, 4, 4, 5])  # Duplicates removed
string_to_set = set("hello")  # {'h', 'e', 'l', 'o'}
tuple_to_set = set((1, 2, 3, 2, 1))

print(f"From list (duplicates removed): {list_to_set}")
print(f"From string: {string_to_set}")
print(f"From tuple: {tuple_to_set}")

# Set comprehension
squares = {x**2 for x in range(10)}
print(f"Squares set: {squares}")

# 2. Adding and Removing Elements
print("\n=== ADDING AND REMOVING ELEMENTS ===")

my_set = {1, 2, 3}

# add() - adds single element
my_set.add(4)
print(f"After add(4): {my_set}")

# add() with duplicate (no effect)
my_set.add(2)  # 2 already exists
print(f"After add(2) again: {my_set}")

# update() - adds multiple elements
my_set.update([5, 6, 7])
print(f"After update([5, 6, 7]): {my_set}")

my_set.update({8, 9})
print(f"After update({{8, 9}}): {my_set}")

# remove() - removes element (raises KeyError if not found)
my_set.remove(9)
print(f"After remove(9): {my_set}")

# discard() - removes element (no error if not found)
my_set.discard(10)  # 10 doesn't exist, but no error
print(f"After discard(10): {my_set}")

# pop() - removes and returns arbitrary element
popped = my_set.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {my_set}")

# clear() - removes all elements
my_set.clear()
print(f"After clear(): {my_set}")

# 3. Set Operations
print("\n=== SET OPERATIONS ===")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union
union = set1 | set2
union_method = set1.union(set2)
print(f"Union (|): {union}")
print(f"Union (method): {union_method}")

# Intersection
intersection = set1 & set2
intersection_method = set1.intersection(set2)
print(f"Intersection (&): {intersection}")
print(f"Intersection (method): {intersection_method}")

# Difference
difference = set1 - set2
difference_method = set1.difference(set2)
print(f"Difference (-): {difference}")
print(f"Difference (method): {difference_method}")

# Symmetric difference
sym_diff = set1 ^ set2
sym_diff_method = set1.symmetric_difference(set2)
print(f"Symmetric difference (^): {sym_diff}")
print(f"Symmetric difference (method): {sym_diff_method}")

# 4. Set Comparison Operations
print("\n=== SET COMPARISON OPERATIONS ===")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# Subset
print(f"A is subset of B: {set_a <= set_b}")
print(f"A is proper subset of B: {set_a < set_b}")

# Superset
print(f"B is superset of A: {set_b >= set_a}")
print(f"B is proper superset of A: {set_b > set_a}")

# Equality
print(f"A equals C: {set_a == set_c}")
print(f"A equals B: {set_a == set_b}")

# Disjoint (no common elements)
set_d = {6, 7, 8}
print(f"A and D are disjoint: {set_a.isdisjoint(set_d)}")
print(f"A and B are disjoint: {set_a.isdisjoint(set_b)}")

# 5. Set Methods
print("\n=== SET METHODS ===")

numbers = {1, 2, 3, 4, 5}

# len() - number of elements
print(f"Length: {len(numbers)}")

# in operator - membership testing
print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")

# copy() - shallow copy
numbers_copy = numbers.copy()
print(f"Copy: {numbers_copy}")

# 6. Practical Examples
print("\n=== PRACTICAL EXAMPLES ===")

# Finding unique elements
grades = [85, 92, 78, 85, 96, 88, 92, 78]
unique_grades = set(grades)
print(f"All grades: {grades}")
print(f"Unique grades: {unique_grades}")

# Removing duplicates from list
unique_list = list(set(grades))
print(f"Unique grades as list: {unique_list}")

# Finding common elements
students_math = {"Alice", "Bob", "Charlie", "David"}
students_science = {"Bob", "Charlie", "Eve", "Frank"}
both_subjects = students_math & students_science
print(f"Students taking both math and science: {both_subjects}")

# Finding students in only one subject
only_math = students_math - students_science
only_science = students_science - students_math
print(f"Only math: {only_math}")
print(f"Only science: {only_science}")

# All students
all_students = students_math | students_science
print(f"All students: {all_students}")

# 7. Set Comprehensions
print("\n=== SET COMPREHENSIONS ===")

# Squares of even numbers
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Length of words
words = ["hello", "world", "python", "programming", "code"]
word_lengths = {len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Prime numbers (simple example)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = {x for x in range(2, 50) if is_prime(x)}
print(f"Primes up to 50: {primes}")

# 8. Frozen Sets (Immutable Sets)
print("\n=== FROZEN SETS ===")

# Creating frozen sets
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")

# Frozen sets can be used as dictionary keys
frozen_dict = {frozenset([1, 2]): "first", frozenset([3, 4]): "second"}
print(f"Dictionary with frozen set keys: {frozen_dict}")

# Frozen sets support set operations
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([3, 4, 5])
frozen_union = frozen1 | frozen2
print(f"Frozen set union: {frozen_union}")

# 9. Advanced Set Operations
print("\n=== ADVANCED SET OPERATIONS ===")

# Multiple set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {5, 6, 7, 8, 9}

# Intersection of all sets
all_intersection = set1 & set2 & set3
print(f"Intersection of all: {all_intersection}")

# Union of all sets
all_union = set1 | set2 | set3
print(f"Union of all: {all_union}")

# Elements in exactly one set
exactly_one = (set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 - set2)
print(f"Elements in exactly one set: {exactly_one}")

# 10. Performance and Use Cases
print("\n=== PERFORMANCE AND USE CASES ===")

import time

# Large sets for performance testing
large_list = list(range(100000))
large_set = set(large_list)

# Membership testing performance
target = 50000

start_time = time.time()
result = target in large_list
list_time = time.time() - start_time

start_time = time.time()
result = target in large_set
set_time = time.time() - start_time

print(f"List membership test: {list_time:.6f}s")
print(f"Set membership test: {set_time:.6f}s")
print(f"Set is {list_time/set_time:.1f}x faster for membership testing")

# 11. Common Patterns
print("\n=== COMMON PATTERNS ===")

# Tag system
article_tags = {"python", "programming", "tutorial", "beginner"}
user_interests = {"python", "data-science", "machine-learning", "tutorial"}

# Find articles matching user interests
matching_tags = article_tags & user_interests
print(f"Article tags: {article_tags}")
print(f"User interests: {user_interests}")
print(f"Matching tags: {matching_tags}")

# Permission system
admin_permissions = {"read", "write", "delete", "admin"}
user_permissions = {"read", "write"}
guest_permissions = {"read"}

def has_permission(user_perms, required_perms):
    return required_perms.issubset(user_perms)

print(f"User can delete: {has_permission(user_permissions, {'delete'})}")
print(f"Admin can delete: {has_permission(admin_permissions, {'delete'})}")
print(f"User can read: {has_permission(user_permissions, {'read'})}")

# 12. Set vs List for Unique Elements
print("\n=== SET VS LIST FOR UNIQUE ELEMENTS ===")

# Removing duplicates from a list
def remove_duplicates_list(items):
    """Remove duplicates using list (preserves order)."""
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

def remove_duplicates_set(items):
    """Remove duplicates using set (doesn't preserve order)."""
    return list(set(items))

# Test with duplicate data
data_with_duplicates = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4]

list_result = remove_duplicates_list(data_with_duplicates)
set_result = remove_duplicates_set(data_with_duplicates)

print(f"Original: {data_with_duplicates}")
print(f"List method (preserves order): {list_result}")
print(f"Set method (no order): {set_result}")

# 13. Set Algebra Examples
print("\n=== SET ALGEBRA EXAMPLES ===")

# Venn diagram simulation
all_students = set("ABCDEFGHIJ")
math_students = set("ABCDE")
science_students = set("CDEFG")
english_students = set("EFGHI")

print(f"All students: {all_students}")
print(f"Math students: {math_students}")
print(f"Science students: {science_students}")
print(f"English students: {english_students}")

# Students taking all three subjects
all_three = math_students & science_students & english_students
print(f"All three subjects: {all_three}")

# Students taking exactly two subjects
math_science = math_students & science_students
math_english = math_students & english_students
science_english = science_students & english_students

exactly_two = (math_science | math_english | science_english) - all_three
print(f"Exactly two subjects: {exactly_two}")

# Students taking only one subject
only_math = math_students - science_students - english_students
only_science = science_students - math_students - english_students
only_english = english_students - math_students - science_students

only_one = only_math | only_science | only_english
print(f"Only one subject: {only_one}")

# Students not taking any of these subjects
none = all_students - math_students - science_students - english_students
print(f"No subjects: {none}")

# 14. Set Methods Summary
print("\n=== SET METHODS SUMMARY ===")

demo_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7, 8}

print(f"Demo set: {demo_set}")
print(f"Other set: {other_set}")

# Update operations (modify the set)
demo_set.update([9, 10])
print(f"After update: {demo_set}")

demo_set.intersection_update(other_set)
print(f"After intersection_update: {demo_set}")

# Check if sets are equal
set_equal = {1, 2, 3}
set_equal_copy = {3, 1, 2}
print(f"Sets are equal: {set_equal == set_equal_copy}")

print("\n" + "="*50)
print("Set examples completed!")
print("="*50)
