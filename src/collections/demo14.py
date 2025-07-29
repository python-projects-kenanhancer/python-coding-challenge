# list: mutable, ordered, allows duplicates
a1 = [1, 1, 2, 2, 3, 3, 4, 4]


a1.append(5)
a1.insert(2, 6)
a1.remove(2)
print(a1)
print(sorted(a1))

a1.reverse()
a1.extend([7, 8, 9])

list = [1, 2, 3, 3, 4, 5]

a2 = list[1]  # O(1) - Accessing an element by index is constant time.
list.append(6)  # O(1) - Occasionally resizes, but average is constant time.
a4 = list.pop()  # O(1) - Removing the last element is constant time.
a5 = list.pop(0)  # O(n) - Requires shifting all remaining elements, so linear time.
list.insert(
    0, 0
)  # O(n) - Requires shifting all elements to the right after the insert index, so linear time.
list.insert(
    len(list), 10
)  # O(1) - Equivalent to append if no resize is needed, average is constant time, but can be O(n) if resize occurs.
list.insert(
    1, 2
)  # O(n) - Requires shifting elements to the right after the insert index, so linear time.
del list[
    2
]  # O(n) - Requires shifting elements to the left after the delete index, so linear time.
a6 = 3 in list  # O(n) - Scans list until match or end, so linear time.
# O(n) - Iterating through the list is linear time.
for x in list:
    pass

list.remove(3)  # O(n) - Scans list until first match, then removes it, so linear time.

list.sort()  # O(n log n) - Timsort algorithm used internally, so average is linearithmic time.

a7 = list[:]  # O(n) - Creates a shallow copy of the list, so linear time.

list.extend([11, 12])  # O(k) - Appends k elements, average is linear time.

a9 = list[1:3]  # O(k) - Slicing creates a new list with k elements, so linear time.
