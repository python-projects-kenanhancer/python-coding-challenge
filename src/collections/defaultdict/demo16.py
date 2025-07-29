from collections import defaultdict

# ✅ List Example – Task list
tasks = ["email", "code review", "email", "meeting"]
print("Unique tasks:", list(set(tasks)))  # remove duplicates via set

# ✅ Tuple Example – Immutable configuration
CONFIG = ("localhost", 5432, "myapp_db")
host, port, db_name = CONFIG  # unpacking tuple
print(f"Connecting to {db_name} at {host}:{port}")

# ✅ Set Example – Track unique visitors
visitors = {"alice", "bob", "charlie"}
visitors.add("alice")  # duplicate won't be added
print("Visitor count:", len(visitors))

# ✅ Dict Example – Product prices
prices = {"apple": 0.99, "banana": 0.59}
print("Banana price:", prices["banana"])

# ✅ defaultdict Example – Group users by department
departments = [
    ("alice", "engineering"),
    ("bob", "hr"),
    ("carol", "engineering"),
]

dept_map = defaultdict(list)
for name, dept in departments:
    dept_map[dept].append(name)

print("Engineering department:", dept_map["engineering"])


# ✅ Class Example – Simple user model
class User:
    def __init__(self, username: str, roles: list[str]):
        self.username = username
        self.roles = roles

    def has_role(self, role: str) -> bool:
        return role in self.roles


# Use the class
user = User("alice", ["admin", "editor"])
print(f"{user.username} is admin?", user.has_role("admin"))
