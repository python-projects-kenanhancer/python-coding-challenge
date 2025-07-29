from collections import defaultdict


employees = [
    ("Alice", "HR"),
    ("Bob", "Engineering"),
    ("Charlie", "HR"),
    ("Dave", "Engineering"),
]

department_counter = defaultdict(list)

for name, department in employees:
    department_counter[department].append(name)

print(dict(department_counter))
