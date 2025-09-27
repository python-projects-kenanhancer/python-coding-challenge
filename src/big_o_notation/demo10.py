from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, item: acc + item, numbers)
print(total)


max_value = reduce(lambda acc, item: acc if acc > item else item, numbers)
print(max_value)

words = ["hello", " ", "World", "!"]
sentence = reduce(lambda acc, item: acc + item, words)
print(sentence)

items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = reduce(lambda acc, item: {**acc, item: acc.get(item, 0) + 1}, items, {})
print(counts)

users = [
    {"id": 1, "type": "premium", "purchases": 100},
    {"id": 2, "type": "free", "purchases": 0},
    {"id": 3, "type": "premium", "purchases": 250},
    {"id": 4, "type": "free", "purchases": 10},
    {"id": 5, "type": "enterprise", "purchases": 1000},
]

dict2 = {}

dict2.update({"premium": {"count": 0, "total_purchases": 4}})
dict2.update({"premium": {"count": 1}})
dict2.update({"enterprise": {"count": 0, "total_purchases": 0}})

user_data = {"name": "Alice"}

# Add multiple items
user_data.update({"age": 30, "city": "NYC"})
user_data.update({"premium": {"count": 0, "total_purchases": 4}})


result = reduce(
    lambda acc, user: (
        acc.update(
            {user["type"]: acc.get(user["type"], {"count": 0, "total_purchases": 0})}
        )
        or acc,
        acc[user["type"]].update(
            {
                "count": acc[user["type"]]["count"] + 1,
                "total_purchases": acc[user["type"]]["total_purchases"]
                + user["purchases"],
            }
        )
        or acc,
    )[1],
    users,
    {},
)
print(result)
