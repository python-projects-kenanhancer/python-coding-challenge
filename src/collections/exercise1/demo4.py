numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=== REVERSE ENUMERATE METHODS DEMO ===")
print("Original list:", numbers)
print("Expected reverse every 2nd:", numbers[::-2])  # [9, 7, 5, 3, 1]
print()


def print_every_two_with_range(numbers: list[int]):
    result: list[int] = []
    for i in range(0, len(numbers), 2):
        result.append(numbers[i])

    return result


def print_every_two_with_enumerate(numbers: list[int]):
    result: list[int] = []
    for i, value in enumerate(numbers):
        if i % 2 == 0:
            result.append(value)

    return result


def print_every_two_with_while(numbers: list[int]):
    result: list[int] = []
    i = 0
    while i < len(numbers):
        result.append(numbers[i])
        i += 2

    return result


def print_every_two_with_range_reverse(numbers: list[int]):
    result: list[int] = []
    for i in range(len(numbers) - 1, -1, -2):  # Fixed: start from len-1, go to -1
        result.append(numbers[i])

    return result


def print_every_two_with_enumerate_reverse(numbers: list[int]):
    result: list[int] = []
    # Method 1: Using enumerate with reversed list
    for i, value in enumerate(reversed(numbers)):
        if i % 2 == 0:  # Every 2nd element from the reversed list
            result.append(value)
    return result


# Removed broken v2 and v3 methods - they don't actually reverse!
# Only keeping the working methods below.


def print_every_two_with_enumerate_reverse_v4(numbers: list[int]):
    result: list[int] = []
    # Method 4: Using enumerate with explicit reverse stepping
    for i, value in enumerate(numbers):
        # We want to include elements at positions: 8, 6, 4, 2, 0
        # This means: len-1, len-3, len-5, len-7, len-9
        if i % 2 == 1:  # Take odd indices (1,3,5,7) and reverse them
            continue
        # For even indices, we need to reverse the order
        result.insert(0, value)  # Insert at beginning to reverse order
    return result


# Show what indices each version generates
print("=== INDEX ANALYSIS ===")
print("v1 indices:", list(range(len(numbers) - 1, -1, -2)))
print("v2 indices:", list(range(len(numbers) - 1, 0, -2)))
print()

print("Testing WORKING reverse methods:")
print("1. Range reverse:", print_every_two_with_range_reverse(numbers))
print(
    "2. Enumerate reverse (reversed):", print_every_two_with_enumerate_reverse(numbers)
)
print(
    "3. Enumerate reverse v4 (insert at start):",
    print_every_two_with_enumerate_reverse_v4(numbers),
)
print()

print("=== WORKING METHODS ONLY ===")
print("✅ Method 1: enumerate(reversed(numbers)) - Most intuitive and efficient")
print("✅ Method 2: insert(0, value) - Works but less efficient")
print("✅ Method 3: range(len-1, -1, -2) - Traditional approach")
print()
print("🎯 RECOMMENDATION: Use numbers[::-2] for production code")
print("🎯 If you MUST use enumerate: Use enumerate(reversed())")
