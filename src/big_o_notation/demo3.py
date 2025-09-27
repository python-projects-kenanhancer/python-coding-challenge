numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

my_set = set(numbers)

print(numbers)
print(my_set)

my_set2 = {1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 2, 2}
print(my_set2)

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names)
print(unique_names)

python_users = {"Alice", "Bob", "Charlie"}
java_users = {"Bob", "Charlie", "David"}
python_and_java_users = python_users & java_users
print(python_and_java_users)

python_only_users = python_users - java_users
print(python_only_users)


java_only_users = java_users - python_users
print(java_only_users)

