# list - Mutable, ordered sequence

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.insert(0, 0)
my_list[2] = 99
print(my_list[1:4])
print(my_list[:5])

# tuple - Immutable, ordered sequence
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
x, y, *rest = my_tuple

# set - Mutable, unordered, unique collection
my_set = {1, 2, 3, 4, 5}
my_set.add(5)
my_set.remove(2)
my_set.discard(10)
other_set = {4, 5, 6}
print(f"my_set | other_set: {my_set | other_set}")  # Union
print(f"my_set & other_set: {my_set & other_set}")  # Intersection
print(f"my_set - other_set: {my_set - other_set}")  # Difference
print(f"my_set ^ other_set: {my_set ^ other_set}")  # Symmetric difference

# frozenset - Immutable, unordered, unique collection
my_frozenset = frozenset([1, 2, 3, 3, 4])
dict_with_frozenset = {my_frozenset: "Immutable set"}
print(dict_with_frozenset)

# dict - Mutable, unordered collection of key-value pairs
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict["d"] = 4
my_dict.pop("d")
del my_dict["c"]
print(my_dict)
for key, value in my_dict.items():
    print(f"{key}: {value}")
