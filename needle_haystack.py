# Leet code 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

needle_string = "but"
haystack_string = "sadbutsad"

def find_needle(needle, haystack):
    needle_len = len(needle)

    for i in range(len(haystack)):
        # print(haystack[i:i+needle_len])
        if haystack[i:i+needle_len] == needle:
            print(f"{i} is the index of where the word {needle} starts")
        
find_needle(needle_string, haystack_string)