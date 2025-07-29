from collections.abc import Collection, Sequence

# Both are collections
print(isinstance([1, 2, 3], Collection))  # True
print(isinstance((1, 2, 3), Collection))  # True
print(isinstance({1, 2, 3}, Collection))  # True (set is collection but not sequence)

# Both are sequences
print(isinstance([1, 2, 3], Sequence))  # True
print(isinstance((1, 2, 3), Sequence))  # True
print(isinstance({1, 2, 3}, Sequence))  # False (set is not a sequence)

# Strings are also sequences
print(isinstance("hello", Sequence))


a1 = [1, 2, 3]
a2 = (1, 2, 3)
a3 = {1, 2, 3}
a4 = {"name": "Alice", "age": 30}
A5 = "hello"
A6 = (1, 2, 3, 4, 5)

# With parentheses
empty_tuple = ()
single_item = (1,)  # Note the comma!
multiple_items = (1, 2, 3)

# Without parentheses (tuple packing)
coordinates = 10, 20
person = "Alice", 25, "Engineer"

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

# Tuple unpacking
x, y, z = (1, 2, 3)
print(x, y, z)  # Output: 1 2 3

# Tuple unpacking with asterisk
a, *b = (1, 2, 3, 4, 5)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]

# String operations
print(A5[0])  # Accessing first character of string
print(A5[-1])  # Accessing last character of string
print(A5[1:4])  # Slicing string from index 1 to 3 (exclusive)
print(A5[::-1])  # Reversing the string
print(A5.upper())  # Converting string to uppercase
print(A5.lower())  # Converting string to lowercase
print(A5.replace("l", "x"))  # Replacing 'l' with 'x' in the string
print(A5.split("l"))  # Splitting string by 'l' character
print(A5.find("l"))  # Finding the first occurrence of 'l' in the string
print(A5.count("l"))  # Counting occurrences of 'l'  # Output: 2
print(isinstance("hello", Collection))  # True (string is a collection)
print(isinstance("hello", Sequence))  # True (string is a sequence)

aa1 = [x * x for x in range(5) if x % 2 == 0]
print(aa1)

aa2 = {x: x * x for x in range(4)}
print(aa2)


def sayHello(firstName: str, lastName: str, *args, **kwargs):
    print(f"Hello {firstName} {lastName}!")
    if args:
        print("Additional positional arguments:", args)
    if kwargs:
        print("Additional keyword arguments:", kwargs)


sayHello("John", "Doe", 30, "Engineer", city="New York", country="USA")

l1 = lambda x: x * x

aa3 = sorted([1, 3, 2, 5, 4], key=lambda x: x % 2 == 0)
print(aa3)


aa4 = sorted([1, 3, 2, 5, 4], key=lambda x: x % 2 == 0, reverse=True)
print(aa4)


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result

    return wrapper


@my_decorator
def greet(first_name: str, last_name: str, *args, **kwargs):
    print(f"Hello {first_name} {last_name}!")
    if args:
        print("Additional positional arguments:", args)
    if kwargs:
        print("Additional keyword arguments:", kwargs)


greet("John", "Doe", 30, "Engineer", city="New York", country="USA")

greet("Alice", "Smith")

aa5 = [[]] * 3
print(aa5)

aa5[1].append(5)
print(aa5)  # Output: [[5], [5], [5]] (

import json

data = {"name": "Alice", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(json_data)

parsed_data = json.loads(json_data)
print(parsed_data)
