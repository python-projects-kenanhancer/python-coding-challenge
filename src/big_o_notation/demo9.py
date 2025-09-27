from collections import defaultdict
from functools import reduce

users = [
    {"id": 1, "type": "premium", "purchases": 100},
    {"id": 2, "type": "free", "purchases": 0},
    {"id": 3, "type": "premium", "purchases": 250},
    {"id": 4, "type": "free", "purchases": 10},
    {"id": 5, "type": "enterprise", "purchases": 1000},
]


def aggregate_users(users):
    user_stats = defaultdict(lambda: {"count": 0, "total_purchases": 0})

    for user in users:
        user_type = user["type"]
        user_stats[user_type]["count"] += 1
        user_stats[user_type]["total_purchases"] += user["purchases"]

    return dict(user_stats)


def reducer(acc, user):
    user_type = user["type"]
    if user_type not in acc:
        acc[user_type] = {"count": 0, "total_purchases": 0}
    acc[user_type]["count"] += 1
    acc[user_type]["total_purchases"] += user["purchases"]
    return acc


print(reduce(reducer, users, {}))
