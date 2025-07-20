user = {
    "name": "Alice",
    "age": 30,
    "city": "NYC",
}
print(user)

print(list(user.keys()))

numbers = (3, 1, 4, 1, 5, 9)
print(sorted(numbers))
print(sorted(set(numbers)))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a + b)  # This will raise an error
print(a | b)  # Union of sets
print(a & b)  # Intersection of sets
