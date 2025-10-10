from collections import defaultdict


documents = [
    {"id": 1, "text": "Python is great for data science"},
    {"id": 2, "text": "Python is also great for web development"},
    {"id": 3, "text": "Data science requires math and statistics"},
]


def build_search_index(documents: list[dict]):
    index = defaultdict(list)

    for doc in documents:
        text = doc["text"]
        # Handle case where text field is None
        if text is None:
            continue

        words = text.lower().split()
        for word in words:
            index[word].append(doc["id"])

    return dict(index)


index = build_search_index(documents)

print(index)


def build_search_index_v2(documents: list[dict]):
    index = defaultdict(set)

    for doc in documents:
        text = doc["text"]

        if text is None:
            continue

        words = text.lower().split()
        for word in words:
            index[word].add(doc["id"])

    return dict(index)


index_v2 = build_search_index_v2(documents)

print(index_v2)
