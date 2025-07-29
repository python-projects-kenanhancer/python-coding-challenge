from collections import defaultdict


def group_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        signature = "".join(sorted(word))
        anagram_groups[signature].append(word)
    return list(anagram_groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
