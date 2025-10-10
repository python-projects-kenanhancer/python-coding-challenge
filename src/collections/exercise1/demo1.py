# This file was originally empty - now contains a simple demo
print("Hello from demo1.py!")
print("This is a simple demonstration file.")


numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
empty_list = []
list_from_range = list(range(10))

# list comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
odd_squares = [x**2 for x in range(10) if x % 2 != 0]

numbers.append(6)

numbers.extend([7, 8, 9])

numbers.insert(0, 0)

numbers.remove(5)

popped = numbers.pop()

popped_at_index = numbers.pop(2)

del numbers[0]

copy_numbers = numbers.copy()
copy_numbers.clear()

