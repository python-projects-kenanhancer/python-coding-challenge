from collections import defaultdict

documents = [
    {"id": 1, "text": "Python is great for data science"},
    {"id": 2, "text": "Python is also great for web development"},
    {"id": 3, "text": "Data science requires math and statistics"},
]


def build_search_index(documents: list[dict]):
    index = defaultdict(lambda: defaultdict(list))

    for doc in documents:
        words = doc["text"].lower().split()
        for position, word in enumerate(words):
            index[word][doc["id"]].append(position)

    return dict(index)


index = build_search_index(documents)

print(index)
