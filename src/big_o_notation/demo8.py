from collections import Counter, defaultdict

my_list = ["A", "C", "X", "C", "B"]

print(len(my_list))

print(sorted(my_list))

print(set(my_list))

c = Counter(my_list)
print(c)

c["A"] += 1

print(c)

persons = defaultdict(int)

for item in my_list:
    persons[item] += 1

print(persons)
