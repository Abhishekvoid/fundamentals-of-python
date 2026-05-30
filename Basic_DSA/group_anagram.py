from collections import defaultdict

def group_anagrams(strs):

    groups = defaultdict(list)

    for word in strs:

        sorted_word = "".join(sorted(word))

        groups[sorted_word].append(word)

    return list(groups.values())


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))