python_devs = {"Alice", "Bob", "Charlie"}
js_devs = {"Bob", "Diana"}

# Who knows both?
both = python_devs & js_devs  # Intersection
print(f"Developers who know both Python and JavaScript: {both}")

# Who knows either?
either = python_devs | js_devs  # Union
print(f"Developers who know either Python or JavaScript: {either}")

# Who knows only Python?
only_python = python_devs - js_devs  # Difference
print(f"Developers who know only Python: {only_python}")
