# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

strs = ["act","pots","tops","cat","stop","hat"] # expected output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

def group_anagram(wordlist):
    anagram_hash = {}
    for word in strs:
        sorted_word = sorted(word)
        sortagain = "".join(sorted_word)
        if sortagain not in anagram_hash:
            anagram_hash[sortagain] = [word]
        else:
            anagram_hash[sortagain].append(word)
    group_list = []
    for key in anagram_hash:
        if key not in group_list:
            group_list.append(anagram_hash[key])
    print(group_list)
    return group_list

group_anagram(strs)
