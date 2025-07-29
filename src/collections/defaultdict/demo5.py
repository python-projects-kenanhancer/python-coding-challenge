from collections import defaultdict

tags = [("python", "dev"), ("python", "scripting"), ("java", "dev"), ("python", "dev")]

tag_counter = defaultdict(set)

for lang, label in tags:
    tag_counter[lang].add(label)

print(dict(tag_counter))
