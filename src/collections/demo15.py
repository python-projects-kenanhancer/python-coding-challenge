my_tuple = (1, 2, 3, 4, 5)

a1 = my_tuple[1]  # O(1) - Accessing an element by index is constant time.


# O(n) - Iterating through all elements is linear time.
for item in my_tuple:
    pass

a2 = len(my_tuple)  # O(1) - Tuples have a fixed size, so length is constant time.

a3 = (1, 2, 3) + (4, 5)  # O(n) - Concatenation creates a new tuple, so linear time.

a4 = my_tuple * 2  # O(n) - Repeating a tuple creates a new tuple, so linear time.

a5 = 3 in my_tuple  # O(n) - Scans tuple until match or end, so linear time.

# O(k) - Slicing creates a new tuple with k elements, so linear time.
a6 = my_tuple[1:3]

a7 = my_tuple.count(2)  # O(n) - Counts occurrences of an element, so linear time.

# O(n) - Finds the index of the first occurrence of an element, so linear time.
a8 = my_tuple.index(3)

