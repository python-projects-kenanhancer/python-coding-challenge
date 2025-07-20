# This code demonstrates the operations on an array/list and their complexities.


# Array/List Operations and their Big O Notations
# 1. Accessing an element by index: O(1)
# 2. Searching for an element: O(n)
# 3. Inserting an element at the end: O(1) (amortized)
# 4. Inserting an element at the beginning: O(n)
# 5. Deleting an element at the end: O(1)
# 6. Deleting an element at the beginning: O(n)
# 7. Finding the length of an array: O(1)
# 8. Getting the first element: O(1)


def access_element(arr, index):
    return arr[index]


def search_element(arr, element):
    for i in arr:
        if i == element:
            return True
    return False


def insert_at_end(arr, element):
    arr.append(element)
    return arr


def insert_at_beginning(arr, element):
    arr.insert(0, element)
    return arr


def delete_at_end(arr):
    if arr:
        arr.pop()
    return arr


def delete_at_beginning(arr):
    if arr:
        arr.pop(0)
    return arr


def get_length(arr):
    return len(arr)


def get_first_element(arr):
    if arr:
        return arr[0]
    return None


def main():
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)

    print("Access element at index 2:", access_element(arr, 2))
    print("Search for element 3:", search_element(arr, 3))

    arr = insert_at_end(arr, 6)
    print("After inserting 6 at the end:", arr)

    arr = insert_at_beginning(arr, 0)
    print("After inserting 0 at the beginning:", arr)

    arr = delete_at_end(arr)
    print("After deleting last element:", arr)

    arr = delete_at_beginning(arr)
    print("After deleting first element:", arr)

    print("Length of array:", get_length(arr))
    print("First element of array:", get_first_element(arr))
    print("Accessing element at index 0:", access_element(arr, 0))
    print("Accessing element at index 1:", access_element(arr, 1))
    print("Accessing element at index 2:", access_element(arr, 2))


if __name__ == "__main__":
    main()
