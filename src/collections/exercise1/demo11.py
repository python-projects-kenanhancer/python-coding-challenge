from collections import defaultdict

documents = [
    {"id": 1, "text": "Python is great for data science"},
    {"id": 2, "text": "Python is also great for web development"},
    {"id": 3, "text": "Data science requires math and statistics"},
]


def build_search_index(documents):
    index = defaultdict(set)

    for doc in documents:
        words = doc["text"].lower().split()
        for word in words:
            index[word].add(doc["id"])

    return dict(index)


index = build_search_index(documents)

print(index)
