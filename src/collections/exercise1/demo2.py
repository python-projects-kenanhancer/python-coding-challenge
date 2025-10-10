numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[:3])
print(numbers[-3:])
print(numbers[2:6])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::1])
print(numbers[::-2])


print("numbers[:5:-1] =", numbers[:5:-1]) # start from index 5 and go backwards
print("numbers[None:5:-1] =", numbers[None:5:-1])  # Same as [:5:-1]
print("numbers[-1:5:-1] =", numbers[-1:5:-1])      # Start from last element
print("numbers[8:5:-1] =", numbers[8:5:-1])        # Start from index 8
print("numbers[7:5:-1] =", numbers[7:5:-1])        # Start from index 7
print("numbers[6:5:-1] =", numbers[6:5:-1])        # Start from index 6 



# Let's explore slice parameters and negative step values
print("Original list:", numbers)
print("Index positions:", list(range(len(numbers))))
print("Negative indices:", list(range(-len(numbers), 0)))
print()

# Understanding numbers[-1:5:-1]
print("=== numbers[-1:5:-1] breakdown ===")
print("Start: -1 (last element, index 8)")
print("Stop: 5 (index 5, element 6)")  
print("Step: -1 (go backwards)")
print("Result:", numbers[-1:5:-1])
print()

# Different negative step values
print("=== Different negative step values ===")
print("numbers[-1:5:-1] =", numbers[-1:5:-1])  # Step -1: every element backwards
print("numbers[-1:5:-2] =", numbers[-1:5:-2])  # Step -2: every 2nd element backwards
print("numbers[-1:5:-3] =", numbers[-1:5:-3])  # Step -3: every 3rd element backwards
print()

# More examples with different start/stop combinations
print("=== More examples ===")
print("numbers[8:2:-1] =", numbers[8:2:-1])    # From index 8 to 2, backwards
print("numbers[8:2:-2] =", numbers[8:2:-2])    # From index 8 to 2, every 2nd backwards
print("numbers[-2:3:-1] =", numbers[-2:3:-1])  # From 2nd last to index 3, backwards 
