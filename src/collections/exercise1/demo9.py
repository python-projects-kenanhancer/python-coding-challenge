user_settings = {
    "theme": "dark",
    "language": "en",
    "notifications": True,
}

theme = user_settings.get("theme", "light")
language = user_settings.get("language", "es")
notifications = user_settings.get("notifications", False)
font_size = user_settings.get("font_size", 12)

documents = [
    {"id": 1, "text": "Python is great for data science"},
    {"id": 2, "text": "Python is also great for web development"},
    {"id": 3, "text": "Data science requires math and statistics"},
]


def build_search_index(documents: list[dict]):
    index = {}

    for doc in documents:
        words = doc["text"].lower().split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc["id"])

    return index


seach_index = build_search_index(documents)

print(seach_index)
