from collections import Counter

s1 = "danger"
s2 = "garden"

def check_anagram(s1,s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        return True
    else:
        return False

#print(check_anagram(s1,s2))

def hashmap_anagram(s1,s2):
    frequency_s1 = {}
    frequency_s2 = {}

    for letter1,letter2 in zip(s1,s2):
        if letter1 not in frequency_s1:
            frequency_s1[letter1] = 1
        else:
            frequency_s1[letter1] += 1

        if letter2 not in frequency_s2:
            frequency_s2[letter2] = 1
        else:
            frequency_s2[letter2] += 1
    print(Counter(s1), Counter(s2))
    if frequency_s1 == frequency_s2:
        return True
    else:
        return False

print(hashmap_anagram(s1,s2))