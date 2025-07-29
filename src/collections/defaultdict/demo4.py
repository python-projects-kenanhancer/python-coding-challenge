from collections import defaultdict


edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]

graph = defaultdict(list)

for src, dest in edges:
    graph[src].append(dest)

print(dict(graph))
